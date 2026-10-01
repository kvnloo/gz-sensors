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

    def normalize(self, xml):
        return self.module.normalize_junit(
            _xml(xml), revision=self.sha, subject_id="dvl-kinematics"
        )

    def test_nonexecuted_google_test_cases_are_unknown(self):
        # The vendored GoogleTest emitter uses attributes, without a <skipped>
        # child, for disabled tests (src/gtest.cc: OutputXmlTestInfo).
        for attributes in (
            'status="notrun" result="suppressed"',
            'status="notrun"',
            'result="suppressed"',
            'status="run" result="skipped"',
            'status="unrecognized"',
            'result="unrecognized"',
        ):
            with self.subTest(attributes=attributes):
                receipt = self.normalize(
                    f'<testsuite><testcase name="disabled" {attributes}/>'
                    '</testsuite>'
                )
                self.assertEqual(receipt["outcome"], "unknown")
                self.assertEqual(receipt["evidence"][0]["result"], "unknown")
                self.assertEqual(receipt["invariants"][0]["result"], "unknown")

    def test_executed_google_test_case_passes(self):
        receipt = self.normalize(
            '<testsuite tests="1" failures="0" errors="0" skipped="0">'
            '<testcase name="static" status="run" result="completed"/>'
            '</testsuite>'
        )
        self.assertEqual(receipt["outcome"], "pass")

    def test_explicit_failure_wins_over_nonexecuted_attributes(self):
        for child in ("failure", "error"):
            with self.subTest(child=child):
                receipt = self.normalize(
                    '<testsuite><testcase name="motion" status="notrun" '
                    f'result="suppressed"><{child}/></testcase></testsuite>'
                )
                self.assertEqual(receipt["outcome"], "fail")
                self.assertEqual(receipt["evidence"][0]["details"]["name"], "motion")

    def test_summary_cannot_hide_missing_test_results(self):
        for attributes in (
            'tests="2"',
            'tests="0"',
            'failures="1"',
            'errors="1"',
            'skipped="1"',
        ):
            with self.subTest(attributes=attributes):
                receipt = self.normalize(
                    f'<testsuite {attributes}><testcase name="static"/>'
                    '</testsuite>'
                )
                self.assertEqual(receipt["outcome"], "unknown")
                self.assertEqual(receipt["invariants"][0]["result"], "unknown")
                # Retain the result we do have, without inventing missing cases.
                self.assertEqual(len(receipt["evidence"]), 1)
                self.assertEqual(receipt["evidence"][0]["result"], "pass")

    def test_malformed_summary_is_unknown(self):
        for attribute in ("tests", "failures", "errors", "skipped"):
            for value in ("", "-1", "1.0", "invalid", "1" * 5000):
                with self.subTest(attribute=attribute, value=value):
                    receipt = self.normalize(
                        f'<testsuite {attribute}="{value}">'
                        '<testcase name="static"/></testsuite>'
                    )
                    self.assertEqual(receipt["outcome"], "unknown")

    def test_missing_results_do_not_hide_an_explicit_failure(self):
        receipt = self.normalize(
            '<testsuite tests="2"><testcase name="motion">'
            '<failure/></testcase></testsuite>'
        )
        self.assertEqual(receipt["outcome"], "fail")
        self.assertEqual(receipt["invariants"][0]["result"], "unknown")

    def test_nested_summary_counts_each_case_once(self):
        receipt = self.normalize(
            '<testsuites tests="2" failures="0">'
            '<testsuite tests="1"><testcase name="static"/></testsuite>'
            '<testsuite tests="1"><testcase name="motion"/></testsuite>'
            '</testsuites>'
        )
        self.assertEqual(receipt["outcome"], "pass")
        self.assertEqual(len(receipt["evidence"]), 2)

    def test_outer_summary_detects_an_omitted_suite(self):
        receipt = self.normalize(
            '<testsuites tests="2"><testsuite tests="1">'
            '<testcase name="static"/></testsuite></testsuites>'
        )
        self.assertEqual(receipt["outcome"], "unknown")

    def test_failure_count_counts_cases_not_assertions(self):
        receipt = self.normalize(
            '<testsuite tests="1" failures="1"><testcase name="motion">'
            '<failure/><failure/></testcase></testsuite>'
        )
        self.assertEqual(receipt["outcome"], "fail")
        self.assertEqual(receipt["invariants"][0]["result"], "pass")

    def test_disabled_case_that_was_explicitly_run_can_pass(self):
        # --gtest_also_run_disabled_tests retains the disabled summary count.
        receipt = self.normalize(
            '<testsuite tests="1" disabled="1"><testcase name="DISABLED_static" '
            'status="run" result="completed"/></testsuite>'
        )
        self.assertEqual(receipt["outcome"], "pass")

    def test_revision_rejects_trailing_newline_and_nonstrings(self):
        for revision in (self.sha + "\n", self.sha + " ", None, 1):
            with self.subTest(revision=revision):
                with self.assertRaises(ValueError):
                    self.module.normalize_junit(
                        _xml("<testsuite/>"), revision=revision, subject_id="dvl"
                    )

    def test_requires_exact_revision(self):
        with self.assertRaises(ValueError):
            self.module.normalize_junit(
                _xml("<testsuite/>"), revision="main", subject_id="dvl"
            )


if __name__ == "__main__":
    unittest.main()
