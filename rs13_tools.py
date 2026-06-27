from __future__ import annotations

import ast
import csv
import math
import os
from pathlib import Path
from typing import Callable

import numpy as np

try:
    from optiprofiler.opclasses import Problem
except ImportError:  # pragma: no cover - exercised by direct local checks.
    Problem = None


CURRENT_DIR = Path(__file__).resolve().parent
PROBINFO_PATH = CURRENT_DIR / "probinfo_rs13.csv"


class RS13ProblemSource:
    """Raw ingredients extracted from one official RS13 Python problem file."""

    __slots__ = ("name", "objective", "x0", "xmin", "xmax", "source_path")

    def __init__(
        self,
        name: str,
        objective: Callable,
        x0: np.ndarray,
        xmin: np.ndarray,
        xmax: np.ndarray,
        source_path: Path,
    ):
        self.name = name
        self.objective = objective
        self.x0 = x0
        self.xmin = xmin
        self.xmax = xmax
        self.source_path = source_path


RS13_SMOKE_PROBLEMS = ("branin", "camel6", "rosenbr", "convex1_10_1")
RS13_PROBINFO_FIELDS = (
    "problem_name",
    "ptype",
    "xtype",
    "dim",
    "mb",
    "ml",
    "mu",
    "mcon",
    "mlcon",
    "mnlcon",
    "m_ub",
    "m_eq",
    "m_linear_ub",
    "m_linear_eq",
    "m_nonlinear_ub",
    "m_nonlinear_eq",
    "f0",
    "fbest",
    "has_known_solution",
    "isfeasibility",
    "isgrad",
    "ishess",
    "isjcub",
    "isjceq",
    "ishcub",
    "ishceq",
    "source_file",
    "problemdata_status",
    "known_solution_status",
)

RS13_EFFECTIVE_UNCONSTRAINED_PREFIXES = (
    "convex1_",
    "convex2_",
    "convex3_",
    "convex4_",
)

# RS13's BAM-facing Python files give every problem a finite search box. For
# the names below, a source-level review found that those boxes are algorithmic
# search boxes rather than mathematical variable bounds. The OptiProfiler
# adapter therefore exposes them as unconstrained problems.
RS13_EFFECTIVE_UNCONSTRAINED_NAMES = frozenset(
    {
        "aircrftb",
        "allinitu",
        "arglina",
        "arglinb",
        "arglinc",
        "beale",
        "brownal",
        "brownbs",
        "brownden",
        "chnrosnb",
        "cube",
        "denschnb",
        "denschnd",
        "denschnf",
        "dixon3dq",
        "djtl",
        "eigenals",
        "eigenb",
        "eigenbls",
        "emfl",
        "emfl_eps",
        "engval2",
        "errinros",
        "esfl",
        "ex8_1_3",
        "ex8_1_4",
        "ex8_1_5",
        "ex8_1_6",
        "extrosnb",
        "fletcbv2",
        "fletchcr",
        "genhumps",
        "hairy",
        "heart6ls",
        "heart8ls",
        "hilberta",
        "hilbertb",
        "himmelbb",
        "himmelbf",
        "hs002",
        "humps",
        "kowosb",
        "loghairy",
        "maratosb",
        "median",
        "mexhat",
        "nasty",
        "nonmsqrt",
        "palmer1c",
        "palmer1d",
        "palmer2c",
        "palmer3c",
        "palmer4c",
        "palmer5c",
        "palmer5d",
        "palmer6c",
        "palmer7c",
        "palmer8c",
        "problem2.10",
        "problem2.11",
        "problem2.12",
        "problem2.14",
        "problem2.15",
        "problem2.16",
        "problem2.17",
        "problem2.18",
        "problem2.19",
        "problem2.20",
        "problem2.21",
        "problem2.24",
        "problem2.3",
        "problem2.4",
        "problem2.5",
        "problem2.6",
        "problem2.7",
        "problem2.8",
        "problem2.9",
        "problem3.1",
        "problem3.10",
        "problem3.11",
        "problem3.12",
        "problem3.15",
        "problem3.16",
        "problem3.17",
        "problem3.18",
        "problem3.19",
        "problem3.2",
        "problem3.20",
        "problem3.21",
        "problem3.22",
        "problem3.23",
        "problem3.24",
        "problem3.5",
        "problem3.6",
        "problem3.7",
        "problem3.8",
        "problem3.9",
        "rosenbr",
        "s201",
        "s202",
        "s204",
        "s205",
        "s206",
        "s207",
        "s208",
        "s209",
        "s210",
        "s211",
        "s212",
        "s213",
        "s214",
        "s240",
        "s243",
        "s246",
        "s256",
        "s258",
        "s260",
        "s266",
        "s271",
        "s273",
        "s274",
        "s275",
        "s276",
        "s281",
        "s282",
        "s283",
        "s286",
        "s287",
        "s288",
        "s290",
        "s291",
        "s292",
        "s293",
        "s294",
        "s295",
        "s296",
        "s297",
        "s298",
        "s299",
        "s300",
        "s301",
        "s302",
        "s303",
        "s304",
        "s305",
        "s308",
        "s309",
        "s311",
        "s312",
        "s350",
        "s351",
        "s352",
        "s370",
        "s371",
        "s386",
        "sineval",
        "sisser",
        "st_e39",
        "tointqor",
        "vardim",
        "watson",
        "yfitu",
        "zangwil2",
    }
)


