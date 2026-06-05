---
name: deal-intelligence
description: >-
  Analyze active deals, deal risk, forecast quality, and deal-review readiness for Mixmax GTM. Two modes: (1) DEAL MANAGEMENT — forecast-category distribution, stuck/stalled deals, stage velocity, concentration risk, close-date accuracy, deal-level and rep-level summaries from the AE Forecast + Rep Summary tabs; (2) DEAL REVIEW PREP — synthesize Mixmax meeting transcripts, summaries, and action items into a MEDDIC brief with pains, objections, competitive mentions, champion/economic-buyer signals, and risk flags. Trigger on deals, deal risk, forecast categories, stuck deals, deal velocity, AE forecast, rep pipeline, deal concentration, close dates, deal stages, 'how are deals looking', 'deal review', 'forecast review', "what's closing", deal health, account brief, 'what do we know about [account]', the AE Forecast tab or Rep Summary Deals by Forecast Category section, or any request to summarize meeting history for an account. Also fire when a manager preps a forecast call.
---

# Deal Intelligence

The unified engine for active-deal analysis at Mixmax, consolidating the former
`deal-management` (sheet-based forecast/risk analysis) and `deal-review-prep`
(MEDDIC briefs from Mixmax meeting data) into one skill with two modes.

| Mode | Question it answers | Source |
|---|---|---|
| **A · Deal Management** | How healthy is the forecast? Which deals are at risk? | AE Forecast + Rep Summary tabs (Gen 1 sheet) |
| **B · Deal Review Prep** | What do we actually know about this deal, from the conversations? | Mixmax meeting transcripts, summaries, action items |

Mode A is the numbers read for forecast/pipeline reviews. Mode B is the
conversation read for deal reviews. They compose: run A to find the risky deals,
then B to understand why and what to do.

---

## Shared reference

### Deal stage definitions
- **0 - Qualification** — initial discovery
- **1 - Discovery** — deeper exploration of needs
- **2 - Scoping/Demo(s)** — defining solution scope
- **3 - Proposal/Negotiation** — formal proposal presented
- **4 - Closed Won** — deal completed
- **5 - Closed Lost** — deal lost

### AE forecast categories
- **Commit** — AE is confident this closes in the period
- **Best Case** — high probability, not guaranteed
- **Pipeline** — active but not yet committed
- **Omit** — excluded from forecast (early stage or pushed)
- **Out** — not expected to close

### Salesforce links
Every deal/account must link to Salesforce:
`https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view`
Account IDs appear in the AE Forecast and Rep Summary tabs.

---

## Mode A — Deal Management

### Data sources
- **Rev Ops AE Forecast - This Year tab** (GID: 1450719288) — individual deal records: Stage (0-5), Close Date, Amount, Forecast Category (Commit / Best Case / Pipeline / Omit / Out), Next Step, Account info with Account ID
- **Rep Summary tab** (GID: 1461552329) — "Deals by Forecast Category" section: all active deals grouped by rep, Opportunity Owner, Stage, AE Forecast Category, Next Step, deal amounts, Account ID

### Analysis framework

**1. Forecast category distribution.** How much pipeline sits in Commit vs Best Case vs Pipeline vs Omit? Is Commit sufficient to cover the remaining target gap? Is Best Case realistic or inflated?

**2. Stage velocity & stuck deals.**
- Flag deals in Stage 0 (Qualification) or Stage 1 (Discovery) with close dates this month — at risk of not closing in time.
- Flag deals with no Next Step documented — likely stalled.
- Flag deals in the same stage for more than 30 days.

**3. Concentration risk.**
- Any single deal > 30% of remaining pipeline → flag.
- Any single rep holding > 50% of total pipeline → flag.
- More than 60% of pipeline in early stages (0-1) → flag the stage mix.

**4. Close date accuracy.**
- Deals with close dates in the past that are still open → flag.
- Deals with close dates moved more than once → flag.

**5. Deal-level detail table (GTM Leadership report).** Columns: Account Name (Salesforce link), Opportunity Owner, Stage, Close Date, Amount, AE Forecast Category, Next Step, Risk flags (color-coded).
- **Red:** Commit/Best Case stuck in early stages, past-due close dates, no next step
- **Yellow:** Pipeline deals closing this month, large deals with no recent activity
- **Green:** Commit deals in Stage 3+ with clear next steps

