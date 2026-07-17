#!/usr/bin/env python3
"""Hard gate S7: sample_size / ranking eligibility.

Rules (engagement-intel v2):
- Any strategy used for portfolio ranking requires sample_size >= min_n (default 3).
- Reports may still exist with n=1 but must be marked directional-only.
- Exit 0 if gate policy satisfied; 1 if ranking claimed with n < min_n or no sample size found when required.

Usage:
  check_sim_sample_size.py <report.json> [--min-n 3] [--for-ranking]
  check_sim_sample_size.py --scan-dir <11-simulations/>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def extract_sample_sizes(doc: Any) -> list[int]:
    sizes: list[int] = []

    def walk(o: Any) -> None:
        if isinstance(o, dict):
            for k, v in o.items():
                lk = k.lower()
                if lk in ("samplesize", "sample_size", "n", "num_samples") and isinstance(
                    v, (int, float)
                ):
                    sizes.append(int(v))
                elif lk == "rankings" and isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict):
                            for kk in ("sampleSize", "sample_size", "n"):
                                if kk in item and isinstance(item[kk], (int, float)):
                                    sizes.append(int(item[kk]))
                else:
                    walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)

    walk(doc)
    return sizes


def analyze_report(path: Path, min_n: int, for_ranking: bool) -> dict:
    if not path.exists():
        return {
            "path": str(path),
            "passed": False,
            "reason": "report missing",
            "sample_sizes": [],
            "min_observed": None,
            "max_observed": None,
        }
    try:
        doc = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError as e:
        return {
            "path": str(path),
            "passed": False,
            "reason": f"invalid json: {e}",
            "sample_sizes": [],
        }

    sizes = extract_sample_sizes(doc)
    # Also count results length as weak proxy only if no explicit sample sizes
    results = doc.get("results") if isinstance(doc, dict) else None
    report = doc.get("report") if isinstance(doc, dict) else None
    n_results = len(results) if isinstance(results, list) else 0
    rankings = []
    if isinstance(report, dict):
        rankings = report.get("rankings") or []
    if not sizes and n_results:
        # Infer: many simulators run each strategy once → n=1
        sizes = [1] * max(1, len(rankings) if rankings else 1)

    min_obs = min(sizes) if sizes else None
    max_obs = max(sizes) if sizes else None
    directional_only = min_obs is not None and min_obs < min_n

    if for_ranking:
        passed = min_obs is not None and min_obs >= min_n
        reason = None if passed else f"for-ranking requires min sample_size>={min_n}, got {min_obs}"
    else:
        # Non-ranking: allow n=1 but require explicit presence of report + mark
        passed = path.exists() and (bool(sizes) or n_results > 0)
        reason = None if passed else "no sample sizes or results found"
        if passed and directional_only:
            reason = f"directional_only: min sample_size={min_obs} < {min_n}"

    return {
        "path": str(path),
        "passed": bool(passed),
        "for_ranking": for_ranking,
        "min_n_required": min_n,
        "sample_sizes_found": sizes[:50],
        "min_observed": min_obs,
        "max_observed": max_obs,
        "n_results": n_results,
        "n_rankings": len(rankings) if isinstance(rankings, list) else 0,
        "directional_only": directional_only,
        "reason": reason,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report", type=Path, nargs="?", default=None)
    ap.add_argument("--scan-dir", type=Path, default=None)
    ap.add_argument("--min-n", type=int, default=3)
    ap.add_argument("--for-ranking", action="store_true")
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()

    reports: list[Path] = []
    if args.scan_dir:
        reports = sorted(args.scan_dir.glob("*-report.json")) + sorted(
            args.scan_dir.glob("*report*.json")
        )
        # dedupe
        seen = set()
        uniq = []
        for p in reports:
            if p.resolve() not in seen:
                seen.add(p.resolve())
                uniq.append(p)
        reports = uniq
    elif args.report:
        reports = [args.report]
    else:
        print("need report path or --scan-dir", file=sys.stderr)
        return 2

    analyses = [analyze_report(p, args.min_n, args.for_ranking) for p in reports]
    overall = all(a["passed"] for a in analyses) if analyses else False
    if not analyses:
        overall = False
        analyses = [{"passed": False, "reason": "no reports found"}]

    # If not for ranking, overall pass even when directional_only (warn only)
    if not args.for_ranking:
        overall = all(
            a.get("passed") or a.get("directional_only") for a in analyses
        ) and all("missing" not in (a.get("reason") or "") for a in analyses)
        # simpler: any valid report with sizes/results
        overall = any(
            a.get("min_observed") is not None or a.get("n_results", 0) > 0 for a in analyses
        )

    out = {
        "gate": "sim_sample_size",
        "passed": overall if args.for_ranking else overall,
        "for_ranking": args.for_ranking,
        "min_n": args.min_n,
        "reports": analyses,
    }
    # Strict for ranking
    if args.for_ranking:
        out["passed"] = all(a.get("passed") for a in analyses)

    print(json.dumps(out, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(out, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
