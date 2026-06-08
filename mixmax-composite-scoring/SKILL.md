---
name: mixmax-composite-scoring
description: Self-contained orchestrator that computes the Mixmax composite ICP score (v5.3 — layered, evidence-weighted) for one or many accounts and returns a stack-ranked priority list. v5 replaces blended pools with a layered model — gates, then an external-signal base rank computed for EVERY account, then product/intent escalators as bounded additive boosts. Three models read one signal library: Model A prospect acquisition, Model B customer expansion, Model C win-back. Weights are locked to a 100-won/60-lost truth-cohort backtest (2026-06-06). Trigger on "composite score", "score these accounts", "rescore", "rank by composite", "stack rank", "ICP score for X", "is this an Aero false negative", "prioritize these leads", or any multi-source account qualification. Canonical methodology: https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html
---

# Mixmax Composite Scoring v6 — Layered Signal Library (MASTER)

**Canonical (locked 2026-06-06, QA-verified):** https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html
Supersedes v4. Three models, one library: **A** prospect acquisition · **B** customer expansion · **C** win-back.

## Architecture — layered, never blended

The v4/v3 lesson: components with different fill rates cannot share one weighted pool — the highest-fill signal dominates regardless of weights. v5 layers:

1. **Layer 0 — gates:** email stack multiplier (Gmail 1.00 / Microsoft 0.55 / unknown-or-other 0.90). **The email question is answered by MX records (DNS) first** — free, every domain; SFDC `Email_Provider__c` is cross-validated against MX, never trusted alone (disagreements -> discrepancy report); Octave disqualifier -> cap 40; zero sales-motion fingerprints -> cap 55.
2. **Layer 1 — base rank** from EXTERNAL signals, renormalized over filled components (`score = SUM(wi*Fi*filledi)/SUM(wi*filledi)`), with a Coverage stamp (cap 65 when <0.5). Missing enrichment is never scored as zero.
3. **Layer 2 — escalators**, bounded ADDITIVE boosts (multiplicative saturates the ceiling): product usage +6 (PES>=40 / free seats / trial) or +12 (PES>=75 / paid usage); first-party buyer intent +8 (1 person, CR ls_464 >=75pct) or +15 (>=2 people). DQ accounts: boosts capped at +4.

## Model A locked base weights (truth-cohort evidence)

| w | Component | Evidence |
|---|---|---|
| .24 | Octave ICP (x10; disqualifier caps at 40) | qualitative anchor |
| .18 | SFDC history gradient: won-lapsed 85 / closed-lost 65 / open 50 / cold 20 | pending echo test; routing-grade |
| .14 | Sales hiring <=90d, **presence-flattened** (>=1 posting=100, 0=40) | **1.55x won/lost** — volume >=3 falsified (0.91x) |
| .13 | Competitor sales-engagement tool in stack (NO COMPETITION=40) | displacement targeting |
| .10 | CR committee depth gradient (20+:100 / 10+:75 / 5+:50 / 1+:25) | |
| .08 | Contact-sales/demo CTA on website | **1.22x** + DQ-tier separation (17% vs ~50%) |
| .07 | CRM in stack | qualifier-grade (1.12x) |
| .06 | Size band (25-2000 FTE=100) | won median 108 vs lost 46 FTE |

**Weight ZERO (falsified or unproven — do not reintroduce without a new backtest):** sales-role presence 0.96x · sales-headcount magnitude ~1.15x · hiring volume >=3 0.91x · YoY headcount growth 1.18x (retest quarterly) · Bombora/third-party topic intent 0.57x (inverse) · **Aero: weight zero, graded** — compute it, emit an accuracy report, never weight it.

**Tiers:** >=80 Hot · 65-79.9 Warm · 50-64.9 Watch · <50 DQ. The action list is the **>=90 strike band**.

## Model B (customer expansion) — per-domain
Adoption/PES .30 · seat-whitespace (seats/employees; *denominator upgrade: Crustdata sales headcount*) .25 · sales-hiring timing .20 · ARR headroom .15 · utilization (used/purchased) .10. **Rule: utilization <40% AND PES <40 -> SAVE-FIRST flag — retention play before any expansion pitch.**

## Execution — the end-to-end run (self-contained; follow in order, checkpoint after every step)

