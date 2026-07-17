# Engagement Intelligence — Anti-Patterns

Named failure modes from the 2026-07-16 Votee + HK partners run.  
Use names in reviews: “this is **Empty-Tool Oracle**.”

Format: **Name** · Symptom · Why harmful · Detection · Fix

---

## 1. Deep-Dive First Tunnel

**Symptom:** Full twin/sim/playbook on one entity before a scored universe exists.  
**Why harmful:** High cost sunk on wrong archetype or wrong company; portfolio learning delayed.  
**Detection:** `03-deep-dives/` or equivalent exists while `01-discovery/` / `02-shortlist/` missing or written after.  
**Evidence:** Votee pack completed before HK universe; called out in `hk-partners/00-reflection-plan/REFLECTION_AND_IMPROVED_PROMPT.md`.  
**Fix:** Hard stage order S1→S2 before S3+; single-target only with explicit waiver.

---

## 2. Wrong-Slug Doppelgänger

**Symptom:** Research attaches to similarly named LI company/handle (staffing firm, different product brand, inactive X).  
**Why harmful:** Twin and outreach address the wrong org; silent corruption.  
**Detection:** Follower counts absurdly low; industry mismatch; site URL not linked from profile.  
**Evidence:** `thinkcol` vs `thinkcol-limited`; HelloVotee vs @Beever_AI; Fabrix name collision notes.  
**Fix:** Identity lock stage; record wrong-slug warnings; require site↔profile bidirectional check.

---

## 3. Empty-Tool Oracle

**Symptom:** “No recent activity” concluded because last30days/X/LI returned zero, not because market is quiet.  
**Why harmful:** False negative on targets; wasted empty artifacts treated as findings.  
**Detection:** stderr shows 0 results + auth/cookie hints; brand known active on other channels.  
**Evidence:** `votee-partnership/08-last30days/votee.stderr` (0 web/reddit/yt); X unlock tips.  
**Fix:** Treat empty tool as **GAP**, not signal; require alternate source before “no activity.”

---

## 4. Schema Cosplay

**Symptom:** All folders 00–12 exist; several are empty or only NOTES saying tool missing.  
**Why harmful:** Creates illusion of multi-source research; downstream twin looks complete.  
**Detection:** Byte counts near zero; README gaps contradict “full pack.”  
**Evidence:** Multiple packs with absent/empty `08-last30days`, thin `04-x`, missing transcripts.  
**Fix:** Folder without content must include `GAP.md` with impact on twin tier; gate on evidence min, not folder presence.

---

## 5. n=1 Monte Carlo Theater

**Symptom:** Strategies ranked with WinRate/Meeting scores at `n=1`; treated as statistical truth in Top-K.  
**Why harmful:** Overfits noise; ranks partners on random sim variance.  
**Detection:** Logs show `n=1`; sample_size not in metrics; TOP docs cite sim meet% heavily.  
**Evidence:** ThinkCol `email-run.log`; TOP5 formula 25% conv-sim with caveat underweighted.  
**Fix:** sample_size≥3 for ranking inputs; else label directional and cap sim weight to 0.

---

## 6. Brochure Twin

**Symptom:** TWIN.md reads like About page + product bullets; no first-person voice, few quotes, weak objections.  
**Why harmful:** Sims optimize against marketing copy, not a decision-maker.  
**Detection:** Twin chars low; SOURCE_MAP cites only homepage; no long-form media.  
**Evidence:** ThinkCol twin ~2.5k vs Votee ~22k; OneAsia/WeExpand media gaps.  
**Fix:** Twin tier T1–T3; block heavy sim on T1 without waiver; prioritize long-form capture.

---

## 7. Source-Map Amnesia

**Symptom:** Twin claims without path citations; SOURCE_MAP missing or one-liners.  
**Why harmful:** Un-auditable; agents invent personality traits.  
**Detection:** No `SOURCE_MAP.md` or claims not listed.  
**Evidence:** Variable quality maps; best practice is Votee SOURCE_MAP.  
**Fix:** Fail-closed gate: every non-obvious twin claim → file path.

---

## 8. Gateway Shrug

**Symptom:** JSON parse errors / HTTP 400 mid-sim; process continues or dies without partial accounting.  
**Why harmful:** Lost runs; silent incomplete N; false “20 strategies” claims.  
**Detection:** `*.stderr` non-empty; completed count < requested.  
**Evidence:** Votee `email.stderr` JSON parse; OneAsia “Simulation 19/20 failed: AI Gateway error (400)”.  
**Fix:** Retry budget; JSON repair; always log completed/failed; don’t assert N without completed.

---

## 9. Parallel Tool Debt Multiplier

**Symptom:** Five agents each discover bird/yt-dlp/cookies missing independently.  
**Why harmful:** Multiplies setup waste; systematic channel gaps across portfolio.  
**Detection:** Same GAP language in every pack’s X/YT notes.  
**Evidence:** WeExpand X_NOTES (no bird/ct0); WeExpand YT (no yt-dlp); OneAsia bridge 403.  
**Fix:** Session preflight `00-preflight/STATUS.md` before swarm spawn.

