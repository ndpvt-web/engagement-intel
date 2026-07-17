#!/usr/bin/env python3
"""Hard gate S3: Identity lock must pass before twin/sim.

Exit 0 = pass, 1 = fail. Prints JSON summary.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "legal_name",
    "primary_brand",
    "dm_name",
    "dm_role",
    "primary_site",
]

# Accept either key: value lines or markdown bold labels
FIELD_PATTERNS = {
    "legal_name": re.compile(r"(?i)legal\s*name\s*[:\|]\s*(.+)"),
    "primary_brand": re.compile(r"(?i)primary\s*brand\s*[:\|]\s*(.+)"),
    "dm_name": re.compile(r"(?i)(?:dm|decision[\s-]*maker)\s*name\s*[:\|]\s*(.+)"),
    "dm_role": re.compile(r"(?i)(?:dm|decision[\s-]*maker)\s*role\s*[:\|]\s*(.+)"),
    "primary_site": re.compile(r"(?i)primary\s*site\s*[:\|]\s*(.+)"),
    "linkedin_slug": re.compile(r"(?i)linkedin\s*(?:slug|url|handle)?\s*[:\|]\s*(.+)"),
    "x_handle": re.compile(r"(?i)(?:x|twitter)\s*handle\s*[:\|]\s*(.+)"),
}


def parse_identity(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    # Markdown table rows: | legal_name | Acme Analytics Limited |
    table_row = re.compile(
        r"(?im)^\|\s*(legal_name|primary_brand|primary_site|dm_name|dm_role|"
        r"linkedin_slug|x_handle|youtube)\s*\|\s*([^|]+)\|"
    )
    for m in table_row.finditer(text):
        key = m.group(1).lower()
        val = m.group(2).strip().strip("*").strip()
        if val and val.lower() not in ("unknown", "tbd", "n/a", "-", "todo", "value"):
            found[key] = val
    for key, pat in FIELD_PATTERNS.items():
        if key in found:
            continue
        m = pat.search(text)
        if m:
            val = m.group(1).strip().strip("*").strip()
            # strip trailing table pipes
            val = val.split("|")[0].strip()
            if val and val.lower() not in ("unknown", "tbd", "n/a", "-", "todo", "value"):
                found[key] = val
    # Heuristic: "## Decision maker" section with a name line
    if "dm_name" not in found:
        m = re.search(
            r"(?im)^(?:##?\s*)?(?:decision\s*maker|primary\s*dm|dm)\s*[:\-]?\s*(.+)$",
            text,
        )
        if m:
            found["dm_name"] = m.group(1).strip()
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("identity_path", type=Path, help="Path to IDENTITY.md")
    ap.add_argument("--require-linkedin", action="store_true")
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()

    if not args.identity_path.exists():
        result = {
            "gate": "identity_lock",
            "passed": False,
            "reason": f"missing file: {args.identity_path}",
            "fields": {},
            "missing": REQUIRED_FIELDS,
        }
        print(json.dumps(result, indent=2))
        if args.json_out:
            args.json_out.write_text(json.dumps(result, indent=2))
        return 1

    text = args.identity_path.read_text(encoding="utf-8", errors="replace")
    fields = parse_identity(text)
    missing = [f for f in REQUIRED_FIELDS if f not in fields]
    if args.require_linkedin and "linkedin_slug" not in fields:
        missing.append("linkedin_slug")

    # Wrong-slug warning presence is optional but good
    has_wrong_slug_section = bool(
        re.search(r"(?i)wrong[\s-]*slug|doppelg[aä]nger|not\s+to\s+use", text)
    )

    passed = len(missing) == 0
    result = {
        "gate": "identity_lock",
        "passed": passed,
        "fields": fields,
        "missing": missing,
        "has_wrong_slug_warnings": has_wrong_slug_section,
        "path": str(args.identity_path),
    }
    if not passed:
        result["reason"] = f"missing required fields: {missing}"
    print(json.dumps(result, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
