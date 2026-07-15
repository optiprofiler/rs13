from pathlib import Path
import os
import sys
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rs13_tools import rs13_load_raw, rs13_problemdata


class RS13ProblemdataAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        required = ("RS13PM_DIR", "RS13_PROBLEMDATA_DIR")
        missing = [name for name in required if not os.environ.get(name)]
        if missing:
            raise RuntimeError(
                "RS13 upstream-data audit requires all official inputs; missing "
                + ", ".join(missing)
            )

    def test_problemdata_matches_raw_loader(self):
        for name in ["branin", "camel6", "convex1_10_1", "rosenbr"]:
            with self.subTest(name=name):
                raw = rs13_load_raw(name)
                data = rs13_problemdata(name)
                np.testing.assert_allclose(data["x0"], raw.x0)
                np.testing.assert_allclose(data["xmin"], raw.xmin)
                np.testing.assert_allclose(data["xmax"], raw.xmax)
                self.assertEqual(data["n"], raw.x0.size)


if __name__ == "__main__":
    unittest.main()
