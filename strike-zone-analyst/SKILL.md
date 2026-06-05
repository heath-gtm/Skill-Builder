---
name: strike-zone-analyst
description: >-
  Mixmax's funnel + PQA diagnostic engine and funnel-leak analyst. Connect Salesforce + Amplitude (+ optional Octave, Common Room, FullEnrich, Mixmax). Three modes: (1) FUNNEL DIAGNOSIS finds leaky conversion gates by channel (Inbound/Outbound/Product) with per-stage leakage, dollarized leverage points, and cohort velocity; (2) SPRINT PLANNING multi-source-enriches PQAs into a ranked backlog with verified buying committees; (3) SCORING AUDIT finds where Aero is failing. Trigger on 'strike zone math', 'funnel diagnosis', 'diagnose the funnel', 'where are we leaking', 'why is [channel] underperforming', 'conversion by channel', 'show rate is dropping', 'meeting-to-SQL conversion', 'should we reallocate budget', "what's our funnel velocity", 'PQA sprint planning', 'score our PQAs', 'is Aero missing accounts', 'find missed ICPs', 'audit the scoring model', or any channel-level cohort-conversion, PQA prioritization, or scoring-gap question. Also fire after the Aero dashboard when the user asks 'now what'.
---

# Strike-Zone Analyst — Diagnostic + Sprint Planning + Scoring Audit

**Required:** Salesforce + Amplitude. **Optional:** Octave (independent ICP), Common Room (community/buying-committee), FullEnrich (verified contacts), Mixmax (sequence-stage attribution), Aero (channel-fit scoring).

## What this skill does

You are the user's diagnostic partner for understanding Mixmax's funnel — why it's
converting or not, which accounts to work next, and where the scoring model is
letting them down. The Aero dashboard tells you *what* is happening. This skill
helps you understand *why*, *what to do about it*, and *which accounts deserve the
next sprint*. (This is the productized, connector-gated version of the original
strike-zone-math skill; it absorbs that skill in full.)

| Mode | Question it answers | Output |
|---|---|---|
| **Funnel Diagnosis** | Where is the funnel leaking, why, and what do I do? | A diagnostic with named leaky gate + recommended action |
| **Sprint Planning** | Which of our PQAs are worth working this sprint? | A ranked xlsx with composite scores + verified buying committees |
| **Scoring Audit** | Where is Aero (or our scoring model) missing real ICPs? | A list of false-negatives + missed ICPs with named accounts |

All three modes use the same six-gate funnel framework, the same multi-source signal stack, and the same cohort-anchored math.

## The six funnel gates

Strike zone is the sequence of conversion gates from a new lead to closed revenue. For each cohort × channel, six gates matter:

1. Cohort created (MQA / OQA / PQA fires) → Meeting booked
2. Meeting booked → Meeting completed (show rate)
3. Meeting completed → SQL (`StageName = '0 - Qualification'`)
4. SQL → SQO (`StageName = '1 - Discovery'`)
5. SQO → Closed Won
6. Closed Won → Average deal size + cycle time

Each gate has a different failure mode and a different intervention. Misdiagnosing the gate wastes weeks fixing the wrong thing.

## Mode 1: Funnel Diagnosis

**Triggers:** "where are we losing meetings", "why is [channel] underperforming", "show rate is dropping", "diagnose the funnel", "review the strike zone", "what's working".

**Default mode is conversational.** Work interactively — don't dump a full report unprompted:

1. **Anchor on a channel + cohort window.** Ask what they want to diagnose. Don't assume.
2. **Pull live data via Salesforce MCP.** Use `references/soql_templates.md`. Always run queries — don't analyze from memory.
3. **Find the leaky gate.** Compare each gate's conversion to the channel's trailing baseline and to the other two channels. The leaky gate has the largest negative gap.
4. **Diagnose with the pattern framework.** See `references/diagnostic_patterns.md` — each leaky gate has 2-4 known failure modes; identify which fits.
5. **Recommend specific action.** Named — a person, a list of accounts, a process change, a target.
6. **Offer the HTML write-up only if asked.** When the user says "write this up", switch to HTML mode.

Conversational-first matters because strike-zone math is judgment-heavy. Surface hypotheses, let the user confirm, then act.

## Mode 2: Sprint Planning (multi-source PQA prioritization)

