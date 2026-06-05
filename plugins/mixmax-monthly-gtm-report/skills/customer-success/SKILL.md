---
name: customer-success
description: Business-unit lens on Mixmax Customer Success performance for the Monthly report — monthly grain, preventive-save posture, canary-list early warning. Action-forward — every section produces named next steps with CSM owner, dollar impact, and Amplitude-backed usage evidence. Use whenever the quarterly analysis needs NRR/GRR decomposition, renewal quality mix, expansion motion, at-risk account saves, CSM book health, cohort stickiness, churn pattern rollup, or time-to-value commentary. Trigger on phrases like "Customer Success", "CS motion", "NRR drivers", "GRR drivers", "renewal quality", "saves", "downgrades", "at-risk accounts", "accounts to save", "expansion targets", "CSM book", "CSM attainment", "churn autopsy", "cohort retention", "second-year retention", "health scores", "QBR targets", "time to value", or any request for a CS-specific read.
---

# Customer Success — Monthly Specialist Lens

The CS motion at **monthly grain**. Monthly is the PREVENTIVE cadence — catching Stage 5→4 and Stage 4→3 drops here is how we stop quarterly's churn autopsy from happening. Quarterly does the post-mortem. Monthly does the save-before-it's-too-late.

Every active-customer action item must be grounded in Amplitude usage evidence — no "at-risk because vibes." Usage data is the trump card.

## Core mandate

1. **Action over analysis.** Every section ends with a named action list.
2. **Every number traces to a source cell.** Cite `{Tab}!{Cell}` in parentheses.
3. **AMPLITUDE IS REQUIRED for every active-customer action.** No at-risk save, no expansion play, no health commentary on a live customer without an Amplitude usage pull. Invoke `amplitude-guide` as the first step of every account-level analysis.
4. **Research-enrich every priority target.** Company context (exec changes, funding, product launches, layoffs) + Amplitude usage = the two-source evidence base.

## Renewal Stage Taxonomy (GOVERNING CLASSIFICATION)

Every renewal account carries a renewal stage. **This is the primary sort key for at-risk analysis.** Stages:

| # | Stage | Meaning | Action posture |
|---|---|---|---|
| 1 | Almost Certainly Will Not | Terminal at-risk — renewal effectively lost unless heroic intervention | Escalate to exec + last-ditch save play |
| 2 | Not Likely | High churn risk — structural issue (no budget, no champion, no usage) | Active save motion required |
| 3 | At Risk | Moderate churn risk — specific blocker identified but solvable | CSM-led save play, QBR, feature re-engagement |
| 4 | Known Issues | Solvable concerns on the table — account is engaged, just working through something | CSM action to resolve the known issue |
| 5 | No Known Issues | Neutral — nothing flagged but nothing signaling locked-in either | Standard renewal motion |
| 6 | Likely | Healthy — renewal on track | Light-touch confirmation + expansion pitch |
| 7 | Almost Certainly Will | Renewal effectively booked — focus on multi-year / expansion | Convert into upsell motion |
| — | Closed Lost | Churned — book the autopsy | Churn analysis required |
| — | Closed Won | Renewed — confirm outcome (at list / downgrade / multi-year) | Expansion motion candidate |

**Rule: Stages 1–3 = churn risk.** These accounts get the deepest analysis, the most Amplitude drill-down, and the strongest Action Items. Stage 1 accounts specifically get exec-escalation plays.

**Rule: Every at-risk and expansion list must be stage-labeled.** An Action Item without a stage annotation is incomplete.

## Inputs

Primary sheet tabs:
- **Renewals** — account-by-account renewal slate with CSM owner, ARR, renewal date, outcome (Renewed / Downgraded / Churned)
- **CS Summary / CSM Renewals / VSB Renewals** — CSM-level rollups, NRR/GRR per book
- **Quarterly Revenue Summary** — DS vs SS, Net ARR Contribution (Upsell $, Downgrade $, Churn $)
- **Health scores** if present in Gen 1 (green/yellow/red distribution per CSM)

Cross-skill references:
- `renewals-management` — at-risk carryover definitions, NRR/GRR computation
- `revenue-analysis` — Net ARR decomposition math
- `mixmax-revenue-reporting` — source-of-truth sheet semantics

**Amplitude is mandatory.** For every account on any action list, pull:
- Active users last 30 / 60 / 90 days and the trend line
- Feature adoption — which Mixmax features this account uses, which they don't
- Usage velocity — up / flat / down over the quarter
- Aha-moment progression — have new seats activated?
- Session frequency — daily actives vs weekly actives vs dormant

External research:
- `enrich_company` for firmographic + recent signals
- `WebSearch` for `"{Account}" news 90 days` — exec changes, funding, layoffs, M&A (all of these predict CS risk)
- `commonroom_list_objects` for community signals if available

## Required analysis sections

### 1. NRR / GRR Decomposition with $ Attribution

Break Net ARR Contribution into: Upsell $, Downgrade $, Churn $ — per CSM book and per segment. QoQ trend. Which CSMs drove the expansion $. Which books leaked the most.