def rs13_load(problem_name: str):
    """
    Load one RS13 problem as an OptiProfiler `Problem`.

    This is the public loader used by OptiProfiler when the library is exposed
    as ``plibs=["rs13"]``. It requires the official RS13 Python archive
    (`rs13pm.zip`) to be extracted locally and discoverable through
    ``RS13PM_DIR`` or an explicit source path.
    """

    return rs13_load_problem(problem_name)


def rs13_select(options: dict | None = None) -> list[str]:
    """
    Select RS13 problems using OptiProfiler's standard filters.

    Parameters are the usual OptiProfiler problem-library options, including
    ``ptype``, ``mindim``, ``maxdim``, ``minb``, ``maxb``, ``mincon``,
    ``maxcon``, and ``excludelist``. Problem metadata is read from the
    committed ``probinfo_rs13.csv`` table. Regenerate that file with
    ``rs13_collect_info(refresh=True)`` or ``scripts/collect_info.py`` after
    updating the upstream RS13 archives.
    """

    options = dict(options or {})
    defaults = {
        "ptype": "ubln",
        "mindim": 1,
        "maxdim": np.inf,
        "minb": 0,
        "maxb": np.inf,
        "minlcon": 0,
        "maxlcon": np.inf,
        "minnlcon": 0,
        "maxnlcon": np.inf,
        "mincon": 0,
        "maxcon": np.inf,
        "oracle": 0,
        "excludelist": [],
    }
    for key, value in defaults.items():
        options.setdefault(key, value)

    if options["oracle"] != 0:
        return []

    exclude_set = {_normalize_problem_name(name) for name in options["excludelist"]}
    selected = []
    for row in rs13_collect_info():
        name = row["problem_name"]
        if _normalize_problem_name(name) in exclude_set:
            continue
        if row["ptype"] not in options["ptype"]:
            continue
        dim = _safe_number(row["dim"])
        mb = _safe_number(row["mb"])
        mlcon = _safe_number(row["mlcon"])
        mnlcon = _safe_number(row["mnlcon"])
        mcon = _safe_number(row["mcon"])
        if not (options["mindim"] <= dim <= options["maxdim"]):
            continue
        if not (options["minb"] <= mb <= options["maxb"]):
            continue
        if not (options["minlcon"] <= mlcon <= options["maxlcon"]):
            continue
        if not (options["minnlcon"] <= mnlcon <= options["maxnlcon"]):
            continue
        if not (options["mincon"] <= mcon <= options["maxcon"]):
            continue
        selected.append(name)

    return selected


