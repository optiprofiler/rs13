from pathlib import Path
from datetime import date
import math
import os
import random
import sys
import unittest

import numpy as np

op_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(op_root / "optiprofiler" / "python"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rs13_tools import (
    rs13_collect_info,
    rs13_known_solution,
    rs13_load_problem,
    rs13_load_raw,
    rs13_problemdata,
    rs13_select,
    rs13_uses_effective_unconstrained_bounds,
)


def _as_array(value):
    if value is None:
        return np.empty(0)
    return np.asarray(value)


def _assert_problem_contract(testcase, problem_name):
    problem = rs13_load_problem(problem_name)
    testcase.assertGreaterEqual(problem.n, 1)
    testcase.assertEqual(problem.x0.size, problem.n)
    testcase.assertIn(problem.ptype, {"u", "b"})

    fx0 = problem.fun(problem.x0)
    testcase.assertTrue(math.isfinite(float(fx0)) or math.isnan(float(fx0)))

    cub0 = _as_array(problem.cub(problem.x0))
    ceq0 = _as_array(problem.ceq(problem.x0))
    testcase.assertEqual(cub0.ndim, 1)
    testcase.assertEqual(ceq0.ndim, 1)

    maxcv0 = problem.maxcv(problem.x0)
    testcase.assertTrue(math.isfinite(float(maxcv0)) or math.isnan(float(maxcv0)))

    # Evaluate twice to catch wrappers that accidentally mutate state.
    fx1 = problem.fun(problem.x0)
    testcase.assertTrue(math.isfinite(float(fx1)) or math.isnan(float(fx1)))


class RS13Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        required = ["RS13PM_DIR", "RS13SOLS_DIR", "RS13_PROBLEMDATA_DIR"]
        missing = [name for name in required if not os.environ.get(name)]
        if missing:
            raise unittest.SkipTest(f"Missing RS13 archive env vars: {', '.join(missing)}")

    def test_load_raw_branin(self):
        raw = rs13_load_raw("branin")
        self.assertEqual(raw.name, "branin")
        self.assertEqual(raw.x0.tolist(), [2.5, 7.5])
        self.assertEqual(raw.xmin.tolist(), [-5.0, 0.0])
        self.assertEqual(raw.xmax.tolist(), [10.0, 15.0])
        self.assertAlmostEqual(raw.objective(raw.x0.tolist()), 24.129964413622268)

    def test_known_solutions_evaluate(self):
        expected = {
            "branin": 3.9788736e-01,
            "camel6": -1.0316285e00,
            "convex1_10_1": 0.0,
            "rosenbr": 0.0,
        }
        for name, fbest in expected.items():
            with self.subTest(name=name):
                raw = rs13_load_raw(name)
                xbest = rs13_known_solution(name)
                self.assertEqual(raw.x0.size, xbest.size)
                self.assertAlmostEqual(raw.objective(xbest.tolist()), fbest, delta=1e-4 * max(1.0, abs(fbest)))

    def test_problemdata_matches_raw_loader(self):
        for name in ["branin", "camel6", "convex1_10_1", "rosenbr"]:
            with self.subTest(name=name):
                raw = rs13_load_raw(name)
                data = rs13_problemdata(name)
                np.testing.assert_allclose(data["x0"], raw.x0)
                np.testing.assert_allclose(data["xmin"], raw.xmin)
                np.testing.assert_allclose(data["xmax"], raw.xmax)
                self.assertEqual(data["n"], raw.x0.size)

    def test_load_optiprofiler_problem(self):
        problem = rs13_load_problem("camel6")
        self.assertEqual(problem.name, "CAMEL6")
        self.assertEqual(problem.n, 2)
        self.assertEqual(problem.ptype, "b")
        self.assertEqual(problem.mb, 4)
        self.assertTrue(math.isfinite(problem.fun(problem.x0)))
        xbest = rs13_known_solution("camel6")
        self.assertAlmostEqual(problem.fun(xbest), -1.0316285, places=5)

    def test_daily_random_small_problem_sample(self):
        seed = int(os.environ.get("OP_RANDOM_SEED", date.today().strftime("%Y%m%d")))
        candidates = rs13_select({"ptype": "ub", "mindim": 1, "maxdim": 10, "maxb": 20})
        self.assertGreaterEqual(len(candidates), 4)

        rng = random.Random(seed)
        sample = rng.sample(candidates, k=min(4, len(candidates)))
        print(f"RS13 random sample seed={seed}: {sample}")
        for problem_name in sample:
            with self.subTest(problem=problem_name):
                _assert_problem_contract(self, problem_name)

    def test_effective_unconstrained_search_boxes_are_hidden(self):
        for name in ["rosenbr", "convex1_10_1", "problem3.15"]:
            with self.subTest(name=name):
                self.assertTrue(rs13_uses_effective_unconstrained_bounds(name))
                problem = rs13_load_problem(name)
                self.assertEqual(problem.ptype, "u")
                self.assertEqual(problem.mb, 0)
                self.assertTrue(np.all(np.isneginf(problem.xl)))
                self.assertTrue(np.all(np.isposinf(problem.xu)))

    def test_intrinsic_bounds_are_preserved(self):
        for name in ["3pk", "camel6", "hatflda", "problem3.13"]:
            with self.subTest(name=name):
                self.assertFalse(rs13_uses_effective_unconstrained_bounds(name))
                problem = rs13_load_problem(name)
                self.assertEqual(problem.ptype, "b")
                self.assertGreater(problem.mb, 0)

    def test_select_filters_smoke_problems(self):
        selected = rs13_select({"ptype": "b", "mindim": 1, "maxdim": 10, "maxb": 20})
        for name in {"branin", "camel6"}:
            self.assertIn(name, selected)
        for name in {"rosenbr", "convex1_10_1"}:
            self.assertNotIn(name, selected)
        selected_u = rs13_select({"ptype": "u", "mindim": 1, "maxdim": 10})
        for name in {"rosenbr", "convex1_10_1"}:
            self.assertIn(name, selected_u)
        selected_default_bound_cap = rs13_select({"ptype": "b", "mindim": 1, "maxdim": 10, "maxb": 10})
        self.assertNotIn("convex1_10_1", selected_default_bound_cap)

    def test_collect_info_and_select_full_index(self):
        rows = rs13_collect_info()
        self.assertEqual(len(rows), 502)
        by_name = {row["problem_name"]: row for row in rows}
        self.assertEqual(by_name["branin"]["ptype"], "b")
        self.assertEqual(by_name["branin"]["dim"], "2")
        self.assertEqual(by_name["branin"]["mb"], "4")
        self.assertEqual(by_name["rosenbr"]["ptype"], "u")
        self.assertEqual(by_name["rosenbr"]["mb"], "0")
        self.assertEqual(by_name["convex1_10_1"]["ptype"], "u")
        self.assertEqual(by_name["3pk"]["ptype"], "b")
        self.assertEqual(by_name["problem3.13"]["ptype"], "b")
        self.assertNotIn("argins", by_name["branin"])
        self.assertNotIn("dims", by_name["branin"])
        self.assertEqual(by_name["problem3.15"]["problemdata_status"], "mismatch")
        self.assertEqual(sum(1 for row in rows if row["ptype"] == "u"), 371)
        self.assertEqual(sum(1 for row in rows if row["ptype"] == "b"), 131)
        selected = rs13_select({"ptype": "ub", "mindim": 1, "maxdim": 300, "maxb": 600})
        self.assertEqual(len(selected), 502)


if __name__ == "__main__":
    unittest.main()
