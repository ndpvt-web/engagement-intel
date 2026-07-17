# Engagement Intelligence Workflow v2 (Abstract Playbook)

Reusable for **any product/offer × any second-party class**  
(customer, partner, investor, hire, press, regulator, co-founder…).

**Do not** hard-code a vendor, geography, or channel stack. Parameterize them.

Related: `../02-overall/OVERALL_REFLECTION.md`, `../04-anti-patterns/ANTI_PATTERNS.md`.

---

## 0. Purpose

Convert public (and permitted private) signal about a second party into:

1. A **decision-maker model** (twin) with explicit evidence,  
2. **Tested outreach frames** (sim),  
3. An **actionable approach playbook**,  
4. Optionally a **ranked portfolio** of counterparties.

Success metric is **decision quality under uncertainty**, not sim score maximization.

---

## 1. Parameterization (fill before run)

Write `00-plan/PARAMETERS.md`:

| Parameter | Description | Example shapes |
|-----------|-------------|----------------|
| `offer` | What you propose (product, partnership, hire, raise) | “runtime under your agents”; “Series A check”; “staff eng role” |
| `offer_non_goals` | What you will not claim | “not a reseller dump”; “not full-time remote” |
| `counterparty_class` | Second-party type | customer / partner / investor / hire |
| `archetypes` | Subtypes to cover in discovery | SI, vertical SaaS, MSP, fund, etc. |
| `geo` | Phase-1 geography | HK only; US-remote; etc. |
| `success_metric` | What “good engagement” means | pilot booked; intro accepted; term sheet meeting |
| `dm_role_priority` | Who to twin first | CEO > CRO > CTO or reverse by class |
| `scoring_rubric` | Weighted 0–5 dimensions | dist, complement, trust, speed, revenue, optionality |
| `deep_dive_bar` | Min weighted + hard floors | e.g. ≥3.2 and complementarity ≥3 |
| `sim_budget` | Modes + N + sample_size | email 20 / conv 10 / n≥3 for top K |
| `tools_allowed` | Session tool set | bridge, bird, yt-dlp, last30days, sim |
| `output_root` | Folder root | `outputs/<run-slug>/` |

**Counterparty class switches (defaults):**

| Class | Primary DM | Emphasize in twin | Sim mode weight |
|-------|------------|-------------------|-----------------|
| Partner | CEO / BD head | complementarity, conflict, attach economics | Conv ≥ email |
| Customer | Economic buyer + champion | pain, budget, procurement | Email then conv |
| Investor | Partner who owns thesis | fund thesis, check size, pace | Short email + partner meeting |
| Hire | Candidate | motivation, constraints, signal authenticity | Conv-heavy |
| Press | Reporter/editor | beat, prior pieces, hooks | Email-only often |

---

## 2. Stage cards

### S0 — Frame
| | |
|--|--|
| **Purpose** | Freeze axioms so research doesn’t invent the offer mid-flight |
| **Inputs** | User goal; product facts; constraints |
| **Outputs** | `00-plan/OFFER.md`, `EXECUTION_PLAN.md`, `PARAMETERS.md`, frozen rubric |
| **Tools** | None required |
| **Quality gate** | Offer, class, geo, success metric, non-goals present |
| **Fail mode** | **Fail-closed** if ambiguous |
| **Skip when** | Re-running same offer with only new targets (reuse OFFER.md) |

### S1 — Universe discovery
| | |
|--|--|
| **Purpose** | Map candidates across archetypes before depth |
| **Inputs** | Parameters; search/browse tools |
| **Outputs** | `01-discovery/UNIVERSE.md` (≥N rows: name, archetype, site, why-fit, conflict flag) |
| **Tools** | Web search, directories, ecosystem lists, light last30days *only if topic is chatter-rich* |
| **Quality gate** | ≥N candidates; ≥3 archetypes (unless class is narrow); reject seeds listed |
| **Fail mode** | **Fail-open** if thin — expand sources; don’t deep-dive random 1 |
| **Skip when** | Single named target already locked (go S3) |

