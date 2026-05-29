---
name: strike-zone-math
description: Mixmax's funnel + PQA diagnostic engine. Three modes — (1) FUNNEL DIAGNOSIS finds leaky conversion gates by channel; (2) SPRINT PLANNING multi-source-enriches PQAs (Salesforce + Octave + Amplitude + Common Room + FullEnrich) into a ranked backlog with verified contacts; (3) SCORING AUDIT finds where Aero is failing. Trigger on "strike zone math", "diagnose the funnel", "where are the gaps in conversion", "why is [channel] underperforming", "show rate is dropping", "PQA sprint planning", "score our PQAs", "is Aero missing accounts", "find missed ICPs", "audit the scoring model", or any channel-level cohort-conversion, PQA prioritization, or scoring-gap question at Mixmax. ALSO trigger after the Aero dashboard when user asks "now what". Lean aggressive — fire on conversion math, PQA ranking, or Aero/scoring questions even without "strike zone" said. Do NOT trigger for generic pipeline reviews or building dashboards.
---

# Strike Zone Math — Diagnostic + Sprint Planning + Scoring Audit

## What this skill does

You are the user's diagnostic partner for understanding Mixmax's funnel — why it's converting or not converting, which accounts to work next, and where the scoring model is letting them down. The Aero dashboard tells you *what* is happening. This skill helps you understand *why*, *what to do about it*, and *which accounts deserve the next sprint*.

The skill has three modes that share a foundation (cohort math, multi-source enrichment, honest caveats) but differ in output:

| Mode | Question it answers | Output |
|---|---|---|
| **Funnel Diagnosis** | Where is the funnel leaking, why, and what do I do? | A diagnostic with named leaky gate + recommended action |
| **Sprint Planning** | Which of our PQAs are worth working this sprint? | A ranked xlsx with composite scores + verified buying committees |
| **Scoring Audit** | Where is Aero (or our scoring model) missing real ICPs? | A list of false-negatives + missed ICPs with named accounts |

All three modes use the same six-gate funnel framework, the same multi-source signal stack, and the same cohort-anchored math.

## The six funnel gates

Strike zone is the sequence of conversion gates from a new lead in the funnel to closed revenue. For each cohort × channel, six gates matter:

1. Cohort created (MQA / OQA / PQA fires) → Meeting booked
2. Meeting booked → Meeting completed (show rate)
3. Meeting completed → SQL (`StageName = '0 - Qualification'`)
4. SQL → SQO (`StageName = '1 - Discovery'`)
5. SQO → Closed Won
6. Closed Won → Average deal size + cycle time

Each gate has a different failure mode and a different intervention. Misdiagnosing the gate wastes weeks of effort fixing the wrong thing.

## Mode 1: Funnel Diagnosis (the original use case)

**Triggers:** "where are we losing meetings", "why is [channel] underperforming", "show rate is dropping", "diagnose the funnel", "review the strike zone", "what's working".

**Default mode is conversational.** When invoked, work with the user interactively — don't dump a full report unprompted. The flow:

1. **Anchor on a channel + cohort window.** Ask what they want to diagnose. Don't assume.
2. **Pull live data via Salesforce MCP.** Use the SOQL templates in `references/soql_templates.md`. Always run queries — don't analyze from memory.
3. **Find the leaky gate.** Compare each gate's conversion rate to the channel's trailing-period baseline and to the other two channels. The leaky gate is the one with the largest negative gap.
4. **Diagnose with the pattern framework.** See `references/diagnostic_patterns.md`. Each leaky gate has 2–4 known failure modes; identify which one fits.
5. **Recommend specific action.** Action has to be named — a person, a list of accounts, a process change, a target.
6. **Offer the HTML write-up only if asked.** When the user says "write this up", switch to HTML mode.

The reason conversational-first matters: strike zone math is judgment-heavy. Dropping a finished report on a stage gate that turned out to be measurement noise is worse than spending three turns confirming the read. Surface hypotheses, let the user confirm, then act.

## Mode 2: Sprint Planning (multi-source PQA prioritization)

**Triggers:** "PQA sprint planning", "score our PQAs", "build a PQA backlog", "which accounts should we work this sprint", "rank our PQA cohort", "give me a sprint list".

**This is the mode that converts the funnel from a diagnostic to an execution backlog.** The output is an xlsx that becomes the rep's sprint queue.

### Workflow

