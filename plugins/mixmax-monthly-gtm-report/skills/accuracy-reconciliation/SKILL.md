---
name: accuracy-reconciliation
description: >
  Defines the accuracy reconciliation protocol for the Mixmax Monthly Revenue Report.
  Use this skill whenever comparing a monthly snapshot against the weekly reports 
  generated during that month, running a pre-publish reconciliation gate, 
  investigating a discrepancy between two revenue artifacts, or deciding whether a 
  monthly number is trustworthy enough to publish. Trigger on phrases like 
  "reconcile monthly against weekly", "accuracy gate", "reconciliation check", 
  "does this match the weekly", "snapshot vs weekly", "revenue discrepancy", 
  "verify the numbers match", "reconciliation table", or any mention of the monthly 
  reconciliation hard-stop before publish.
---

# Accuracy Reconciliation

The monthly report is read by leadership, the entire company, and (in CRO form) directly by the CRO. A confidently wrong number in the monthly report doesn't just erode trust — it can drive real decisions in the wrong direction.

This skill exists to make that impossible. Before any monthly report is published, the numbers must reconcile against the four weekly reports that preceded them. If they don't, we stop.

---

## The reconciliation principle

Weekly reports and the monthly snapshot are two views of the same revenue reality. They should agree on:
- MTD Bookings
- MTD Pipeline coverage
- MTD Activity metrics (Accounts Engaged, Meetings, SQLs, SQOs)
- Flagged risks

They may legitimately differ slightly because:
- The weekly is live (sheet as-of a week-ending date)
- The monthly snapshot is closed (sheet at month-end)
- Late-booked deals, adjustments, and corrections accumulate between the final weekly and the monthly snapshot

**Legitimate variance** comes from these end-of-month adjustments. **Illegitimate variance** comes from data-entry errors, stale formulas, or the reporter pulling the wrong cell.

Our job is to separate the two.

---

## The reconciliation gate — hard-stop thresholds

Run the gate before ANY retrospective report is generated. For each material metric, compare:
- **Monthly Snapshot value** (what we are about to report)
- **Final weekly report value** (last weekly of the month, typically the week ending closest to month-end)

Flag any deviation that exceeds BOTH of these thresholds:
- **Relative:** >2% variance
- **Absolute:** >$10K variance

Either threshold being exceeded triggers a flag. Using both prevents tiny metrics from generating noise (a 5% shift on a $200 number is $10 — not a real issue) and prevents massive metrics from hiding issues (a 1% shift on a $10M number is $100K — definitely a real issue).

**If a flag fires, you do not publish.** You investigate.

---

## The reconciliation checklist

Run this exact checklist. Every monthly report. Every time.

### Metrics to reconcile (minimum set)

| # | Metric | Monthly Source | Weekly Source |
|---|---|---|---|
| 1 | Total ARR (EOM) | Monthly Revenue Summary, Total ARR row | Final weekly, Total ARR row |
| 2 | Total DS Contribution | Monthly Revenue Summary, DS row | Final weekly, DS row |
| 3 | Total SS Contribution | Monthly Revenue Summary, SS row | Final weekly, SS row |
| 4 | Total Bookings (MTD / final) | Monthly Bookings Summary, Total Bookings | Final weekly, MTD Bookings |
| 5 | New Business Bookings | Monthly Bookings Summary | Final weekly |
| 6 | Expansion Bookings | Monthly Bookings Summary | Final weekly |
| 7 | Total Pipeline Created | Monthly Bookings Summary, Pipeline Total | Final weekly, Pipeline Total |
| 8 | Inbound / Outbound / Product / Expansion Pipeline | Monthly Bookings Summary | Final weekly |
| 9 | Accounts Engaged | Monthly Bookings Summary, Activity | Final weekly, Activity |
| 10 | Meetings Booked | Monthly Bookings Summary | Final weekly |
| 11 | SQLs / SQOs | Monthly Bookings Summary | Final weekly |
| 12 | NRR % | CS Summary | Final weekly (if present) |
| 13 | GRR % (ARR Retention) | CS Summary | Final weekly (if present) |
| 14 | Total Churn $ | Monthly Revenue Summary | Final weekly |
| 15 | Total Downgrade $ | Monthly Revenue Summary | Final weekly |