### S2 — Score / shortlist
| | |
|--|--|
| **Purpose** | Allocate expensive depth only above bar |
| **Inputs** | Universe + rubric |
| **Outputs** | `02-shortlist/SCORED.md` with weights, YES/NO deep-dive, notes |
| **Tools** | Spreadsheet/markdown only |
| **Quality gate** | Every YES has complementarity ≥ floor; every NO has reason |
| **Fail mode** | **Fail-closed** for deep-dive if below bar |
| **Skip when** | Forced single-target mandate (still score for audit) |

### S3 — Identity lock
| | |
|--|--|
| **Purpose** | Prevent researching the wrong entity/brand |
| **Inputs** | Shortlisted entity |
| **Outputs** | `00-plan/IDENTITY.md`: legal name, brands, DM, secondary stakeholders, LI slugs, X handles, YT, emails, wrong-slug warnings |
| **Tools** | Site, SERP, LI, X, company registries |
| **Quality gate** | DM name+role confirmed by ≥2 sources OR one authoritative bio; brand handles verified |
| **Fail mode** | **Fail-closed** for twin/sim until pass (research spike allowed) |
| **Skip when** | Never for deep-dive; only for universe rows |

### S4 — Raw multi-source research
| | |
|--|--|
| **Purpose** | Collect raw signal; prefer first-person long-form |
| **Inputs** | Identity lock |
| **Outputs** | Channel folders (see §5); each empty channel has `GAP.md` |
| **Tools** | Site scrape, LI (authenticated browser), X (cookies/bird), YT transcripts, articles, podcasts, last30days optional |
| **Quality gate** | **Minimum evidence threshold** (§4) |
| **Fail mode** | Per-channel **fail-open** with GAP; overall **fail-closed** if min evidence unmet |
| **Parallel** | Channels after identity lock; entities after shortlist |

### S5 — Signal analysis
| | |
|--|--|
| **Purpose** | Structure evidence into decision-relevant model |
| **Inputs** | Raw corpus |
| **Outputs** | `09-analysis/signal-analysis.md` with EVIDENCE/INFERENCE labels: timeline, values, decision style, pains, objections, fit/conflict, stakeholders |
| **Tools** | LLM analysis only on saved files |
| **Quality gate** | ≥5 evidence-backed claims about DM or org decision process |
| **Fail mode** | **Fail-closed** to twin if only marketing slogans |
| **Skip when** | Never if running twin |

### S6 — Digital twin
| | |
|--|--|
| **Purpose** | Compress analysis into a reusable decision-maker model |
| **Inputs** | Analysis + raw |
| **Outputs** | `10-digital-twin/TWIN.md`, `prospect.json` (or class-specific schema), `SOURCE_MAP.md` |
| **Tools** | Twin schema / simulator prospect schema |
| **Quality gate** | SOURCE_MAP maps non-obvious claims → paths; declare twin tier T1/T2/T3 |
| **Fail mode** | **Fail-closed** for sim if SOURCE_MAP missing |
| **Skip when** | Portfolio light-touch (shortlist only) |

### S7 — Monte Carlo outreach simulation
| | |
|--|--|
| **Purpose** | Stress-test frames/channels against twin; surface objections |
| **Inputs** | Twin + offer + strategy space |
| **Outputs** | `11-simulations/*-report.json`, samples, stderr logs, RUN metrics |
| **Tools** | Sales/conversation simulator + AI gateway |
| **Quality gate** | ≥50% strategies complete; sample_size logged; errors counted |
| **Fail mode** | **Fail-open** partial; **fail-closed** if <50% or twin < T2 without waiver |
| **Skip when** | Twin T1 and no time for evidence upgrade; or success_metric doesn’t need outreach language |

