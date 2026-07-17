# Preset: HappyCapy × Hong Kong B2B partners

**Preset id:** `happycapy-partner-hk`  
**Skill:** engagement-intel v2  
**Mode:** portfolio (default) or single  
**Class:** partner (complementary collab, not pure SaaS dump)

Use this when the user wants HappyCapy partnership discovery / twin+sim / playbooks in **Hong Kong** (or APAC with HK phase-1).

---

## 1. Offer axioms (freeze in `00-plan/OFFER.md`)

### Product (HappyCapy)
Source of truth: `~/.claude/happycapy-platform-overview.md`

HappyCapy = **always-on cloud computer + AI agent** with unrestricted in-sandbox access (browser entrypoint).

Primitives:
1. Isolated always-on machine (persistent disk/network)
2. Agent with full terminal + root (default Claude Code harness; other harnesses installable)
3. Multi-model AI gateway (LLM + image/video/audio)
4. Skills marketplace (ClawHub / installed skills)
5. Instant public URLs for services in the sandbox
6. Connect My Mac / bridge — local files, terminal, browser sessions
7. In-sandbox browser automation

### What we sell / propose to partners
**Execution runtime (“agent computer”)** that sits **under or beside** their agents/products:

- They own: domain, models, context, CX workflows, SI delivery, GTM, data-centre channel, etc.
- We own: durable always-on computer, tool install, deploy, long multi-step agent work, multi-model gateway, Mac bridge

**Winning frame (from prior sims):**  
**context / domain / agent product + computer (HappyCapy)** — co-build / co-sell / embed runtime.

### Non-goals (do not claim)
- Not “another chatbot / agent builder that replaces theirs”
- Not competing as private-assistant UI when they already sell OneGenie-class products
- Not pure reseller dump of seats with no joint pilot
- Not hyperscaler peer positioning (AWS/Azure/Tencent as equals)
- Not military / dual-use if counterparty redlines say so

### Ideal outcomes to optimize for
1. Intro / technical call accepted  
2. Joint pilot with a **named** enterprise client (bank, corporate, gov-adjacent)  
3. Integration workshop (CTO / chief scientist / SI lead)  
4. Channel attach (SI SOW line item, CX package, DC/GPU attach, GTM embed)  
5. Ecosystem referral (Cyberport, HKMA sandbox network, HKSTP)

### Proof points agents may use (update as product evolves)
- Always-on sandbox + root agent (real computer, not chat session)
- Multi-model gateway without customer key sprawl
- Skills extensibility
- Mac bridge for hybrid enterprise workflows
- Instant public URL export for demos/pilots
- Prior partner frames: Votee (context+computer), ThinkCol (SI runtime), Set Sail (CX + computer), OneAsia (DC attach, non-compete layering), beNovelty (FabriXAI harness), WeExpand (GTM embed)

---

## 2. PARAMETERS defaults

Copy into `00-plan/PARAMETERS.md` (adjust geo if needed):

| Parameter | Value |
|-----------|-------|
| offer | Complementary **partnership**: HappyCapy as agent **execution computer** under/beside partner agents (co-build, co-sell, embed) |
| offer_non_goals | Not replace their agent product; not reseller-only dump; not compete as private chatbot UI; not hyperscaler peer |
| counterparty_class | partner |
| archetypes | SI/AI consultancy; vertical agent SaaS (CX, sales, ops); private AI + DC/MSP; agent builder / API platform; GTM/sales-agent services; localized LLM/context layer; hub/accelerator (light touch) |
| geo | **Hong Kong first** (phase-1 deep-dives). Singapore / SEA = phase-2 names only unless user expands |
| success_metric | Joint pilot booked or technical working session with DM + clear attach economics |
| dm_role_priority | CEO/Co-founder > Head of Sales/BD > CTO/Chief Scientist (bring tech peer early on calls) |
| scoring_rubric | Dist 25%, Complementarity 20%, Enterprise trust 15%, Speed 15%, Revenue 15%, Optionality 10% (0–5 each) |
| deep_dive_bar | weighted ≥ **3.2** AND complementarity ≥ **3** |
| sim_email_n | 20 |
| sim_conversation_n | 10 |
| sim_sample_size | **3** (required for any sim weight in Top-K) |
| sim_for_ranking_min_n | 3 |
| sim_weight_if_n_lt_3 | **0** (directional only; redistribute to economic_attach + complementarity) |
| mode | portfolio |
| preset | happycapy-partner-hk |
| product_doc | ~/.claude/happycapy-platform-overview.md |
| reflections | outputs/workflow-reflections/ (if present in workspace) |

