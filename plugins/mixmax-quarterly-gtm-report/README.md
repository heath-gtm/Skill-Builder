# Mixmax Quarterly GTM Report

End-to-end automated quarterly revenue reporting for the Mixmax GTM team. Runs a three-phase workflow — closed-quarter retrospective, forward-looking Quarter-Ahead, and full distribution — producing four reports per close: a transparent **Quarterly Wrap-Up** for the entire company, a detailed **CRO Quarterly**, a forward-looking **Quarter-Ahead**, and a one-page **Board Snapshot** for the Board and CEO. Distributed across GitHub Pages, Notion, and Slack.

## What It Does

Every quarter, this plugin powers a workflow that:

1. Reads a values-only **Quarterly Lookback Snapshot** of the Gen 1 sheet (9 tabs)
2. Cross-references the three monthly reports generated during the quarter (reconciliation hard-stop)
3. Runs specialist analysis across revenue, deals, renewals, and pipeline
4. Categorizes and quantifies risks with Quarter + YTD impact
5. Generates three retrospective HTML reports at three audience tiers
6. Pauses for approval, publishes to GitHub Pages, updates Notion, sends Slack messages
7. Reads a **Quarterly Lookahead Snapshot** (taken by Heath on the new quarter) for targets + opening position
8. Generates a forward-looking Quarter-Ahead report from the Lookahead snapshot
9. Requires human approval at five gates before anything is published

## The Four Reports

### Quarterly Wrap-Up (All Company)
Sent to both `#gtm-central` and `#gtm-leadership` — everyone sees the same thing.
- Revenue position vs target at EOQ, DS/SS breakdown, QoQ + YTD rollups
- Bookings by channel, pipeline creation, activity metrics (all quarterly totals)
- Deal forecast accuracy and slipped/pulled deals (no individual rep names)
- NRR/GRR at EOQ, renewal outcomes across the quarter, at-risk summary going into new Q
- Team-Level Attack Plan (AE, SDR, CS teams)
- Top 10 Accounts to Go After with WHY justification
- Full Risk Register (9 categories, Quarter + YTD impact, owning team, account/rep names redacted)
- Monthly Report Timeline with one-line summary per monthly

### CRO Quarterly (Direct to CRO)
Everything in the Quarterly Wrap-Up, plus:
- Rep-level bookings, forecast accuracy, quota attainment (quarterly totals)
- Deal-by-deal autopsy for every deal ≥$25K that slipped or pulled in
- At-risk account detail with CSM owner, $ exposure, and renewal quarter
- Full reconciliation appendix (quarterly snapshot vs 3 monthly reports)
- Last Quarter Risk Resolution table (Resolved / Ongoing / Escalated / Deferred / Materialized)

### Quarter-Ahead Report
Produced after the retrospective, from the Quarterly Lookahead snapshot.
- New-quarter targets (ARR, Bookings, Pipeline by channel, Activity, Renewals)
- Opening position vs targets
- YTD trajectory (closed-quarter actuals + new-quarter forecast → where YTD lands)
- Carry-over risks from the retrospective register with mitigation plans
- Priority focus areas for the quarter (AE / SDR / CS)
- Refreshed Top 10 Accounts for the new quarter

### Board Snapshot (Board + CEO)
One-page executive report. Delivered to the CRO DM; Heath controls the Board handoff himself.
- 4–6 metric tiles (Total ARR EOQ, Net ARR Contribution, Bookings, NRR, GRR, Pipeline Coverage)
- One-paragraph CEO narrative — what closed, what moved, what's at stake
- Top 3 Risks (compact format)
- QoQ + YTD trendline (compact table)
- Reconciliation footnote + links to full Wrap-Up and CRO Quarterly

## Skills Included

| Skill | Purpose |
|-------|---------|
| `mixmax-revenue-reporting` | Orchestrator hub — sheet schema, metric definitions, accuracy rules |
| `revenue-analysis` | ARR position, DS/SS breakdown, channel pacing, YTD rollup |
| `deal-management` | Forecast categories, deal risk, team-level attack plan |
| `pipeline-building` | Pipeline coverage, activity metrics, Top 10 with WHY |
| `renewals-management` | NRR/GRR, at-risk accounts, churn analysis |
| `accuracy-reconciliation` | Quarterly-vs-monthly reconciliation protocol (incl. bootstrap / first-run mode) |
| `quarterly-risk-register` | 9-category risk taxonomy, Quarter + YTD impact, confidence scoring, Board Snapshot top-3 format |
| `quarterly-report-setup` | One-time setup guide + pre-run snapshot protocol |