**Action output:** name the CSMs driving expansion — what are they doing that others aren't? Name the CSMs with book leakage — what's the coaching intervention?

### 2. Renewal Quality Mix

Of the renewals closed this quarter, what's the mix:
- **Renewed at list** (full ARR retained, no discount) — count + $
- **Renewed with downgrade** (kept logo, lost ARR) — count + $ + downgrade reason rollup
- **Churned** (lost logo) — count + $ + churn reason rollup
- **Multi-year** (locked in >12 months) — count + $

**Action output:** if downgrade-rate or churn-rate is trending up QoQ, name the pattern (is it a segment? a CSM book? a price tier?) and a specific play to counter.

### 3. Top 5 At-Risk Accounts to Save THIS MONTH — THE HEART

**Monthly cadence means preventive save.** Priority targeting (in order):

1. **Any account at Stage 1 or 2** — immediate escalation
2. **Stage 3 accounts where the blocker is time-sensitive** (renewal date inside 45 days)
3. **Stage 4 accounts that DROPPED from Stage 5+ this month** — the canary signal. Catch here or they become quarterly problems.
4. **Accounts with severe Amplitude usage decay this month** (active users down >40% MoM, feature adoption collapsed) regardless of stage

This section caps at 5 actions. Discipline over breadth. For each:

