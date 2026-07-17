#!/usr/bin/env python3
"""Aggregate hard gates for an engagement-intel run or deep-dive pack."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_gate(args: list[str]) -> dict:
    p = subprocess.run(
        [sys.executable, *args],
        capture_output=True,
        text=True,
    )
    try:
        data = json.loads(p.stdout or "{}")
    except json.JSONDecodeError:
        data = {"raw_stdout": p.stdout, "raw_stderr": p.stderr, "passed": False}
    data["_exit"] = p.returncode
    if "passed" not in data:
        data["passed"] = p.returncode == 0
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("run_root", type=Path)
    ap.add_argument("--mode", choices=["portfolio", "single"], default="portfolio")
    ap.add_argument("--entity", default=None, help="Deep-dive slug under 03-deep-dives/")
    ap.add_argument("--for-ranking", action="store_true")
    ap.add_argument("--min-n", type=int, default=3)
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()
    root = args.run_root

    gates = {}
    gates["stage_order"] = run_gate(
        [
            str(HERE / "check_stage_order.py"),
            str(root),
            "--mode",
            args.mode,
        ]
    )

    # Identity
    id_path = root / "00-plan" / "IDENTITY.md"
    if args.entity:
        cand = root / "03-deep-dives" / args.entity / "00-plan" / "IDENTITY.md"
        if cand.exists():
            id_path = cand
    gates["identity_lock"] = run_gate([str(HERE / "check_identity_lock.py"), str(id_path)])

    # Twin
    twin_dir = root / "10-digital-twin"
    if args.entity:
        twin_dir = root / "03-deep-dives" / args.entity / "10-digital-twin"
    if twin_dir.exists():
        gates["twin"] = run_gate([str(HERE / "check_twin_gate.py"), str(twin_dir)])
    else:
        gates["twin"] = {"gate": "twin", "passed": False, "reason": "twin dir missing"}

    # Sims
    sim_dir = root / "11-simulations"
    if args.entity:
        sim_dir = root / "03-deep-dives" / args.entity / "11-simulations"
    if sim_dir.exists():
        cmd = [
            str(HERE / "check_sim_sample_size.py"),
            "--scan-dir",
            str(sim_dir),
            "--min-n",
            str(args.min_n),
        ]
        if args.for_ranking:
            cmd.append("--for-ranking")
        gates["sim_sample_size"] = run_gate(cmd)
    else:
        gates["sim_sample_size"] = {
            "gate": "sim_sample_size",
            "passed": not args.for_ranking,
            "reason": "sim dir missing",
        }

    hard = ["stage_order", "identity_lock"]
    # twin/sim only hard if those stages claimed complete
    if twin_dir.exists():
        hard.append("twin")
    if args.for_ranking:
        hard.append("sim_sample_size")

    passed = all(gates[k].get("passed") for k in hard if k in gates)
    out = {
        "passed": passed,
        "hard_gates": hard,
        "gates": gates,
        "run_root": str(root),
        "entity": args.entity,
    }
    print(json.dumps(out, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(out, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