## Setup

1. Confirm the Weekly + Monthly GTM Report plugins are already installed and healthy (the quarterly builds on top of their outputs)
2. Install this plugin in Claude Cowork
3. Say "set up quarterly report" to trigger the setup guide
4. Install the standalone `scripts/apps_script_quarterly_snapshot.gs` as a new file in the Gen 1 sheet's Apps Script project (it does NOT replace the existing weekly + monthly script — it adds a new `RevOps Tools — Quarterly` menu)
5. Add `addQuarterlyMenu_()` to the existing `onOpen()` function so the new menu builds on sheet open
6. Create a **Quarterly Snapshots** folder in Google Drive and paste its ID into `QCONFIG.QUARTERLY_SNAPSHOT_FOLDER_ID`
7. Authorize via `authorizeQuarterlyDrive`
8. Connect the required tools: Google Drive, Chrome extension, Notion, Slack, GitHub PAT
9. Create the scheduled task and run a dry-run (stop at Checkpoint 1)

## Required Connections

- **Google Drive MCP** — snapshot discovery
- **Chrome extension** — data extraction via gviz CSV endpoint, Apps Script menu clicks
- **Notion MCP** — 3 pages touched per run: Quarterly Workflow hub (`3427507ac622818d9e67cd19c13bb550`), Mixmax Quarterly Wrap-Up (`3427507ac62281878cd4d3fe996ecf69`), CRO Quarterly (`3427507ac62281ff8afce5ae923cade3`). Already created under the Mixmax GTM Team Notion page as siblings to Weekly + Monthly.
- **Slack MCP** — message delivery to `#gtm-central`, `#gtm-leadership`, and CRO DM (3 CRO DMs for quarterly: CRO Quarterly, Quarter-Ahead, Board Snapshot)
- **GitHub PAT** — report publishing to GitHub Pages at `quarterly/{QN-YYYY}-{gtm|cro|ahead|board}.html`

## How to Run (Quarterly)

**Before clicking Run Now, take BOTH snapshots:**

1. Open the Gen 1 Google Sheet with dropdowns still on the final month of the closing quarter (and any quarterly selector cells on the closed quarter)
2. Click **RevOps Tools — Quarterly > Create Quarterly Lookback Snapshot**
3. Manually update dropdowns to the new quarter's first month (Monthly Revenue/Bookings C2, Rep Summary E3/F3, CS Summary E3/F3) and any Quarterly Revenue/Bookings B2 selectors
4. Click **RevOps Tools — Quarterly > Create Quarterly Lookahead Snapshot**

**Then trigger the workflow:**

5. In Cowork, go to the `quarterly-revenue-report` scheduled task and click **Run Now**
6. **Checkpoint 1 — Context Intake + Snapshot Verification:** answer the 5 intake questions; Claude verifies both snapshots
7. **Checkpoint 2 — QA Look-Behind:** review the three retrospective reports (Wrap-Up, CRO Quarterly, Board Snapshot), approve or ask for edits
8. **Checkpoint 3 — QA Look-Ahead:** review the Quarter-Ahead report, approve or ask for edits
9. **Checkpoint 4 — Slack Message Review:** review all 7 Slack drafts together, approve the bundle
10. **Checkpoint 5 — Final Distribution Confirm:** one sign-off → GitHub Pages + Notion + all Slack sends fire

## Bootstrap / First-Run Mode

If this is the first quarterly run AND fewer than 2 monthly reports exist for the closing quarter, answer "Yes" to the first-run question in intake. Bootstrap mode will:
- Skip the monthly cross-reference and metric reconciliation
- Replace the reconciliation table with a Bootstrap Note
- Degrade the First Flagged column in the risk register (will show "New this quarter" more often)
- Still run the intra-snapshot integrity check (non-negotiable)

From quarter 2 forward, the standard reconciliation gate runs against the three monthly reports generated during the quarter.

## Quarterly-Specific Accuracy Rules

- **Reconciliation thresholds:** >2% AND >$25K (higher than monthly's $10K because quarterly aggregates more noise)
- **Closing-value metrics** (EOQ Total ARR, NRR, GRR) must equal Month 3's EOM value exactly — any variance is a bug, not an adjustment
- **Accumulating metrics** (bookings, pipeline, activity, churn $) may legitimately exceed the monthly sum due to end-of-quarter true-ups, reclassifications, and late-booked deals — these go in a "Q-Close Adjustments" subsection of the Reconciliation Appendix
- **Board Snapshot never publishes with unresolved reconciliation flags** — if the gate can't clear, the run pauses and Heath decides