For each, compute:
- **Absolute variance:** Monthly − Weekly (in $ or units)
- **Relative variance:** (Monthly − Weekly) / Weekly × 100

Flag if BOTH thresholds are exceeded.

### Legitimate variance corpus

Before flagging, check whether the variance is explained by a known end-of-month event. Typical legitimate sources:
- Late deal booked after the final weekly (AE confirmed close date inside the last ~3 business days)
- Churn finalized at month-end (legal/ops processes complete after the weekly)
- Expansion / upgrade recognized at month-end
- Reactivation batch processed after the weekly cut
- Target line refresh (leadership adjusted the target line itself between weekly and monthly)
- Late renewal decision (At Risk → Renewed or At Risk → Churned flipped between the weekly and monthly)

If the variance matches a known event AND the event is documented in the weekly report (or confirmed by the user during intake), mark the item **Reconciled (expected variance)** and proceed.

If the variance does NOT match a known event, it's unexplained. Investigate.

---

## Investigation protocol (when a flag fires)

When reconciliation flags an unexplained variance, follow this sequence:

1. **Re-read the monthly snapshot cell.** Confirm no formula error, no `#DIV/0!`, no `#N/A`. If the cell is broken, the snapshot is stale — stop and ask the user to re-take the snapshot.

2. **Re-read the weekly source.** Same check. Weeklies are live, so if a weekly is stale, the weekly was wrong at publish time.

3. **Check the As Of dates.** If the final weekly was "as of March 28" but the monthly snapshot was taken on April 2, late activity between those two dates is the legitimate source of variance. Log this as expected and move on.

4. **Diff the underlying raw data.** For deal-level metrics, pull the AE Forecast or Renewals tab in both artifacts and identify which specific deals/accounts account for the delta.

5. **Document the finding.** Regardless of outcome, the investigation result goes into the reconciliation table that will be appended to the CRO Monthly Report.

6. **Decide:** 
   - **Resolved (expected variance)** → proceed to publish
   - **Resolved (snapshot corrected)** → user re-takes snapshot, restart the monthly workflow
   - **Unresolved** → STOP. Do not publish. Create a Reporting Integrity risk in the register and escalate to the user.

---

## The reconciliation table

The output of this skill is a reconciliation table. Build it in memory during Step 5 of the monthly workflow.

| # | Metric | Monthly Value | Final Weekly Value | Δ $ | Δ % | Threshold? | Explanation | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Total ARR | $8,502,315 | $8,499,000 | +$3,315 | +0.04% | No | Within tolerance | ✅ Reconciled |
| 2 | Total DS Contribution | $4,538,200 | $4,620,000 | −$81,800 | −1.77% | No | Within tolerance | ✅ Reconciled |
| 3 | Total Bookings | $104,500 | $89,000 | +$15,500 | +17.4% | **YES** | Late $16K Acme expansion booked Mar 30 | ✅ Reconciled (expected) |
| 4 | Total DS Churn | −$273,000 | −$180,000 | −$93,000 | +51.7% | **YES** | Globex churn finalized Mar 31, confirmed by CS | ✅ Reconciled (expected) |
| 5 | NRR % | 87% | 92% | −5pp | −5.4% | **YES** | UNRESOLVED | ⚠️ Flag |

This table lives in two places:
- **CRO Monthly Report:** full table in the appendix
- **GTM Monthly Report:** summary statement at the top ("N of M metrics reconciled; N flags resolved; N unresolved")

If there is ANY unresolved flag, the GTM report says so explicitly, and the unresolved flag becomes a "Reporting Integrity" risk in the register.

---

## Flagged risk cross-reference

Beyond metric reconciliation, the gate also checks whether weekly-flagged risks made it into the monthly register.

