---
name: monthly-risk-register
description: >
  Defines the structured risk register format for the Mixmax Monthly Revenue Report.
  Use this skill whenever building the risk section of a closed-month retrospective, 
  when categorizing and quantifying revenue risks, when rolling up Month and 
  Quarter-To-Date (QTD) exposure, or when cross-referencing risks back to the weekly
  reports that first flagged them. Trigger on phrases like "risk register", "monthly 
  risks", "QTD exposure", "churn risk", "deal slip risk", "pipeline gap risk", 
  "risk rollup", "what are we worried about", "categorize risks", "risk accountability",
  or any mention of deep-risk monthly analysis. Authoritative source for risk category
  taxonomy, required fields, source-cell trace requirements, confidence scoring, and
  owning-team attribution.
---

# Monthly Risk Register

The risk register is the most-read section of the Monthly Revenue Report. Leadership uses it to understand what just cost us money, what is about to cost us money, and who owns fixing it. Sloppy risk narration destroys trust faster than any other part of the report.

Your job with this skill is to make every risk in the register:
1. **Traceable** — every number points to a source cell
2. **Quantified** — Month impact AND QTD impact in dollars
3. **Accountable** — owned by exactly one team with a specific action
4. **Scored** — confidence level (High/Medium/Low)
5. **Historied** — if a weekly flagged this first, the weekly report is referenced

---

## The risk register schema

Every risk in the register captures these 9 fields. Missing fields are not acceptable — if you cannot fill one, either investigate further or do not include the risk.

| Field | Format | Example |
|---|---|---|
| **Risk Name** | Short identifier, 3–8 words | "Churn concentration in SMB segment" |
| **Category** | One of the 8 categories below | "Churn" |
| **Source Cell(s)** | Tab + row/col references | "Monthly Revenue Summary, row 42 (Total DS Churn)" |
| **Month Impact ($)** | Dollar impact in the closed month | "−$273K" |
| **QTD Impact ($)** | Running exposure across the quarter | "−$565K" |
| **First Flagged** | Weekly report reference or "This month" | "Week of March 16, 2026" |
| **Owning Team** | Exactly one of: AE Team / SDR Team / CS Team / RevOps | "CS Team" |
| **Action Plan** | Specific next-month action, not "monitor" | "CSM outreach to 5 at-risk accounts by April 17" |
| **Confidence** | High / Medium / Low | "High" |

---

## The 8 risk categories

Every risk gets exactly one category. If a risk spans multiple categories, split it.

1. **Deal Slip** — a deal that was forecasted to close in the month but pushed to a future period. Source: AE Forecast tab; compare close dates MoM.

2. **Churn** — an account that fully churned (no longer paying). Source: CS Summary + Renewals tab. Include the $ amount and the account name (redact for GTM report, keep for CRO report).

3. **Downgrade** — an account that reduced but did not churn. Source: CS Summary (downgrade line) + Renewals tab. Treated separately from Churn because downgrades often indicate product/value gaps, not competitive loss.

4. **Pipeline Gap** — new pipeline created in the month was below target. Source: Monthly Bookings Summary (Pipeline created by channel vs target). Always quantify as $ short AND % short.

5. **Forecast Miss** — a rep or the team committed to a number at month-start that came in materially under. Source: Rep Summary (forecast vs actual) + AE Forecast (what was in Commit at month-start, what actually closed).

6. **CS At-Risk** — an account that did not churn in the closed month but is flagged as at-risk for the coming month or quarter. Source: Renewals tab (At Risk column) + CS Summary. Include the renewal date so the exposure window is clear.

7. **Activity Shortfall** — SDR/AE activity metrics (Accounts Engaged, Meetings Booked, SQLs, SQOs) came in below target. Source: Monthly Bookings Summary (activity section). Activity shortfalls are leading indicators for future pipeline gaps.

