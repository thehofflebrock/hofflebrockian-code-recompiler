"""Sealed evaluator for the HCR v0.1 toy order-quote trial.

Keep this file outside both builder workspaces. It compares candidate behavior
against the legacy substrate over fixed edge cases and seeded randomized cases,
then reports simple structural and timing evidence.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
from pathlib import Path
import random
import statistics
import subprocess
import sys
import time


TOY_ROOT = Path(__file__).resolve().parents[1]


def load_quote(path: Path):
    spec = importlib.util.spec_from_file_location(f"hcr_{path.parent.name}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.quote_order


def outcome(function, case):
    args, kwargs = case
    try:
        return {"kind": "return", "value": function(*args, **kwargs)}
    except Exception as exc:  # Exact observable failure behavior is compared.
        return {
            "kind": "error",
            "type": type(exc).__name__,
            "message": str(exc),
        }


def fixed_cases():
    return [
        ((0, 1, "US"), {}),
        ((2499, 1, "US"), {"promo_code": "FREESHIP"}),
        ((2500, 1, "US"), {"promo_code": " freeship "}),
        ((4999, 9, " us "), {}),
        ((5000, 10, "us"), {}),
        ((1000, 1, "US"), {"promo_code": "halfship", "member": True}),
        ((5000, 1, "US"), {"expedited": True}),
        ((2500, 10, "US"), {"expedited": True, "promo_code": "FREESHIP"}),
        ((7499, 1, "CA"), {"member": True}),
        ((7500, 10, " ca "), {"member": True}),
        ((8000, 1, "CA"), {"expedited": True, "promo_code": "HALFSHIP", "member": True}),
        ((1000, 1, "CA"), {"promo_code": "FREESHIP"}),
        ((1000, 1, "INTL"), {"promo_code": "HALFSHIP", "member": True}),
        ((1000, 10, " intl "), {"promo_code": "UNKNOWN"}),
        ((1000, 1, "INTL"), {"expedited": True}),
        ((-1, 1, "US"), {}),
        ((True, 1, "US"), {}),
        ((1.5, 1, "US"), {}),
        ((1000, 0, "US"), {}),
        ((1000, 51, "US"), {}),
        ((1000, False, "US"), {}),
        ((1000, 1.2, "US"), {}),
        ((1000, 1, None), {}),
        ((1000, 1, "EU"), {}),
        ((1000, 1, "US"), {"member": 1}),
        ((1000, 1, "US"), {"expedited": 0}),
        ((1000, 1, "US"), {"promo_code": 7}),
        ((1000, 50, "CA"), {"member": True, "promo_code": ""}),
    ]


def randomized_cases(count: int, seed: int = 8612):
    rng = random.Random(seed)
    subtotals = [0, 1, 2499, 2500, 4999, 5000, 7499, 7500, 10000]
    items = [1, 2, 9, 10, 11, 49, 50]
    regions = ["US", " us ", "CA", "ca", "INTL", " intl "]
    promos = [None, "FREESHIP", " freeship ", "HALFSHIP", "halfship", "UNKNOWN", ""]
    cases = []
    for _ in range(count):
        subtotal = rng.choice(subtotals + [rng.randint(0, 20000)])
        item_count = rng.choice(items + [rng.randint(1, 50)])
        region = rng.choice(regions)
        kwargs = {
            "member": rng.choice([False, True]),
            "expedited": rng.choice([False, True]),
            "promo_code": rng.choice(promos),
        }
        cases.append(((subtotal, item_count, region), kwargs))
    return cases


def compare(reference, candidate, cases, sample_limit=8):
    mismatches = []
    total = 0
    for case in cases:
        total += 1
        expected = outcome(reference, case)
        actual = outcome(candidate, case)
        if expected != actual and len(mismatches) < sample_limit:
            mismatches.append(
                {"args": case[0], "kwargs": case[1], "expected": expected, "actual": actual}
            )
        elif expected != actual:
            mismatches.append(None)
    return {
        "cases": total,
        "mismatch_count": len(mismatches),
        "samples": [item for item in mismatches if item is not None],
    }


def source_metrics(path: Path):
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text)
    source_lines = sum(
        1
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
    branch_score = 1
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.IfExp, ast.For, ast.AsyncFor, ast.While)):
            branch_score += 1
        elif isinstance(node, ast.BoolOp):
            branch_score += max(1, len(node.values) - 1)
        elif isinstance(node, ast.Try):
            branch_score += len(node.handlers) + int(bool(node.orelse)) + int(bool(node.finalbody))
        elif isinstance(node, ast.Match):
            branch_score += len(node.cases)
        elif isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            branch_score += len(node.generators)
        elif isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    return {
        "source_lines": source_lines,
        "branch_score": branch_score,
        "imports": sorted(set(imports)),
    }


def visible_test_result(workspace: Path):
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=workspace,
        text=True,
        capture_output=True,
        check=False,
    )
    combined = (completed.stdout + "\n" + completed.stderr).strip()
    return {"exit_status": completed.returncode, "output": combined[-3000:]}


def benchmark(function, repeats=5, calls=10000):
    cases = [
        ((1000, 1, "US"), {}),
        ((5000, 10, "US"), {}),
        ((8000, 1, "CA"), {"member": True}),
        ((1000, 1, "CA"), {"expedited": True, "promo_code": "HALFSHIP"}),
        ((1000, 10, "INTL"), {"promo_code": "HALFSHIP"}),
    ]
    samples = []
    try:
        for _ in range(repeats):
            start = time.perf_counter()
            for index in range(calls):
                args, kwargs = cases[index % len(cases)]
                function(*args, **kwargs)
            samples.append((time.perf_counter() - start) * 1_000_000 / calls)
    except Exception as exc:
        return f"error:{type(exc).__name__}:{exc}"
    return round(statistics.median(samples), 3)


def markdown_report(report):
    lines = [
        "# Toy Trial Audit Results",
        "",
        f"Audit cases per candidate: {report['audit_case_count']}",
        "",
        "| Candidate | Visible tests | Mismatches | Source lines | Branch score | Imports | Median us/call |",
        "|---|---:|---:|---:|---:|---|---:|",
    ]
    for name in ("legacy", "control", "blind"):
        item = report[name]
        visible = "baseline" if name == "legacy" else ("pass" if item["visible_tests"]["exit_status"] == 0 else "fail")
        lines.append(
            f"| {name} | {visible} | {item['comparison']['mismatch_count']} | "
            f"{item['metrics']['source_lines']} | {item['metrics']['branch_score']} | "
            f"{', '.join(item['metrics']['imports']) or 'none'} | {item['median_microseconds_per_call']} |"
        )
    lines.extend(["", "## Mismatch samples", ""])
    for name in ("control", "blind"):
        samples = report[name]["comparison"]["samples"]
        lines.append(f"### {name}")
        lines.append("")
        if not samples:
            lines.append("No mismatches detected.")
        else:
            lines.append("```json")
            lines.append(json.dumps(samples, indent=2, sort_keys=True))
            lines.append("```")
        lines.append("")
    lines.append("These measures are audit evidence, not an automatic promotion decision.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-root", type=Path, default=TOY_ROOT / "runs")
    parser.add_argument("--random-cases", type=int, default=2000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    runs_root = args.runs_root.expanduser().resolve()
    paths = {
        "legacy": TOY_ROOT / "legacy" / "order_quote.py",
        "control": runs_root / "control" / "order_quote.py",
        "blind": runs_root / "blind" / "order_quote.py",
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise SystemExit("missing candidate file(s):\n" + "\n".join(missing))

    functions = {name: load_quote(path) for name, path in paths.items()}
    cases = fixed_cases() + randomized_cases(args.random_cases)
    reference = functions["legacy"]

    report = {"audit_case_count": len(cases)}
    for name in ("legacy", "control", "blind"):
        workspace = runs_root / name if name != "legacy" else None
        report[name] = {
            "comparison": compare(reference, functions[name], cases),
            "metrics": source_metrics(paths[name]),
            "median_microseconds_per_call": benchmark(functions[name]),
            "visible_tests": (
                {"exit_status": 0, "output": "legacy behavior is the comparison substrate"}
                if workspace is None
                else visible_test_result(workspace)
            ),
        }

    rendered = markdown_report(report)
    print(rendered)
    if args.output:
        output = args.output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        output.with_suffix(".json").write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
