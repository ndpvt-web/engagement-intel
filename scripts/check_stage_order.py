#!/usr/bin/env python3
"""Hard gate: portfolio stage order — no deep-dive before shortlist (unless single-target).

Exit 0 pass, 1 fail.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("run_root", type=Path)
    ap.add_argument(
        "--mode",
        choices=["portfolio", "single"],
        default="portfolio",
    )
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()
    root = args.run_root

    plan = root / "00-plan"
    discovery = root / "01-discovery"
    shortlist = root / "02-shortlist"
    deep = root / "03-deep-dives"
    preflight = root / "00-preflight" / "STATUS.md"

    issues = []
    if not (plan / "PARAMETERS.md").exists() and not (plan / "OFFER.md").exists():
        issues.append("S0 missing: need 00-plan/PARAMETERS.md or OFFER.md")

    if args.mode == "portfolio":
        if deep.exists() and any(deep.iterdir()):
            scored = list(shortlist.glob("*.md")) if shortlist.exists() else []
            universe = list(discovery.glob("*.md")) if discovery.exists() else []
            if not universe:
                issues.append("Deep-Dive First Tunnel: 03-deep-dives exists without 01-discovery")
            if not scored:
                issues.append("Deep-Dive First Tunnel: 03-deep-dives exists without 02-shortlist")
        if not preflight.exists():
            issues.append("Missing 00-preflight/STATUS.md before portfolio deep-dives")

    # Per deep-dive identity
    id_missing = []
    if deep.exists():
        for ent in sorted(p for p in deep.iterdir() if p.is_dir()):
            id_paths = [
                ent / "00-plan" / "IDENTITY.md",
                ent / "IDENTITY.md",
                root / "00-plan" / "IDENTITY.md",
            ]
            if not any(p.exists() for p in id_paths):
                id_missing.append(ent.name)
    if id_missing and args.mode == "portfolio":
        issues.append(f"Identity lock missing for deep-dives: {id_missing}")

    passed = len(issues) == 0
    result = {
        "gate": "stage_order",
        "mode": args.mode,
        "passed": passed,
        "issues": issues,
        "run_root": str(root),
    }
    print(json.dumps(result, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