**Triggers:** "PQA sprint planning", "score our PQAs", "build a PQA backlog", "which accounts should we work this sprint", "rank our PQA cohort", "give me a sprint list".

Converts the funnel from a diagnostic into an execution backlog. Output is an xlsx that becomes the rep's sprint queue.

1. **Define the cohort.** Default: all accounts with `Sales_PQA_Date_Account__c` (or MQA / OQA equivalent) in the target window. Confirm with the user.
2. **Multi-source enrich every account in parallel** (see `references/sprint_planning_workflow.md`):
   - **Salesforce** — firmographics, Aero scores, GTM stage, owner, contacts
   - **Octave** (`mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__qualify_company`) — independent ICP qualification
   - **Amplitude** — Product Engagement Story via the 11-event framework (see `product-engagement-story`)
   - **Common Room** (`mcp__32d1a164-1bd3-41cb-a019-b2c320f13201__commonroom_list_objects`) — community signals + buying-committee depth
   - **FullEnrich** (`mcp__63157928-2125-4a53-b8f6-c0881c12ac2e__*`) — phones + verified emails on top tier (credit-gated — check `get_credits` first)
3. **Compute composite scores** per `references/multi_source_scoring.md`. Tier into Hot / Warm / Watch / Disqualify.
4. **Build the xlsx** with five tabs: Sprint Ranking, Top Buying Committee (FullEnriched contacts), Scoring Rubric, Cohort Summary, Aero Scoring Gaps.
5. **Hand off.** Reps work Tab 2 top-down; managers use Tabs 1 and 5.

**Cost guardrails.** FullEnrich is the only paid source (~8.7 credits per contact for work email + mobile). Cap spend per run unless approved — 5 contacts × top 50 = 250 × 8.7 ≈ 2,200 credits/run. Use `get_credits` first; warn if balance is tight.

## Mode 3: Scoring Audit (find missed ICPs)

**Triggers:** "is Aero missing accounts", "find missed ICPs", "audit the scoring model", "where is Aero wrong", "are our PQAs actually good", "cross-reference scoring".

When Octave, Amplitude, Common Room, and Salesforce disagree with Aero, the disagreement IS the finding (see `references/scoring_audit_methodology.md`). Two patterns surface most:

- **Aero False-Negatives** — Aero PES at floor (28.04 in the current model) but Amplitude shows real sustained team adoption. Flag: `aero_false_negative`.
- **Aero-Missed ICPs** — an independent qualifier (Octave) scores ≥7 (strong fit) but Aero Account Fit is <40 or null. Firmographic miss, not engagement. Flag: `aero_missed`.

In Mixmax's 2026 PQA cohort this audit found **34 Aero False-Negatives and 9 Aero-Missed ICPs out of 261 accounts (16%)** — accounts reps would have de-prioritized had they trusted Aero alone.

### Documented Aero failure modes
1. **PES floor at 28.04** — most "low-engagement" PQAs share this exact score; loses distinction.
2. **"No Score" silence ≠ "low fit"** — sparse usage → no score, but reps read it as low fit. No firmographic-only fallback.
3. **No buying-title weighting** on the PQA-triggering user — a VP of Sales reads identical to an IC.
4. **No trend velocity** — 700→50 events scores the same as flat 50.
5. **No ICP penetration ratio** — 2 active / 21 mapped (9.5%) reads identical to 2 active / 3 mapped (67%).

Detailed in `references/diagnostic_patterns.md` ("Gate 1 failure modes") and `references/scoring_audit_methodology.md`.

## Audience awareness

Default to **leader mode** unless told otherwise.

- **Leader mode** (RevOps, GTM leadership): strategic recommendations — change targets, reallocate reps, kill/reinvest in channels, change the qualification rubric or playbook. Never recommend "have reps do better outreach" — the leader-mode equivalent is structural and ownable ("the Outbound playbook needs a touchpoint-cadence rewrite; data shows 14+ touches before a meeting on accounts that book, vs team baseline of 9").
- **Rep mode** (fired when the user says "drill into [name]" or names a rep): tactical — these accounts to call, these objections, this messaging. Pull the rep's cohort via `Account.OwnerId` / `Opportunity.OwnerId`, compare to team baseline, identify their specific leak.

## Action format (all modes)

Every recommendation needs three parts: **Who** (named person/role), **What** (a specific change), **By when** (a date or sprint). If you can't fill all three, diagnose deeper.

## Data sources

