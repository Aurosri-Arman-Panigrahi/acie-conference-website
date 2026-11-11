"""
tests/e2e/run_all_tests.py
Standalone master test runner for ACIE 2027 E2E Test Suite.
Zero external dependencies required (uses built-in unittest, argparse, time, sys, pathlib).
Supports --tier, --feature, --filter, --verbose, --json, --md, and returns exit code 0 or 1.
"""
from __future__ import annotations
import argparse
import inspect
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
import unittest
from typing import Any, Dict, List, Optional, Tuple

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

class TestRecord:
    def __init__(self, test_id: str, name: str, tier: int, feature: str, doc: str):
        self.test_id = test_id
        self.name = name
        self.tier = tier
        self.feature = feature
        self.doc = doc.strip().split("\n")[0] if doc else ""
        self.status = "PENDING"
        self.duration = 0.0
        self.error_msg = ""
        self.traceback = ""

class E2ECustomResult(unittest.TestResult):
    def __init__(self, verbose: bool = False):
        super().__init__()
        self.verbose = verbose
        self.records: Dict[str, TestRecord] = {}
        self._start_times: Dict[str, float] = {}

    def register_test(self, test: unittest.TestCase, tier: int, feature: str):
        test_id = test.id()
        method_name = test._testMethodName
        method = getattr(test, method_name, None)
        doc = getattr(method, "__doc__", "") or ""
        self.records[test_id] = TestRecord(test_id, method_name, tier, feature, doc)

    def startTest(self, test: unittest.TestCase):
        super().startTest(test)
        self._start_times[test.id()] = time.perf_counter()

    def addSuccess(self, test: unittest.TestCase):
        super().addSuccess(test)
        t_id = test.id()
        dur = time.perf_counter() - self._start_times.get(t_id, time.perf_counter())
        if t_id in self.records:
            self.records[t_id].status = "PASS"
            self.records[t_id].duration = dur
        if self.verbose:
            print(f"  [PASS] {t_id} ({dur*1000:.1f}ms)")

    def addFailure(self, test: unittest.TestCase, err: Any):
        super().addFailure(test, err)
        t_id = test.id()
        dur = time.perf_counter() - self._start_times.get(t_id, time.perf_counter())
        if t_id in self.records:
            self.records[t_id].status = "FAIL"
            self.records[t_id].duration = dur
            self.records[t_id].error_msg = str(err[1])
            self.records[t_id].traceback = "".join(traceback.format_exception(*err))
        if self.verbose:
            print(f"  [FAIL] {t_id} ({dur*1000:.1f}ms) - {err[1]}")

    def addError(self, test: unittest.TestCase, err: Any):
        super().addError(test, err)
        t_id = test.id()
        dur = time.perf_counter() - self._start_times.get(t_id, time.perf_counter())
        if t_id in self.records:
            self.records[t_id].status = "ERROR"
            self.records[t_id].duration = dur
            self.records[t_id].error_msg = str(err[1])
            self.records[t_id].traceback = "".join(traceback.format_exception(*err))
        if self.verbose:
            print(f"  [ERROR] {t_id} ({dur*1000:.1f}ms) - {err[1]}")

    def addSkip(self, test: unittest.TestCase, reason: str):
        super().addSkip(test, reason)
        t_id = test.id()
        dur = time.perf_counter() - self._start_times.get(t_id, time.perf_counter())
        if t_id in self.records:
            self.records[t_id].status = "SKIP"
            self.records[t_id].duration = dur
            self.records[t_id].error_msg = reason
        if self.verbose:
            print(f"  [SKIP] {t_id} - {reason}")

def resolve_test_tier(test: unittest.TestCase) -> int:
    """Extract tier level from decorator attribute or method name fallback."""
    method_name = test._testMethodName
    method = getattr(test, method_name, None)
    if method:
        t = getattr(method, "__tier__", None)
        if t is not None:
            return int(t)
    m = re.search(r"t([1-4])", method_name.lower())
    if m:
        return int(m.group(1))
    class_name = test.__class__.__name__.lower()
    m_cls = re.search(r"tier([1-4])", class_name)
    if m_cls:
        return int(m_cls.group(1))
    return 1

def resolve_test_feature(test: unittest.TestCase) -> str:
    """Extract feature tag (r1..r5, pairwise, scenario) from decorator or module name."""
    method_name = test._testMethodName
    method = getattr(test, method_name, None)
    if method:
        f = getattr(method, "__feature__", None)
        if f:
            return ",".join(f) if isinstance(f, list) else str(f)
    module_name = test.__class__.__module__.lower()
    for req in ["r1", "r2", "r3", "r4", "r5"]:
        if req in module_name:
            return req
    return "general"

