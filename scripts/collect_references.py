"""Offline reference audit using the pinned official solution archive.

Run on the approved numerical test host. This script never modifies upstream
sources, clips a solution, or writes coordinates to its outputs.
"""
import argparse
import hashlib
import json
import math
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
    with ZipFile(args.solutions_archive) as archive:
        solutions = {}
        for member in archive.namelist():
            if member.endswith(".sol"):
                name = Path(member).stem
                if name in solutions:
                    raise ValueError(f"Ambiguous solution file for {name}.")
                solutions[name] = member
        for source in sorted(adapter.VENDORED_RS13PM_DIR.glob("*.py")):
            name = source.stem
            status = {"name": name, "status": "rejected"}
            try:
                if name not in solutions:
                    raise ValueError("missing_solution")
                solution_bytes = archive.read(solutions[name])
                x = np.asarray([float(v) for v in solution_bytes.decode("utf-8").split()], dtype=float)
                problem = adapter.rs13_load_problem(name)
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
                source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
                solution_hash = hashlib.sha256(solution_bytes).hexdigest()
                bound_hash = bounds_digest(problem.n, problem.xl, problem.xu)
                records[name] = {
                    "dimension": problem.n, "problem_sha256": source_hash,
                    "bounds_sha256": bound_hash, "solution_sha256": solution_hash,
                    "reference": {"merit": value, "kind": "best_known",
                        "mapping": "feasible_objective/1",
                        "source": f"RS13 official {name}.sol; rs13sols SHA256 {archive_hash}; "
                                  f"solution SHA256 {solution_hash}; problem SHA256 {source_hash}; "
                                  "offline finite/feasible adapter evaluation; doi:10.1007/s10898-012-9951-y"},
                }
                status.update(status="accepted", merit=value)
            except Exception as exc:
                status["reason"] = f"{type(exc).__name__}:{exc}"
            audit.append(status)
    catalog = {"schema": "rs13-best-known/1", "adapter_sha256": adapter_digest(),
               "runtime_archive_sha256": snapshot["runtime"]["sha256"],
               "solution_archive_sha256": archive_hash, "records": records}
    args.output.write_text(json.dumps(catalog, indent=2, sort_keys=True, allow_nan=False) + "\n")
    report = {"accepted": len(records), "rejected": len(audit)-len(records),
              "evaluations_per_accepted_record": 2, "coordinates_stored": False,
              "python": platform.python_version(), "numpy": np.__version__,
              "records": audit}
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({key: report[key] for key in ("accepted", "rejected", "coordinates_stored")}))


if __name__ == "__main__":
    main()