### S8 — Approach playbook
| | |
|--|--|
| **Purpose** | Convert twin+sim into executable first touches |
| **Inputs** | Twin, analysis, sim |
| **Outputs** | `12-playbook/APPROACH_PLAYBOOK.md` (+ email/conversation subdocs) |
| **Required sections** | Open · Frame · Proof · Objections · Do-not-say · First message · Secondary stakeholders · Confidence |
| **Quality gate** | First message present; do-not-say ≥3; confidence tag |
| **Fail mode** | **Fail-closed** if only sim dump without human synthesis |
| **Skip when** | Internal research-only mandate |

### S9 — Portfolio rank (optional)
| | |
|--|--|
| **Purpose** | Order multi-target action under resource constraint |
| **Inputs** | All shortlist packs + frozen formula |
| **Outputs** | `04-rank/TOPK.md` action queue + rejects + phase-2 list |
| **Quality gate** | Formula version; confidence bands; sim weight capped if n=1 |
| **Fail mode** | **Fail-closed** if ranks hide formula |
| **Skip when** | Single target |

---

## 3. Parallelization rules

| Unit | Parallel? | Notes |
|------|-----------|-------|
| Session tool preflight | **No** | One `00-preflight/STATUS.md` for all agents |
| Universe search queries | Yes | Merge + dedupe |
| Shortlist scoring | No (fast) | Single scorer for consistency |
| Deep-dives per entity | **Yes** | After shortlist YES |
| Channels within entity | **Yes** | After identity lock |
| Sim email ‖ conversation | **Yes** | Same twin version |
| Portfolio rank | No | After deep-dives complete or timed out |

**Anti-thrash:** Do not spawn a new deep-dive agent until identity lock file exists for that entity.

---

## 4. Minimum evidence thresholds (before twin / sim)

### Before twin (S6)
Must have **at least one** of:

| Path | Requirement |
|------|-------------|
| **A Long-form** | ≥1 first-person interview/podcast/talk transcript ≥10 min effective content |
| **B Multi-channel composite** | Company primary site **and** ≥5 first-party posts (LI/X/blog) **and** ≥1 third-party corroboration |
| **C Operator docs** | Detailed public technical docs + named DM quotes in ≥2 places |

If none: stay at S4 or downgrade target to shortlist-only.

### Twin tier labels (declare in TWIN.md)
- **T3:** Path A + corroboration  
- **T2:** Path B or C  
- **T1:** Below — twin is hypothesis; **do not run expensive sim without waiver**

### Before sim (S7)
- Twin ≥ T2 **or** explicit `SIM_WAIVER.md` (reason + risk)  
- Identity lock pass  
- Offer frame non-goals listed  
- Recommended: `sample_size ≥ 3` for any target used in portfolio ranking; if n=1, mark scores **directional only**

---

## 5. Output folder contract

```
outputs/<run-slug>/
  README.md
  00-plan/
    PARAMETERS.md
    OFFER.md
    EXECUTION_PLAN.md
    IDENTITY.md          # per target if multi, or inside each pack
  00-preflight/
    STATUS.md            # bridge, bird, yt-dlp, cookies, gateway
  01-discovery/
    UNIVERSE.md
  02-shortlist/
    SCORED.md
  03-deep-dives/<entity-slug>/
    README.md
    00-plan/             # entity-specific offer angle + identity
    01-company/
    02-people/
    03-linkedin/
    04-x/
    05-youtube/          # inventory + transcripts (normalize name)
    06-web/
    07-podcasts/         # optional
    08-recency/          # last30days or manual recency notes
    09-analysis/
    10-digital-twin/
      TWIN.md
      prospect.json
      SOURCE_MAP.md
    11-simulations/
      email-report.json
      conversation-report.json
      *.stderr
      sample-best-*.md
    12-playbook/
      APPROACH_PLAYBOOK.md
    RUN_METRICS.json
    tmp/
  04-rank/
    TOPK.md
  99-rejects/
    REJECTS.md
```

**Normalization rules:**
- Prefer `05-youtube/` containing both inventory and transcripts (avoid split names).  
- Prefer `06-web/` over `06-web-articles`.  
- Prefer `08-recency/` over hard dependency on last30days branding.  
- Empty channel = `GAP.md`, never silent absence.

