"""Internal, fail-closed lookup of offline-verified feasible scalar records.

No solution coordinates, downloads, or oracle evaluations belong here. The
whole loader module is conservatively fingerprinted; unrelated README/tests
are not dependencies. A loader refactor requires regeneration even if its
mathematical effect is neutral.
"""
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
CATALOG_PATH = ROOT / "references.json"


def adapter_digest():
    return hashlib.sha256((ROOT / "rs13_tools.py").read_bytes()).hexdigest()


def bounds_digest(n, xl, xu):
    """Bind the actual exposed bounds, not the original BAM search box."""
    digest = hashlib.sha256(str(int(n)).encode("ascii"))
    for values, default in ((xl, -math.inf), (xu, math.inf)):
        array = np.full(n, default, dtype="<f8") if values is None else np.asarray(values, dtype="<f8").reshape(-1)
        if array.size != n or np.isnan(array).any():
            raise ValueError("Invalid reference bounds.")
        digest.update(array.tobytes())
    return digest.hexdigest()


@lru_cache(maxsize=4)
def _read_catalog(filename, size, modified):
    del size, modified
    with Path(filename).open(encoding="utf-8") as stream:
        return json.load(stream)


def load_reference(name, source_path, n, xl, xu):
    """Return a public reference record or None; never evaluate the problem."""
    try:
        stat = CATALOG_PATH.stat()
        catalog = _read_catalog(str(CATALOG_PATH), stat.st_size, stat.st_mtime_ns)
        if catalog.get("schema") != "rs13-best-known/1" or catalog.get("adapter_sha256") != adapter_digest():
            return None
        entry = catalog["records"][name]
        if entry["dimension"] != n or entry["bounds_sha256"] != bounds_digest(n, xl, xu):
            return None
        if entry["problem_sha256"] != hashlib.sha256(Path(source_path).read_bytes()).hexdigest():
            return None
        reference = entry["reference"]
        if set(reference) != {"merit", "kind", "source", "mapping"}:
            return None
        merit = reference["merit"]
        if isinstance(merit, bool) or not isinstance(merit, (int, float)) or not math.isfinite(merit):
            return None
        if isinstance(merit, int) and int(float(merit)) != merit:
            return None
        if reference["kind"] != "best_known" or reference["mapping"] != "feasible_objective/1":
            return None
        if not isinstance(reference["source"], str) or not reference["source"].strip():
            return None
        return dict(reference)
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError):
        # Missing, stale and malformed records mean unknown, not noisy runtime
        # repair attempts. Maintenance rejection reasons are reported offline.
        return None