(retain the full quarterly treatment below, but scoped to this month's save window)

### 3b. Canary List — Stage Drops This Month

Every account that moved DOWN in stage this month, with the delta called out (e.g. "5 → 4," "4 → 3," "6 → 4"). Not an action list — a watchlist for Month-Ahead. Each canary account gets a one-line "what triggered the drop" inference from Amplitude + company research.

**Output:** if the canary list is longer than 8 accounts in a given month, that's a structural signal — flag it as a CS-org-level issue, not account-by-account.

### 3c. Deeper At-Risk Roster (full Stage 1–3 list)

Beyond the Top 5 save list, the full roster of every Stage 1, 2, or 3 account. Rank-order by `ARR × save-probability` where save-probability is inversely correlated with stage number (Stage 3 = high save-probability, Stage 1 = low but highest-$-at-stake). This is the CSM team's working queue for the month.

**Deep analysis per account — required fields:**
- **Stage** (1 / 2 / 3) and stage-change history this quarter (did it move from 4 → 3? 2 → 1? stable?)
- **Amplitude usage trend** (90-day) — active users, feature adoption, session frequency, aha-moment state
- **Company context** — exec changes, layoffs, funding, M&A, product direction shifts
- **Specific churn trigger** — usage decline, exec turnover, reduced seat count, overdue QBR, support ticket surge, contract renegotiation, competitive displacement, budget freeze
- **Save play** — exec alignment call, feature re-enablement workshop, expanded use-case pitch, ROI case review, contract re-negotiation with multi-year, executive sponsor change request

**Stage-specific posture (bake into the Action):**
- **Stage 1 (Almost Certainly Will Not):** escalate to Mixmax exec + CSM — propose last-ditch save like deep discount + scope change OR book the churn cleanly and capture the learning for the autopsy.
- **Stage 2 (Not Likely):** structural save motion — identify the root cause (no champion / no budget / no usage / wrong fit) and match to a targeted play.
- **Stage 3 (At Risk):** tactical save motion — the blocker is known and solvable; get the specific unlock on the calendar next 14 days.

Follow the Action Item Format for each. Top 10 at minimum; go deeper if Stage 1+2 count exceeds 10.

### 4. Top Expansion Targets (NEXT 60 DAYS)

**Primary filter: Stage 6 (Likely) and Stage 7 (Almost Certainly Will).** These accounts are locked in or effectively so — the renewal is not the story, the expansion is. Rank-order by expansion-$-potential × usage-signal-strength. For EACH:
- **Stage** (6 or 7) and duration at this stage
- **Amplitude evidence** of expansion readiness: usage spike, new seat activation, feature breadth increase, team growth (e.g. "active users grew from 12 to 34 last quarter", "adopted Feature X for the first time — that's the pre-cursor to our Pro tier")
- **Company research context:** funding round, hiring surge, new product launch, territory expansion — all expansion triggers
- **Named motion:** QBR with ROI case, seat-expansion pitch, cross-sell into adjacent team, multi-year-with-discount lock-in, tier upgrade pitch

Also call out **Stage 4–5 accounts with strong Amplitude usage spikes** — these are "hidden expansion" candidates where the sheet says "neutral" but the product data says "they're ready."

### 4b. Churn Autopsy — Closed Lost This Quarter

**Every Closed Lost gets an autopsy.** Not just rolled up into "churn reason" — an actual post-mortem with named fields:

For each Closed Lost account:
- **Account** — name + ARR lost + CSM owner + renewal date
- **Final stage before Closed Lost** — was it Stage 1 for months, or did it crash from Stage 4 to Lost in 30 days? Stage trajectory matters.
- **Amplitude usage pattern** in last 90 days before churn — was it a slow decay or sudden cliff? Which features declined first? Did the primary champion stop logging in?
- **Company context** — did they get acquired? Layoffs? Exec turnover? Migrated to competitor?
- **Root-cause theme** — classify into one of: *No Champion, Budget Cut, Competitive Loss, Product Gap, Mis-Sold (poor fit from day 1), Usage Decay, Acquisition/M&A, Exec Turnover, Price*
- **What should have happened 60/90/180 days earlier** — identify the earliest save-opportunity we missed
- **Pattern match** — does this look like a previous Closed Lost? Are we seeing a cluster?

**Action output at end of section:** the top 3 systemic patterns across all Closed Losts this quarter, each with a named counter-play for the coming quarter (e.g. "4 of 9 Closed Losts this Q had champion departure as root cause — CS enablement play: build champion-backup process into every QBR starting next Q").

This section is the most important learning loop in the CS function. Do not short-cut it.

### 5. At-Risk Movement (Flow Analysis)

At-risk pipeline flow this quarter:
- **Carryover** — at-risks from last Q still open entering this Q
- **New this Q** — flagged during the quarter
- **Resolved in-quarter** — moved from at-risk to healthy (how? name the play that worked)
- **Closed (lost)** — churned or downgraded
- **Still open entering next Q** — the carryover into Q+1

**Action output:** for each account "Still open entering next Q," an Action Item with the save play. These are the priority CSM actions for the first 2 weeks of next quarter.

### 6. CSM Book Coverage & Health

Per CSM: book size ($ARR), account count, health score distribution (green/yellow/red counts), renewal slate for next quarter (count + $).

Flag CSM books into:
- **Overloaded** — >$X ARR or >N accounts where X/N exceed org average by 25%
- **Undersaturated** — underutilized capacity, candidate to take on at-risks from overloaded books
- **At-risk books** — health distribution skewed to yellow/red

**Action output:** rebalancing plays + coaching plays + hiring recommendation if overload is systemic.

### 7. Cohort Stickiness

Of the logos that renewed this quarter, how many also renewed last quarter? (Second-year retention is the leading indicator of true PMF.) Trend QoQ.

**Action output:** if second-year retention is declining, name it as a CS strategic risk and propose an investigation (what's changing between Year 1 and Year 2?).

### 8. Time-to-Value for Renewing Accounts

For accounts renewing this quarter, what was their onboarding trajectory? Did they hit aha-moment in their first 30 days? Correlate onboarding-quality (Amplitude: feature adoption in first 30d) with renewal outcome (at list / downgrade / churn). Expect the correlation to be strong.

**Action output:** if onboarding cohorts from 12 months ago had poor aha-moment progression, those are the at-risks to watch for next Q.

### 9. Churn Pattern Rollup

Aggregate churn reasons across the quarter with $ weight. Top 3 themes. Compare to last quarter — are we seeing the same pattern or is it shifting?

**Action output:** one named counter-play per top theme (e.g. "competitor X is winning on feature Y — CS enablement on feature Y for renewals books Q+1").

## Action Item Format (MANDATORY)

```
#{rank}. {Account name} — CSM: {name} — ${ARR}

Action: {specific next step in ≤20 words — e.g. "Schedule exec alignment call with CRO this week; propose ROI case review" not "check in"}

Amplitude evidence: {specific usage signal — e.g. "Active users dropped from 45 to 18 over last 60 days; feature X usage fell to zero after the Mar 15 admin turnover"}

Company context: {1–2 sentences from research — e.g. "Company raised Series C last month and hired new VP Sales; their CRM migration closed last week — this is a seat-expansion window, not an at-risk"}

Expected impact: ${amount saved / expanded} — {timeframe}
```

**No action allowed without Amplitude evidence for active customers.** If Amplitude has no data for that account, flag it as a data gap and propose instrumentation — don't invent a usage narrative.

## Research + Amplitude discipline

Before writing any Action Item on the Top-10 At-Risk or Top-10 Expansion lists:

1. **Amplitude pull (required):** invoke `amplitude-guide` with the account's domain / org ID to get usage trend, feature adoption, active users, session frequency for last 90 days.
2. **Company enrichment:** `enrich_company` for firmographic + recent signals.
3. **News scan:** `WebSearch` for `"{Account}" exec changes OR layoffs OR funding last 90 days` — look for things that shift CS risk.
4. **Synthesize** into specific Action + Amplitude evidence + Context lines. If Amplitude is silent, the account may not be a top-10 candidate.

## Output modes

**Quarterly Wrap-Up:** CSM books summarized by bucket (no public book-by-book naming), full Top-10 At-Risk + Top-10 Expansion lists (accounts named).

**CRO Quarterly:** everything. CSM-by-CSM attainment named, book health called out, full Action Items.

**Quarter-Ahead:** forward-looking. Carryover at-risks + new-quarter renewal slate + expansion targets + CSM coverage plan.

**Board Snapshot:** 3-bullet distillation. NRR/GRR vs target (green/yellow/red + one sentence), top-line risk (churn theme), top-line opportunity (expansion motion working).

## When something isn't covered

If Amplitude has no data for an account, say so and propose instrumentation. If a CSM book doesn't have health scores, propose adding them for Gen 2. Don't invent.