**6. Rep-level pipeline summary.** Per rep: total pipeline value, pipeline by forecast category, number of deals, average deal size, largest deal (concentration check).

### Output guidelines (Mode A)
- Always lead with the forecast gap: how much Commit + Best Case covers vs remaining target.
- Flag the top 3 riskiest deals with specific reasons.
- **TL;DR report:** forecast category totals + number of flagged deals only (no individual deal names).
- **GTM Leadership report:** full deal-level detail with Salesforce links and risk flags.
- Currency `$X,XXX`, color coding as above.

---

## Mode B — Deal Review Prep (MEDDIC from Mixmax)

You are a deal review analyst. Pull meeting intelligence from Mixmax and
synthesize it into a structured brief a rep or manager can walk into a deal
review with — fully prepared, with evidence from actual conversations.

### Critical: always use Mixmax for meeting data
When retrieving meeting data, transcripts, summaries, or action items, ALWAYS use
the Mixmax MCP server tools. Do NOT pull meeting content from Google Calendar,
Notion, email, or any other source. A calendar event tells you a meeting
happened — Mixmax tells you what was said, decided, and what needs to happen next.

### Step 1 — Clarify scope
- **Which account(s)?** Single deep-dive or a portfolio review across deals?
- **What time range?** Default to last 30 days if unspecified.
- **Who's the audience?** Their own deal review, or briefing a manager/VP?

### Step 2 — Pull meeting data from Mixmax
Retrieve all meetings for the account(s) and range — transcripts, summaries, action items, participant lists. With many meetings, prioritize the most recent but scan all for themes.

### Step 3 — Structure with MEDDIC
MEDDIC isn't just formatting: teams using it improve forecast accuracy from ~65% to ~90% because the qualification data is predictive. For each element, pull evidence directly from transcripts.

- **Metrics** — quantified outcomes the prospect mentioned (revenue, cost/time savings, headcount). If found, quote it and the meeting; if missing, flag "No quantified business case discussed yet."
- **Economic Buyer** — has the actual decision-maker been in any meeting? Check participant lists/titles. If absent, flag — significant risk late in the deal.
- **Decision Criteria** — requirements, must-haves, evaluation criteria (features, integrations, security, pricing thresholds, competitive comparisons). If unclear, flag.
- **Decision Process** — steps, timeline, approvals (procurement, legal, pilot, committee, board). Note any stated deadline.
- **Identified Pain** — specific problems, direct quotes. Categorize "burning platform" vs "nice to fix." Repetition across meetings signals real urgency.
- **Champion** — is someone internally advocating? Look for forward-looking questions ("how would we roll this out?"), volunteering intros. No champion = high risk.

### Step 4 — Surface deal-risk signals
- No economic-buyer involvement (especially past discovery)
- Stale deal (no meetings 2+ weeks, no clear next step)
- Competitor mentioned (quote it + which meeting)
- Missing business case (no quantified metrics/ROI)
- Vague timeline ("sometime next quarter")
- Single-threaded (one contact; if they leave, deal dies)
- Action items overdue

### Step 5 — Compile open action items
List all outstanding items grouped by owner (rep vs prospect), noting which are overdue based on dates mentioned.

### Step 6 — Suggest next steps
2-3 specific, prescriptive moves, e.g.:
- "Schedule a meeting that includes [economic buyer] — they haven't been in any conversation."
- "Quantify the ROI: prospect mentioned [pain] but no number — prep a business case with estimated savings."
- "Prospect is evaluating [competitor] on [date] — prepare a comparison focused on [their criteria]."

### Output format (Mode B)
Clear headers per section. Use direct transcript quotes to keep the brief credible and specific. Open with a 2-3 sentence executive summary capturing current state, biggest risk, and recommended next action.

### Adapting for portfolio reviews
When a manager wants a review across deals: a shorter summary per account (exec summary + top risk + next step), a portfolio-level view (healthy / at-risk / stalled), and patterns across the portfolio (common objections, competitive threats in multiple deals, qualification gaps signaling a coaching opportunity).

---

## When NOT to use this skill
- Top-of-funnel coverage / account prioritization → `pipeline-intelligence`
- Monthly pipeline ICP-quality → `pipeline-intelligence` (Mode C)
- Single-account strategic deep dive → `customer-strategy-deep-dive`
- Closed-lost autopsy → `closed-lost-runbook`
- Channel-level funnel-leak math → `strike-zone-analyst`
