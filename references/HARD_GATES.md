# Hard gates — engagement-intel v2

Run these before advancing. Exit code **1 = stop**.

## Scripts

All under `~/.claude/skills/engagement-intel/scripts/`:

| Script | When |
|--------|------|
| `init_run.py <run-root>` | Start of run |
| `check_stage_order.py <run-root> --mode portfolio\|single` | Before deep-dives / validate |
| `check_identity_lock.py <IDENTITY.md>` | Before S4 twin path / before S6–S7 |
| `check_twin_gate.py <10-digital-twin/>` | Before S7 |
| `check_sim_sample_size.py --scan-dir <11-simulations/> [--for-ranking] [--min-n 3]` | After S7; **required with --for-ranking before S9** |
| `validate_run.py <run-root> [--entity slug] [--for-ranking]` | Aggregate |

## Identity lock required fields

Parsed from IDENTITY.md:

- legal_name  
- primary_brand  
- primary_site  
- dm_name  
- dm_role  

Recommended: linkedin_slug, x_handle, wrong-slug warnings, ≥2 confirmation sources.

## Twin gate

- TWIN.md + prospect.json + SOURCE_MAP.md present  
- Tier T1|T2|T3 declared in TWIN.md  
- SOURCE_MAP has real citations  
- T1 needs SIM_WAIVER.md to sim  

## Sim / ranking gate

- `--for-ranking` requires min observed sample_size ≥ 3  
- Without it, n=1 is allowed only as **directional_only**  
- Portfolio TOPK must zero sim weight if directional_only  

## Stage order (portfolio)

Fails if `03-deep-dives/` populated while discovery or shortlist missing, or preflight STATUS.md missing, or deep-dives lack IDENTITY.md.