### Ranking formula (freeze for S9)

```
rank_score =
  0.30 * economic_attach
+ 0.25 * complementarity
+ 0.15 * speed_to_pilot
+ 0.15 * trust_credibility
+ 0.15 * sim_frame_fit   # ONLY if twin ≥ T2 AND sample_size ≥ 3; else 0 and reweight
```

Hard exclude / cap: pure competitive agent-cloud (e.g. Tencent WorkBuddy-class), hyperscaler-as-peer.

---

## 3. Archetype map (HK-oriented)

| Archetype | Why complementary | Revenue path | Conflict watch |
|-----------|-------------------|--------------|----------------|
| SI / AI consultancy | They implement agents; need durable runtime | SOW line item / multi-client reuse | Don’t displace their AWS/Databricks story |
| Vertical agent SaaS (CX, sales) | They own workflows; need hybrid staging/integrations | Co-sell package; implementer seats | Don’t pitch as competing contact-centre product |
| Private AI + DC / MSP | Infra + regulated channel | GPU/DC attach + joint FSI/edu pilots | Layer beside private assistant; never “we replace your private AI” |
| Agent builder / API platform | They author agents; we run them | Runtime per deployment; bank pilots via API gateways | Architecture boundary first |
| GTM / sales-agent services | Channel into inbound clients | Embed under their agents; co-sell | Protect client ownership; not a competing sequencer |
| Localized LLM / context | Context layer + computer | Co-sell enterprise; regulated language | Long cycle; dense hyperscaler graph |
| Hub / accelerator | Dealflow + brand | Pipeline only | Light touch — not full twin unless strategic |

---

## 4. Tool paths (HappyCapy sandbox defaults)

Declare actual status in `00-preflight/STATUS.md` each session (IDs rotate).

| Capability | Default path / method |
|------------|----------------------|
| Skill | `~/.claude/skills/engagement-intel/` |
| Init | `python3 ~/.claude/skills/engagement-intel/scripts/init_run.py` |
| Gates | `check_identity_lock.py`, `check_twin_gate.py`, `check_sim_sample_size.py --for-ranking`, `validate_run.py` |
| Product facts | `~/.claude/happycapy-platform-overview.md` |
| Process memory | `outputs/workflow-reflections/` |
| last30days | `last30days` CLI / `~/.claude/skills/last30days/` — **optional**; brand-thin HK → skip or directory fallback |
| Mac bridge | Fresh `GET /api/bridge/machines` — do **not** hardcode stale bridge IDs |
| LinkedIn | Kimi Web Bridge on Mac (`http://127.0.0.1:10086` via bridge `terminal/exec`); profile with real login |
| X / Twitter | Mac Chrome cookies → `AUTH_TOKEN`+`CT0` in `~/.config/last30days/.env` or env; bird-search: `~/.claude/skills/last30days/scripts/lib/vendor/bird-search/bird-search.mjs` |
| YouTube transcripts | Mac `yt-dlp` + chrome cookies via bridge; **quote URLs** for zsh; skill `youtube-transcript` |
| Sales simulator | Prefer `outputs/votee-partnership/tmp/ai-sales-agent-simulator` if present (gateway patched), else install/clone `ai-sales-agent-simulator` |
| AI gateway | `$AI_GATEWAY_BASE_URL/api/v1/chat/completions` + `$AI_GATEWAY_API_KEY`; browser-like User-Agent; `Accept-Encoding: identity` |
| Python for gates | system `python3` OK for scripts; sales-sim may need Node 18+ |

