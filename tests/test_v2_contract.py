"""Installed-provider checks against the OptiProfiler 2.0 candidate.

Set OP_TEST_V2=1 only in the isolated candidate environment. Native provider
validation belongs on a supported test host, not in a source-only lint job.
"""
import os
import unittest
import numpy as np
from optiprofiler import Feature, FeaturedProblem, Problem


@unittest.skipUnless(os.environ.get("OP_TEST_V2") == "1", "Requires the V2 candidate environment")
class V2ContractTests(unittest.TestCase):
    def test_reference_and_core_owned_recording(self):
        from optiprofiler_rs13 import rs13_load as load
        for specification in ("plain", "noisy+permuted"):
            with self.subTest(feature=specification):
                problem = load("rosenbr")
                self.assertIs(type(problem), Problem)
                self.assertEqual(problem.reference.kind, "best_known")
                trial = FeaturedProblem(problem, Feature(specification), 5, 19)
                self.assertEqual(trial.reference, problem.reference)
                before = (trial.n_eval_fun, trial.n_eval_cub, trial.n_eval_ceq)
                self.assertTrue(np.isfinite(trial.fun(trial.x0)))
                self.assertEqual(trial.n_eval_fun, before[0] + 1)
                self.assertEqual((trial.n_eval_cub, trial.n_eval_ceq), before[1:])
                self.assertEqual(len(trial.fun_hist), trial.n_eval_fun)

    def test_missing_evidence_remains_unknown(self):
        from optiprofiler_rs13 import rs13_load
        for name in ("biggs5", "problem2.1"):
            self.assertIsNone(rs13_load(name).reference)

    def test_invalidating_feature_drops_reference(self):
        from optiprofiler_rs13 import rs13_load
        problem = rs13_load("rosenbr")
        self.assertIsNotNone(problem.reference)
        self.assertIsNone(FeaturedProblem(problem, Feature("quantized"), 5, 19).reference)


if __name__ == "__main__":
    unittest.main()
