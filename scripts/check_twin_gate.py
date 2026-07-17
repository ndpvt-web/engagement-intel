#!/usr/bin/env python3
"""Hard gate S6: twin files + SOURCE_MAP + tier before sim.

Exit 0 pass, 1 fail.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("twin_dir", type=Path, help=".../10-digital-twin/")
    ap.add_argument("--allow-t1-sim", action="store_true", help="Allow T1 with waiver file")
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()

    twin = args.twin_dir / "TWIN.md"
    prospect = args.twin_dir / "prospect.json"
    source_map = args.twin_dir / "SOURCE_MAP.md"
    waiver = args.twin_dir.parent / "SIM_WAIVER.md"

    missing = []
    for p, label in [
        (twin, "TWIN.md"),
        (prospect, "prospect.json"),
        (source_map, "SOURCE_MAP.md"),
    ]:
        if not p.exists() or p.stat().st_size < 40:
            missing.append(label)

    tier = None
    if twin.exists():
        text = twin.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"(?i)\btier\s*[:\-]?\s*(T[123])\b", text)
        if m:
            tier = m.group(1).upper()
        else:
            m2 = re.search(r"\b(T[123])\b", text)
            if m2:
                tier = m2.group(1).upper()

    source_map_ok = source_map.exists() and source_map.stat().st_size >= 20
    # At least one path-like citation or explicit mapping line
    if source_map_ok:
        sm = source_map.read_text(encoding="utf-8", errors="replace")
        source_map_ok = bool(
            re.search(
                r"\.(md|json|html|txt)\b|https?://|outputs/|01-company|02-people|<-|→|->",
                sm,
            )
        )

    sim_allowed = False
    reason_bits = []
    if missing:
        reason_bits.append(f"missing: {missing}")
    if not tier:
        reason_bits.append("tier not declared in TWIN.md (need T1/T2/T3)")
    if not source_map_ok:
        reason_bits.append("SOURCE_MAP missing or lacks citations")

    if not missing and source_map_ok and tier in ("T2", "T3"):
        sim_allowed = True
    elif not missing and source_map_ok and tier == "T1":
        if args.allow_t1_sim and waiver.exists():
            sim_allowed = True
            reason_bits.append("T1 allowed via SIM_WAIVER.md")
        else:
            reason_bits.append("T1 twin cannot run expensive sim without SIM_WAIVER.md")

    # prospect.json parse check
    prospect_ok = False
    if prospect.exists():
        try:
            json.loads(prospect.read_text(encoding="utf-8"))
            prospect_ok = True
        except json.JSONDecodeError as e:
            reason_bits.append(f"prospect.json invalid: {e}")
            sim_allowed = False

    passed = sim_allowed and prospect_ok and not missing
    result = {
        "gate": "twin",
        "passed": passed,
        "sim_allowed": sim_allowed,
        "tier": tier,
        "missing": missing,
        "source_map_ok": source_map_ok,
        "prospect_ok": prospect_ok,
        "reason": "; ".join(reason_bits) if reason_bits else "ok",
        "path": str(args.twin_dir),
    }
    print(json.dumps(result, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(result, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