### Preflight checklist (this preset)

- [ ] Bridge online (fresh list)  
- [ ] Kimi reachable on Mac for LinkedIn  
- [ ] X cookies valid or declare X = GAP  
- [ ] yt-dlp on Mac or declare YT = GAP  
- [ ] Gateway JSON smoke  
- [ ] Simulator path exists; prospect schema known  
- [ ] last30days: use only if chatter-rich; else skip  

---

## 5. Research priorities (S4)

Order of ROI for HK B2B partners:

1. **Company site + product pages** (always)  
2. **Long-form founder interview** (YT/podcast) — highest twin quality  
3. **LinkedIn** company + DM (Kimi; resolve slug carefully)  
4. **X** active brand (verify handle; avoid doppelgängers)  
5. Third-party press / case studies  
6. last30days only if topic is noisy globally  

Empty channel → `GAP.md` with twin-tier impact. Never silent empty folders.

### Identity lock extras (HK)

- Confirm **legal name vs brand** (e.g. Set Sail Software vs chatbot.com.hk)  
- Confirm **active X brand** (e.g. HelloVotee vs Beever_AI pattern)  
- LI company slug ≠ staffing/doppelgänger  
- Record Cyberport / HKSTP / HKMA sandbox adjacency if claimed  

---

## 6. Twin + sim guidance

### Twin
- Declare **Tier T1/T2/T3** in `TWIN.md`  
- `SOURCE_MAP.md` required  
- Include stakeholder map: CEO, CTO/scientist, sales head  
- Biases: EVIDENCE vs INFERENCE  
- Partnership posture: partner-curious / buy-skeptical defaults for HK enterprise  

### prospect.json
Include HappyCapy **partnership** framing in `companyInfo` (complementary computer, not SaaS dump).

### Sim
- Modes: **email 20 + conversation 10** (conversation weighted for partners)  
- Strategy prompts **must** include product name “HappyCapy” and non-goals  
- Ban invented mutuals, fake logos, unverified ROI % in playbook synthesis  
- If simulator only supports n=1: mark `directional_only: true` and **zero sim weight in S9**  
- Prefer human `APPROACH_PLAYBOOK.md` over raw auto-playbook  

### Do-not-say (default list for playbooks)
1. “We replace your agent platform”  
2. “Just buy seats / reseller only”  
3. Generic AGI hype without architecture  
4. Claim bank logos or metrics without SOURCE_MAP evidence  
5. Compete head-on with their private assistant / CX bot product  

---

## 7. Output defaults

| Item | Default |
|------|---------|
| Run root | `outputs/happycapy-partners-hk-<YYYYMMDD>/` or user slug |
| Deep-dives | `03-deep-dives/<entity-slug>/` |
| Rank | `04-rank/TOPK.md` |
| Rejects | `99-rejects/REJECTS.md` |
| Prior art (read, don’t overwrite) | `outputs/votee-partnership/`, `outputs/hk-partners/` |

---

## 8. How to apply this preset

```bash
python3 ~/.claude/skills/engagement-intel/scripts/init_run.py \
  outputs/<run-slug> --mode portfolio --preset happycapy-partner-hk
```

Or in-agent:

1. Skill `engagement-intel`  
2. Read `references/presets/happycapy-partner-hk.md`  
3. Copy axioms into `00-plan/OFFER.md` + `PARAMETERS.md`  
4. Run S0→S9 with hard gates  

### Slash

`/engagement-intel happycapy-partner-hk`  
`/engagement-intel portfolio HK partners for HappyCapy` (should load this preset)

---

## 9. Known good / known bad (from 2026-07-16 run)

**Often strong fit:** SI (ThinkCol), CX agents (Set Sail), agent builder (beNovelty), GTM embed (WeExpand), DC/private AI channel (OneAsia if layered), context LLM (Votee).  

**Usually reject / deprioritize:** competitive agent workspace (Tencent WorkBuddy-class), Microsoft as peer, pure robotics without software attach.

**Process:** Always follow `outputs/workflow-reflections/` non-negotiables if present.
