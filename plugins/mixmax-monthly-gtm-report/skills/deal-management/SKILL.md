---
name: deal-management
description: >
  Analyze active deals and deal risk for the Mixmax GTM team. Use this skill
  whenever the user asks about deals, deal risk, forecast categories, pipeline
  deals, stuck deals, deal velocity, AE forecast, rep pipeline, deal
  concentration, close dates, stalled deals, deal stages, "how are deals
  looking", or any mention of the AE Forecast tab or the Rep Summary Deals by
  Forecast Category section. Also trigger on phrases like "deal review",
  "forecast review", "what's closing", "deal health", or "pipeline quality".
---

# Deal Management

Analyze active deal management and risk for the Mixmax GTM team's weekly revenue reporting.

## Data Sources

### AE Forecast - This Year Tab (GID: 1450719288)
- Individual deal records with:
  - Stage (0-5)
  - Close date
  - Amount
  - Forecast category (Commit, Best Case, Pipeline, Omit, Out)
  - Next step
  - Account info with Account ID

### Rep Summary Tab (GID: 1461552329)
- "Deals by Forecast Category" section listing:
  - All active deals grouped by rep
  - Opportunity Owner
  - Stage
  - AE Forecast Category
  - Next Step
  - Deal amounts
  - Account ID

## Salesforce Links
Every deal/account referenced must link to Salesforce:
```
https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view
```
Account IDs appear in both tabs.

## Deal Stage Definitions
Stages progress as follows:
- **0 - Qualification**: Initial discovery phase
- **1 - Discovery**: Deeper exploration of needs
- **2 - Scoping/Demo(s)**: Defining solution scope
- **3 - Proposal/Negotiation**: Formal proposal presented
- **4 - Closed Won**: Deal completed
- **5 - Closed Lost**: Deal lost

## AE Forecast Categories
- **Commit**: AE is confident this will close in the period
- **Best Case**: High probability but not guaranteed
- **Pipeline**: Active but not yet committed
- **Omit**: Excluded from forecast (early stage or pushed)
- **Out**: Not expected to close

## Analysis Framework

### 1. Forecast Category Distribution
- How much pipeline sits in Commit vs Best Case vs Pipeline vs Omit?
- Is Commit sufficient to cover the remaining target gap?
- Is Best Case realistic or inflated?

### 2. Stage Velocity & Stuck Deals
- Flag deals in Stage 0 (Qualification) or Stage 1 (Discovery) with close dates in the current month — these are at risk of not closing in time
- Flag deals with no Next Step documented — they're likely stalled
- Flag deals that have been in the same stage for more than 30 days

### 3. Concentration Risk
- If any single deal represents more than 30% of remaining pipeline, flag it
- If any single rep holds more than 50% of total pipeline, flag it
- If more than 60% of pipeline is in early stages (0-1), flag the stage mix

### 4. Close Date Accuracy
- Compare close dates to current date — are there deals with close dates in the past that are still open?
- Flag deals with close dates moved more than once

### 5. Deal-Level Detail Table
For the CRO Report, produce a table with:
- Account Name (linked to Salesforce)
- **Opportunity Owner (rep name) — CRO Report Only**
- Stage
- Close Date
- Amount
- AE Forecast Category
- Next Step
- Risk flags (color-coded)

For the Mixmax GTM Report, produce the same table but WITHOUT the Opportunity Owner column — deals are visible for transparency, but individual rep attribution is not shown.

**Color coding for rows:**
- **Red**: Commit/Best Case deals stuck in early stages, past-due close dates, no next step
- **Yellow**: Pipeline deals with close dates this month, large deals with no recent activity
- **Green**: Commit deals in Stage 3+ with clear next steps

### 6. Rep-Level Pipeline Summary — CRO Report Only
For each rep:
- Total pipeline value
- Pipeline by forecast category
- Number of deals
- Average deal size
- Largest deal (concentration check)

This section is ONLY included in the CRO Report. It is never shown in the Mixmax GTM Report.

### 7. Team-Level Attack Plan

Aggregate deal risk and pipeline gaps by team/role (AE Team, SDR Team, CS Team). This section appears in BOTH reports — it drives org-wide accountability without exposing individual rep performance.

