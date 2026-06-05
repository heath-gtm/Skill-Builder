---
name: quarterly-risk-register
description: >
  Defines the structured risk register format for the Mixmax Quarterly Revenue Report.
  Use this skill whenever building the risk section of a closed-quarter retrospective,
  when categorizing and quantifying revenue risks at quarterly grain, when rolling up
  Quarter and Year-To-Date (YTD) exposure, or when cross-referencing risks back to the
  three monthly reports and weekly reports that first flagged them. Trigger on phrases
  like "quarterly risk register", "Q1 risks", "Q2 risks", "YTD exposure", "quarter-over-
  quarter risk", "board risk register", "deep risk for the quarter", "what are we
  worried about going into next quarter", or any mention of the risk section of the
  Quarterly Wrap-Up, CRO Quarterly, or Board Snapshot. Authoritative source for risk
  category taxonomy, required fields, source-cell trace requirements, confidence scoring,
  owning-team attribution, and monthly-report cross-reference.
---

# Quarterly Risk Register

The risk register is the most-read section of the Quarterly Revenue Report. Leadership, and especially the Board, uses it to understand what cost us money in the quarter, what is about to cost us money next quarter, and who owns fixing it. Sloppy risk narration destroys trust faster than any other part of the report.

Your job with this skill is to make every risk in the register:
1. **Traceable** — every number points to a source cell in the Quarterly Lookback snapshot
2. **Quantified** — Quarter impact AND YTD impact in dollars
3. **Accountable** — owned by exactly one team with a specific action
4. **Scored** — confidence level (High/Medium/Low)
5. **Historied** — if a monthly report flagged this first, the monthly report is referenced (and drilled to the weekly that surfaced it inside that month)

---

## The risk register schema

Every risk in the register captures these 9 fields. Missing fields are not acceptable — if you cannot fill one, either investigate further or do not include the risk.

| Field | Format | Example |
|---|---|---|
| **Risk Name** | Short identifier, 3–8 words | "SMB churn concentration" |
| **Category** | One of the 9 categories below | "Churn" |
| **Source Cell(s)** | Tab + row/col references in the Quarterly Lookback | "Quarterly Revenue Summary, row 42 (Total DS Churn Q1)" |
| **Quarter Impact ($)** | Dollar impact in the closed quarter | "−$665K" |
| **YTD Impact ($)** | Running exposure across the fiscal year through the closed quarter | "−$665K" (Q1 only) |
| **First Flagged** | Earliest reference — monthly report and the weekly inside that month | "March Monthly (carried from Week of March 9)" |
| **Owning Team** | Exactly one of: AE Team / SDR Team / CS Team / RevOps | "CS Team" |
| **Action Plan** | Specific next-quarter action, not "monitor" | "CSM outreach to top 10 at-risk accounts by April 30; exec sponsor for accounts >$20K ARR" |
| **Confidence** | High / Medium / Low | "High" |

---

## The 9 risk categories

Every risk gets exactly one category. If a risk spans multiple categories, split it.

1. **Deal Slip** — deals forecasted to close in the quarter but pushed to a future period. Source: AE Forecast tab + quarterly deal close-date analysis.

2. **Churn** — accounts that fully churned during the quarter (no longer paying). Source: CS Summary + Renewals tab, summed across the 3 months. Include $ and account names (redact for Wrap-Up, keep for CRO + Board).

3. **Downgrade** — accounts that reduced but did not churn. Tracked separately from Churn because downgrades indicate product/value gaps, not competitive loss.

4. **Pipeline Gap** — new pipeline created in the quarter below target. Source: Quarterly Bookings Summary (pipeline by channel vs Q target). Always quantify as $ short AND % short.

5. **Forecast Miss** — quarterly Commit at quarter-start vs what actually closed. Source: AE Forecast tab snapshots from the start of the quarter vs Lookback.

6. **CS At-Risk** — accounts flagged as at-risk heading into the new quarter. Source: Renewals tab (At Risk column). Include renewal dates so the exposure window is clear.

7. **Activity Shortfall** — SDR/AE activity metrics came in below quarterly targets. Source: Quarterly Bookings Summary (activity section). Activity shortfalls are leading indicators for next-quarter pipeline gaps.

8. **Rep Performance** — an individual rep came in materially below their quarterly quota. Source: Rep Summary. **Wrap-Up: never name the rep.** CRO Quarterly + Board: name the rep and their manager.

