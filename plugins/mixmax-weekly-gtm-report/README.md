# Mixmax Weekly GTM Report

End-to-end automated weekly revenue reporting for the Mixmax GTM team. Transforms raw data from the Gen 1 Google Sheet into two reports — a transparent **Mixmax GTM Report** for the entire org and a detailed **CRO Report** — distributed across GitHub Pages, Notion, and Slack.

## What It Does

Every week, this plugin powers a workflow that:

1. Extracts data from a values-only snapshot of the Gen 1 sheet (9 tabs)
2. Runs specialist analysis across revenue, deals, renewals, and pipeline
3. Generates two HTML reports with different levels of detail
4. Publishes to GitHub Pages, updates Notion, and sends Slack messages
5. Requires human approval before anything is published

## The Two Reports

### Mixmax GTM Report (Org-Wide)
Sent to **both** #gtm-central and #gtm-leadership — everyone sees the same thing.
- Revenue pacing, pipeline coverage, activity metrics
- Team-Level Attack Plan (AE, SDR, CS teams)
- Top 10 Accounts to Go After with WHY justification
- No individual rep names

### CRO Report (Direct to CRO)
The CRO's personal command center — everything in the GTM Report plus:
- Rep-level pipeline summary and performance
- Full deal table with rep attribution
- Individual at-risk account detail

## Skills Included

| Skill | Purpose |
|-------|---------|
| `mixmax-revenue-reporting` | Orchestrator hub — sheet schema, metric definitions, accuracy rules |
| `revenue-analysis` | ARR position, DS/SS breakdown, channel pacing |
| `deal-management` | Forecast categories, deal risk, team-level attack plan |
| `pipeline-building` | Pipeline coverage, activity metrics, Top 10 with WHY |
| `renewals-management` | NRR/GRR, at-risk accounts, churn analysis |
| `weekly-report-setup` | One-time setup guide for connecting tools and creating the task |

## Setup

1. Install this plugin in Claude Cowork
2. Say "set up weekly report" to trigger the setup guide
3. Connect the required tools: Google Drive, Chrome extension, Notion, Slack
4. Provide your GitHub repo and PAT for report hosting
5. Create your first snapshot and run the task

## Required Connections

- **Google Drive MCP** — snapshot discovery
- **Chrome extension** — data extraction via gviz CSV endpoint
- **Notion MCP** — page updates
- **Slack MCP** — message delivery
- **GitHub PAT** — report publishing to GitHub Pages

## How to Run (Weekly)

1. Open the Gen 1 Google Sheet
2. Click **RevOps Tools > Create Weekly Snapshot**
3. In Cowork, go to the `weekly-revenue-report` scheduled task
4. Click **Run Now**
5. Answer the intake questions, review reports, approve distribution
