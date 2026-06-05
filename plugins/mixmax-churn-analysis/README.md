# mixmax-churn-analysis

Monthly and quarterly churn & downgrade analysis for Mixmax GTM.

## What this plugin produces

A single self-contained HTML report per period (monthly or quarterly) that analyzes every account that churned or downgraded. Combines Gen 1 sheet data with Amplitude product-usage deep-dives and Mixmax meeting transcript intelligence.

Sections:
1. Executive Summary
2. Churn Reason Summary (raw reasons table)
3. Thematic Categorization + SVG Pie Chart (inferred themes by ARR share)
4. Managed vs Non-Managed Split
5. Managed Account Deep Dives (per-account cards with Amplitude, meetings, verdicts)
6. Non-Managed Account Deep Dives
7. Cross-Cut Analysis (preventability, usage classification, feature adoption, pricing, meetings)
8. Recommendations

File lands at `Revenue Reviews/Churn Analysis/{Period}_Churn_Analysis.html` and is published to GitHub Pages at `churn/{filename}`.

## Skills

- **`churn-analysis-setup`** — one-time installer. Verifies MCP connections, confirms Churn Analysis tab, drops spec into working folder, registers the `mixmax-churn-analysis-report` scheduled task.
- **`churn-analysis-runbook`** — reference for ad-hoc generation, thematic categorization logic, SVG pie chart specs, account deep-dive protocol, and troubleshooting.

## Dependencies

- **`mixmax-publishing-core`** — required (GitHub Pages publishing config)
- **Google Sheets / Chrome MCP** — to read the Churn Analysis tab from Gen 1
- **Amplitude MCP** — project 130895 (Mixmax App Prod) for product-usage deep-dives
- **Mixmax MCP** — for meeting transcript searches
- **Notion MCP** (optional) — for posting summaries
- **Slack MCP** (optional) — for DM delivery

## Data Source

Gen 1 Google Sheet → Churn Analysis tab (gid=1283374228):
- Column A: Account Name
- Column B: Domain
- Column E: CSM (blank = non-managed)
- Column F: Previous Contract Value (PCV)
- Column R: Close Date (determines period)
- Columns S-Z: Downgrade Reason, Win/Loss Reason, Win/Loss Details, Aero scores

## Install

1. Install `mixmax-publishing-core` and run `publishing-config-setup`.
2. Install this plugin.
3. Run `churn-analysis-setup`.
4. Trigger `mixmax-churn-analysis-report` from the scheduled tasks panel, specifying the period (e.g., "Q1 2026").
5. Recommended cadence: monthly (first week of new month) + quarterly (first week after quarter close).