def rs13_collect_info(
    source_dir: str | os.PathLike | None = None,
    sols_dir: str | os.PathLike | None = None,
    problemdata_dir: str | os.PathLike | None = None,
    output_path: str | os.PathLike | None = None,
    refresh: bool = False,
) -> list[dict[str, str]]:
    """
    Return or regenerate the RS13 problem-information table.

    With the default arguments, the function reads the committed
    ``probinfo_rs13.csv`` table. Set ``refresh=True`` to rebuild the table from
    local extracts of the official RS13 archives. The source locations can be
    provided explicitly or through ``RS13PM_DIR``, ``RS13SOLS_DIR``, and
    ``RS13_PROBLEMDATA_DIR``. The committed table reflects this adapter's
    effective problem types: confirmed BAM search boxes are exposed as
    unconstrained problems.
    """

    path = Path(output_path).expanduser().resolve() if output_path is not None else PROBINFO_PATH
    if not refresh and source_dir is None and sols_dir is None and problemdata_dir is None and path.exists():
        return _read_probinfo(path)

    rows = _build_probinfo(source_dir=source_dir, sols_dir=sols_dir, problemdata_dir=problemdata_dir)
    _write_probinfo(rows, path)
    return rows


def rs13_load_raw(problem_name: str, source_dir: str | os.PathLike | None = None) -> RS13ProblemSource:
    """
    Load an RS13 objective and bounds from the official `rs13pm` Python file.

    The upstream files are BAM driver scripts, not importable problem modules.
    This loader parses the file, keeps imports except `bam`, keeps assignments
    and helper/objective functions, and drops top-level BAM solve/print calls.
    The returned bounds are the official BAM-driver bounds; `rs13_load_problem`
    decides whether those bounds should be exposed to OptiProfiler.
    """

    name = _normalize_problem_name(problem_name)
    path = _problem_script_path(name, source_dir)
    namespace = _exec_sanitized_rs13_script(path)

    missing = [key for key in ("objective", "x0", "xmin", "xmax") if key not in namespace]
    if missing:
        raise ValueError(f"RS13 script {path} is missing required fields: {', '.join(missing)}")

    x0 = _as_vector(namespace["x0"], "x0")
    xmin = _as_vector(namespace["xmin"], "xmin")
    xmax = _as_vector(namespace["xmax"], "xmax")
    if not (x0.size == xmin.size == xmax.size):
        raise ValueError(f"RS13 problem {name} has inconsistent x0/xmin/xmax dimensions.")

    return RS13ProblemSource(
        name=name,
        objective=namespace["objective"],
        x0=x0,
        xmin=xmin,
        xmax=xmax,
        source_path=path,
    )


def rs13_load_problem(problem_name: str, source_dir: str | os.PathLike | None = None):
    """
    Convert an RS13 problem into an OptiProfiler `Problem` instance.

    RS13's current public Python files are BAM driver scripts for scalar
    objective problems. Nonlinear and linear constraints are not exposed in this
    interface. Bounds that were confirmed to be BAM search boxes rather than
    mathematical constraints are hidden from the OptiProfiler `Problem`.
    """

    if Problem is None:
        raise ImportError("optiprofiler is required to construct an OptiProfiler Problem.")

    raw = rs13_load_raw(problem_name, source_dir=source_dir)

    def fun(x):
        return float(raw.objective(np.asarray(x, dtype=float).reshape(-1).tolist()))

    kwargs = {"name": raw.name.upper()}
    if not rs13_uses_effective_unconstrained_bounds(raw.name):
        kwargs.update({"xl": raw.xmin, "xu": raw.xmax})
    return Problem(fun, raw.x0, **kwargs)


def rs13_uses_effective_unconstrained_bounds(problem_name: str) -> bool:
    """
    Return whether RS13 search-box bounds should be hidden from OptiProfiler.

    The official RS13 Python files are BAM driver scripts and therefore use
    finite boxes even for problems whose mathematical definitions are
    unconstrained. Confirmed search-box-only cases are exposed as
    unconstrained problems by this adapter.
    """

    name = _normalize_problem_name(problem_name)
    return name.startswith(RS13_EFFECTIVE_UNCONSTRAINED_PREFIXES) or name in RS13_EFFECTIVE_UNCONSTRAINED_NAMES