| Source | MCP / tool | What it adds |
|---|---|---|
| Salesforce | `mcp__d50c041d-378a-4fbe-b287-5541902dd1b9__*` | Cohort anchor dates, Aero scores, opp history, contacts, owner |
| Amplitude | `mcp__21ac7e4d-f1d6-44a3-81b3-242377655978__*` | Real product engagement, the 11-event PES framework |
| Octave | `mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__*` | Independent ICP qualification + playbook match + hard disqualifiers |
| Common Room | `mcp__32d1a164-1bd3-41cb-a019-b2c320f13201__*` | Community/intent signals, extra buying-committee contacts |
| FullEnrich | `mcp__63157928-2125-4a53-b8f6-c0881c12ac2e__*` | Phone numbers + verified emails (credit-gated, top tier only) |
| Mixmax | `mcp__229af089-f88a-40ac-ae96-42d07e09ff31__*` | Meeting history + sequence performance |

## Caveats the team cares about

- **Use CHAMP + SPRINT + PLAN, not MEDDPICC.** Mixmax doesn't run MEDDPICC.
- **Lead with conversion, not volume.**
- **Cohort math, not snapshot math.** Anchor the cohort by entry date (MQA / OQA / PQA) and trace forward — never compute "this month's win rate" from opps that closed this month.
- **Honest caveats.** If a cohort is too young, a field isn't groupable, or you're inferring — say so.
- **Audience's own taxonomy.** Inbound / Outbound / Product are the channels. Expansion is its own motion, not a channel in strike-zone math.
- **No MQL_Date__c.** The Inbound cohort anchor is `Account.MQA_Date_2024__c`; legacy `MQA_Date__c` is retired.
- **`Channel_Source__c` is a formula field** — non-groupable in SOQL; filter on it, don't GROUP BY.
- **Filter renewals out of new-business math:** `Opportunity.Type IN ('New Business', 'Convert SS to DS')`.

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
- For building the Aero dashboard itself (use the Aero prompt file)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.Channel_Source__c (canonical channel attribution, § 5; `Account.LeadSource` is fallback only — never `Opportunity.Channel__c`)
- Opportunity.StageName, CloseDate, IsClosed, IsWon (cohort conversion math)
- Opportunity.Amount (dollarization of leverage points)
- Account.Website (Amplitude join for Product channel cohort, § 10)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

Lock-ins #11 (channel classifier), #18 (PQA detection). This skill is the canonical strike-zone engine (absorbed the former strike-zone-math).

## Make.com / API packaging

**Input:** `{ mode: "full_diagnosis | single_channel | compare_channels | leverage_point", channel: string, window_days: number }`

**Output:** `{ cohorts_per_channel, conversion_rates, leakage_points, leverage_point_dollarized, velocity, recommended_actions }`

**Failure modes:** No Amplitude → Product channel cannot be analyzed. Insufficient sample size → analyst surfaces "low confidence" and reports sample size in output.

## Shippable as

Standalone connector-gated SKU. Make.com node. The RevOps + VP Sales funnel-leak diagnostic. Different audience from Pipeline-Creation — strikes at "where" not "how much."

## Related skills

- `product-engagement-story` — the 11-event Amplitude PES analysis on a single account. This skill calls into that framework for Modes 2 and 3.
- `customer-strategy-brief` — 60-second brief on a single account. After this skill produces the sprint backlog, the brief runs on the top accounts.
- `customer-strategy-suite` — brief + deep dive + battle plan in one pass. Use after Mode 2 picks the top sprint targets.
- `pipeline-intelligence` — adjacent skill; account prioritization, pipeline coverage, and monthly ICP-quality without the funnel diagnostic.

## Reference files

- `references/soql_templates.md` — Ready-to-run SOQL for every strike-zone metric, field names verified against the live Mixmax SFDC org.
- `references/diagnostic_patterns.md` — For each leaky gate: known failure modes, disambiguating queries, typical interventions.
- `references/multi_source_scoring.md` — The v2 composite scoring rubric: weights, sub-score logic, tier thresholds, signal-richness bonus, flag definitions.
- `references/sprint_planning_workflow.md` — The staged enrichment workflow for Mode 2: which sources, in what order, with guardrails and cost caps.
- `references/scoring_audit_methodology.md` — The Mode 3 method: cross-referencing signals to find Aero false-negatives and missed ICPs.
