# engagement-intel

**Engagement Intelligence Workflow v2** — a Claude skill that turns an **offer** + **counterparty class** into:

1. Candidate discovery & scoring  
2. Hard **identity lock** (no wrong-slug research)  
3. Multi-source research  
4. Decision-maker **digital twin** (+ `SOURCE_MAP`)  
5. Monte Carlo **email / conversation** simulations  
6. Approach **playbook** (optional portfolio Top-K)

Hard gates block deep twin/sim without identity lock and block portfolio ranking on `sample_size < 3`.

> Success metric: **decision quality under uncertainty** — not maximized sim scores.

---

## Install

### Claude Code / skills directory

```bash
git clone https://github.com/ndpvt-web/engagement-intel.git \
  ~/.claude/skills/engagement-intel
```

Or copy this repo into `~/.claude/skills/engagement-intel/`.

Optional slash command: point `/engagement-intel` at this skill (see `SKILL.md`).

---

## Quick start

```bash
# Generic portfolio run
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/my-run --mode portfolio

# HappyCapy × Hong Kong partners (preset — offer/rubric/tools prefilled)
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/my-run --mode portfolio --preset happycapy-partner-hk

# Single named target
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/my-run --mode single --entity acme-ai --preset happycapy-partner-hk
```

Then follow stages in [`SKILL.md`](SKILL.md):

```
OFFER + CLASS
  → UNIVERSE
  → SCORE (bar)
  → IDENTITY LOCK   ← hard gate
  → RAW CHANNELS (parallel; GAP if empty)
  → ANALYSIS
  → TWIN + SOURCE_MAP (tier T1/T2/T3)
  → SIM email ‖ conversation
  → PLAYBOOK
  → PORTFOLIO RANK (optional; sim weight only if n≥3)
```

Validate before ranking:

```bash
python3 scripts/check_identity_lock.py \
  outputs/<run>/03-deep-dives/<entity>/00-plan/IDENTITY.md

python3 scripts/check_twin_gate.py \
  outputs/<run>/03-deep-dives/<entity>/10-digital-twin

python3 scripts/check_sim_sample_size.py \
  --scan-dir outputs/<run>/03-deep-dives/<entity>/11-simulations \
  --min-n 3 --for-ranking

python3 scripts/validate_run.py outputs/<run> --entity <entity> --for-ranking
```

---

## Repository layout

```
engagement-intel/
├── SKILL.md                 # Skill entry (frontmatter + procedure)
├── README.md                # This file
├── LICENSE
├── scripts/
│   ├── init_run.py          # Scaffold run folders (+ --preset)
│   ├── check_stage_order.py
│   ├── check_identity_lock.py
│   ├── check_twin_gate.py
│   ├── check_sim_sample_size.py
│   └── validate_run.py      # Aggregate gates
├── references/
│   ├── WORKFLOW_V2.md       # Full stage cards (S0–S9)
│   ├── HARD_GATES.md        # Gate contract
│   ├── ANTI_PATTERNS.md     # Named failure modes
│   └── presets/
│       ├── README.md
│       └── happycapy-partner-hk.md
├── evals/
│   └── evals.json
└── assets/
```

---

## Hard gates (why they exist)

| Gate | Script | Blocks |
|------|--------|--------|
| Stage order | `check_stage_order.py` | Deep-dive before shortlist / missing preflight |
| Identity lock | `check_identity_lock.py` | Twin/sim without DM + brand + site |
| Twin tier + SOURCE_MAP | `check_twin_gate.py` | Expensive sim on brochure (T1) twins |
| sample_size ≥ 3 | `check_sim_sample_size.py --for-ranking` | Portfolio rank on n=1 “Monte Carlo theater” |

Empty tool output is a **GAP**, never “no market activity.”

Named anti-patterns: [references/ANTI_PATTERNS.md](references/ANTI_PATTERNS.md)  
(e.g. Deep-Dive First Tunnel, Wrong-Slug Doppelgänger, n=1 Monte Carlo Theater, Brochure Twin, Sim-Led Ranking).

---

## Presets

Specialize without a second skill.

| Preset | Use when |
|--------|----------|
| [`happycapy-partner-hk`](references/presets/happycapy-partner-hk.md) | HappyCapy complementary B2B partners, Hong Kong phase-1 |

Presets fill `OFFER.md`, `PARAMETERS.md`, preflight checklist, and copy full axioms into the run.

---

## What this is / is not

**Is:** An abstract engagement intelligence system for partners, customers, investors, hires, etc.  
**Is not:** CRM truth, real reply-rate prediction, or a statistical ranking engine when `sample_size = 1`.

Calibrate sim scores against real outreach outcomes when you have them.

---

## Requirements

- Python 3.10+ (gate scripts; stdlib only)
- Claude Code (or compatible agent) for the research/twin/sim loop
- Optional: Mac bridge, Kimi (LinkedIn), bird-search + X cookies, yt-dlp, sales-sim, last30days — declare in preflight

---

## License

MIT — see [LICENSE](LICENSE).

---

## Credits

Workflow distilled from multi-pack partner runs and process reflections (Engagement Intelligence Workflow v2). Product-specific HappyCapy framing lives only in the optional preset, not in the abstract core.