---

## 10. Sim-Led Ranking

**Symptom:** Partner with weaker economic evidence ranks above stronger shortlist because conversation meeting score is higher.  
**Why harmful:** Ranks model self-talk over distribution/complementarity.  
**Detection:** Rank order inverse to shortlist without new hard evidence; T1 twin + high sim.  
**Evidence:** WeExpand shortlist 3.85 but rank #1 on sim; Set Sail shortlist 4.30 → #3.  
**Fix:** Freeze formula; sim only reorders among T2+; economic score primary.

---

## 11. Claim Laundering

**Symptom:** Company-asserted metrics (logos, “150 solutions”, “120M replies”) enter twin as facts.  
**Why harmful:** Outreach and ranking treat marketing as audited truth.  
**Detection:** Numbers only on own site; no third-party corroboration; labeled EVIDENCE incorrectly.  
**Evidence:** Set Sail metrics path in SOURCE_MAP from site summary.  
**Fix:** Label **CLAIM** vs **EVIDENCE**; require third-party for ranking-critical numbers.

---

## 12. Captions-or-Nothing

**Symptom:** YouTube found but no EN captions → entire video abandoned; no description/chapters/alternate.  
**Why harmful:** Drops highest-ROI voice source.  
**Detection:** INVENTORY lists video with “no EN”; no fallback extract.  
**Evidence:** Votee Unsensible gap; Set Sail promo-only inventory; ID collision note.  
**Fix:** Fallback chain: manual auto-subs → description → chapters → related interview → GAP impact.

---

## 13. Confidence Laundering

**Symptom:** Playbook language absolute (“always”, “will disengage immediately”) from n=1 sim prose.  
**Why harmful:** Operators overtrust; no uncertainty for A/B outreach.  
**Detection:** Playbook lacks confidence tag; copies simulator boilerplate.  
**Evidence:** Votee APPROACH_PLAYBOOK sim-generated sections read certain.  
**Fix:** Require confidence + twin tier header; rewrite sim dump into conditional advice.

---

## 14. Channel Monoculture

**Symptom:** One strong channel (site or LI company) used for everything; others not attempted or failed silently.  
**Why harmful:** Misses contradictory signals (CTO essays vs CEO stage voice).  
**Detection:** SOURCE_MAP dominated by one folder.  
**Evidence:** Several HK packs site-heavy; Votee success was multi-channel.  
**Fix:** Min two source classes for T2; attempt each channel or GAP.

---

## 15. Partnership-as-Product Pitch

**Symptom:** Outreach frame is seat/SaaS dump despite offer axioms saying co-build/partner.  
**Why harmful:** Triggers need/overlap objections; kills meeting rates in sim and likely in life.  
**Detection:** Email lead with features not architecture boundary; no attach economics.  
**Evidence:** Sims consistently rewarded complementarity frames (“context+computer”, “runtime under agents”).  
**Fix:** Encode non-goals in offer; reject strategies that violate non-goals before sim scoring.

---

## 16. Process-Cost Ranking

**Symptom:** Already-researched target demoted because “cycle already spent,” not strategy.  
**Why harmful:** Confuses sunk cost with expected value.  
**Detection:** Honorable mention rationales about effort already spent.  
**Evidence:** Votee TOP5 honorable mention wording.  
**Fix:** Rank on expected outcome only; track research cost separately.

---

## 17. Authwall Surrender

**Symptom:** LI personal profile authwalled once → permanent “no LinkedIn” for pack.  
**Why harmful:** Abandons primary B2B voice surface in many geos.  
**Detection:** Notes say authwall; no bridge/Kimi retry; no SERP post reconstruction.  
**Evidence:** ThinkCol Kane feed; OneAsia bridge 403 without recovery.  
**Fix:** Authwall playbook: bridge health → alternate machine → SERP posts → employee list → GAP.

---

## 18. Analyzer-Afterlife

**Symptom:** Simulations complete; analysis step crashes; samples missing or playbook incomplete.  
**Why harmful:** Raw results unusable without ranking/insights.  
**Detection:** results present, report/playbook absent; stderr on analyzer.  
**Evidence:** Votee first email run fatal in result-analyzer JSON parse.  
**Fix:** Persist raw results before analyze; analyzer retries independent of sim.

---

## Quick match table

| If you see… | Call it… |
|-------------|----------|
| Beautiful empty folders | Schema Cosplay |
| last30days zero = “quiet market” | Empty-Tool Oracle |
| Rank by sim meet% | Sim-Led Ranking |
| Twin from homepage only | Brochure Twin |
| Five agents lack yt-dlp | Parallel Tool Debt Multiplier |
| thinkcol (wrong co) | Wrong-Slug Doppelgänger |
| WinRate 100% n=1 | n=1 Monte Carlo Theater |
| “Always open with…” from sim | Confidence Laundering |
