#!/usr/bin/env python3
"""Validate PM-Codex markdown artifacts for basic traceability IDs.

Usage:
    python scripts/validate_pm_artifacts.py docs/**/*.md
    python scripts/validate_pm_artifacts.py PRD.md TASKS.md

This script intentionally performs lightweight checks only:
- Detects Goal Lock, REQ, US, AC, TASK, PR references.
- Warns when TASK IDs exist but no AC IDs exist.
- Warns when AC IDs exist but no REQ IDs exist.
- Prints a compact ID inventory for human/Codex review.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

PATTERNS = {
    "GL": re.compile(r"\bGL-\d{3,}\b"),
    "REQ": re.compile(r"\bREQ-\d{3,}\b"),
    "US": re.compile(r"\bUS-\d{3,}\b"),
    "AC": re.compile(r"\bAC-\d{3,}\b"),
    "TASK": re.compile(r"\bTASK-\d{3,}\b"),
    "PR": re.compile(r"\bPR-\d{3,}\b"),
}


def collect_ids(path: Path) -> dict[str, set[str]]:
    text = path.read_text(encoding="utf-8")
    return {name: set(pattern.findall(text)) for name, pattern in PATTERNS.items()}


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python scripts/validate_pm_artifacts.py <markdown files>")
        return 2

    overall: dict[str, set[str]] = defaultdict(set)
    file_results: list[tuple[Path, dict[str, set[str]]]] = []

    for raw in argv:
        for item in sorted(Path().glob(raw)) if any(ch in raw for ch in "*?[]") else [Path(raw)]:
            if not item.exists() or not item.is_file():
                print(f"WARN: missing file: {item}")
                continue
            ids = collect_ids(item)
            file_results.append((item, ids))
            for kind, values in ids.items():
                overall[kind].update(values)

    print("# PM Artifact ID Inventory")
    for path, ids in file_results:
        summary = ", ".join(f"{kind}:{len(values)}" for kind, values in ids.items() if values)
        print(f"- {path}: {summary or 'no IDs found'}")

    print("\n# Overall")
    for kind in PATTERNS:
        values = sorted(overall[kind])
        print(f"- {kind}: {len(values)} {' '.join(values[:20])}")

    warnings: list[str] = []
    if overall["TASK"] and not overall["AC"]:
        warnings.append("TASK IDs exist but no AC IDs were found. Tasks may lack acceptance criteria.")
    if overall["AC"] and not overall["REQ"]:
        warnings.append("AC IDs exist but no REQ IDs were found. Acceptance criteria may not trace to requirements.")
    if overall["REQ"] and not overall["GL"]:
        warnings.append("REQ IDs exist but no Goal Lock ID was found. Requirements may not trace to original goal.")

    if warnings:
        print("\n# Warnings")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print("\nNo basic traceability warnings found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
