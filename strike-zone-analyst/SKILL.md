---
name: strike-zone-analyst
description: Your funnel-leak analyst. Connect Salesforce + Amplitude — turns any "where is the funnel leaking?" question into channel-cohort conversion math (Inbound / Outbound / Product), per-stage leakage diagnosis, and "what specific action moves the number". RevOps + leader diagnostic. Productized version of the existing strike-zone-math skill. Trigger on "strike zone math", "funnel diagnosis", "where are we leaking?", "is {channel} working?", "conversion by channel", "show rate is dropping", "meeting-to-SQL conversion", "channel-by-channel cohort", "should we reallocate budget?", "is {channel} worth the investment?", "what's our funnel velocity?", or any channel-level conversion diagnostic. Also fire after the Aero strike-zone dashboard when the user asks "now what?" — the handoff is this skill.
---

# Strike-Zone Analyst — your funnel-leak companion

**Required:** Salesforce + Amplitude. **Optional:** Mixmax (sequence-stage attribution), Aero (channel-fit scoring).

## What this analyst answers

- "Where is the funnel leaking?" — per-channel, per-stage leakage diagnosis
- "Is {channel} working?" — cohort-conversion math vs target
- "What specific action moves the number?" — leverage point identification
- "Should we reallocate budget from {channel A} to {channel B}?" — comparative cohort math
- "What's our funnel velocity?" — cycle time per stage per channel

## What it owns internally

- **Cohort-based conversion math**: meeting-set → SQL → SQO → Closed Won by channel
- **Per-stage leakage diagnostics**: where in the funnel each channel loses momentum
- **Leverage point detector**: identifies the single stage transition that, if improved 10%, moves the largest amount of revenue
- **Channel-cohort velocity tracker**: average days from meeting to close per channel
- **Productizes the existing strike-zone-math skill** as a discrete agent

## Quality gates

**No conversion rate without sample size.** "Outbound meeting → SQL is 34%" must be accompanied by "(based on 47 meetings, ±8% margin of error)."

**Leverage point math is dollarized.** "Improving Outbound meeting→SQL by 10% would add 8 SQLs/Q = $176K in pipeline at current ASP."

**Comparative cohort math accounts for cycle time.** A channel with 6-month sales cycles can't be directly compared to a 30-day-cycle channel; the analyst normalizes.

## Output format example

```
🎯 STRIKE-ZONE FUNNEL DIAGNOSIS · Trailing 90 days

INBOUND COHORT
  Meeting Set:     127
  → SQL:           94  (74% — strong, above 65% benchmark)
  → SQO:           58  (62% — slight decline from Q1's 71%)
  → Closed Won:    23  (40% — at expected range)
  Velocity: avg 38 days meeting → close
  Diagnosis: Healthy. Slight SQL→SQO decline worth watching.

OUTBOUND COHORT
  Meeting Set:     47
  → SQL:           16  (34% — BELOW 55% target ★)
  → SQO:            9  (56% — strong)
  → Closed Won:     4  (44% — strong)
  Velocity: avg 82 days meeting → close
  Diagnosis: ★ LEAKAGE AT MEETING → SQL. We're getting meetings,
             not qualifying them in.

PRODUCT COHORT (PQA)
  PQAs Generated:   83
  → Meeting Set:   24  (29% — strong for cold)
  → SQL:           19  (79% — best on team)
  → SQO:           13  (68%)
  → Closed Won:     6  (46%)
  Velocity: avg 24 days PQA → close (fastest channel)
  Diagnosis: Healthiest funnel. Worth scaling investment.

LEVERAGE POINT (dollarized):
  Outbound meeting → SQL improvement of 10% = 5 additional SQLs/Q
  At current ASP ($22K), that's +$110K pipeline + 2 additional Closed Won
  = +$44K ARR/Q assuming current win rate

WHAT MOVES THE NUMBER:
  Diagnosis: Outbound meetings are reaching the right people but the
             qualification conversation isn't landing.
  Root cause hypothesis (verify with sample):
    • Are we treating Outbound meetings as discovery instead of qualification?
    • Are we missing PLAN fields by SQL stage?
    • Is the pre-meeting research deep enough?
  Recommended actions:
    1. Listen to 5 outbound meeting recordings + identify qualification gaps
    2. Test: PLAN-first meeting structure on next 10 outbound meetings
    3. Compare conversion rate of Inbound vs Outbound at SQL stage to find delta

BUDGET REALLOCATION CONSIDERATION:
  Product channel has best unit economics ($22K won per PQA-generated meeting).
  Outbound has highest leak. Recommend:
    • Increase PQA-source investment (Amplitude tooling, signal generation)
    • Pause outbound headcount expansion until SQL conversion improves
```

## Used by

- **Sales-leader-weekly-report** (funnel diagnosis section, optional deep dive)
- **Monthly + Quarterly revenue reports** (channel-cohort math)
- **Pipeline-Creation Analyst** as downstream signal source ("you have coverage but you're leaking at SQL → that's where to focus")
- Standalone for RevOps / VP Sales / CEO funnel diagnosis

## When NOT to use

- For account-level pipeline coverage (use Pipeline-Creation Analyst)
- For per-deal diagnosis (use Deal-Health Analyst)
- For dashboard-style building (use the existing strike-zone-math skill directly)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.LeadSource + Opportunity.Channel__c (canonical channel classification, § 5)
- Opportunity.StageName, CloseDate, IsClosed, IsWon (cohort conversion math)
- Opportunity.Amount (dollarization of leverage points)
- Account.Website (Amplitude join for Product channel cohort, § 10)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

Lock-ins #11 (channel classifier), #18 (PQA detection), strike-zone-math skill (parent).

## Make.com / API packaging

**Input:** `{ mode: "full_diagnosis | single_channel | compare_channels | leverage_point", channel: string, window_days: number }`

**Output:** `{ cohorts_per_channel, conversion_rates, leakage_points, leverage_point_dollarized, velocity, recommended_actions }`

**Failure modes:** No Amplitude → Product channel cannot be analyzed. Insufficient sample size → analyst surfaces "low confidence" and reports sample size in output.

## Shippable as

Standalone connector-gated SKU. Make.com node. The RevOps + VP Sales funnel-leak diagnostic. Different audience from Pipeline-Creation — strikes at "where" not "how much."