def render_ascii_table(headers: List[str], rows: List[List[str]]) -> str:
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    header_str = "| " + " | ".join(h.ljust(w) for h, w in zip(headers, col_widths)) + " |"
    lines = [sep, header_str, sep]
    for row in rows:
        lines.append("| " + " | ".join(str(val).ljust(w) for val, w in zip(row, col_widths)) + " |")
    lines.append(sep)
    return "\n".join(lines)

def generate_markdown_report(tier_stats: Dict[int, Any], records: Dict[str, TestRecord], total_duration: float) -> str:
    lines = [
        "# ACIE 2027 E2E Test Execution Summary",
        "",
        f"**Date**: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}  ",
        f"**Total Duration**: {total_duration:.2f}s  ",
        "",
        "## Tier Breakdown",
        "",
        "| Tier | Description | Total | Pass | Fail | Error | Skip | Duration | Pass Rate |",
        "|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|",
    ]
    tot_all = tot_pass = tot_fail = tot_err = tot_skip = 0
    for t_idx in [1, 2, 3, 4]:
        st = tier_stats[t_idx]
        tot_all += st["total"]
        tot_pass += st["pass"]
        tot_fail += st["fail"]
        tot_err += st["error"]
        tot_skip += st["skip"]
        executed = st["pass"] + st["fail"] + st["error"]
        rate = f"{(st['pass'] / executed * 100):.1f}%" if executed > 0 else "100.0%"
        lines.append(f"| Tier {t_idx} | {st['desc']} | {st['total']} | {st['pass']} | {st['fail']} | {st['error']} | {st['skip']} | {st['time']:.2f}s | {rate} |")

    tot_executed = tot_pass + tot_fail + tot_err
    overall_rate = f"{(tot_pass / tot_executed * 100):.1f}%" if tot_executed > 0 else "100.0%"
    lines.append(f"| **TOTAL** | **Complete E2E Suite** | **{tot_all}** | **{tot_pass}** | **{tot_fail}** | **{tot_err}** | **{tot_skip}** | **{total_duration:.2f}s** | **{overall_rate}** |")
    lines.append("")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="ACIE 2027 E2E Standalone Test Runner")
    parser.add_argument("--tier", choices=["1", "2", "3", "4", "all"], default="all", help="Execute specific tier only")
    parser.add_argument("--feature", choices=["r1", "r2", "r3", "r4", "r5", "all"], default="all", help="Execute specific feature only")
    parser.add_argument("--filter", type=str, default="", help="Regex filter on test ID/name")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose test-by-test output")
    parser.add_argument("--json", type=str, default="", help="Path to export JSON test report")
    parser.add_argument("--md", type=str, default="", help="Path to export Markdown test summary")
    args = parser.parse_args()

    tests_dir = PROJECT_ROOT / "tests" / "e2e"
    print("=" * 80)
    print(" ACIE 2027 E2E STANDALONE TEST SUITE RUNNER")
    print("=" * 80)
    print(f" Environment : Python {sys.version.split()[0]} on {sys.platform}")
    print(f" Project Dir : {PROJECT_ROOT}")
    print(f" Tests Dir   : {tests_dir}")
    print(f" Tier Filter : {args.tier.upper()}")
    print(f" Feat Filter : {args.feature.upper()}")
    print("=" * 80)

    loader = unittest.TestLoader()
    discovered_suite = loader.discover(str(tests_dir), pattern="test_*.py")

    result = E2ECustomResult(verbose=args.verbose)
    filtered_suite = unittest.TestSuite()

    target_tier = int(args.tier) if args.tier != "all" else None
    target_feat = args.feature.lower() if args.feature != "all" else None
    filter_re = re.compile(args.filter, re.IGNORECASE) if args.filter else None

    def extract_tests(suite: unittest.TestSuite):
        for item in suite:
            if isinstance(item, unittest.TestSuite):
                extract_tests(item)
            elif isinstance(item, unittest.TestCase):
                t_tier = resolve_test_tier(item)
                t_feat = resolve_test_feature(item)
                if target_tier and t_tier != target_tier:
                    continue
                if target_feat and target_feat not in t_feat.lower():
                    continue
                if filter_re and not filter_re.search(item.id()):
                    continue
                result.register_test(item, t_tier, t_feat)
                filtered_suite.addTest(item)

    extract_tests(discovered_suite)
    total_to_run = filtered_suite.countTestCases()
    print(f" Discovered and selected {total_to_run} test cases.")
    print("-" * 80)

    start_suite_time = time.perf_counter()
    filtered_suite.run(result)
    total_duration = time.perf_counter() - start_suite_time

    # Calculate metrics
    tier_stats = {
        1: {"desc": "Tier 1: Feature Coverage (R1-R5)", "total": 0, "pass": 0, "fail": 0, "error": 0, "skip": 0, "time": 0.0},
        2: {"desc": "Tier 2: Boundary & Corner Cases", "total": 0, "pass": 0, "fail": 0, "error": 0, "skip": 0, "time": 0.0},
        3: {"desc": "Tier 3: Cross-Feature Interactions", "total": 0, "pass": 0, "fail": 0, "error": 0, "skip": 0, "time": 0.0},
        4: {"desc": "Tier 4: Real-World Scenarios", "total": 0, "pass": 0, "fail": 0, "error": 0, "skip": 0, "time": 0.0},
    }

    for rec in result.records.values():
        t = rec.tier if rec.tier in tier_stats else 1
        tier_stats[t]["total"] += 1
        tier_stats[t]["time"] += rec.duration
        if rec.status == "PASS":
            tier_stats[t]["pass"] += 1
        elif rec.status == "FAIL":
            tier_stats[t]["fail"] += 1
        elif rec.status == "ERROR":
            tier_stats[t]["error"] += 1
        elif rec.status == "SKIP":
            tier_stats[t]["skip"] += 1

    table_headers = ["Tier", "Description", "Total", "Pass", "Fail", "Error", "Skip", "Duration", "Pass Rate"]
    table_rows = []
    tot_all = tot_pass = tot_fail = tot_err = tot_skip = 0

    for t_idx in [1, 2, 3, 4]:
        st = tier_stats[t_idx]
        tot_all += st["total"]
        tot_pass += st["pass"]
        tot_fail += st["fail"]
        tot_err += st["error"]
        tot_skip += st["skip"]
        executed = st["pass"] + st["fail"] + st["error"]
        rate = f"{(st['pass'] / executed * 100):.1f}%" if executed > 0 else "100.0%"
        table_rows.append([
            f"Tier {t_idx}",
            st["desc"],
            str(st["total"]),
            str(st["pass"]),
            str(st["fail"]),
            str(st["error"]),
            str(st["skip"]),
            f"{st['time']:.2f}s",
            rate
        ])

    tot_executed = tot_pass + tot_fail + tot_err
    overall_rate = f"{(tot_pass / tot_executed * 100):.1f}%" if tot_executed > 0 else "100.0%"
    table_rows.append([
        "TOTAL",
        "Complete E2E Test Suite",
        str(tot_all),
        str(tot_pass),
        str(tot_fail),
        str(tot_err),
        str(tot_skip),
        f"{total_duration:.2f}s",
        overall_rate
    ])

    print("\n" + render_ascii_table(table_headers, table_rows) + "\n")

    # Failures detail
    failures = [r for r in result.records.values() if r.status in ("FAIL", "ERROR")]
    if failures:
        print("=" * 80)
        print(f" FAILURES & ERRORS BREAKDOWN ({len(failures)} issues)")
        print("=" * 80)
        for idx, f in enumerate(failures, 1):
            print(f"\n[{idx}] {f.status}: {f.test_id}")
            print(f"    Description: {f.doc}")
            print(f"    Error: {f.error_msg}")
            if f.traceback:
                print("    Traceback:")
                for line in f.traceback.strip().split("\n"):
                    print(f"      {line}")
        print("=" * 80)

    # Optional exports
    if args.json:
        export_data = {
            "summary": {
                "total": tot_all, "pass": tot_pass, "fail": tot_fail,
                "error": tot_err, "skip": tot_skip, "duration": total_duration,
                "pass_rate": overall_rate
            },
            "tiers": tier_stats,
            "tests": {k: vars(v) for k, v in result.records.items()}
        }
        with open(args.json, "w", encoding="utf-8") as jf:
            json.dump(export_data, jf, indent=2)
        print(f" Test results exported to JSON: {args.json}")

    if args.md:
        md_content = generate_markdown_report(tier_stats, result.records, total_duration)
        with open(args.md, "w", encoding="utf-8") as mf:
            mf.write(md_content)
        print(f" Test summary exported to Markdown: {args.md}")

    exit_code = 0 if (tot_fail == 0 and tot_err == 0 and tot_all > 0) else 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
