---
name: accuracy-reconciliation
description: >
  Defines the accuracy reconciliation protocol for the Mixmax Quarterly Revenue Report.
  Use this skill whenever comparing a Quarterly Lookback snapshot against the three
  monthly reports generated during the quarter, running a pre-publish reconciliation gate,
  investigating a discrepancy between the quarterly and monthly artifacts, or deciding
  whether a quarterly number is trustworthy enough to publish to the Board. Trigger on
  phrases like "reconcile quarterly against monthly", "accuracy gate", "quarterly
  reconciliation check", "does this match the monthlies", "snapshot vs monthly",
  "revenue discrepancy at quarter close", "verify the quarterly numbers", "Q-to-M
  reconciliation", or any mention of the quarterly reconciliation hard-stop before publish.
---

# Accuracy Reconciliation (Quarterly)

The quarterly report goes to the Board, the CEO, and the entire company. A confidently wrong number in the quarterly doesn't just erode trust — it can drive real board-level decisions in the wrong direction.

This skill exists to make that impossible. Before any quarterly retrospective report is published, the quarterly numbers must reconcile against the three monthly reports that preceded them. If they don't, we stop.

---

## The reconciliation principle

The three monthly reports and the Quarterly Lookback snapshot are two views of the same revenue reality. They should agree on:
- Quarter Bookings (sum of monthly bookings)
- Quarter Pipeline created by channel (sum of monthly pipeline)
- Quarter Activity metrics (sum of monthly Accounts Engaged, Meetings, SQLs, SQOs)
- Quarter Churn / Downgrade / Expansion $ (sum of monthly)
- NRR / GRR (closing-quarter value — not summed, but should match the final month's EOM)
- Flagged risks (monthly-flagged risks should appear in the quarterly register unless resolved)

They may legitimately differ slightly because:
- Monthly reports are closed snapshots as-of each month end
- The Quarterly Lookback is a single snapshot at quarter-end that may include late-arriving adjustments
- Late-booked deals, true-ups, reclassifications, and corrections can accumulate between the final monthly and the quarterly snapshot

**Legitimate variance** comes from these end-of-quarter adjustments. **Illegitimate variance** comes from data-entry errors, stale formulas, reclassification drift, or the reporter pulling the wrong cell.

Our job is to separate the two.

---

## The reconciliation gate — hard-stop thresholds

Run the gate before ANY retrospective quarterly report is generated. For each material metric, compare:
- **Quarterly Lookback value** (what we are about to report)
- **Sum of the 3 monthly Lookback values** (Month 1 + Month 2 + Month 3)

Flag any deviation that exceeds BOTH of these thresholds:
- **Relative:** >2% variance
- **Absolute:** >$25K variance (higher than monthly's $10K because quarterly aggregates more noise)

Either threshold being exceeded triggers a flag. Using both prevents tiny metrics from generating noise AND prevents massive metrics from hiding issues.

**If a flag fires, you do not publish.** You investigate.

---

## The reconciliation checklist

Run this exact checklist. Every quarterly report. Every time.

### Metrics to reconcile (minimum set)

| # | Metric | Quarterly Source | Monthly Source (sum of 3) |
|---|---|---|---|
| 1 | Total ARR (EOQ) | Quarterly Revenue Summary, Total ARR | Month 3's EOM Total ARR (should match exactly) |
| 2 | Total DS Contribution | Quarterly Revenue Summary, DS row | Sum of 3 monthly DS contributions |
| 3 | Total SS Contribution | Quarterly Revenue Summary, SS row | Sum of 3 monthly SS contributions |
| 4 | Total Bookings (Quarter) | Quarterly Bookings Summary, Total Bookings | Sum of 3 monthly Total Bookings |
| 5 | New Business Bookings | Quarterly Bookings Summary | Sum of 3 monthlies |
| 6 | Expansion Bookings | Quarterly Bookings Summary | Sum of 3 monthlies |
| 7 | Total Pipeline Created | Quarterly Bookings Summary, Pipeline Total | Sum of 3 monthlies |
| 8 | Inbound / Outbound / Product / Expansion Pipeline | Quarterly Bookings Summary | Sum per channel across 3 monthlies |
| 9 | Accounts Engaged | Quarterly Bookings Summary, Activity | Sum of 3 monthlies |
| 10 | Meetings Booked | Quarterly Bookings Summary | Sum of 3 monthlies |
| 11 | SQLs / SQOs | Quarterly Bookings Summary | Sum of 3 monthlies |
| 12 | NRR % (EOQ) | CS Summary | Month 3's EOM NRR (closing value — should match) |
| 13 | GRR % (EOQ) | CS Summary | Month 3's EOM GRR (closing value — should match) |
| 14 | Total Churn $ | Quarterly Revenue Summary | Sum of 3 monthly churn |
| 15 | Total Downgrade $ | Quarterly Revenue Summary | Sum of 3 monthly downgrade |

**Note:** For *closing-value* metrics (EOQ Total ARR, NRR, GRR), quarterly MUST equal Month 3. Any variance is a bug, not an adjustment. For *accumulating* metrics (bookings, pipeline, activity, churn $), quarterly may legitimately exceed the monthly sum due to late-arriving adjustments.

---

## Bootstrap mode

If this is the first quarterly run AND fewer than 2 monthly reports exist for the quarter, skip the reconciliation gate and record `bootstrap_mode = true`. Replace the reconciliation table with this note:

> **Bootstrap note:** This is the first quarterly report under the new workflow, and monthly coverage was partial (< 2 monthlies available for Q{N}). Full monthly-to-quarterly reconciliation will be active starting next quarter.

Still run the intra-snapshot integrity check (below) — that doesn't require monthly reports.

---

## Intra-snapshot integrity check (always)

Independent of monthly reconciliation, the Quarterly Lookback must pass:
- No `#DIV/0!`, `#N/A`, `#REF!`, `#VALUE!` anywhere pulled
- Totals reconcile within the snapshot (DS = NB + Expansion + Churn + Downgrade; Total Bookings = sum across channels)
- Target columns populated where targets are reported
- Quarterly rollups equal the sum of their monthly columns (this is a self-consistency check within the Quarterly Revenue Summary tab)

ANY failure → pause, tell Heath at Checkpoint 2 (QA Look-Behind), don't silently paper over.

---

## Investigating a flagged variance

When a reconciliation flag fires, work this sequence:

1. **Identify the metric and the size of the variance** ($ and %).
2. **Check Month 3 first.** The final month of the quarter is where most late adjustments land. Open the Month 3 monthly HTML and compare its EOM value to the quarterly value.
3. **If Month 3 matches quarterly:** the variance lives in Month 1 or Month 2 re-statements. Check if any monthly report was re-published after-the-fact.
4. **If Month 3 does NOT match quarterly:** look at the Quarterly Lookback source cell — is there a formula that over-aggregates (double-counting) or pulls from the wrong tab? Fix at source.
5. **If the variance is a legitimate end-of-quarter adjustment** (e.g., a Q-close true-up on an expansion deal): document it in a "Q-Close Adjustments" subsection of the Reconciliation Appendix with $ amount, account, reason, source cell.
6. **If the variance cannot be explained:** do not publish. Escalate to Heath at Checkpoint 2.

---

## Reconciliation table output

Render the reconciliation result as a table at the top of the CRO Quarterly's appendix (and in the Board Snapshot's Reconciliation footnote if material):

| Metric | Quarterly | Σ Monthlies | Variance ($) | Variance (%) | Flag | Explanation |
|---|---|---|---|---|---|---|
| Total ARR (EOQ) | $X | $X (Month 3) | $0 | 0% | — | Closing value matches |
| Total Bookings | $Y | $Y' | +$Z | +N% | ⚠️ | Late-booked {account} $Z on {date} |
| ... | ... | ... | ... | ... | ... | ... |

A clean run shows no flags. Any flag shown must have an explanation. No blank explanation fields.

---

## Confidence posture in the narrative

If the reconciliation is clean, the quarterly narrative can use strong language: "Q{N} closed at $X (reconciled against monthly reports)."

If there are flagged-but-explained variances, soften: "Q{N} closed at $X; $Z of variance vs. monthly sum is attributable to end-of-quarter adjustments (detail in appendix)."

If there are unresolved flags, the workflow pauses and Heath decides whether to publish.

Never fake a reconciliation. If it's not clean, say so.