For each team, analyze:

- **Pipeline Contribution**: Total pipeline value and forecast category distribution by team
- **Gap Analysis**: How much additional Commit does each team need to close the remaining target gap?
- **Stage Mix Risk**: Identify concentration risk at the team level (e.g., "AE Team pipeline is 70% early-stage")
- **Activity Bottleneck**: For SDR Team — meetings generated and pipeline coverage; for AE Team — deals in motion and velocity; for CS Team — expansion pipeline and renewal conversion
- **Team-Level Actions**: 2-3 specific, actionable initiatives each team should execute this week
  - Examples: "AE Team: Accelerate 3 stalled Stage 2 deals with executive follow-ups this week"
  - "SDR Team: Generate 12 additional meetings to reach 3:1 pipeline coverage ratio"
  - "CS Team: Schedule expansion reviews with top 5 accounts by ARR to uncover upsell opportunities"

## Output Guidelines

### Mixmax GTM Report (Org-Wide)
Shows aggregate pipeline health and team-level action items — full transparency, no individual rep attribution:
- Forecast category totals (Commit, Best Case, Pipeline, Omit)
- Forecast gap analysis: how much Commit + Best Case covers vs remaining target
- **Team-Level Attack Plan** with specific team initiatives
- Deal-Level Detail Table WITHOUT Opportunity Owner column
- Number of flagged deals with risk categories
- Team-level concentration risk flags
- **Does NOT include**: Individual rep names, rep-level pipeline summary, or Opportunity Owner details

### CRO Report (Direct to CRO)
Contains full deal-level transparency and rep-level detail:
- Forecast gap analysis and forecast category totals
- Full Deal-Level Detail Table with all columns including Opportunity Owner (rep names)
- Rep-Level Pipeline Summary for each rep
- Individual risk flags for each deal
- Team-Level Attack Plan with team-level actions
- Top 3 riskiest deals with specific reasons
- Salesforce links to all accounts

### General Principles
- Always lead with the forecast gap: how much Commit + Best Case covers vs remaining target
- Flag the top 3 riskiest deals with specific reasons (CRO Report: named deals, GTM Report: anonymized or count only)
- Currency as $X,XXX, color coding as described above

---

## Monthly Cadence Addendum (added for mixmax-monthly-gtm-report)

In the Monthly workflow, deal management goes DEEP. Focus areas:

### 1. Forecast accuracy by category

At month-start, each deal sat in a forecast category (Commit, Best Case, Pipeline, Omitted). At month-end, we know what actually closed.

Build this table:
| Category | Month-Start $ | Month-End Closed $ | Accuracy % |
|---|---|---|---|
| Commit | $X | $Y | Y/X |
| Best Case | $X | $Y | Y/X |
| Pipeline | $X | $Y | Y/X |

If Commit accuracy < 85%, that's a Forecast Miss risk.

### 2. Deal-by-deal autopsy (≥$10K threshold)

For every deal ≥$10K that EITHER slipped out of the month OR pulled into the month:
- Deal name and account (redact for GTM report, keep for CRO report)
- Original close date → new close date
- Amount
- Stage at month-start → stage at month-end
- Reason for change (1 sentence)
- Rep owner (CRO report only)

Slipped deals create Deal Slip risks. Pulled-in deals are called out as positives.

### 3. Stalled deals carried forward

Any deal that has been in the same stage for >14 days at month-end is "stalled." List:
- Deal name, amount, stage, days in stage, rep owner
- Next-month action plan for each

### 4. Stage concentration MoM

Report % of open pipeline in each stage, and the MoM shift:
- If concentration is moving toward late stages → healthy pull-forward
- If concentration is moving toward early stages → pipeline freshness, possibly a conversion concern

### 5. CRO-only: rep-level deal attribution

In the CRO Monthly Report, for each rep:
- Number of deals closed
- Forecast accuracy by category
- Average deal size
- Largest deal (won or lost)
- Any deal autopsy items attributed to them

This section is omitted from the GTM Monthly Report per the transparency-without-naming rule.
