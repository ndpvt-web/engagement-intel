---
name: engagement-intel
description: >
  Run the Engagement Intelligence Workflow v2: offer/frame → discover candidates → score →
  hard identity lock → multi-source research → digital twin → Monte Carlo email/conversation
  sims → approach playbook (optional portfolio rank). Use whenever the user wants partner
  research, B2B outreach strategy, digital twins of decision-makers, sales simulation,
  approach playbooks, "who should we sell/partner with", portfolio partner discovery,
  investor/hire/customer engagement intel, or to re-run the Votee/HK-style pipeline.
  Prefer this skill over ad-hoc twin+sim. Hard gates block deep twin/sim without identity
  lock and block portfolio ranking on sample_size < 3. Also use when user mentions
  engagement-intel, EIW v2, or "run the engagement workflow".
version: "2.0.0"
argument-hint: '<offer or goal> | preset happycapy-partner-hk | single <entity> | portfolio | validate <run-root>'
---

# Engagement Intelligence (v2)

Convert an **offer** + **counterparty class** into researched twins, gated simulations, and approach playbooks.

**Success metric:** decision quality under uncertainty — not maximized sim scores.

## When this skill is active

1. Read this file fully before spawning deep-dive agents.
2. **If HappyCapy partnership / HK partners / Votee-style pipeline:** load preset [references/presets/happycapy-partner-hk.md](references/presets/happycapy-partner-hk.md) first and init with `--preset happycapy-partner-hk`.
3. Read [references/HARD_GATES.md](references/HARD_GATES.md) before twin/sim.
4. Use scripts in `scripts/` as fail-closed checks — do not invent “PASS”.
5. For stage detail, load [references/WORKFLOW_V2.md](references/WORKFLOW_V2.md) as needed.
6. For named failures, load [references/ANTI_PATTERNS.md](references/ANTI_PATTERNS.md).

## Presets (specialize without a second skill)

| Preset | When |
|--------|------|
| [happycapy-partner-hk](references/presets/happycapy-partner-hk.md) | HappyCapy complementary B2B partners, Hong Kong phase-1, same shape as Votee/HK portfolio run |

```bash
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode portfolio --preset happycapy-partner-hk
```

Preset fills `OFFER.md`, `PARAMETERS.md`, preflight checklist, and copies full preset into `00-plan/PRESET_*.md`. Index: [references/presets/README.md](references/presets/README.md).

## Hard rules (why they exist)

Past runs ranked partners on **n=1** sim theater, deep-dived before scoring, and built twins on wrong brands. Gates encode those lessons:

| Gate | Blocks | Why |
|------|--------|-----|
| Stage order | Twin/sim before shortlist (portfolio) | Deep-Dive First Tunnel |
| Identity lock | Twin/sim without IDENTITY.md fields | Wrong-Slug Doppelgänger |
| Twin tier + SOURCE_MAP | Expensive sim on brochure twins | Brochure Twin / Source-Map Amnesia |
| sample_size ≥ 3 | Portfolio ranking on n=1 | n=1 Monte Carlo Theater |
| Preflight | Parallel deep-dives without STATUS.md | Parallel Tool Debt Multiplier |

Empty tool output is a **GAP**, never “no market activity”.

## Modes

### A) Portfolio (default for “find partners / candidates”)
S0 Frame → S1 Universe → S2 Score → **preflight** → for each YES: S3 Identity → S4 Research → S5 Analysis → S6 Twin → **gates** → S7 Sim → S8 Playbook → S9 Rank.

### B) Single target (named company/person)
S0 Frame → S3 Identity → S4–S8. Still score for audit. Skip S1 breadth / S9 if not needed.

### C) Validate only
`python3 scripts/validate_run.py <run-root> [--entity slug] [--for-ranking]`

## Scaffold

```bash
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode portfolio
# HappyCapy HK partners (recommended for that task):
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode portfolio --preset happycapy-partner-hk
# single target:
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode single --entity <slug> --preset happycapy-partner-hk
```

## Stage procedure

### S0 — Frame (fail-closed if ambiguous)
Write `00-plan/PARAMETERS.md` + `OFFER.md`:
- offer, offer_non_goals, counterparty_class, geo, success_metric
- scoring rubric + deep_dive_bar
- sim budget: email N, conversation N, **sample_size ≥ 3** when results will rank portfolios

### S1 — Universe
`01-discovery/UNIVERSE.md` ≥N candidates across ≥3 archetypes (unless class is narrow). Reject seeds listed.

### S2 — Score
`02-shortlist/SCORED.md`. Deep-dive only above bar. Every NO needs a reason.

**Do not create `03-deep-dives/<entity>/` until S2 YES and identity work starts.**

### Preflight (once per session, before parallel deep-dives)
`00-preflight/STATUS.md` — bridge, LI browser, X cookies/bird, yt-dlp, gateway JSON smoke, simulator path. Narrow channels if tools fail.

### S3 — Identity lock (HARD)
Write `03-deep-dives/<slug>/00-plan/IDENTITY.md` using the template fields:

```
legal_name | primary_brand | primary_site | dm_name | dm_role
linkedin_slug | x_handle | wrong-slug warnings | confirmation sources
```

Run:

```bash
python3 ~/.claude/skills/engagement-intel/scripts/check_identity_lock.py \
  outputs/<run>/03-deep-dives/<slug>/00-plan/IDENTITY.md
```