def rs13_known_solution(problem_name: str, sols_dir: str | os.PathLike | None = None) -> np.ndarray:
    """Read the known solution vector from `rs13sols.zip` output."""

    name = _normalize_problem_name(problem_name)
    directory = _resolve_dir(sols_dir, "RS13SOLS_DIR")
    path = directory / f"{name}.sol"
    if not path.exists():
        raise FileNotFoundError(f"RS13 solution file not found: {path}")
    return _as_vector([float(token) for token in path.read_text(encoding="utf-8").split()], "solution")


def rs13_problemdata(problem_name: str, problemdata_dir: str | os.PathLike | None = None) -> dict:
    """Read dimension, bounds, and starting point from `problemdata.zip` output."""

    name = _normalize_problem_name(problem_name)
    directory = _resolve_dir(problemdata_dir, "RS13_PROBLEMDATA_DIR")
    path = directory / f"{name}.problem.data"
    if not path.exists():
        raise FileNotFoundError(f"RS13 problemdata file not found: {path}")
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(lines) < 4:
        raise ValueError(f"RS13 problemdata file is too short: {path}")
    n = int(float(lines[0].split()[0]))
    xmin = _as_vector([float(token) for token in lines[1].split()], "xmin")
    xmax = _as_vector([float(token) for token in lines[2].split()], "xmax")
    x0 = _as_vector([float(token) for token in lines[3].split()], "x0")
    if not (xmin.size == xmax.size == x0.size == n):
        raise ValueError(f"RS13 problemdata has inconsistent dimensions: {path}")
    return {"name": name, "n": n, "xmin": xmin, "xmax": xmax, "x0": x0, "path": path}


def _build_probinfo(
    source_dir: str | os.PathLike | None = None,
    sols_dir: str | os.PathLike | None = None,
    problemdata_dir: str | os.PathLike | None = None,
) -> list[dict[str, str]]:
    source_path = _resolve_dir(source_dir, "RS13PM_DIR")
    names = sorted(path.stem for path in source_path.glob("*.py") if not path.name.startswith("."))
    rows = []
    for name in names:
        rows.append(_collect_one_problem_info(name, source_dir=source_path, sols_dir=sols_dir, problemdata_dir=problemdata_dir))
    return rows


def _collect_one_problem_info(
    problem_name: str,
    source_dir: str | os.PathLike | None = None,
    sols_dir: str | os.PathLike | None = None,
    problemdata_dir: str | os.PathLike | None = None,
) -> dict[str, str]:
    raw = rs13_load_raw(problem_name, source_dir=source_dir)
    dim = raw.x0.size
    if rs13_uses_effective_unconstrained_bounds(raw.name):
        finite_lower = np.zeros(dim, dtype=bool)
        finite_upper = np.zeros(dim, dtype=bool)
    else:
        finite_lower = np.isfinite(raw.xmin)
        finite_upper = np.isfinite(raw.xmax)
    ml = int(np.count_nonzero(finite_lower))
    mu = int(np.count_nonzero(finite_upper))
    mb = ml + mu
    ptype = "b" if mb > 0 else "u"
    f0 = _safe_eval(raw.objective, raw.x0)
    fbest = math.nan
    has_known_solution = 0
    known_solution_status = "missing"
    try:
        xbest = rs13_known_solution(problem_name, sols_dir=sols_dir)
        if xbest.size != dim:
            known_solution_status = f"dimension_mismatch:{xbest.size}!={dim}"
        else:
            fbest = _safe_eval(raw.objective, xbest)
            has_known_solution = int(math.isfinite(fbest))
            known_solution_status = "ok" if has_known_solution else "nonfinite"
    except FileNotFoundError:
        known_solution_status = "missing"
    except Exception as exc:
        known_solution_status = f"error:{type(exc).__name__}"

    problemdata_status = "missing"
    try:
        data = rs13_problemdata(problem_name, problemdata_dir=problemdata_dir)
        problemdata_match = (
            data["n"] == dim
            and data["x0"].size == dim
            and data["xmin"].size == dim
            and data["xmax"].size == dim
            and np.allclose(data["x0"], raw.x0)
            and np.allclose(data["xmin"], raw.xmin)
            and np.allclose(data["xmax"], raw.xmax)
        )
        problemdata_status = "ok" if problemdata_match else "mismatch"
    except FileNotFoundError:
        problemdata_status = "missing"
    except ValueError:
        problemdata_status = "mismatch"
    except Exception as exc:
        problemdata_status = f"error:{type(exc).__name__}"

    return {
        "problem_name": raw.name,
        "ptype": ptype,
        "xtype": "r",
        "dim": str(dim),
        "mb": str(mb),
        "ml": str(ml),
        "mu": str(mu),
        "mcon": "0",
        "mlcon": "0",
        "mnlcon": "0",
        "m_ub": "0",
        "m_eq": "0",
        "m_linear_ub": "0",
        "m_linear_eq": "0",
        "m_nonlinear_ub": "0",
        "m_nonlinear_eq": "0",
        "f0": _format_float(f0),
        "fbest": _format_float(fbest),
        "has_known_solution": str(has_known_solution),
        "isfeasibility": "0",
        "isgrad": "0",
        "ishess": "0",
        "isjcub": "0",
        "isjceq": "0",
        "ishcub": "0",
        "ishceq": "0",
        "source_file": raw.source_path.name,
        "problemdata_status": problemdata_status,
        "known_solution_status": known_solution_status,
    }


