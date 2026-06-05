---
name: revenue-analysis
description: >-
  Analyzes Mixmax revenue position and pacing. Triggers on phrases about ARR,
  revenue position, Total ARR, Direct Sales ARR, Self-Serve ARR, Net ARR
  Contribution, DS vs SS breakdown, revenue pacing, EOM forecast, monthly or
  quarterly revenue, "how are we pacing", revenue variance, or mentions of the
  Monthly/Quarterly Revenue Summary tabs.
---

# Revenue Analysis Skill

Specialized revenue position analysis for the Mixmax GTM team's weekly revenue reporting. This skill focuses exclusively on revenue metrics, pacing, and forecasts. Other skills handle pipeline creation, deal management, and renewals.

## Data Sources

### Primary Data Sheets
- **Monthly Revenue Summary tab** (GID: 586801175) — Primary source for weekly and monthly revenue analysis
- **Quarterly Revenue Summary tab** (GID: 2066645768) — Used for quarterly context and comparisons

### Data Integrity Rules
- Never mix monthly and quarterly data in the same section
- Always read pre-calculated forecasts from the sheet — never invent your own pacing math
- Skip error cells (#DIV/0!, #REF!, #N/A, #VALUE!, Error) and note as "data unavailable"

## Key Metrics to Analyze

### Total ARR (Top-Level)
- Current ARR: What has actually closed/is in the system as of the As-Of date
- Target ARR: The committed number for the period (set by leadership)
- Variance: Difference between Current and Target (in dollars and %)
- % to Target: Progress toward target as a percentage

### Direct Sales (DS) Channel
- Current ARR, Target, Variance, % to Target
- **DS Channel Breakdown** (4 components):
  - Net New Business (Current, Target, Variance)
  - Expansion (Current, Target, Variance)
  - Downgrade (Current, Target, Variance)
  - Churn (Current, Target, Variance)

### Self-Serve (SS) Channel
- Current ARR, Target, Variance, % to Target
- **SS Channel Breakdown** (7 components):
  - Net New SS (Current, Target, Variance)
  - Reactivation (Current, Target, Variance)
  - Upgrade (Current, Target, Variance)
  - Seat Expansion (Current, Target, Variance)
  - Seat Contraction (Current, Target, Variance)
  - Downgrade (Current, Target, Variance)
  - Churn (Current, Target, Variance)

### Net ARR Contribution
- Current: ARR closed to date
- Target: Committed number for the period
- Forecast: What the team is committing to based on current visibility
- Projected vs Target: Whether forecast tracks to hit target

### EOM Forecast & Pacing
- EOM Forecast: What the team expects to land at end-of-month/quarter
- Projected % to Target: ALWAYS read from the sheet, never calculate
- Monthly pacing, quarterly pacing, or year-to-date pacing as relevant

## Three Core Definitions (Never Blur These)

1. **Target** = The committed number for the period, set by leadership. This is the goal.
2. **Forecast** = What the team is committing to based on current visibility into pipeline and expected closures. This is the commitment.
3. **Current** = What has actually closed and is in the system as of the As-Of date. This is the reality.

These three tell a complete story: Where are we? Where are we going? What did we commit to getting?

## Analysis Framework

### Five-Step Process
1. **Headline**: Lead with Total ARR position vs target — are we above, below, or on target?
2. **Breakdown by Channel**: DS vs SS — which channel is driving the gap (or surplus)?
3. **Drill into Driver**: For the channel with the most significant variance, analyze the specific sub-channel breakdown (e.g., DS Churn vs New Business, or SS Upgrade vs Reactivation).
4. **Forecast Comparison**: Compare Current vs Forecast vs Target — are we tracking to close the gap by EOM?
5. **Forward Outlook**: What does the EOM Forecast say about where we'll land? Quantify projected variance at close.

### Variance Flagging Rule
- Flag any metric where variance exceeds 10% of target as requiring attention
- Color code in output: red for >10% gap, yellow for 5-10% gap, green for on/above target

## Revenue Narrative Guidelines

### Headline Structure
Always lead with the headline before diving into details:
- **On/Above Target**: "We are on track to hit our revenue target. Total ARR is currently $X,XXX (Y% to target)."
- **Below Target**: "We are tracking below our monthly revenue target by $X,XXX (Z% gap)."

### Quantification
- Express gaps in both dollars and percentages (e.g., "$500K below target, representing a 12% variance")
- For channel-level analysis, show the dollar impact of each component
- Always compare Current vs Forecast to show whether we're tracking to close the gap

### Attribution
- Name the specific channels and sub-channels driving performance
- For example: "The shortfall is driven by DS Churn ($300K) and lower-than-targeted SS Net New ($150K)"
- Avoid vague statements; always point to concrete line items

### Forward-Looking Perspective
- Lead with Current but immediately pivot to Forecast and EOM Forecast
- Example: "Current is $800K below target, but our forecast reflects a closing of that gap to $200K by EOM"
- This tells the GTM team whether we're tracking to recover

### Tone by Audience

**For Weekly Reports (GTM Audience)**
- Direct, candid, action-oriented
- Assume audience knows the business and can handle blunt language
- Focus on what's moving the needle and what actions to take
- Example: "We are down 15% on DS New Business. This is a pipeline problem, not an execution problem."

**For Monthly Reports (Company-Wide Audience)**
- Accessible, contextual, explanatory
- Provide more business context for non-GTM readers
- Celebrate wins, acknowledge challenges with solutions
- Example: "Our Direct Sales team is tracking slightly below target for new customer acquisition. We're seeing strong expansion revenue that partially offsets the gap."

## Accuracy Contract

### Every Number Must Trace to Source
- Every dollar amount and percentage must be traceable to a specific cell or row in the Monthly or Quarterly Revenue Summary sheet
- Include cell references (e.g., "B12: $2.5M Current Total ARR") when citing specific numbers in detailed analysis

### Read Pre-Calculated Values
- Always read pre-calculated forecasts, EOM forecasts, and % to Target from the sheet
- Never compute your own pacing math or projection formulas
- If a calculation appears to be missing or incorrect on the sheet, flag it and request clarification

### Handling Error Cells
- When you encounter error cells (#DIV/0!, #REF!, #N/A, #VALUE!, or other errors), note that data is unavailable
- Do not attempt to estimate or work around missing data
- Flag the issue to the team so data quality can be addressed

### Period Separation
- Monthly and quarterly periods never mix in the same section
- Clearly label which period(s) each analysis covers
- If comparing across periods, use separate paragraphs or tables

## HTML Output Format for Reports

### Currency & Percentage Formatting
- All currency values formatted as $X,XXX (e.g., $2,500, $150,000)
- Percentages shown with 1 decimal place (e.g., 12.5%, 98.0%)

### Color Coding
- **Green** (#00AA00): On target or above target
- **Yellow** (#FFCC00): Watch zone (5-10% below target)
- **Red** (#CC0000): Significantly below target (>10% gap)

### Variance Table Format
Standard variance tables should display:

| Metric | Current | Target | Variance ($) | Variance (%) |
|--------|---------|--------|--------------|--------------|
| Total ARR | $2,500K | $2,750K | -$250K | -9.1% |
| DS ARR | $1,500K | $1,750K | -$250K | -14.3% |
| SS ARR | $1,000K | $1,000K | $0K | 0.0% |

Use color coding on the Variance ($) and Variance (%) columns based on threshold rules above.

### Narrative + Table Combination
- Lead with a brief narrative summary (2-3 sentences)
- Follow with variance table for detailed numbers
- Include a forward-looking statement with Forecast and EOM Forecast data
- Close with specific action recommendations if variance exceeds thresholds

## Scope Boundaries

### What This Skill Covers
- Revenue position analysis (Total ARR, DS ARR, SS ARR)
- Channel-level variance analysis (DS vs SS, and sub-channel drilldowns)
- Forecast vs current vs target comparisons
- EOM forecast and pacing analysis
- Variance flagging and threshold alerts

### What Other Skills Handle
- **Pipeline creation & account strategy** → account-pipeline-analysis skill
- **Deal management & velocity** → Handled by other specialized skills
- **Customer renewals & retention** → Handled by other specialized skills
- **Product metrics & activation** → **ALWAYS invoke the `amplitude-guide` skill** before reporting any Self-Serve driver (signups, activation, upgrade, reactivation, churn-to-free). Do not infer product behavior from sheet aggregates alone — pull live Amplitude events, cross-reference with the sheet, and flag discrepancies. Self-Serve ARR commentary without an Amplitude cross-check is incomplete.

---

**Last Updated:** April 2026  
**Skill Owner:** GTM Revenue Operations  
**For Questions:** Contact the Revenue Operations team
