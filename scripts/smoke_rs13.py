from pathlib import Path
import sys

from scipy.optimize import Bounds, minimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rs13_tools import rs13_known_solution, rs13_load_problem


CASES = [
    ("branin", "Nelder-Mead", {"maxfev": 2000}),
    ("camel6", "Nelder-Mead", {"maxfev": 2000}),
    ("rosenbr", "Nelder-Mead", {"maxfev": 2000}),
    ("convex1_10_1", "Powell", {"maxfev": 3000}),
]


def main():
    for name, method, options in CASES:
        problem = rs13_load_problem(name)
        xbest = rs13_known_solution(name)
        kwargs = {"method": method, "options": options}
        if method != "Nelder-Mead":
            kwargs["bounds"] = Bounds(problem.xl, problem.xu)
        result = minimize(lambda x: problem.fun(x), problem.x0, **kwargs)
        print(
            f"{name:14s} n={problem.n:3d} ptype={problem.ptype} "
            f"method={method:11s} f0={problem.fun(problem.x0): .6e} "
            f"f_known={problem.fun(xbest): .6e} "
            f"f_solver={result.fun: .6e} evals={result.nfev}"
        )


if __name__ == "__main__":
    main()