def _read_probinfo(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_probinfo(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RS13_PROBINFO_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in RS13_PROBINFO_FIELDS})


def _safe_eval(objective: Callable, x: np.ndarray) -> float:
    try:
        value = float(objective(np.asarray(x, dtype=float).reshape(-1).tolist()))
    except Exception:
        return math.nan
    return value


def _format_float(value: float) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    if value == 0:
        return "0"
    return f"{value:.12g}"


def _exec_sanitized_rs13_script(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    kept_nodes = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            names = [alias for alias in node.names if alias.name != "bam"]
            if names:
                node.names = names
                kept_nodes.append(node)
        elif isinstance(node, ast.ImportFrom):
            if node.module != "bam":
                kept_nodes.append(node)
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.FunctionDef)):
            if not _contains_name(node, "bam"):
                kept_nodes.append(node)
        # Drop top-level Expr, With, and other driver statements. In the
        # official RS13 Python archives, these are BAM solve calls and prints.

    module = ast.Module(body=kept_nodes, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = {"__builtins__": __builtins__}
    exec(compile(module, str(path), "exec"), namespace)
    return namespace


def _contains_name(node: ast.AST, name: str) -> bool:
    return any(isinstance(child, ast.Name) and child.id == name for child in ast.walk(node))


def _problem_script_path(problem_name: str, source_dir: str | os.PathLike | None) -> Path:
    directory = _resolve_dir(source_dir, "RS13PM_DIR")
    path = directory / f"{problem_name}.py"
    if not path.exists():
        raise FileNotFoundError(f"RS13 Python problem file not found: {path}")
    return path


def _resolve_dir(value: str | os.PathLike | None, env_name: str) -> Path:
    raw = value if value is not None else os.environ.get(env_name)
    if raw is None:
        raise FileNotFoundError(
            f"Set {env_name} to the extracted official RS13 directory before using this adapter."
        )
    path = Path(raw).expanduser().resolve()
    if not path.is_dir():
        raise FileNotFoundError(f"{env_name} does not point to a directory: {path}")
    return path


def _normalize_problem_name(problem_name: str) -> str:
    if not isinstance(problem_name, str) or not problem_name.strip():
        raise ValueError("RS13 problem name must be a nonempty string.")
    return problem_name.strip().lower()


def _as_vector(values, label: str) -> np.ndarray:
    array = np.asarray(values, dtype=float).reshape(-1)
    if array.ndim != 1:
        raise ValueError(f"{label} must be one-dimensional.")
    return array


def _safe_number(value):
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except (TypeError, ValueError):
        return float(value)