9. **Reporting Integrity** — a discrepancy between the Quarterly Lookback and the three Monthly reports that cannot be resolved. Source: monthly-to-quarterly reconciliation output. This category makes reporting quality visible.

Categories 1–8 are business risks. Category 9 is a meta-risk about our own reporting.

---

## Source-cell trace requirement

Every risk MUST cite at least one source cell in the Quarterly Lookback snapshot. Use the format:

> **Source:** `[Tab Name]`, row `[N]` / col `[X]` — `[metric label in sheet]`

Examples:
- `Source: Quarterly Revenue Summary, row 42 (Total DS Churn Q1 Actual)`
- `Source: Rep Summary, rows 8–24 (Bookings by rep, Q1 2026 totals)`
- `Source: Renewals - This Year, filtered to "Renewal Quarter" = "Q1 2026", col H (ARR)`

If the source is a cross-tab calculation (e.g., "Q1 DS Churn / Q1 DS Bookings"), cite both cells AND show the math briefly.

**Never report a risk without a source.** If you cannot point to a cell, investigate first, then include it once the source is identified.

---

## Quarter Impact vs YTD Impact

Both fields are required for every risk. The logic:

- **Quarter Impact ($)** = dollar impact in the closed quarter ONLY. Cite the source cell.
- **YTD Impact ($)** = running impact for the fiscal year through the close of the reported quarter. This is the closed quarter's impact PLUS any earlier-quarter impact from the same risk theme.

**Worked example (Q2 2026 closes):**
- Risk: SMB Churn
- Q1 2026 SMB churn: $423K
- Q2 2026 SMB churn: $665K
- Quarter Impact: −$665K
- YTD Impact: −$1.09M (Q1 + Q2)

**If the risk is new in the closed quarter** (no prior-quarter exposure), YTD Impact equals Quarter Impact.

**If this is the first quarter of the fiscal year (Q1)**, YTD = Quarter by definition.

For forward-looking at-risk items (CS At-Risk category), Quarter Impact is $0 (not yet realized), and YTD Impact is the potential exposure if the risk materializes next quarter.

---

## First Flagged — the monthly + weekly accountability field

This field is what makes the quarterly report accountable. For every risk, trace it back as far as possible. The order of precedence:

1. **Check the three Monthly Reports in the quarter** — was this risk named in any of them?
2. **If yes, check the weekly references inside that monthly** — which week in which month first surfaced it?
3. **If no monthly named it, check the weeklies directly** — was it in a weekly that didn't escalate to monthly?
4. **If no prior mention, mark "New this quarter"**

Formats:
- Monthly + weekly: `"January Monthly → Week of Jan 12 (pipeline coverage below 3x for New Business)"`
- Monthly only: `"February Monthly — first surfaced in monthly reconciliation"`
- Weekly only: `"Week of March 23 (weekly only, did not escalate to monthly)"`
- New: `"New this quarter — surfaced in Q1 reconciliation"`
- Carried without action: `"Carried — first flagged January Monthly, re-flagged February + March Monthly (no action taken)"`

**Rule:** A risk carried across all 3 months of the quarter with "no action taken" triggers a separate callout at the top of the risk register titled "Unacted Quarterly Flags." Board and leadership need to see these.

Pull monthly references from the 3 monthly retrospective HTMLs saved at `Revenue Reviews/Monthly Report/Mixmax_Monthly_Report_{YYYY-MM}.html`. Pull weekly references from the `Revenue Reviews/Weekly Report/` folder or GitHub Pages index.

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
- A specific target (account name, deal name, metric, or segment)
- A date (when it will be completed by — typically mid-quarter or end-of-quarter for quarterly risks)

**Good examples:**
- "CS Team: outreach to top 10 at-risk accounts (list in appendix) by April 30 with executive sponsor for accounts >$20K ARR"
- "AE Team: pull forward $200K in late-stage deals (Acme, Globex, Initech) to Q2 Month 1 close by running exec alignment calls in April"
- "SDR Team: +600 outbound touches in April–May to close Q1 pipeline gap of $300K before Q2 forecast lock"
- "RevOps: rebuild Pipeline Coverage calculation with stage-weighted probability by April 20; memo to CRO + CEO"

