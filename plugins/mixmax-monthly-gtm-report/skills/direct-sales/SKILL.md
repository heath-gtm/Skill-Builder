---
name: direct-sales
description: Business-unit lens on Mixmax Direct Sales performance for the Monthly report — monthly grain, 30-day action windows, intervention-focused. Action-forward — every section produces named next steps with owner, dollar impact, and research-backed context. Use whenever the quarterly analysis needs rep-level attainment, deal-by-deal forecast quality, unstick-the-stuck deal plays, new-business target identification, segment mix, sales velocity, or early-churn attribution on DS-owned deals. Trigger on phrases like "Direct Sales", "DS engine", "rep performance", "rep attainment", "AE quota", "deal autopsy", "deals to move", "deals to unstick", "new business targets", "sales velocity", "segment mix", "SMB/MM/Enterprise", "pipeline concentration", "forecast accuracy by rep", "early churn", "90-day churn", "ramp health", or any request for a DS-specific read.
---

# Direct Sales — Monthly Specialist Lens

The DS engine diagnostic at **monthly grain**. Monthly is the intervention cadence — weekly is too noisy to change behavior, quarterly is too late to save the quarter. This skill produces the specific 30-day plays (deals, reps, coaching moves) that actually change outcomes this month.

Every output ends in named actions with owners and dollar impact.

## Core mandate

1. **Action over analysis.** Every analytical section must end with a named action list — who, what, by when, $ at stake, why now.
2. **Every number traces to a source cell.** Same contract as other specialists. Cite `{Tab}!{Cell}` in parentheses.
3. **Research-enrich every priority target.** For every deal or rep on an action list, pull company / industry / rep context before writing the "why now." A priority without context is incomplete.
4. **Amplitude cross-reference for Product-led deals.** If a Product-channel account appears on any action list, invoke `amplitude-guide` for usage evidence.

## Inputs

Primary sheet tabs (Gen 1 Quarterly snapshots):
- **AE Forecast** — rep-by-rep deal list with forecast category, close date, ACV, stage
- **Rep Summary / Rep Summary Deals by Forecast Category** — rep-level attainment, quota, commit, best case, pipeline
- **Quarterly Bookings Summary** — bookings by channel and by segment
- **Quarterly Revenue Summary** — DS ARR, New Biz vs Expansion split
- **Renewals tab** — for DS-owned early-churn attribution (new-biz deals booked last quarter that churned this quarter)

Cross-skill references:
- `deal-management` — forecast category definitions, stage semantics
- `revenue-analysis` — DS-total rollups, segment boundaries
- `pipeline-building` — top-of-funnel context for next-quarter setup
- `amplitude-guide` — usage evidence for Product-channel deals on action lists

External research tools (use for every priority target):
- `enrich_company` / `find_company` / `generate_call_prep` (Aero toolkit) for firmographic + recent signals
- `WebSearch` for recent news (funding, leadership changes, product launches, hiring surges)
- `commonroom_list_objects` for community / signal tracking if the account is in Common Room

## Required analysis sections

### 1. Rep Attainment & Health

For each AE: Closed-Won $ vs Quota, % attainment, tenure (new / ramping / veteran), forecast accuracy (did Month-1 Commit land?), pipeline coverage entering next quarter (target: 3x commit).

Flag reps into three buckets:
- **Crushing** — ≥110% attainment, healthy coverage, accurate forecast
- **On track** — 80–110%, coverage acceptable
- **At risk** — <80% or coverage <2x or forecast miss >25%

**Action output:** for every at-risk rep, a named coaching action (see format below). For every crushing rep, a named reinforcement action (bigger territory? mentor assignment?).

### 2. Deal Forecast Quality

Forecast accuracy autopsy: at Month-1 of this quarter, what was Commit + Best Case? What actually closed? Variance by rep, by segment, by forecast category. Call out systematic over-forecasting or under-forecasting patterns.

**Action output:** coaching actions for reps with chronic forecast drift.

### 3. Top 5 Deals to Pull In THIS MONTH — THE HEART

Not 60 days. **This month.** Rank order the 5 deals that, if closed in the next 30 days, most move the quarter. For each:
- Current stage + days in stage
- Commit / Best Case / Pipeline status today
- Specific unlock needed (decision-maker meeting, procurement, legal, exec sponsorship, pricing)
- Named unblock action with calendar date

Apply the Action Item Format. This list drives the CRO's week.

### 3b. Top 5 Deals to DEFEND (At Risk of Slipping Out)