---

## 6. When to skip stages

| Situation | Skip | Still required |
|-----------|------|----------------|
| Single named target | S1 breadth, S9 | S0, S3–S8 |
| Re-approach known twin <90 days | S4 full recrawl | S8 delta; light S4 recency |
| Investor class with public partner essays only | Heavy X | Essays + fund thesis + sim email |
| T1 twin, low stakes list-building | S6–S8 | S1–S2 only |
| Tool preflight fails (no LI/X/YT) | Those channels | Site+web + GAP impact; possibly stop before sim |
| Competitor conflict high | S6–S8 | Record in rejects |
| Phase-2 geo list | S3–S8 | Names + archetype + why only |

---

## 7. Channel playbook (abstract)

| Channel | Best for | Fail-open behavior |
|---------|----------|--------------------|
| Company site | Product, logos, claims | Always try first |
| Long-form YT/podcast | Voice, decision style | Highest ROI; prioritize |
| LinkedIn | Founder voice (esp. Asia B2B) | Authwall → SERP snippets + GAP |
| X/Twitter | Real-time narrative | Cookies required; else GAP |
| last30days / recency engines | Chatter-rich global topics | Brand-thin → skip or directory fallback |
| Third-party press | Corroboration | Prefer quotes over fluff |
| Job posts | Priorities / hiring signal | Secondary |

---

## 8. Simulation contract

1. Twin + offer only — no hidden agent knowledge.  
2. Log `sample_size`, model, gateway errors.  
3. Run **email** and **conversation** when class is partner/customer; email-only for cold press.  
4. Extract: top frames, objection histogram, channel recommendation.  
5. **Human synthesis** must reconcile sim with analysis (reject sim advice that contradicts strong evidence).  
6. Never present sim meeting% as probability of real meeting without calibration data.

---

## 9. Ranking contract (portfolio)

Freeze in S0, example:

```
rank_score =
  0.35 * economic_attach
+ 0.25 * complementarity
+ 0.15 * speed_to_pilot
+ 0.15 * trust_credibility
+ 0.10 * sim_frame_fit   # ONLY if twin ≥ T2 and sample_size ≥ 3; else 0 and redistribute
```

Rules:
- Conflict/competitor flag → hard exclude or cap.  
- T1 twins cannot outrank T3 solely on sim.  
- Publish confidence: High (T3+multi-signal), Med (T2), Low (T1/waiver).

---

## 10. Preflight checklist (once per session)

Write `00-preflight/STATUS.md`:

- [ ] Bridge online (fresh machine list; no stale ID)  
- [ ] Browser session for LI (correct profile)  
- [ ] X cookies valid (`auth_token` + `ct0`) or bird installed  
- [ ] yt-dlp available (sandbox or bridge)  
- [ ] AI gateway reachable; JSON mode smoke test  
- [ ] Simulator path + prospect schema version  
- [ ] last30days optional keys (X/Brave) — or declare skip  

If preflight fails, **narrow channel plan** before spawning five deep-dives.

---

## 11. Agent roles (recommended swarm)

| Role | Stages | Model bias |
|------|--------|------------|
| Orchestrator | S0, S2, S9, gates | Strong reasoner |
| Discoverer | S1 | Fast search |
| Identity locker | S3 | Careful, verify |
| Channel researchers | S4 | Parallel workers |
| Analyst + twin | S5–S6 | Citation discipline |
| Sim runner | S7 | Tooling reliability |
| Playbook writer | S8 | Blunt, operational |

---

## 12. Definition of done (single deep-dive)

1. README with start-here + honest gaps  
2. Identity lock pass  
3. Min evidence met; gaps documented  
4. Analysis labeled EVIDENCE/INFERENCE  
5. Twin + SOURCE_MAP + tier  
6. Sims (or explicit skip/waiver) with metrics  
7. Playbook with first message + do-not-say + confidence  
8. RUN_METRICS.json  

Portfolio done = all deep-dives done or timed out + TOPK + rejects + action queue.
