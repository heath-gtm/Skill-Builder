# Mixmax Report Accuracy

Dedicated QA skill for auditing any Mixmax revenue report before publishing.

## What it does

Runs a comprehensive accuracy audit on any generated report, producing a pass/warning/fail result with individual check details. The QA result feeds into the "If You Read Nothing Else" cover page badge.

## Checks

**Universal (every report):**
- Data completeness — all expected rows present
- Math accuracy — totals reconcile to source
- Snapshot freshness — data within acceptable age
- Section coverage — all required sections populated
- Cross-reference — numbers agree across sections
- HTML integrity — no broken SVG or missing cards

**Report-specific:** Additional checks tailored to each report type (weekly, monthly, quarterly, churn, closed won/lost, AE pipeline, CSM book, leader weeklies, update slides).

## Skills

- **report-accuracy** — Run the full QA audit on any report

## Usage

1. Install plugin
2. Generate any Mixmax revenue report
3. Before publishing, invoke `report-accuracy`
4. Review the QA results at the checkpoint
5. If PASS: publish. If WARNING: review and confirm. If FAIL: fix issues first.