This section is sufficient to run the entire scoring workflow autonomously. Rules of the road: **a component is a question, the CRM is a source, never the verdict** — cross-validate filled SFDC fields against their external source on every full pass; fill gaps from the waterfall; store every answer locally (domain · question · answer · source · validated-by · timestamp) as the backfill payload. Keep SOQL responses ≤100 records (chunk with LIMIT/OFFSET or `Id IN` lists). Pull high-volume Amplitude events in gp:domain `glob match` letter chunks (`a*`…`[!a-z]*`) — the 1,000-group cap silently truncates the long tail otherwise. Checkpoint each pull to disk before the next.

### The question → waterfall map (run one row at a time)

| # | Question | First answer | Cross-validate / fill | Last resort |
|---|---|---|---|---|
| 0 | Lifecycle + commercial state? | SFDC `RecordTypeId` + `DWH_DS/SS_Customer_ARR__c` | never cached, never overridden | — |
| 1 | Which email stack? | **MX records** (`dig +short MX {domain}` — free, every domain) | SFDC `Email_Provider__c` audited vs MX; disagreements → discrepancy report | DWH connected-client |
| 2 | Salesforce / HubSpot in stack? | SFDC `CRM__c` | Common Room / Crustdata technographics | BuiltWith via Deepline |
| 3 | Hiring sales now? | TheirStack via Deepline (≤90d, batches of 40 domains) | — single tested source | PDL jobs |
| 4 | Sell like our buyers (CTA)? | PredictLeads via Deepline | Firecrawl crawl on miss | — |
| 5 | Reachable sales DM? | SFDC contacts / `Decision_Maker__c` | FullEnrich `search_people` (FREE — run on every account) | FullEnrich credit waterfall (ONLY on play entry) |
| 6 | Right size? | Crustdata headcount (25/batch) | SFDC `CR_Number_of_Employees__c` | LinkedIn via Deepline |
| 7 | Using the product? | Amplitude → PES-M v2 (chunked pulls) | SFDC verdict + existing brief = cache only, never source | — |
| 8 | Anyone in-market? | Common Room `ls_464` ≥75pct | — | — |
| 9 | ICP at all? | Octave `qualify_company` — shortlist only, after cheap signals | — | — |

### Every provider in the flow — the complete enrichment map

| Provider | Via | Delivers | Consumed by | Cost posture |
|---|---|---|---|---|
| Salesforce | MCP direct | RecordType, PQA/OQA dates, opps, contacts, Sold_to_*, PLAN fields | Play gate · triggers · context | free, every refresh |
| Warehouse (DWH) | SFDC fields | DS/SS ARR, customer type, team+user counts | Model selection · Model B · whitespace | free, every refresh |
| MX records | DNS direct | Email provider ground truth | Email gate + SFDC audit | free, every domain |
| Amplitude | MCP direct (proj 130895, gp:domain) | Capability matrix → PES-M v2 + AI Score | Product escalator · AI escalator · ghost trigger | free, every refresh |
| TheirStack | Deepline | Sales postings ≤90d | Hiring (.30, 1.55x) | cheap, weekly |
| PredictLeads | Deepline | CTA / pricing evolution | CTA (.13, 1.22x) · sales-motion gate | cheap, monthly |
| Firecrawl | Deepline fallback | Direct crawl on PredictLeads miss | CTA backfill | cheap, on miss |
| Crustdata | Deepline | Headcount by role, totals, growth | Size (.10) · CRM cross-check · Model B denominator | moderate, monthly |
| Common Room | MCP direct | Intent people (ls_464), contacts, technographics | Intent +8/+15 (3.22x) · CRM cross-check | licensed, weekly |
| FullEnrich | MCP direct / Deepline | Search = DM findability (free); waterfall = verified email+mobile (credits) | DM (.12) · SS→DS gate · outreach contacts | search free; credits on play entry ONLY |
| Octave | MCP direct | Qualitative ICP + hard DQs + playbook | DQ gate · Octave Play column | expensive — shortlist only |

**Budget posture (locked): money follows the score, it never precedes it.** Rank everyone with the free/cheap rows; spend (FullEnrich credits, Octave) only where an account enters a play. Freshness, not trust: `*_Refreshed_At__c` stamps decide when to re-pull, never whether to verify.

### Run order