8. **Rep Performance** — an individual rep (or SDR) came in materially below their quota/activity target. Source: Rep Summary. **GTM Monthly Report: never name the rep.** CRO Monthly Report: name the rep and their manager.

9. **Reporting Integrity** — a discrepancy between the monthly snapshot and the weekly reports that cannot be resolved. Source: reconciliation gate output (see `accuracy-reconciliation` skill). This category exists to make reporting quality visible.

Categories 1–8 are business risks. Category 9 is a meta-risk about our own reporting. Include all of them when relevant.

---

## Source-cell trace requirement

Every risk MUST cite at least one source cell. Use the format:

> **Source:** `[Tab Name]`, row `[N]` / col `[X]` — `[metric label in sheet]`

Examples:
- `Source: Monthly Revenue Summary, row 42 (Total DS Churn Actual)`
- `Source: Rep Summary, rows 8–24 (Bookings by rep, Mar 2026)`
- `Source: Renewals - This Year, filtered to "At Risk" = TRUE, col H (ARR)`

If the source is a cross-tab calculation (e.g., "Total DS Churn / Total DS Bookings"), cite both cells AND show the math briefly.

**Never report a risk without a source.** If you cannot point to a cell, do not include the risk — investigate first, then include it once the source is identified.

---

## Month Impact vs QTD Impact

Both fields are required for every risk. The logic:

- **Month Impact ($)** = dollar impact in the closed month ONLY. Cite the source cell.
- **QTD Impact ($)** = running impact for the quarter through the close of the reported month. This is the closed month's impact PLUS any earlier-quarter impact from the same risk theme.

**Worked example (March 2026 closes Q1):**
- Risk: SMB Churn
- January SMB churn: $58K
- February SMB churn: $92K
- March SMB churn: $273K
- Month Impact: −$273K
- QTD Impact: −$423K (Jan + Feb + Mar)

**If the risk is new in the closed month** (no prior-month exposure), QTD Impact equals Month Impact.

**If the risk started mid-quarter**, only sum from when it first appeared.

For forward-looking at-risk items (CS At-Risk category), Month Impact is $0 (not yet realized), and QTD Impact is the potential exposure if the risk materializes.

---

## First Flagged — the weekly accountability field

This field is what makes the monthly report accountable. For every risk, answer: *was this flagged in a weekly report this month?*

- **If yes:** cite the weekly — `"Week of March 9, 2026 — flagged as 'pipeline coverage below 3x for New Business'"`
- **If no:** state `"New this month"` or `"First surfaced in monthly reconciliation"`
- **If yes but not acted on:** mark as `"Carried — Week of March 9, 2026 (no action taken)"` — this is how we surface repeat offenders

**Rule:** A risk flagged three weeks in a row with "Carried — no action" triggers a separate callout at the top of the risk register titled "Unacted Weekly Flags." Leadership needs to see these.

Pull the weekly references from Step 2 (Weekly Report Discovery) of the monthly workflow — the Weekly Trendline Table you built has the MTD numbers and flagged risks for each week.

---

## Owning Team attribution

Exactly one of:

- **AE Team** — revenue close execution, deal progression, forecast accuracy
- **SDR Team** — pipeline creation, outbound activity, meeting generation
- **CS Team** — renewals, expansion, downgrade prevention, churn reduction
- **RevOps** — reporting integrity, forecast methodology, data quality, sheet hygiene

If the risk genuinely belongs to two teams, split it into two risks. Shared ownership means no ownership.

---

## Action Plan — specificity requirement

"Monitor," "review," "discuss with team," "keep an eye on" — **none of these are acceptable action plans.** They are non-actions.

An action plan passes the bar if it has:
- A verb (the team will *do* something)
- A specific target (account name, deal name, metric)
- A date (when it will be completed by)

**Good examples:**
- "CS Team: outreach to 5 at-risk accounts (list in appendix) by April 17 with executive sponsor"
- "AE Team: pull forward $50K in late-stage deals (Acme, Globex) to April close by running exec alignment calls in week 1"
- "SDR Team: +200 outbound touches in week 1 to close March pipeline gap of $75K"