**Exit 1 ⇒ stop.** Research spike allowed; twin/sim forbidden until PASS.

### S4 — Research
Channel folders under the entity pack. Prefer long-form first-person (YT/podcast). Each empty channel gets `GAP.md` with impact on twin tier. Never silent empty folders.

### S5 — Analysis
`09-analysis/signal-analysis.md` with **EVIDENCE / INFERENCE** labels. Need ≥5 evidence-backed decision-process claims before twin.

### S6 — Twin (HARD before sim)
Outputs:
- `10-digital-twin/TWIN.md` (declare **Tier: T1|T2|T3**)
- `prospect.json` (or class schema)
- `SOURCE_MAP.md` (non-obvious claims → paths)

```bash
python3 ~/.claude/skills/engagement-intel/scripts/check_twin_gate.py \
  outputs/<run>/03-deep-dives/<slug>/10-digital-twin
```

- **T2/T3** → sim allowed  
- **T1** → sim only with `SIM_WAIVER.md` (reason + risk)

### S7 — Simulation (HARD for ranking)
Default budget: email 20 + conversation 10. For any target entering **portfolio rank**, set **sample_size ≥ 3** (repeat strategies or raise simulator n). Log stderr, completed/failed counts, models.

If the sales-sim only supports n=1 per strategy today:
1. Mark all scores **directional_only** in RUN_METRICS.json  
2. **Do not** use sim meet%/winRate in S9 ranking weights (set sim weight = 0)  
3. Prefer conversation for qualitative frames only  

```bash
python3 ~/.claude/skills/engagement-intel/scripts/check_sim_sample_size.py \
  --scan-dir outputs/<run>/03-deep-dives/<slug>/11-simulations \
  --min-n 3 --for-ranking
```

Exit 1 with `--for-ranking` ⇒ cannot place entity in ranked Top-K on sim scores.

Offer fidelity: strategy prompts must include product/offer name and non-goals. Reject invented mutuals/metrics in playbook synthesis.

### S8 — Playbook
`12-playbook/APPROACH_PLAYBOOK.md` must include: Open · Frame · Proof · Objections · **Do-not-say (≥3)** · First message · Secondary stakeholders · **Confidence** (High/Med/Low). Human synthesis over raw sim dump.

### S9 — Portfolio rank (optional)
Freeze formula in PARAMETERS. Cap/zero sim weight unless twin ≥ T2 **and** sample_size ≥ 3. Publish confidence bands. Write `04-rank/TOPK.md` + `99-rejects/REJECTS.md`.

```bash
python3 ~/.claude/skills/engagement-intel/scripts/validate_run.py \
  outputs/<run> --mode portfolio --entity <slug> --for-ranking
```

## Parallelization

| Unit | Parallel? |
|------|-----------|
| Preflight | No |
| Universe queries | Yes |
| Scoring | No |
| Deep-dives after shortlist YES | Yes |
| Channels after identity lock | Yes |
| Email ‖ conversation sim | Yes |
| Rank | No |

**Do not spawn a deep-dive agent until IDENTITY.md exists for that entity.**

## Output contract

```
outputs/<run-slug>/
  README.md
  00-plan/ PARAMETERS.md OFFER.md
  00-preflight/ STATUS.md
  01-discovery/ UNIVERSE.md
  02-shortlist/ SCORED.md
  03-deep-dives/<entity>/
    00-plan/IDENTITY.md
    01-company/ … 06-web/ 08-recency/
    09-analysis/ 10-digital-twin/ 11-simulations/ 12-playbook/
    RUN_METRICS.json
  04-rank/ TOPK.md
  99-rejects/ REJECTS.md
```

## RUN_METRICS.json (per deep-dive)

```json
{
  "entity": "slug",
  "twin_tier": "T2",
  "identity_lock": true,
  "channels": {"site": "ok", "linkedin": "gap", "x": "ok", "youtube": "ok"},
  "sim_email_completed": 20,
  "sim_email_failed": 0,
  "sim_conversation_completed": 10,
  "sample_size": 3,
  "directional_only": false,
  "gateway_errors": 0
}
```

## Definition of done

**Deep-dive:** identity PASS · min evidence · labeled analysis · twin+SOURCE_MAP+tier · sims or waiver · playbook with first message + do-not-say · RUN_METRICS.json · README gaps honest.

**Portfolio:** all deep-dives done/timed out · TOPK with formula · rejects · action queue · no sim-led rank on n=1.

## Tools (typical HappyCapy session)

- last30days (optional; brand-thin → skip)
- Mac bridge + Kimi (LinkedIn)
- bird-search + AUTH_TOKEN/CT0 (X)
- yt-dlp transcripts via bridge (quote URLs for zsh)
- ai-sales-agent-simulator (patched gateway if needed)

Paths may vary; declare actual paths in preflight.

## Anti-patterns to refuse

If you catch yourself doing any of these, stop and fix gates: Deep-Dive First Tunnel, Wrong-Slug Doppelgänger, Empty-Tool Oracle, Schema Cosplay, n=1 Monte Carlo Theater, Brochure Twin, Sim-Led Ranking, Claim Laundering. Full list: [references/ANTI_PATTERNS.md](references/ANTI_PATTERNS.md).
