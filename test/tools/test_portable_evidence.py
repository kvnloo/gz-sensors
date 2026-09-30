import importlib.util
import pathlib
import unittest
import xml.etree.ElementTree as ET


_PATH = pathlib.Path(__file__).with_name("portable_evidence.py")


def _load():
    spec = importlib.util.spec_from_file_location("portable_evidence", _PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _xml(text):
    return ET.fromstring(text)


class PortableEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.module = _load()
        self.sha = "0123456789abcdef0123456789abcdef01234567"

    def test_all_executed_tests_pass(self):
        root = _xml(
            '<testsuite><testcase classname="dvl" name="static" time="0.1"/>'
            '<testcase classname="dvl" name="motion" time="0.2"/></testsuite>'
        )
        receipt = self.module.normalize_junit(
            root, revision=self.sha, subject_id="dvl-kinematics"
        )
        self.assertEqual(receipt["outcome"], "pass")
        self.assertEqual(receipt["invariants"][0]["result"], "pass")

    def test_failed_case_preserves_identity(self):
        root = _xml(
            '<testsuite><testcase classname="dvl" name="motion">'
            '<failure message="mismatch"/></testcase></testsuite>'
        )
        receipt = self.module.normalize_junit(
            root, revision=self.sha, subject_id="dvl-kinematics"
        )
        self.assertEqual(receipt["outcome"], "fail")
        self.assertEqual(receipt["evidence"][0]["details"]["name"], "motion")

    def test_skipped_case_keeps_run_unknown(self):
        root = _xml(
            '<testsuite><testcase classname="dvl" name="ogre">'
            '<skipped/></testcase></testsuite>'
        )
        receipt = self.module.normalize_junit(
            root, revision=self.sha, subject_id="dvl-kinematics"
        )
        self.assertEqual(receipt["outcome"], "unknown")

    def test_empty_report_is_unknown(self):
        receipt = self.module.normalize_junit(
            _xml("<testsuite/>"), revision=self.sha, subject_id="dvl-kinematics"
        )
        self.assertEqual(receipt["outcome"], "unknown")

    def test_requires_exact_revision(self):
        with self.assertRaises(ValueError):
            self.module.normalize_junit(
                _xml("<testsuite/>"), revision="main", subject_id="dvl"
            )


if __name__ == "__main__":
    unittest.main()
