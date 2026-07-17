# engagement-intel presets

Presets specialize the abstract workflow without a second skill.

| Preset id | File | Use when |
|-----------|------|----------|
| `happycapy-partner-hk` | [happycapy-partner-hk.md](happycapy-partner-hk.md) | HappyCapy complementary B2B partnerships, Hong Kong phase-1 |

## Apply

```bash
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode portfolio --preset happycapy-partner-hk
```

Or tell the agent: “run engagement-intel with preset happycapy-partner-hk”.

## Add a preset

1. Add `references/presets/<id>.md` (offer, params, tools, archetypes).
2. Register in `scripts/init_run.py` → `PRESET_MAP`.
3. Link from this README and SKILL.md presets section.
