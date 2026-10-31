"""Installed-provider tests for offline, source-bound reference records."""
import copy
import json
import multiprocessing
import os
from pathlib import Path
import pickle
import shutil
import tempfile
import unittest
from unittest import mock

import numpy as np


# Dimension mismatch, or an official value no better than the initial point.
UNKNOWN_REFERENCES = ("biggs5", "problem2.1", "problem2.17", "problem2.23", "ex8_1_4",
                      "ex4_1_4", "convex4_25_3", "convex1_10_1")


def _worker_load(name):
    from optiprofiler_rs13 import rs13_load
    from optiprofiler import Feature, FeaturedProblem
    problem = rs13_load(name)
    trials = []
    for specification in ("plain", "noisy+permuted", "quantized"):
        trial = FeaturedProblem(problem, Feature(specification), 5, 19)
        value = trial.fun(trial.x0)
        trials.append((None if trial.reference is None else trial.reference.as_dict(),
                       value, trial.n_eval_fun, trial.n_eval_cub, trial.n_eval_ceq))
    return problem.reference.as_dict(), trials


@unittest.skipUnless(os.environ.get("OP_TEST_V2") == "1", "Requires installed V2 candidate")
class ReferenceTests(unittest.TestCase):
    def setUp(self):
        from optiprofiler_rs13 import rs13_reference, rs13_tools
        self.reader = rs13_reference
        self.adapter = rs13_tools
        self.catalog = json.loads(rs13_reference.CATALOG_PATH.read_text())

    def lookup(self, catalog):
        source = self.adapter.VENDORED_RS13PM_DIR / "rosenbr.py"
        with mock.patch.object(self.reader, "_read_catalog", return_value=catalog):
            return self.reader.load_reference("rosenbr", source, 2, None, None)

    def test_catalog_has_raw_values_not_merits_or_points(self):
        records = self.catalog["records"]
        self.assertEqual(self.catalog["schema"], "rs13-best-known/2")
        self.assertEqual(len(records), 350)
        for name in UNKNOWN_REFERENCES:
            self.assertNotIn(name, records)
        for entry in records.values():
            self.assertEqual(set(entry), {"dimension", "problem_sha256", "bounds_sha256",
                                          "solution_sha256", "reference"})
            reference = entry["reference"]
            self.assertEqual(set(reference), {"fun", "maxcv", "kind", "source"})
            self.assertTrue(np.isfinite(reference["fun"]))
            self.assertEqual(reference["maxcv"], 0.0)
            self.assertEqual(reference["kind"], "feasible")

    def test_every_reference_improves_on_the_initial_point(self):
        # A target that x0 attains would pass every run at its first evaluation.
        for name, entry in self.catalog["records"].items():
            problem = self.adapter.rs13_load_problem(name)
            self.assertLess(entry["reference"]["fun"], problem.fun(problem.x0), name)

    def test_load_adds_no_oracle_evaluation(self):
        raw = self.adapter.rs13_load_raw("rosenbr")
        raw.objective = mock.Mock(wraps=raw.objective)
        with mock.patch.object(self.adapter, "rs13_load_raw", return_value=raw):
            problem = self.adapter.rs13_load_problem("rosenbr")
        raw.objective.assert_not_called()
        self.assertEqual(problem.reference.as_dict(), self.catalog["records"]["rosenbr"]["reference"])
        self.assertIsNone(problem.reference.x_ref)
        self.assertTrue(np.isfinite(problem.fun(problem.x0)))
        self.assertEqual(raw.objective.call_count, 1)

    def test_unknown_malformed_and_stale_records_fail_closed(self):
        self.assertIsNotNone(self.lookup(self.catalog))
        malformed = [None, [], {}, {"schema": "old"}]
        stale = copy.deepcopy(self.catalog)
        stale["adapter_sha256"] = "0" * 64
        malformed.append(stale)
        for field, value in (("dimension", 3), ("bounds_sha256", "0" * 64),
                             ("problem_sha256", "0" * 64), ("reference", {})):
            bad = copy.deepcopy(self.catalog)
            bad["records"]["rosenbr"][field] = value
            malformed.append(bad)
        for field, value in (("fun", True), ("fun", float("inf")),
                             ("fun", float("nan")), ("fun", "0"),
                             ("fun", 2 ** 53 + 1), ("fun", 10 ** 400),
                             ("maxcv", 1.0), ("maxcv", True), ("maxcv", "0"),
                             ("kind", "merit"), ("kind", "best_known"),
                             ("mapping", "feasible_objective/1"), ("merit", 0.0),
                             ("source", ""), ("point", [1, 1]), ("x_ref", [1, 1])):
            bad = copy.deepcopy(self.catalog)
            bad["records"]["rosenbr"]["reference"][field] = value
            malformed.append(bad)
        for index, bad in enumerate(malformed):
            with self.subTest(index=index):
                self.assertIsNone(self.lookup(bad))
        with mock.patch.object(self.reader, "CATALOG_PATH", Path("/missing/references.json")):
            self.assertIsNone(self.adapter.rs13_load_problem("rosenbr").reference)

    def test_source_override_binds_bytes_not_installation_path(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "rosenbr.py"
            shutil.copyfile(self.adapter.VENDORED_RS13PM_DIR / source.name, source)
            problem = self.adapter.rs13_load_problem("rosenbr", source_dir=directory)
            self.assertIsNotNone(problem.reference)
            source.write_bytes(source.read_bytes() + b"\n# Isolated override identity change.\n")
            changed = self.adapter.rs13_load_problem("rosenbr", source_dir=directory)
            self.assertIsNone(changed.reference)
            with mock.patch.dict(os.environ, {"RS13PM_DIR": directory}):
                self.assertIsNone(self.adapter.rs13_load("rosenbr").reference)
            self.assertEqual(problem.fun(problem.x0), changed.fun(changed.x0))

    def test_effective_bound_change_invalidates_reference(self):
        with mock.patch.object(self.adapter, "rs13_uses_effective_unconstrained_bounds", return_value=False):
            self.assertIsNone(self.adapter.rs13_load_problem("rosenbr").reference)

    def test_reference_pickle(self):
        problem = self.adapter.rs13_load_problem("rosenbr")
        self.assertEqual(pickle.loads(pickle.dumps(problem.reference)), problem.reference)

    def test_serial_and_two_spawn_workers_agree(self):
        names = ["rosenbr", "branin", "camel6"]
        expected = list(map(_worker_load, names))
        with multiprocessing.get_context("spawn").Pool(2) as pool:
            self.assertEqual(pool.map(_worker_load, names), expected)


if __name__ == "__main__":
    unittest.main()
