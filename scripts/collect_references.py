"""Offline reference audit using the pinned official solution archive.

Run on the approved numerical test host. This script never modifies upstream
sources, clips a solution, or writes coordinates to its outputs.
"""
import argparse
import hashlib
import json
import math
import os
import platform
from pathlib import Path
import sys
from zipfile import ZipFile

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import rs13_tools as adapter
from rs13_reference import adapter_digest, bounds_digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--solutions-archive", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    snapshot = json.loads((ROOT / "UPSTREAM_SNAPSHOT.json").read_text())
    archive_hash = hashlib.sha256(args.solutions_archive.read_bytes()).hexdigest()
    if archive_hash != snapshot["solution_oracle"]["sha256"]:
        raise ValueError("Solution archive differs from the reviewed upstream snapshot.")
    records = {}
    audit = []
    runtime_root = adapter.VENDORED_RS13PM_DIR.resolve()
    with ZipFile(args.solutions_archive) as archive:
        solutions = {}
        for member in archive.namelist():
            if member.endswith(".sol"):
                name = Path(member).stem
                if name in solutions:
                    raise ValueError(f"Ambiguous solution file for {name}.")
                solutions[name] = member
        for source in sorted(runtime_root.glob("*.py")):
            name = source.stem
            status = {"name": name, "status": "rejected"}
            try:
                if name not in solutions:
                    raise ValueError("missing_solution")
                solution_bytes = archive.read(solutions[name])
                x = np.asarray([float(v) for v in solution_bytes.decode("utf-8").split()], dtype=float)
                source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
                raw = adapter.rs13_load_raw(name, source_dir=runtime_root)
                actual_source = raw.source_path.resolve()
                if actual_source != source.resolve():
                    raise ValueError("source_identity_mismatch")
                status.update(source_path=str(source.resolve()), raw_source_path=str(actual_source),
                              problem_sha256=source_hash)
                # Bind both loads explicitly: maintainer RS13PM_DIR overrides
                # must never be relabeled as evidence for bundled source.
                problem = adapter.rs13_load_problem(name, source_dir=runtime_root)
                if x.size != problem.n:
                    raise ValueError(f"dimension_mismatch:{x.size}!={problem.n}")
                if not np.all(np.isfinite(x)):
                    raise ValueError("nonfinite_coordinates")
                if np.any(x < problem.xl) or np.any(x > problem.xu):
                    raise ValueError("outside_adapter_bounds")
                value = float(problem.fun(x))
                repeated = float(problem.fun(x))
                if not math.isfinite(value) or not math.isfinite(repeated):
                    raise ValueError("nonfinite_objective")
                if value != repeated:
                    raise ValueError("nonrepeatable_objective")
                violation = float(problem.maxcv(x))
                if violation != 0.0:
                    raise ValueError(f"infeasible_solution:{violation}")
                # Many official files merely repeat the starting point, and some
                # plain solvers go far below their value. A target that x0 already
                # attains says nothing, and every run would pass its first
                # evaluation. Unknown keeps the empirical target instead.
                initial = float(problem.fun(problem.x0))
                if not math.isfinite(initial) or value >= initial:
                    raise ValueError("not_better_than_initial_point")
                if hashlib.sha256(actual_source.read_bytes()).hexdigest() != source_hash:
                    raise ValueError("source_changed_during_audit")
                solution_hash = hashlib.sha256(solution_bytes).hexdigest()
                bound_hash = bounds_digest(problem.n, problem.xl, problem.xu)
                records[name] = {
                    "dimension": problem.n, "problem_sha256": source_hash,
                    "bounds_sha256": bound_hash, "solution_sha256": solution_hash,
                    "reference": {"fun": value, "maxcv": 0.0, "kind": "feasible",
                        "source": f"RS13 official {name}.sol; rs13sols SHA256 {archive_hash}; "
                                  f"solution SHA256 {solution_hash}; problem SHA256 {source_hash}; "
                                  "offline finite/feasible adapter evaluation; doi:10.1007/s10898-012-9951-y"},
                }
                status.update(status="accepted", fun=value)
            except Exception as exc:
                status["reason"] = f"{type(exc).__name__}:{exc}"
            audit.append(status)
    catalog = {"schema": "rs13-best-known/2", "adapter_sha256": adapter_digest(),
               "runtime_archive_sha256": snapshot["runtime"]["sha256"],
               "solution_archive_sha256": archive_hash, "records": records}
    args.output.write_text(json.dumps(catalog, indent=2, sort_keys=True, allow_nan=False) + "\n")
    report = {"accepted": len(records), "rejected": len(audit)-len(records),
              "evaluations_per_accepted_record": 3, "coordinates_stored": False,
              "python": platform.python_version(), "numpy": np.__version__,
              "runtime_root": str(runtime_root), "ignored_RS13PM_DIR": os.environ.get("RS13PM_DIR"),
              "adapter_sha256": adapter_digest(), "collector_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "records": audit}
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({key: report[key] for key in ("accepted", "rejected", "coordinates_stored")}))


if __name__ == "__main__":
    main()