For each risk flagged in the weeklies during the month, verify the monthly register includes it OR includes a note explaining why not (e.g., "Week of Mar 9 flagged 'pipeline coverage below 3x' — resolved by Mar 23, not carried into monthly register").

If a weekly-flagged risk is *missing* from the monthly register with no explanation, that is itself a finding and creates a Reporting Integrity risk.

---

## The "no silent pass" rule

Reconciliation is not optional or best-effort. If you cannot complete the reconciliation table because:
- The monthly snapshot is incomplete
- Weekly reports are missing from the archive
- Source cells are broken
- You cannot access the final weekly for the month

…you do NOT publish the monthly report. You tell the user exactly what is missing and ask how to proceed.

**Never** present a monthly report with "reconciliation pending" or "reconciliation skipped." Either it's done or we don't publish.

---

## Where reconciliation data comes from

- **Monthly snapshot:** the Google Sheet `Gen1_Monthly_Lookback_Snapshot_{YYYY-MM-DD}` in the Drive folder `RevOps Monthly Snapshots` (https://drive.google.com/drive/folders/1X8aSTCum6kh6YsXLew1ZgDlRaU6FHdJ7). Pulled via the gviz CSV endpoint `https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={TAB_NAME}`.
- **Weekly reports:** HTML files in `Revenue Reviews/Weekly Report/` or published at `https://heath-gtm.github.io/mixmax-revenue-reports/weekly/`
- **Weekly Trendline Table:** built in Step 2 of the monthly workflow, stored in-memory for use here

If any of these sources is unavailable, STOP and surface to the user before proceeding — UNLESS bootstrap mode applies (see below).

---

## Bootstrap / first-run mode

The reconciliation gate assumes four weekly reports exist for the month being closed. There is exactly one scenario where that assumption legitimately fails: **the first run of the monthly workflow**, before a full month of weekly reports has accumulated under the new system.

### When bootstrap mode applies

All of the following must be true:
1. The month being reported is the first month the monthly workflow is running
2. Fewer than 2 weekly reports exist for the target month in the archive
3. The user explicitly authorizes bootstrap mode during Step 1 intake ("first run — no weekly cross-reference")

If any of those is false, bootstrap mode does NOT apply and the standard reconciliation gate runs.

### What bootstrap mode changes

In bootstrap mode:
- Skip the metric-vs-weekly variance comparison (steps 1–15 of the reconciliation checklist)
- Skip the flagged-risk cross-reference
- Replace the reconciliation table with a **Bootstrap Note** in both the CRO and GTM reports:
  > "First monthly run under the new workflow. No weekly cross-reference available for this month. Future monthly reports will include full reconciliation against four weekly reports."
- Still run the **intra-snapshot integrity check** (see below) — this is non-negotiable even in bootstrap mode

### Intra-snapshot integrity check (ALWAYS runs, including bootstrap)

Before publishing in bootstrap mode, verify the monthly snapshot is internally consistent:
- No `#DIV/0!`, `#N/A`, `#REF!`, or `#VALUE!` errors in any pulled cell
- Totals reconcile to their components (DS Contribution = New Biz + Expansion + Churn + Downgrade; Bookings sum across channels matches the reported total; etc.)
- Target columns are populated (no blank targets in source cells being reported)
- Quarterly rollups match the sum of the three monthly columns

If intra-snapshot integrity fails, STOP. Bootstrap mode does not exempt a broken snapshot from being wrong.

### Transition out of bootstrap mode

Bootstrap mode applies to month 1 only. Month 2 forward, the standard reconciliation gate runs against however many weeklies exist (minimum 2; fewer than 2 triggers a hard-stop that is NOT bootstrap).

---

## Edge cases

- **Only 3 weeklies exist for the month** (e.g., short month, skipped week): reconcile against all available weeklies. Note the gap in the reconciliation table.
- **A weekly report was corrected after publish:** use the corrected version for reconciliation. Note which one was used.
- **Monthly snapshot was taken more than 3 business days into the new month:** higher variance is expected. Document and proceed.
- **A risk appears in the monthly but not in any weekly:** flag in the register as "New this month." Not a reconciliation failure — just transparency.
