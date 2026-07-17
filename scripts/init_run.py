#!/usr/bin/env python3
"""Scaffold engagement-intel run folder contract. Optional --preset fills OFFER/PARAMETERS."""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from textwrap import dedent

SKILL_ROOT = Path(__file__).resolve().parents[1]
PRESETS_DIR = SKILL_ROOT / "references" / "presets"

PARAMS = dedent(
    """\
    # PARAMETERS

    | Parameter | Value |
    |-----------|-------|
    | offer | TODO |
    | offer_non_goals | TODO |
    | counterparty_class | partner |
    | archetypes | TODO |
    | geo | TODO |
    | success_metric | pilot booked |
    | dm_role_priority | CEO > BD > CTO |
    | deep_dive_bar | weighted >= 3.2 and complementarity >= 3 |
    | sim_email_n | 20 |
    | sim_conversation_n | 10 |
    | sim_sample_size | 3 |
    | sim_for_ranking_min_n | 3 |
    | output_root | (this run root) |
    | mode | portfolio |
    """
)

OFFER = dedent(
    """\
    # OFFER

    ## What we propose
    TODO

    ## Non-goals (do not claim)
    - TODO

    ## Proof points available
    - TODO
    """
)

PREFLIGHT = dedent(
    """\
    # Preflight STATUS

    - [ ] Bridge online (fresh machine list)
    - [ ] LinkedIn browser session / Kimi
    - [ ] X cookies (auth_token + ct0) or bird
    - [ ] yt-dlp available
    - [ ] AI gateway smoke (JSON)
    - [ ] Simulator path OK
    - [ ] last30days optional — declare skip if brand-thin

    ## Declared channel plan
    - Will use: TODO
    - Will GAP: TODO
    """
)

IDENTITY_TMPL = dedent(
    """\
    # IDENTITY LOCK

    | Field | Value |
    |-------|-------|
    | legal_name | TODO |
    | primary_brand | TODO |
    | primary_site | https://TODO |
    | dm_name | TODO |
    | dm_role | TODO |
    | linkedin_slug | TODO or GAP |
    | x_handle | TODO or GAP |
    | youtube | TODO or GAP |
    | secondary_stakeholders | TODO |

    ## Wrong-slug / doppelgänger warnings
    - Do NOT use: TODO

    ## Confirmation sources (>=2 preferred)
    1. TODO
    2. TODO

    ## Gate
    - [ ] Identity lock PASS
    """
)

# Extracted from happycapy-partner-hk.md for init (keep in sync with preset file)
HAPPYCAPY_PARTNER_HK_PARAMS = dedent(
    """\
    # PARAMETERS

    **Preset:** `happycapy-partner-hk`
    **Source:** `references/presets/happycapy-partner-hk.md` (full axioms — read it)

    | Parameter | Value |
    |-----------|-------|
    | offer | Complementary partnership: HappyCapy as agent **execution computer** under/beside partner agents (co-build, co-sell, embed) |
    | offer_non_goals | Not replace their agent product; not reseller-only dump; not compete as private chatbot UI; not hyperscaler peer |
    | counterparty_class | partner |
    | archetypes | SI/AI consultancy; vertical agent SaaS (CX, sales, ops); private AI + DC/MSP; agent builder / API platform; GTM/sales-agent services; localized LLM/context layer; hub/accelerator (light) |
    | geo | Hong Kong first (phase-1 deep-dives). Singapore/SEA = phase-2 names only unless expanded |
    | success_metric | Joint pilot booked or technical working session with DM + clear attach economics |
    | dm_role_priority | CEO/Co-founder > Head of Sales/BD > CTO/Chief Scientist |
    | scoring_rubric | Dist 25%, Complementarity 20%, Enterprise trust 15%, Speed 15%, Revenue 15%, Optionality 10% (0–5) |
    | deep_dive_bar | weighted >= 3.2 AND complementarity >= 3 |
    | sim_email_n | 20 |
    | sim_conversation_n | 10 |
    | sim_sample_size | 3 |
    | sim_for_ranking_min_n | 3 |
    | sim_weight_if_n_lt_3 | 0 |
    | mode | portfolio |
    | preset | happycapy-partner-hk |
    | product_doc | ~/.claude/happycapy-platform-overview.md |
    | output_root | (this run root) |

    ## Ranking formula (S9)

    ```
    rank_score =
      0.30 * economic_attach
    + 0.25 * complementarity
    + 0.15 * speed_to_pilot
    + 0.15 * trust_credibility
    + 0.15 * sim_frame_fit   # ONLY if twin ≥ T2 AND sample_size ≥ 3; else 0
    ```

    Hard exclude: competitive agent-cloud peers; hyperscaler-as-peer.
    """
)

