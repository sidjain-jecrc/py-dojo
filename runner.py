#!/usr/bin/env python3
"""
Test runner for coding practice problems.
Usage: python runner.py <problem_name>
Example: python runner.py two_sum
"""

import sys
import importlib.util
import traceback
from pathlib import Path


def load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_tests(problem_name: str):
    problem_dir = Path("problems") / problem_name

    if not problem_dir.exists():
        print(f"Problem '{problem_name}' not found in problems/")
        sys.exit(1)

    solution_path = problem_dir / "solution.py"
    tests_path = problem_dir / "tests.py"

    if not solution_path.exists():
        print(f"Missing solution.py in problems/{problem_name}/")
        sys.exit(1)
    if not tests_path.exists():
        print(f"Missing tests.py in problems/{problem_name}/")
        sys.exit(1)

    # Load solution
    try:
        solution = load_module(solution_path, "solution")
    except Exception:
        print("Failed to load solution.py:\n")
        traceback.print_exc()
        sys.exit(1)

    # Load tests
    try:
        tests_mod = load_module(tests_path, "tests")
    except Exception:
        print("Failed to load tests.py:\n")
        traceback.print_exc()
        sys.exit(1)

    test_cases = tests_mod.TEST_CASES

    print(f"\n{'='*55}")
    print(f"  Problem: {problem_name.replace('_', ' ').title()}")
    print(f"{'='*55}")

    passed = 0
    failed = 0

    for i, tc in enumerate(test_cases, 1):
        description = tc.get("description", f"Test {i}")
        args = tc.get("args", [])
        kwargs = tc.get("kwargs", {})
        expected = tc["expected"]
        fn_name = tc.get("fn", "solve")

        fn = getattr(solution, fn_name, None)
        if fn is None:
            print(f"\n  [{i}] {description}")
            print(f"       SKIP — function '{fn_name}' not found in solution.py")
            failed += 1
            continue

        try:
            result = fn(*args, **kwargs)
            if result == expected:
                print(f"\n  [{i}] {description}")
                print(f"       PASS")
                passed += 1
            else:
                print(f"\n  [{i}] {description}")
                print(f"       FAIL")
                print(f"       Input:    {args if args else ''}{kwargs if kwargs else ''}")
                print(f"       Expected: {expected}")
                print(f"       Got:      {result}")
                failed += 1
        except NotImplementedError:
            print(f"\n  [{i}] {description}")
            print(f"       SKIP — solution not implemented yet")
            failed += 1
        except Exception:
            print(f"\n  [{i}] {description}")
            print(f"       ERROR")
            print(f"       Input:    {args if args else ''}{kwargs if kwargs else ''}")
            print(f"       Expected: {expected}")
            traceback.print_exc()
            failed += 1

    total = passed + failed
    print(f"\n{'='*55}")
    print(f"  Results: {passed}/{total} passed", end="")
    if failed == 0:
        print("  -- All tests passed!")
    else:
        print(f"  -- {failed} failed")
    print(f"{'='*55}\n")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py <problem_name>")
        print("Example: python runner.py two_sum")
        sys.exit(1)
    run_tests(sys.argv[1])