**Bad examples:**
- "Monitor churn closely" — no verb, no target, no date
- "Improve forecast accuracy" — too vague
- "Work with CS on renewals" — no specific action

If the specialist skill that surfaced the risk cannot produce an action plan that passes this bar, mark the risk `Confidence: Low` and note "Action plan TBD — escalated to leadership."

---

## Confidence scoring

Every risk gets High / Medium / Low confidence. This reflects how certain we are in the Quarter Impact and YTD Impact numbers, not how likely the risk is.

- **High** — source cells are clean, numbers reconcile against all 3 monthlies, no `#DIV/0!` or `#N/A` in the trace path
- **Medium** — source cells are clean but the calculation involves an estimate OR a small reconciliation discrepancy vs monthlies
- **Low** — source cells contain errors, data is missing across one or more months, or the number is based on an inference not directly observable

Low-confidence risks still go in the register — we don't suppress them. But leadership needs to know the number might move.

---

## Output format — the table

In the retrospective HTML report, render the risk register as a table. Order by:
1. Quarter Impact (largest negative first)
2. Then by YTD Impact
3. Then by Category (Churn / Deal Slip / Downgrade before Pipeline Gap / Activity Shortfall)

The Quarterly Wrap-Up (org) shows all fields except rep names in the Rep Performance category.
The CRO Quarterly + Board Snapshot show everything, with rep names and account names intact.

Example rendering:

| # | Risk | Category | Quarter | YTD | First Flagged | Team | Action | Conf |
|---|---|---|---|---|---|---|---|---|
| 1 | SMB Churn Concentration | Churn | −$665K | −$1.09M | Jan Monthly (carried all 3) | CS Team | CSM outreach top 10 by Apr 30 | High |
| 2 | Net New Deal Slippage | Deal Slip | −$280K | −$280K | March Monthly | AE Team | Pull-forward review Apr 6 | Medium |
| 3 | Q2 Pipeline Gap (exposure) | Pipeline Gap | $0 | −$1.2M exposure | New this quarter | SDR Team | +600 touches Apr–May | High |

---

## Unacted Quarterly Flags callout

At the top of the risk register, BEFORE the table, include a callout IF any risk was carried across all 3 months of the quarter with no action:

> ⚠️ **Unacted Quarterly Flags:**
> These risks were surfaced in every monthly report this quarter but no action was taken. Board visibility requested.
> - **[Risk Name]** — first flagged [Month Monthly], re-flagged [Month + Month]. Owning team: [Team]. YTD exposure: [$X].

If empty, say so: "No unacted quarterly flags this quarter. All flagged risks were addressed, escalated, or resolved."

---

## Closing the loop — last quarter's risks

A quarterly report isn't complete without reporting on what happened to LAST quarter's risks.

At the bottom of the risk register, include a "Last Quarter Risk Resolution" table. Pull the prior-quarter register (if available at `Revenue Reviews/Quarterly Report/{PriorQuarter}_Risks.md` or embedded in the prior HTML report) and for each risk mark:

- **Resolved** — no longer a risk
- **Ongoing** — still live, re-listed in this quarter's register
- **Escalated** — became a larger risk (show the $ delta from prior to current quarter)
- **Deferred** — action not taken, carried forward
- **Materialized** — the risk came true; show the realized $ impact

This is non-negotiable. Board and CEO want to know: *"you flagged X last quarter — what happened?"*

---

## A note on double-counting

A single underlying event can show up in multiple categories — e.g., a rep who missed quarterly forecast because $100K of deals slipped. That single event creates:
- A Deal Slip risk ($100K)
- A Forecast Miss risk (likely also $100K on that rep)
- Possibly a Rep Performance risk

**Do not sum these three into the register total.** When reporting the aggregate "Total Quarterly Risk Exposure," dedupe by underlying event. In the table, show each as a separate row but mark them as "Linked: Risk #N" so the reader sees the relationship.

---

## Board Snapshot — abbreviated risk register

The Board Snapshot is a one-page executive report. The risk section there is NOT the full table — it's the top 3 risks by Quarter Impact, rendered as a compact list:

> **Top 3 Risks**
> 1. **[Risk Name]** — [Category] · [$ Quarter Impact] · [Owning Team] · [One-line action]
> 2. ...
> 3. ...

Plus a single line at the bottom: "Full quarterly risk register: [link to Wrap-Up or CRO Quarterly]."