Different play from pull-in. These are deals currently forecasted in this quarter that are showing slip signals:
- Days-in-stage increasing
- Forecast category moved DOWN (Commit → Best Case → Pipeline)
- Stakeholder dropout (champion left, procurement stalled)
- Deal size shrinking in negotiation

Slip-defense is a specific play: re-establish momentum, escalate to exec sponsor, re-validate timeline with buyer, offer multi-year-with-incentive to lock urgency. Name the defense play per deal.

### 4. Monthly Win/Loss Momentum

MoM pattern on wins and losses. Same cut as quarterly but tighter:
- Win rate this month vs last month
- Competitors beaten vs competitors lost to (any pattern shift?)
- Win-on-price vs win-on-product vs win-on-speed ratio
- Loss reasons aggregated MoM — are we losing on the same thing twice?

**Output:** if a pattern shift exists (e.g. "suddenly losing to Competitor X on 3 of last 5 deals"), name it as an urgent input to Month-Ahead and flag for CRO enablement action.

### 4b. New-Business Targets for Next Month

Top 5 accounts to prospect in the next 30 days. Monthly-grain pipeline compression version of the quarterly Top-10. Research-enrich each one via `enrich_company` + `WebSearch` + `generate_call_prep`. Monthly-grain means: only include accounts with a NEAR-TERM buying signal (recent funding in last 60 days, leadership change in last 60 days, inbound signal in last 14 days, competitive displacement signal in last 30 days).

### 5. Segment Mix & Velocity

SMB / MM / Enterprise breakdown if that cut exists in the sheet — segment contribution to quarter bookings, QoQ trend, segment-level win rate. Compute sales velocity: `Deals × Avg ACV × Win Rate ÷ Cycle Days`. Compare to last quarter.

**Action output:** if a segment is eroding, name a play to address it (ICP re-cut? compensation shift? SDR team re-pointed?).

### 6. Pipeline Concentration & Early-Churn Attribution

Top 5 deals as % of next-quarter commit. If concentration >40% on top 3 deals, that's a risk — call it out with specific deal names and a "what if this slips" dollar impact.

Early-churn: any new-biz deal booked last quarter that churned this quarter gets called out by rep, with $ and root-cause theme (onboarding miss, mis-sold, buyer left, etc.).

## Action Item Format (MANDATORY for every action listed)

```
#{rank}. {Account or Deal name} — {Owner (AE name)} — ${ARR or Opp size}

Action: {specific next step in ≤20 words — e.g. "Executive sponsor meeting with CEO this week" not "follow up"}

Why now: {specific trigger with source — sheet cell, Amplitude event, external news. Quote the evidence.}

Context: {1–2 sentences of company / industry / rep context from research — tech stack, recent funding, competitive moment, rep's book saturation, whatever is real and relevant.}

Expected impact: ${amount} — {close this quarter / next 30 days / unblock move to next stage / etc.}
```

**No generic actions allowed.** "Follow up with {Account}" is banned. Actions must be specific enough that a named human reading this could execute tomorrow.

## Research discipline

Before writing any Action Item on the Top-10 Deals list or New-Business Targets list:

1. Pull company record via `enrich_company` or `find_company` — get size, industry, tech stack, recent raises
2. `WebSearch` for `"{Account name}" news last 90 days` — look for funding, exec changes, product launches, layoffs, M&A
3. If Product-channel deal: invoke `amplitude-guide` to pull usage over last 30 days
4. Synthesize into a 1–2 sentence Context line that sounds like an account executive who's done their homework, not a template

Skipping research is not acceptable. If research returns nothing useful, say so explicitly ("No material news found in last 90 days; basing WHY NOW on internal engagement signals from sheet").

## Output modes

**Quarterly Wrap-Up (org-wide):** summarize rep buckets (counts + narrative, no public naming of at-risk reps), full Top-10 Deals list with research, full Top-10 New-Business Targets list.

**CRO Quarterly (CRO-only):** everything. Rep-by-rep attainment named, at-risk reps named, full autopsy, full coaching actions.

**Quarter-Ahead:** forward-looking only. New-Business Targets + Top-10 Deals-to-Move list + rep coverage health going into new quarter.

**Board Snapshot:** 3-bullet distillation. DS engine health (green/yellow/red + one sentence), top-line risk, top-line opportunity.

## When something isn't covered

If the sheet doesn't have rep-level attribution on a booking, or segment cut isn't present, say so and skip — don't invent. Flag the gap as a Gen 2 data request for next quarter.
