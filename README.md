# engagement-intel

Engagement Intelligence Workflow **v2** as a Claude skill with **hard gates**.

## Install

Already at `~/.claude/skills/engagement-intel/`.  
Workspace copy: `engagement-intel/`  
Slash: `/engagement-intel`

## Quick start

```bash
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py outputs/my-run --mode portfolio
# HappyCapy × HK partners (preset — offer/rubric/tools prefilled):
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py outputs/my-run \
  --mode portfolio --preset happycapy-partner-hk
# fill remaining preflight, universe, shortlist
# per entity: IDENTITY.md then research → twin → sim → playbook
python3 ~/.claude/skills/engagement-intel/scripts/validate_run.py outputs/my-run --entity <slug> --for-ranking
```

### Presets
- [references/presets/happycapy-partner-hk.md](references/presets/happycapy-partner-hk.md) — HappyCapy complementary partnerships, Hong Kong first
- Index: [references/presets/README.md](references/presets/README.md)

## Hard gates

| Gate | Script |
|------|--------|
| Stage order | `check_stage_order.py` |
| Identity lock | `check_identity_lock.py` |
| Twin tier + SOURCE_MAP | `check_twin_gate.py` |
| sample_size ≥ 3 for ranking | `check_sim_sample_size.py --for-ranking` |
| Aggregate | `validate_run.py` |

Details: `references/HARD_GATES.md`, full stages: `references/WORKFLOW_V2.md`.

## Validation (single suite, 2026-07-16)

See `engagement-intel-workspace/iteration-1/gate-validation/outputs/SUMMARY.json` — **ALL_PASS**.