HAPPYCAPY_PARTNER_HK_OFFER = dedent(
    """\
    # OFFER — HappyCapy partnership (HK preset)

    **Preset:** `happycapy-partner-hk`
    Full detail: skill `references/presets/happycapy-partner-hk.md`
    Product facts: `~/.claude/happycapy-platform-overview.md`

    ## What we propose
    Complementary **B2B partnership**: HappyCapy as the **always-on agent execution computer** under or beside the partner’s agents/products (co-build, co-sell, embed runtime).

    They own domain / models / context / CX / SI delivery / GTM / DC channel.
    We own durable computer, root agent, multi-model gateway, skills, Mac bridge, public URLs.

    **Frame:** context / domain / agent product **+ computer (HappyCapy)**.

    ## Non-goals (do not claim)
    - Not “another chatbot / agent builder that replaces theirs”
    - Not competing as private-assistant UI when they already sell private AI assistants
    - Not pure reseller dump of seats with no joint pilot
    - Not hyperscaler peer positioning (AWS/Azure/Tencent as equals)

    ## Ideal outcomes
    1. Intro / technical call accepted
    2. Joint pilot with a **named** enterprise client
    3. Integration workshop (CTO / scientist / SI lead)
    4. Channel attach (SOW line, CX package, DC/GPU attach, GTM embed)
    5. Ecosystem referral (Cyberport / HKMA sandbox / HKSTP)

    ## Proof points (update as product evolves)
    - Always-on sandbox + root agent
    - Multi-model gateway
    - Skills extensibility
    - Mac bridge for hybrid workflows
    - Instant public URL export for pilots
    """
)

HAPPYCAPY_PARTNER_HK_PREFLIGHT = dedent(
    """\
    # Preflight STATUS — happycapy-partner-hk

    - [ ] Bridge online (fresh machine list; IDs rotate)
    - [ ] Kimi Web Bridge on Mac for LinkedIn (`127.0.0.1:10086` via bridge)
    - [ ] X cookies (auth_token + ct0) → bird-search or declare X = GAP
    - [ ] yt-dlp on Mac + chrome cookies (quote URLs for zsh) or YT = GAP
    - [ ] AI gateway smoke (`$AI_GATEWAY_BASE_URL` + key; User-Agent; identity encoding)
    - [ ] Simulator path (e.g. outputs/votee-partnership/tmp/ai-sales-agent-simulator if present)
    - [ ] last30days optional — skip if brand-thin HK targets
    - [ ] Read preset: references/presets/happycapy-partner-hk.md
    - [ ] Read product: ~/.claude/happycapy-platform-overview.md

    ## Declared channel plan
    - Will use: site, LinkedIn (Kimi), X (if cookies), YT long-form (priority), press
    - Will GAP: channels that fail preflight (document impact on twin tier)

    ## Tool path notes
    - bird: ~/.claude/skills/last30days/scripts/lib/vendor/bird-search/bird-search.mjs
    - engagement-intel scripts: ~/.claude/skills/engagement-intel/scripts/
    - reflections: outputs/workflow-reflections/ (if in workspace)
    """
)

PRESET_MAP = {
    "happycapy-partner-hk": {
        "params": HAPPYCAPY_PARTNER_HK_PARAMS,
        "offer": HAPPYCAPY_PARTNER_HK_OFFER,
        "preflight": HAPPYCAPY_PARTNER_HK_PREFLIGHT,
        "file": "happycapy-partner-hk.md",
    }
}


def resolve_preset(name: str | None) -> dict | None:
    if not name:
        return None
    key = name.strip().lower().replace("_", "-")
    # allow path-like or with .md
    key = re.sub(r"\.md$", "", Path(key).name)
    if key not in PRESET_MAP:
        known = ", ".join(sorted(PRESET_MAP))
        raise SystemExit(f"Unknown preset '{name}'. Known: {known}")
    return PRESET_MAP[key]