1. **Define the cohort.** Default: all accounts with `Sales_PQA_Date_Account__c` (or MQA / OQA equivalent) in the target window. Confirm with the user.
2. **Multi-source enrich every account in parallel.** See `references/sprint_planning_workflow.md` for the staged enrichment pattern. Sources:
   - **Salesforce** — firmographics, Aero scores, GTM stage, owner, contacts
   - **Octave** (`mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__qualify_company`) — independent ICP qualification
   - **Amplitude** — Product Engagement Story via the 11-event framework (see `product-engagement-story` skill)
   - **Common Room** (`mcp__32d1a164-1bd3-41cb-a019-b2c320f13201__commonroom_list_objects`) — community signals + extra buying-committee depth
   - **FullEnrich** (`mcp__63157928-2125-4a53-b8f6-c0881c12ac2e__*`) — phones + verified emails on top tier (gated by credits — check `get_credits` first)
3. **Compute composite scores** per the v2 rubric in `references/multi_source_scoring.md`. Tier the cohort into Hot / Warm / Watch / Disqualify.
4. **Build the xlsx** with five tabs: Sprint Ranking (all accounts), Top Buying Committee (FullEnriched contacts), Scoring Rubric, Cohort Summary, Aero Scoring Gaps.
5. **Hand off the spreadsheet.** The reps work Tab 2 top-down; managers use Tabs 1 and 5 for prioritization conversations.

### Cost guardrails

FullEnrich is the only paid source. ~8.7 credits per contact for work email + mobile. Cap spend per run unless explicitly approved — at 5 contacts × top 50 = 250 contacts × 8.7 = ~2,200 credits per run. Use `get_credits` first; warn the user if balance is tight.

## Mode 3: Scoring Audit (find missed ICPs)

**Triggers:** "is Aero missing accounts", "find missed ICPs", "audit the scoring model", "where is Aero wrong", "are our PQAs actually good", "cross-reference scoring".

**The premise:** Aero (or any scoring model) is one signal among many. When Octave, Amplitude, Common Room, and Salesforce disagree with Aero, the disagreement IS the finding. See `references/scoring_audit_methodology.md` for the full method.

Two patterns surface most often:

### Aero False-Negatives
Accounts where Aero PES sits at floor (28.04 in the current Mixmax model) but Amplitude shows real, sustained team adoption. These are accounts already using Mixmax weekly — the scoring model just isn't seeing it. Flag: `aero_false_negative`.

### Aero-Missed ICPs
Accounts where an independent ICP qualifier (Octave) scores ≥7 (strong fit) but Aero Account Fit is <40 or null. Different miss pattern — firmographic, not engagement. Flag: `aero_missed`.

Both patterns are quantifiable, both are addressable, and both produce specific account lists. In Mixmax's 2026 PQA cohort, this audit found **34 Aero False-Negatives and 9 Aero-Missed ICPs out of 261 accounts (16%)** — accounts the rep team would have de-prioritized had they trusted Aero alone.

## Documented Aero failure modes

Surfaced through this analysis. Useful context when a user asks "why is Aero wrong on this account":

1. **PES floor at 28.04.** Most "low-engagement" PQAs share this exact score. The model loses distinction between a real low-engagement account and one where the signal collapsed.
2. **"No Score" silence ≠ "low fit".** When usage data is sparse, Aero produces no score — but reps see that as low fit in the queue. There's no firmographic-only fallback.
3. **No buying-title weighting on the PQA-triggering user.** A VP of Sales firing a PQA reads identical to an IC firing one.
4. **No trend velocity.** Account collapsing from 700 → 50 events scores the same as a flat 50.
5. **No ICP penetration ratio.** 2 active users / 21 mapped ICP contacts (9.5% penetration) reads identical to 2 active / 3 mapped (67%) — different stories, same Aero score.

These are documented in detail in `references/diagnostic_patterns.md` under "Gate 1 failure modes" and in `references/scoring_audit_methodology.md`.

## Audience awareness

This skill writes for two audiences. Default to **leader mode** unless told otherwise.

**Leader mode** (RevOps, GTM leadership): Recommendations are strategic — change targets, reallocate reps, kill or reinvest in channels, change the qualification rubric, change the playbook. Treat the user as someone with authority to change the operating model.

**Rep mode** (AE, SDR, CSM — fired when the user says "drill into [name]" or names a specific rep): Recommendations are tactical — these accounts to call, these objections to address, this messaging to use. Pull the rep's individual cohort using `Account.OwnerId` or `Opportunity.OwnerId`, compare to team baseline, identify their specific leak.

