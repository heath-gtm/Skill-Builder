# Mixmax Monthly GTM Report

End-to-end automated monthly revenue reporting for the Mixmax GTM team. Runs a three-phase workflow — closed-month retrospective, sheet reset to the new month, forward-looking Month-Ahead — producing a transparent **Mixmax Monthly Report** for the entire company and a detailed **CRO Monthly Report**, distributed across GitHub Pages, Notion, and Slack.

## What It Does

Every month, this plugin powers a workflow that:

1. Extracts data from a values-only **Monthly Lookback Snapshot** of the Gen 1 sheet (9 tabs)
2. Cross-references the four weekly reports generated during the month (reconciliation hard-stop)
3. Runs specialist analysis across revenue, deals, renewals, and pipeline
4. Categorizes and quantifies risks with Month + QTD impact
5. Generates two retrospective HTML reports with different levels of detail
6. Pauses for approval, publishes to GitHub Pages, updates Notion, sends Slack messages
7. Resets the Gen 1 sheet forward to the new month via a single Apps Script menu item, capturing a **Monthly Lookahead Snapshot** with the new-month targets
8. Generates a forward-looking Month-Ahead report from the Lookahead snapshot
9. Requires human approval at three gates before anything is published

## The Three Reports

### Mixmax Monthly Report (All Company)
Sent to both `#gtm-central` and `#gtm-leadership` — everyone sees the same thing.
- Revenue position vs target, DS/SS breakdown, MoM + QTD rollups
- Bookings by channel, pipeline creation, activity metrics
- Deal forecast accuracy and slipped/pulled deals (no individual rep names)
- NRR/GRR, renewal outcomes, at-risk summary
- Team-Level Attack Plan (AE, SDR, CS teams)
- Top 10 Accounts to Go After with WHY justification
- Full Risk Register (9 categories, Month + QTD impact, owning team)
- Weekly Report Timeline with one-line summary per week

### CRO Monthly Report (Direct to CRO)
Everything in the Monthly Report, plus:
- Rep-level bookings, forecast accuracy, quota attainment
- Deal-by-deal autopsy for every deal ≥$10K that slipped or pulled in
- At-risk account detail with CSM owner and $ exposure
- Full reconciliation table (monthly snapshot vs final weekly)

### April Month-Ahead Report
Produced after the sheet reset, from the Monthly Lookahead snapshot.
- New-month targets (ARR, Bookings, Pipeline, Activity, Renewals)
- Carry-over risks from the retrospective register with mitigation plans
- Priority focus areas for the month

## Skills Included

| Skill | Purpose |
|-------|---------|
| `mixmax-revenue-reporting` | Orchestrator hub — sheet schema, metric definitions, accuracy rules |
| `revenue-analysis` | ARR position, DS/SS breakdown, channel pacing, QTD rollup |
| `deal-management` | Forecast categories, deal risk, team-level attack plan |
| `pipeline-building` | Pipeline coverage, activity metrics, Top 10 with WHY |
| `renewals-management` | NRR/GRR, at-risk accounts, churn analysis |
| `accuracy-reconciliation` | Hard-stop reconciliation protocol (incl. bootstrap / first-run mode) |
| `monthly-risk-register` | 9-category risk taxonomy, Month + QTD impact, confidence scoring |
| `monthly-report-setup` | One-time setup guide + sheet-reset protocol |

## Setup

1. Install this plugin in Claude Cowork
2. Say "set up monthly report" to trigger the setup guide
3. Install the combined `scripts/apps_script_monthly_snapshot.gs` on the Gen 1 sheet (drop-in replacement — preserves all weekly functions, adds the two monthly menu items)
4. Create a **Monthly Snapshots** folder in Google Drive and paste its ID into `CONFIG.MONTHLY_SNAPSHOT_FOLDER_ID`
5. Connect the required tools: Google Drive, Chrome extension, Notion, Slack, GitHub PAT
6. Create the scheduled task and run a dry-run (stop at Approval Gate #1)

## Required Connections

- **Google Drive MCP** — snapshot discovery
- **Chrome extension** — data extraction via gviz CSV endpoint, Apps Script menu clicks
- **Notion MCP** — monthly hub page updates
- **Slack MCP** — message delivery to `#gtm-central`, `#gtm-leadership`, and CRO DM
- **GitHub PAT** — report publishing to GitHub Pages at `reports/monthly/{YYYY-MM}/`

## How to Run (Monthly)

**Before clicking Run Now, take BOTH snapshots:**

1. Open the Gen 1 Google Sheet with dropdowns still on the closing month
2. Click **RevOps Tools > Create Monthly Lookback Snapshot**
3. Manually update the 6 dropdowns to the new month (Monthly Revenue/Bookings C2, Rep Summary E3/F3, CS Summary E3/F3)
4. Click **RevOps Tools > Create Monthly Lookahead Snapshot**

**Then trigger the workflow:**

5. In Cowork, go to the `mixmax-monthly-revenue-report` scheduled task and click **Run Now**
6. **Checkpoint 1 — Context Intake + Snapshot Verification:** answer the 4 intake questions; Claude verifies both snapshots
7. **Checkpoint 2 — QA Look-Behind:** review the two retrospective reports, approve or ask for edits
8. **Checkpoint 3 — QA Look-Ahead:** review the Month-Ahead report, approve or ask for edits
9. **Checkpoint 4 — Slack Message Review:** review all 6 Slack drafts together, approve the bundle
10. **Checkpoint 5 — Final Distribution Confirm:** one sign-off → GitHub Pages + Notion + all Slack sends fire

## Bootstrap / First-Run Mode

If this is the first monthly run under the new workflow, answer "Yes" to the first-run question in intake. Bootstrap mode will:
- Skip the weekly cross-reference and metric reconciliation
- Replace the reconciliation table with a Bootstrap Note
- Still run the intra-snapshot integrity check (non-negotiable)

From month 2 forward, the standard reconciliation gate runs against the four weekly reports generated during the month.
