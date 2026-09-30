#!/usr/bin/env python3
"""Normalize CTest/JUnit output into z0.evidence.v0."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET


_SCHEMA = "z0.evidence.v0"
_SHA = re.compile(r"^[0-9a-fA-F]{40}$")


def _test_result(case):
    if case.find("failure") is not None or case.find("error") is not None:
        return "fail"
    if case.find("skipped") is not None:
        return "unknown"
    return "pass"


def normalize_junit(root, *, revision, subject_id):
    if not _SHA.match(revision):
        raise ValueError("revision must be a full 40-character Git SHA")

    evidence = []
    for index, case in enumerate(root.iter("testcase")):
        name = case.get("name") or f"test-{index}"
        classname = case.get("classname") or ""
        evidence.append({
            "id": f"test-{index}",
            "kind": "ctest-case",
            "result": _test_result(case),
            "details": {
                "name": name,
                "classname": classname,
                "time_s": case.get("time"),
            },
        })

    results = [item["result"] for item in evidence]
    if "fail" in results:
        outcome = "fail"
    elif not results or "unknown" in results:
        outcome = "unknown"
    else:
        outcome = "pass"

    completeness = "pass" if evidence and "unknown" not in results else "unknown"
    return {
        "schema": _SCHEMA,
        "producer": {
            "name": "gz-sensors",
            "repository": "kvnloo/gz-sensors",
            "revision": revision,
        },
        "subject": {
            "kind": "ctest",
            "id": subject_id,
        },
        "outcome": outcome,
        "evidence": evidence,
        "invariants": [
            {
                "name": "focused-test-results-complete",
                "result": completeness,
                "evidence_refs": [item["id"] for item in evidence],
            }
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--junit", required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--subject", required=True)
    args = parser.parse_args()

    root = ET.parse(args.junit).getroot()
    receipt = normalize_junit(
        root,
        revision=args.revision,
        subject_id=args.subject,
    )
    json.dump(receipt, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