When in leader mode, NEVER recommend "have reps do better outreach" — that's not an action. The leader-mode equivalent is "the Outbound playbook needs a touchpoint-cadence rewrite; the data shows 14+ touches before a meeting on accounts that eventually book, vs. team baseline of 9." Specific, structural, ownable.

## Action format (all modes)

Every recommendation needs three parts:
- **Who** (named person or named role)
- **What** (a specific change)
- **By when** (a date or sprint)

If you can't fill all three slots, the recommendation isn't ready — diagnose deeper.

## Data sources

| Source | MCP / tool | What it adds |
|---|---|---|
| Salesforce | `mcp__d50c041d-378a-4fbe-b287-5541902dd1b9__*` | Cohort anchor dates, Aero scores, opp history, contacts, owner |
| Amplitude | `mcp__21ac7e4d-f1d6-44a3-81b3-242377655978__*` | Real product engagement, the 11-event PES framework |
| Octave | `mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__*` | Independent ICP qualification + playbook match + hard disqualifiers |
| Common Room | `mcp__32d1a164-1bd3-41cb-a019-b2c320f13201__*` | Community/intent signals, extra buying-committee contacts beyond SFDC |
| FullEnrich | `mcp__63157928-2125-4a53-b8f6-c0881c12ac2e__*` | Phone numbers + verified emails (credit-gated, top tier only) |
| Mixmax | `mcp__229af089-f88a-40ac-ae96-42d07e09ff31__*` | Meeting history + sequence performance |

## Caveats the team cares about

- **Use CHAMP + SPRINT + PLAN, not MEDDPICC.** Mixmax doesn't run MEDDPICC. Don't introduce it.
- **Lead with conversion, not volume.** Conversion-rate-first reporting; volume is secondary context.
- **Cohort math, not snapshot math.** Never compute "this month's win rate" using opps that closed this month — that's a snapshot. Always anchor the cohort by entry date (MQA / OQA / PQA) and trace the cohort forward.
- **Honest caveats.** If a cohort is too young, say so. If a field isn't groupable, say so. If you're inferring, say so.
- **Audience's own taxonomy.** Inbound / Outbound / Product are the channels. Expansion is its own motion, not a channel in strike zone math.
- **No MQL_Date__c.** The Inbound cohort anchor is `Account.MQA_Date_2024__c`. The legacy `MQA_Date__c` is retired.
- **`Channel_Source__c` is a formula field.** Non-groupable in SOQL. Filter on it, don't GROUP BY.
- **Filter renewal stages out of new-business math.** `Opportunity.Type IN ('New Business', 'Convert SS to DS')`.

## When NOT to use this skill

- Building the Aero dashboard itself → use the Aero prompt file
- Generic pipeline review (deal-by-deal status) → use `deal-management` or `sales-leader-weekly`
- Deal-specific autopsy ("why did Acme lose?") → use `customer-strategy-deep-dive` or `closed-lost-runbook`
- Renewal/churn analysis → use `churn-analysis-runbook` or `cs-leader-weekly-runbook`
- "What should I send to [prospect]?" → use `octave-outreach-drafter`
- Single-account deep research → use `customer-strategy-brief` or `customer-strategy-suite`

## Related skills

- `product-engagement-story` — runs the 11-event Amplitude PES analysis on a single account. This skill calls into that framework for Mode 2 and Mode 3.
- `customer-strategy-brief` — produces a 60-second brief on a single account. After this skill produces the sprint backlog, the brief runs on the top accounts.
- `customer-strategy-suite` — brief + deep dive + battle plan in one pass. Use after Mode 2 picks the top sprint targets.
- `account-pipeline-analysis` — adjacent skill; different scope (account prioritization without the funnel diagnostic).

## Reference files

- `references/soql_templates.md` — Ready-to-run SOQL for every strike-zone metric, with field names verified against the live Mixmax SFDC org.
- `references/diagnostic_patterns.md` — The pattern framework: for each leaky gate, the known failure modes, the disambiguating queries, and the typical interventions.
- `references/multi_source_scoring.md` — The v2 composite scoring rubric. Weights, sub-score logic, tier thresholds, signal-richness bonus, flag definitions.
- `references/sprint_planning_workflow.md` — The staged enrichment workflow for Mode 2: which sources to run, in what order, with what guardrails and cost caps.
- `references/scoring_audit_methodology.md` — The Mode 3 method: how to cross-reference signals to find Aero false-negatives and missed ICPs.