**Bad examples:**
- "Monitor churn closely" — no verb, no target, no date
- "Improve forecast accuracy" — too vague
- "Work with CS on renewals" — no specific action

If the specialist skill that surfaced the risk cannot produce an action plan that passes this bar, mark the risk `Confidence: Low` and note "Action plan TBD — escalated to leadership."

---

## Confidence scoring

Every risk gets High / Medium / Low confidence. This reflects how certain we are in the Month Impact and QTD Impact numbers, not how likely the risk is.

- **High** — source cells are clean, numbers reconcile against weeklies, no #DIV/0! or #N/A in the trace path
- **Medium** — source cells are clean but the calculation involves an estimate (e.g., projecting a mid-stage deal's close probability) or a small reconciliation discrepancy
- **Low** — source cells contain errors, data is missing, or the number is based on an inference not directly observable in the sheet

Low-confidence risks still go in the register — we don't suppress them. But leadership needs to know the number might move.

---

## Output format — the table

In the retrospective HTML report, render the risk register as a table. Order by:
1. Month Impact (largest negative first)
2. Then by QTD Impact
3. Then by Category (Churn / Deal Slip / Downgrade before Pipeline Gap / Activity Shortfall)

The GTM Monthly Report shows all fields except rep names in the Rep Performance category.
The CRO Monthly Report shows everything.

Example rendering:

| # | Risk | Category | Month | QTD | First Flagged | Team | Action | Conf |
|---|---|---|---|---|---|---|---|---|
| 1 | SMB Churn Concentration | Churn | −$273K | −$423K | Week of Mar 9 (carried) | CS Team | CSM outreach to top 5 by Apr 17 | High |
| 2 | New Business Deal Slip | Deal Slip | −$86K | −$86K | Week of Mar 23 | AE Team | Pull-forward review Apr 6 | Medium |
| 3 | Q2 Pipeline Gap | Pipeline Gap | $0 | −$750K (exposure) | New this month | SDR Team | +400 touches wk1–2 | High |

---

## Unacted Weekly Flags callout

At the top of the risk register, BEFORE the table, include a callout IF any risk has been "Carried — no action taken" for 3+ consecutive weeks:

> ⚠️ **Unacted Weekly Flags (3+ weeks):**  
> These risks were surfaced in multiple weekly reports during the month but no action was taken. Leadership visibility requested.
> - **[Risk Name]** — first flagged [Week of X], re-flagged [Week of Y], [Week of Z]. Owning team: [Team].

This is the accountability lever. If it is empty, say so: "No unacted weekly flags this month. All flagged risks were addressed or escalated."

---

## Closing the loop — last month's risks

A monthly report isn't complete without reporting on what happened to LAST month's risks.

At the bottom of the risk register, include a "Last Month Risk Resolution" table. Pull the prior-month register (if available at `Revenue Reviews/Monthly Report/[Prior_Month]_Risks.md` or embedded in the prior HTML report) and for each risk mark:

- **Resolved** — no longer a risk
- **Ongoing** — still live, re-listed in this month's register
- **Escalated** — became a larger risk (show the $ delta)
- **Deferred** — action not taken, carried forward

This is non-negotiable. Leadership wants to know: *"you flagged X last month — what happened?"*

---

## A note on double-counting

A single underlying event can show up in multiple categories — e.g., a rep who missed forecast because a $50K deal slipped. That single event creates:
- A Deal Slip risk ($50K)
- A Forecast Miss risk (likely also $50K on that rep)
- Possibly a Rep Performance risk

**Do not sum these three into the register total.** When reporting the aggregate "Total Monthly Risk Exposure," dedupe by underlying event. In the table, show each as a separate row but mark them as "Linked: Risk #N" so the reader sees the relationship.
