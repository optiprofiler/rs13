"""Offline collector must evaluate the same source it fingerprints."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock


@unittest.skipUnless(os.environ.get("RS13_REFERENCE_SOLUTIONS_ARCHIVE"),
                     "Requires the pinned official solution archive for offline audit")
class CollectorSourceTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location("rs13_reference_collector", root / "scripts/collect_references.py")
        self.collector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.collector)
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.trusted = self.root / "trusted"
        self.override = self.root / "override"
        self.trusted.mkdir()
        self.override.mkdir()
        source = root / "runtime/rs13pm/rosenbr.py"
        shutil.copyfile(source, self.trusted / source.name)
        text = source.read_text()
        self.assertIn("return f", text)
        (self.override / source.name).write_text(text.replace("return f", "return f - 1000.0"))

    def collect(self):
        output = self.root / "references.json"
        report = self.root / "report.json"
        args = ["collect_references.py", "--solutions-archive", os.environ["RS13_REFERENCE_SOLUTIONS_ARCHIVE"],
                "--output", str(output), "--report", str(report)]
        with mock.patch.object(self.collector.adapter, "VENDORED_RS13PM_DIR", self.trusted), \
                mock.patch.object(sys, "argv", args), \
                mock.patch.dict(os.environ, {"RS13PM_DIR": str(self.override)}):
            self.collector.main()
        return json.loads(output.read_text()), json.loads(report.read_text())

    def test_environment_override_cannot_poison_vendored_reference(self):
        catalog, report = self.collect()
        self.assertEqual(report["accepted"], 1)
        value = catalog["records"]["rosenbr"]["reference"]["fun"]
        self.assertGreaterEqual(value, 0.0, "The f-1000 override was mislabeled with the trusted source hash")
        self.assertAlmostEqual(value, 1.236405056073363e-7, places=14)

    def test_record_holds_raw_feasible_values_only(self):
        catalog, _ = self.collect()
        reference = catalog["records"]["rosenbr"]["reference"]
        self.assertEqual(set(reference), {"fun", "maxcv", "kind", "source"})
        self.assertEqual((reference["maxcv"], reference["kind"]), (0.0, "feasible"))

    def test_value_no_better_than_the_initial_point_is_rejected(self):
        # Official files for these problems repeat x0 or are worse than it.
        root = Path(__file__).resolve().parents[1]
        for name in ("convex1_10_1", "problem2.17"):
            shutil.copyfile(root / f"runtime/rs13pm/{name}.py", self.trusted / f"{name}.py")
        catalog, report = self.collect()
        self.assertEqual(sorted(catalog["records"]), ["rosenbr"])
        reasons = {item["name"]: item.get("reason", "") for item in report["records"]}
        for name in ("convex1_10_1", "problem2.17"):
            self.assertIn("not_better_than_initial_point", reasons[name])

    def test_wrong_actual_raw_source_is_rejected(self):
        real_loader = self.collector.adapter.rs13_load_raw

        def wrong_identity(*args, **kwargs):
            raw = real_loader(*args, **kwargs)
            raw.source_path = self.override / "rosenbr.py"
            return raw

        with mock.patch.object(self.collector.adapter, "rs13_load_raw", side_effect=wrong_identity):
            catalog, report = self.collect()
        self.assertEqual(catalog["records"], {})
        self.assertEqual(report["rejected"], 1)
        self.assertIn("source_identity_mismatch", report["records"][0]["reason"])


if __name__ == "__main__":
    unittest.main()
