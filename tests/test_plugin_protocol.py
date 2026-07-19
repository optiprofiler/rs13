from __future__ import annotations

from importlib import metadata
import multiprocessing
import os
import unittest
from unittest import mock


IMPORT_ERROR = None
try:
    import optiprofiler_rs13
    from optiprofiler.problem_libraries import (
        PROBLEM_LIBRARY_ENTRY_POINT_GROUP,
        ProblemLibraryRef,
        _resolve_problem_library_options,
        load_problem_library,
    )
except Exception as exc:  # pragma: no cover - exercised before installation.
    IMPORT_ERROR = exc


def _spawn_select_rs13(problem_options, library_options):
    import optiprofiler_rs13

    return optiprofiler_rs13.get_problem_library().select(
        problem_options,
        library_options,
    )


@unittest.skipIf(IMPORT_ERROR is not None, f"Plugin package is not installed: {IMPORT_ERROR}")
class RS13PluginProtocolTests(unittest.TestCase):
    def test_entry_point_metadata_is_installed(self):
        entry_points = metadata.entry_points()
        if hasattr(entry_points, "select"):
            selected = entry_points.select(group=PROBLEM_LIBRARY_ENTRY_POINT_GROUP)
        else:
            selected = entry_points.get(PROBLEM_LIBRARY_ENTRY_POINT_GROUP, [])
        values = {entry_point.name: entry_point.value for entry_point in selected}
        self.assertEqual(values.get("rs13"), "optiprofiler_rs13:get_problem_library")

    def test_factory_is_api_v1_and_declares_no_library_options(self):
        plugin = optiprofiler_rs13.get_problem_library()
        self.assertEqual(plugin.name, "rs13")
        self.assertEqual(plugin.api_version, 1)
        self.assertIsNotNone(plugin.check_available)
        self.assertIsNone(plugin.get_default_options)
        self.assertIsNone(plugin.validate_options)
        self.assertEqual(_resolve_problem_library_options(plugin), {})
        with self.assertRaises(ValueError):
            _resolve_problem_library_options(plugin, {"source_dir": "/tmp/rs13"})

    def test_factory_uses_bundled_runtime_without_environment(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            plugin = optiprofiler_rs13.get_problem_library()
            self.assertEqual(plugin.name, "rs13")
            plugin.check_available()
            problem = plugin.load("branin", {})
            self.assertEqual(problem.n, 2)
            self.assertAlmostEqual(
                float(problem.fun(problem.x0)),
                24.129964413622268,
            )

    def test_entry_point_reference_loads_and_uses_empty_options(self):
        reference = ProblemLibraryRef(
            "rs13",
            "entry_point",
            "optiprofiler_rs13:get_problem_library",
            distribution="optiprofiler-rs13",
        )
        plugin = load_problem_library(reference)
        selected = plugin.select({"ptype": "u", "mindim": 2, "maxdim": 2}, {})
        self.assertIn("rosenbr", selected)
        with self.assertRaises(ValueError):
            optiprofiler_rs13.rs13_select({}, {"source_dir": "/tmp/rs13"})

    def test_api_v1_callbacks_work_in_spawned_process(self):
        with multiprocessing.get_context("spawn").Pool(1) as pool:
            selected = pool.apply(
                _spawn_select_rs13,
                ({"ptype": "u", "mindim": 2, "maxdim": 2}, {}),
            )
        self.assertIn("rosenbr", selected)


if __name__ == "__main__":
    unittest.main()