def main() -> None:
    ap = argparse.ArgumentParser(description="Scaffold engagement-intel run")
    ap.add_argument("run_root", type=Path)
    ap.add_argument("--mode", choices=["portfolio", "single"], default="portfolio")
    ap.add_argument("--entity", default=None, help="Optional first entity slug for single mode")
    ap.add_argument(
        "--preset",
        default=None,
        help="Preset id (e.g. happycapy-partner-hk) — fills OFFER/PARAMETERS/preflight",
    )
    args = ap.parse_args()
    root = args.run_root
    preset = resolve_preset(args.preset)

    for d in [
        "00-plan",
        "00-preflight",
        "01-discovery",
        "02-shortlist",
        "03-deep-dives",
        "04-rank",
        "99-rejects",
    ]:
        (root / d).mkdir(parents=True, exist_ok=True)

    params_text = preset["params"] if preset else PARAMS
    offer_text = preset["offer"] if preset else OFFER
    preflight_text = preset["preflight"] if preset else PREFLIGHT

    # If mode single but preset forces portfolio table, still allow single scaffold
    if preset and args.mode == "single":
        params_text = params_text.replace("| mode | portfolio |", "| mode | single |")

    (root / "00-plan" / "PARAMETERS.md").write_text(params_text)
    (root / "00-plan" / "OFFER.md").write_text(offer_text)
    (root / "00-preflight" / "STATUS.md").write_text(preflight_text)

    if preset:
        # Copy full preset markdown into the run for offline reading
        src = PRESETS_DIR / preset["file"]
        if src.exists():
            shutil.copy2(src, root / "00-plan" / f"PRESET_{preset['file']}")
        (root / "00-plan" / "PRESET_ID.txt").write_text(
            (args.preset or "").strip().lower().replace("_", "-") + "\n"
        )

    (root / "01-discovery" / "UNIVERSE.md").write_text(
        "# UNIVERSE\n\n| name | archetype | site | why_fit | conflict |\n|------|-----------|------|---------|----------|\n"
    )
    (root / "02-shortlist" / "SCORED.md").write_text(
        "# SCORED SHORTLIST\n\n"
        "Weights (happycapy-partner-hk default): Dist 25% · Comp 20% · Trust 15% · "
        "Speed 15% · Rev 15% · Opt 10%\n\n"
        "| name | Dist | Comp | Trust | Speed | Rev | Opt | weighted | deep_dive | notes |\n"
        "|------|------|------|-------|-------|-----|-----|----------|-----------|-------|\n"
        if preset and "happycapy" in (args.preset or "")
        else "# SCORED SHORTLIST\n\n| name | scores… | weighted | deep_dive | notes |\n|------|---------|----------|-----------|-------|\n"
    )
    (root / "99-rejects" / "REJECTS.md").write_text("# REJECTS\n\n| name | reason |\n|------|--------|\n")
    (root / "04-rank" / "TOPK.md").write_text(
        "# TOP-K\n\nFormula version: v2"
        + (" · preset happycapy-partner-hk\n" if preset else "\n")
    )
    preset_note = f"\nPreset: `{args.preset}`\n" if args.preset else "\n"
    (root / "README.md").write_text(
        f"# Engagement intel run\n\nMode: {args.mode}{preset_note}\n"
        f"Follow engagement-intel skill stages S0–S9 with hard gates.\n"
    )

    if args.mode == "single" and args.entity:
        ent = root / "03-deep-dives" / args.entity
        for sub in [
            "00-plan",
            "01-company",
            "02-people",
            "03-linkedin",
            "04-x",
            "05-youtube",
            "06-web",
            "08-recency",
            "09-analysis",
            "10-digital-twin",
            "11-simulations",
            "12-playbook",
            "tmp",
        ]:
            (ent / sub).mkdir(parents=True, exist_ok=True)
        (ent / "00-plan" / "IDENTITY.md").write_text(IDENTITY_TMPL)
        (root / "00-plan" / "IDENTITY.md").write_text(IDENTITY_TMPL)

    print(f"scaffolded {root}" + (f" preset={args.preset}" if args.preset else ""))


if __name__ == "__main__":
    main()