1. **Universe (SFDC):** bulk SOQL — Id, Name, Website, `RecordTypeId`, `Account_GTM_Stage__c`, Owner.Name, `Email_Provider__c`, `CRM__c`, `Sales_Acceleration_Tool__c`, `Channel_Source__c`, DWH ARR fields, PQA/OQA dates, opp history. Re-pull lifecycle every run; drift is real.
2. **Lifecycle gate → play candidate** (mutually exclusive, priority order): Competitor-exclude → In-Flight → Expansion → SS→DS → Win-Back → PQA Re-Engage → Net-New. Channel segments within a play, never defines it.
3. **Enrich** every account through the question→waterfall map above (full universe BEFORE scoring; coverage caps flag pipeline failures, they never excuse unanswered questions). Hiring: `theirstack_job_search`, `posted_at_max_age_days` 90, title patterns ["sdr","bdr","sales development","account executive","account manager","revenue operations","head of sales","sales manager","vp sales"]. CTA: `predictleads_company_website_evolution`, regex `(?i)(contact[ -]sales|talk[ -]to[ -]sales|book[ -]a[ -]demo|request[ -]a?[ -]?demo|get[ -]a[ -]demo|schedule[ -]a[ -]demo|speak (to|with) (sales|an expert))`.
4. **PES-M v2 + AI Score:** run `Revenue Reviews/specs/pesm_v2_scorer.py` against fresh chunked Amplitude pulls (or reuse a ≤7-day-old score set).
5. **Score** per the layer math above (gates → renormalized base → escalators). Model by commercial state (DWH ARR>0 → Model B), never by play.
6. **Deliver:** stack rank + tier + per-component "why this score" + Coverage + AI negative-space line + play + Octave playbook + best contact. The score is never delivered without its evidence.
7. **Local store:** write the enrichment store + scores to disk; this is the system of record until RevOps creates the `Composite_*` fields, then it is the backfill payload.

### Self-QA (mandatory before any deliverable leaves the run)

