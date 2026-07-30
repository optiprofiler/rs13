import unittest

from scripts.check_upstream_candidate import _defines_x0


class RS13CandidateInspectionTests(unittest.TestCase):
    def test_x0_assignment_is_detected(self):
        self.assertTrue(_defines_x0("x0 = [0.0, 1.0]\n"))
        self.assertTrue(_defines_x0("x0: list[float] = [0.0]\n"))
        self.assertFalse(_defines_x0("xmin = [0.0]\n"))


if __name__ == "__main__":
    unittest.main()