1. **Lifecycle audit:** zero Fall-Off/Customer accounts in prospect plays; spot-check 5 accounts' RecordType live.
2. **Distribution sanity:** tier distribution within ±30% of the last accepted run (flag, don't auto-ship, if outside).
3. **Known-account regression:** Disqo-class spot checks — 3 accounts with briefs; score story must match brief story.
4. **Coverage audit:** % accounts with each question answered; any component <80% filled on the scored cohort → investigate truncation/pipeline failure before shipping.
5. **Discrepancy report:** SFDC-vs-external disagreements (email, CRM, size) written out for RevOps.
6. **Math audit:** recompute 5 random scores by hand from components; must match.
7. **Evidence audit:** every delivered row has non-empty why-text, play, and tier.

### Model feedback report (ship with every full run)

Emit `model_feedback_{date}.md` with: (a) per-component fill rates + any component whose fill changed >10pts; (b) per-component paying-vs-free separation on the current universe vs the locked benchmarks (CRM 1.64x · hiring 1.55x · CTA 1.22x · intent 3.22x · PES-M verdict 4.7x · AI>0 1.43x); (c) escalator hit-rates (how many accounts got +6/+12, +3/+5, +8/+15); (d) DQ + ghost-active counts; (e) **suggested updates** — any component whose live separation falls below 1.2x (flag for demotion test), any shadow signal above 1.5x (flag for promotion test), instrumentation bugs hit. Suggestions feed the quarterly re-fit; nothing changes weights without a pre-registered test (section: Discipline).

## Discipline (the AI-native loop)
New signals enter at weight zero -> shadow-score -> won/lost lift test (promotion >=~1.5x; <1.2x stays qualifier) -> promote/retire. Quarterly re-fit on the grown cohort; every re-fit ships as a versioned, QA-verified canonical page. Tests are pre-registered before data is seen (canonical doc section 06b falsification protocol).


## v5.3.1 delivery layer — Plays + per-account evidence (2026-06-07)

Scores rank; **plays decide the motion.** One account = one play, evaluated top-down (canonical doc section 06d):
Competitor-exclude > In-Flight (open opp) > Expansion (`DWH_DS_Customer_ARR__c` > 0 or RT=Customer) > SS->DS (`DWH_SS_Customer_ARR__c` > 0, DS=0) > Win-Back (RT=Fall Off, no ARR) > PQA Re-Engage (RT=Prospect + PQA date) > Net-New.

**Hard rules:**
- `Account.RecordTypeId` is the lifecycle gate — never derive cohorts from field filters alone. Re-pull on every refresh (drift is real week-to-week).
- ARR truth = `DWH_DS/SS_Customer_ARR__c` + `DWH_Customer_Type__c`. Never read ARR from derived sheets. Self-serve payers keep RT=Prospect by design.
- Channel (`Channel_Source__c`) segments WITHIN a play; it is never a model input or play gate. (2026-06-07 product-channel remap in SFDC: model + plays unaffected; channel cuts in downstream reports have a break-in-series at that date.)

**Per-account evidence contract ("Why this score"), in order:**
1. Escalators first (live product usage + buyer-intent) — the rep's outreach context.
2. Fit case: CRM-in-stack (Salesforce/HubSpot = the strongest correlated stack signal), hiring count, displaceable competitor, talk-to-sales CTA.
3. Gmail as qualifier ("they qualify for our motion"), never as the win driver. Microsoft = the cap explained.
4. Caveats stated plainly: Octave DQ cap, coverage cap, unknown email stack haircut.
Plus per account: Amplitude capability breakdown (what they use / don't, from `amplitude-event-taxonomy`; flag ghost-active), Octave play (native assignment where scored; rule-based fallback marked *), SFDC deep link, and for Win-Back the loss story (last lost renewal CloseDate + Amount + `Loss_Reason__c` + `Main_Competitor__c`, `Past_Renewals__c` tenure, still-active users).

**Proposed v5.4 (not yet weighted):** capability breadth (uses x/6 tracked capabilities) as a bounded escalator. Requires backtest per the discipline loop.

**Field/event fixes (verified live 2026-06-07):** Opportunity competitor field is `Main_Competitor__c` (`Competitor__c` does not exist). Amplitude `Template` filter is `action = "Create"` (capitalized). `followup created` returned zero volume in 90d — taxonomy needs the current AI-followups event name.


## v5.4 (sample-validated 2026-06-07) — pipeline changes

Validated on an 18-account stratified sample (3 per play, full enrichment rebuild, byte-identical re-run). Weights unchanged pending re-fit; these are STRUCTURAL changes:

1. **People component (.10) = DM findability, not committee depth.** FullEnrich database search (search_people, zero credits): sales-leadership title found at the domain = 100, not found = 0. Found 12/18 on sample; misses correctly identify non-ICP motion (nonprofits, VCs, consumer). Waterfall enrichment (email+mobile) only fires on play entry.
2. **Product escalator reads Amplitude ONLY** (never Aero PES): +6 = >=5 active users 30d at gp:domain; +12 = >=2 capabilities with >=3 users (or paying + active). Read order: SFDC Product_Engagement_Verdict__c (fresh) -> existing Customer Strategy Brief (same taxonomy — apples-to-apples) -> fresh Amplitude pull last.
3. **DQ accounts: flagged, never ranked.** They exit play work queues; capped score retained for audit/grading only.
4. **Model selection by commercial state, never play:** DWH ARR > 0 -> Model B; else Model A. (In-Flight prospects = A; In-Flight payers = B.)
5. **Octave reframed: validated qualifier.** Flat-within-closed-deals (1.03x) is the expected result for a gate — every tested deal already passed ICP. The DQ boundary is the validated part; keep gate + weight, revisit at re-fit with this framing.
6. **Shadow signals (computed, not weighted):** capability breadth (x/6) and team whitespace (teams sold / DWH teams present, fields: Sold_to_SDRs/AEs/full_cycle_AE_team/Success/Partner_Manager_Team/Recruiting/Other__c over DWH_of_Teams__c + DWH_of_AE/SDR/CS_Users__c). Promote per the discipline loop only.
7. **SS->DS play gate:** a paying SS account with no findable sales-titled DM cannot run a conversion motion — route to usage-expansion touch instead.

Field name corrections (verified live): `Sold_to_AEs__c`, `Sold_to_full_cycle_AE_team__c` (not Sold_to_full_cycle_AE__c); Opportunity competitor = `Main_Competitor__c`; channel context = `Channel_Source__c` for prospects without an open opp, `Opportunity_Source__c` on new-business/conversion deals.


## Model close-out (2026-06-07) — all open questions resolved

- **History: OUT of the score.** Echo test: prior-won accounts won at 84% vs 82% baseline (1.02x) within engaged accounts — flat + circular. History is context-grade: evidence text + routing only. Weights renormalize over remaining filled components.
- **PES-M v2 locked 2026-06-07** (the Mixmax Product Engagement Score, separate model): `0.25*Activity + 0.35*Breadth + 0.40*Depth` at gp:domain, plus a separate **AI Score** (0-100 over 4 AI products — AI Compose, Smart Send AI ai-recommendation only, Smart Follow-ups, Meeting Copilot — with a per-account negative-space gap line). Activity = blend of WAU percentile (40%) + power users = 4-wk floor of weekly sequence users (30%) + core sequence adoption rate (30%). Breadth = 4 product buckets: Engagement 40 / CRM&Platform 25 / Meetings 20 / AI 15 (bucket credit = best member tier; the grid is the SKU whitespace map). Depth = credibility-scaled adoption_rate (min(1,users/3)), sequences 3x, CRM sync 2x. Email sends excluded by design. Tier guards: Power needs rate>=Q3 AND >=3 users; Established rate>=median AND >=2; unknown _active denominator caps at Emerging. Calibration = population quartiles (pesm_v2_calibration.json). GHOST_ACTIVE/NO_DATA overrides retained; momentum 'woke up' flag for zero->active capabilities in last 4 weeks. Validated on 5,427 domains: verdict separation 4.7x paying vs free (3.8x SS-only — the cleaner test; v1's 9.0x was partly size-circular), >=3 power users = 2.3x, AI>0 = 1.43x. Known exclusions (instrumentation bugs filed): Sequences_AIGeneration_Created zero volume; MCP_Tool_Succeeded lacks gp:domain on 157/190 uniques (MCP = flag only). Scorer (reproducible): Revenue Reviews/specs/pesm_v2_scorer.py; scores v2pull/pesm_v2.csv. Methodology: https://psychic-adventure-p3jj6y9.pages.github.io/operational/pesm-v2-methodology-2026-06-07.html The product escalator and Model B adoption component read PES-M v2; Aero PES is graded against it, never used.
- **Team whitespace validated on the full paying book:** computable 495/777; median coverage 0.00; 280 zero-Sold_to accounts (partly flag hygiene — on the DQ list); 185 addressable targets (>=3 users on unsold teams) on $3.25M ARR. Stays shadow until the forward expansion-outcome lift test; target list ships into the Expansion play now.
- **T8 forward test registered + baselined:** 173 strike vs 173 size-matched 50-79 controls; outcome = new opp or external meeting 2026-06-07 -> 2026-09-04; pass >=2.0x; baseline opp counts snapshotted. Register: Revenue Reviews/specs/t8_forward_test_register.json.


## v6 MASTER (locked 2026-06-07) — the shipping spec

Supersedes the v5.x weight tables above. Rule: weighted only if tested won/lost lift OR written reason survives challenge. Weights evidence-proportional (excess lift), renormalized over filled.

**Gates (all validated):** email via MX-primary (Gmail 1.00 / unknown-or-other 0.90 / Microsoft 0.55, 2.67x; SFDC field audited against MX) · Octave DQ -> FLAG (not ranked) · zero sales-motion fingerprints -> cap 55.

**Rank (Model A):**
| w | Component | Source | Evidence |
|---|---|---|---|
| .35 | Salesforce/HubSpot in stack | SFDC CRM__c | tested 1.64x (52% vs 32%, n=160) |
| .30 | Sales hiring presence <=90d | TheirStack via Deepline | tested 1.55x |
| .13 | Contact-sales/demo CTA | PredictLeads + Firecrawl | tested 1.22x |
| .12 | DM findability | FullEnrich search (free) | reason-kept: feasibility; 12/18 sample; lift test pre-registered |
| .10 | Size band 25-2000 FTE | Crustdata | tested (won 108 vs lost 46 median FTE) |

**Removed from rank:** Octave score (gate+context only; 1.03x within deals), history (echo 1.02x; context), competitor-in-stack (7/160 fills untestable; messaging layer — picks the Octave play), committee depth (superseded by DM findability).

**Escalators:** product +6 = PES-M v2 EMERGING with >=2 capabilities adopted (foothold guard — v2 Emerging is broad), +12 = ESTABLISHED/POWER; AI adoption +3 = AI Score >=25 (1 AI product), +5 = AI Score >=50 (2+) — locked 2026-06-07 on tested 1.43x lift, the PLG commitment, re-fit quarterly (breadth escalator removed — redundant, 35% of PES-M) · intent +8/+15 (CR ls_464, 3.22x) · DQ flagged-not-ranked.

**Model B:** adoption .30 = PES-M v2 (validated 4.7x verdict separation, see PES-M v2 methodology); seat-whitespace .25, hiring .20, headroom .15, util .10 = heuristic, pre-registered for expansion-outcome backtest. SAVE-FIRST unchanged. Team whitespace = trigger/context until forward lift test.

**Architecture:** Score ranks -> Triggers flip the play (SAVE-FIRST, GHOST_ACTIVE, DQ, no-sales-DM, declining-usage v1.1) -> Brief explains (>=90 auto first wave, >=80 second, ad-hoc via agents). Nothing flows backward; the only door into the score is a pre-registered lift test.

## Context output framework (lifecycle-aware) — locked 2026-06-08

`Account.Score_Context__c` (the rep-facing narrative) follows ONE four-block skeleton that adapts its CONTENT to the account's lifecycle/play (section 06d gate). Labels stay constant so reps learn one format; the evidence block is rendered per lifecycle. Voice = heath-no-fluff: plain English, humanized counts ("32 weekly users"), no internal jargon (no "PES-M", no raw scores — those are their own fields), one named next move + contact at the end.

**Skeleton:** (1) SITUATION/USING — who they are to us + the headline signal · (2) EVIDENCE — the lifecycle-specific proof; **buyer intent surfaced here whenever present** · (3) FIT — company + commercial · (4) MOVE — one specific action + named contact (or "Find a sales DM first").

**By lifecycle (play from 06d):**
- **Product lead (PQA / product-channel prospect)** — renders `USING: <adopted capabilities> — N weekly users, M power users` / `NOT USING: <dark capabilities>` / `FIT:` / `REACH OUT ABOUT: <one capability hook>. Contact: …`. Capabilities = the 4 PES-M buckets (Sequences / CRM sidebar / Meetings / AI) per `amplitude-event-taxonomy`. Hook picker (first match): heavy-sequences-no-AI → AI Compose; books-demos-no-Copilot → Meeting Copilot; runs-Salesforce/HubSpot-no-sidebar → CRM sidebar; else Smart Send AI. **Ghost-active** → "seats idle, nothing created" + activation move (never a feature pitch); **Dormant** → "used earlier, gone quiet" + re-light; **product-silent** (PQA, no Amplitude footprint) → "raised hand, not active yet" + re-engage.
- **Open deal (In-Flight)** — SITUATION = stage + amount + close date · EVIDENCE = last meeting, champion status, buyer intent, any product usage · MOVE = the next step to advance + owner/champion.
- **Expansion (DS customer)** — SITUATION = ARR + renewal + health · EVIDENCE = teams sold vs using-but-not-sold (whitespace), product depth, intent · MOVE = which unsold team/product to open + the buyer.
- **SS→DS** — SITUATION = self-serve payer · EVIDENCE = usage depth + DM presence · MOVE = conversion pitch on real usage, or usage-expansion touch if no sales DM.
- **Win-Back (Fall Off)** — SITUATION = churned date + ARR + tenure · EVIDENCE = loss reason/competitor, still-active users, intent · MOVE = re-entry angle on what changed.
- **Cold / Net-New** — SITUATION = fits ICP, not in product · EVIDENCE = buyer intent + fit signals · MOVE = value hook + contact.

Locked product-lead template + generator backfilled to `Account.Score_Context__c` on the June 2026 PQA Strike Sprint cohort (125 accounts) 2026-06-08.

**Buyer intent — make it a first-class buying signal (decision 2026-06-08):**
- **Buyer intent regraded continuously (v1 applied 2026-06-08).** Common Room intent (`ls_464`) moved from the binary ≥75th-percentile gate to a CONTINUOUS score in the Signals block. Curve: `intent_v = clamp01((CR_percentile − 55) / 35)` — 0 below the 55th pct, full credit at the 90th+ (so a 93rd-pct account keeps full weight); v6_intent count fallback when no percentile (1 person = 0.6, ≥2 = 1.0). Sized to the tested **3.22x (11x at ≥2 people)** — the one validated continuous lever; other Signals sub-signals stay binary (presence) because volume variants were falsified (hiring ≥3 = 0.91x). Applied to the 125 PQA Strike Sprint cohort as a low-lift change (12 of 125 accounts moved, mean composite −0.07, 2 tier moves) and it spreads the round-number Signals distribution (20→25 distinct values on the cohort). Anchor point + weight still pending a formal re-fit / pre-registered lift test.
- **Strengthen the source in Common Room** (Heath/RevOps): configure CR so the emitted buyer-intent signal maps to real buying behavior — a STRONG buying indicator — then both the model and the context lean on it.
- **Surface intent in the context EVIDENCE block across all lifecycles** whenever present ("N people in-market this week").

## Cross-references
Canonical model doc: https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html (s09 = pipeline + provider map, s13 = PES-M v2 appendix) · PES-M v2 methodology: https://psychic-adventure-p3jj6y9.pages.github.io/operational/pesm-v2-methodology-2026-06-07.html · `sfdc-field-library` · `product-engagement-story` · `strike-zone-analyst`
