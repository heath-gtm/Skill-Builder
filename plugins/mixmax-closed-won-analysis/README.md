# mixmax-closed-won-analysis

Monthly and quarterly Closed Won analysis for Mixmax GTM.

## What this plugin produces

A single self-contained HTML report per period (monthly or quarterly) that analyzes every deal that closed won. Combines Gen 1 sheet data with Amplitude product-usage deep-dives and Mixmax meeting transcript intelligence.

Sections:
1. Executive Summary (total deals, ARR, by channel/segment/rep)
2. Winning Patterns Summary (raw win reasons table)
3. Thematic Categorization + SVG Pie Chart (inferred themes by ARR share)
4. By Channel Breakdown (Inbound, Outbound, Product-Led, Expansion)
5. By Rep Breakdown (deal count + ARR per rep)
6. By Segment (Net New vs Expansion vs Conversion)
7. Per-Deal Deep Dives (cards with Amplitude usage, meeting intelligence, "What Worked" verdicts)
8. Cross-Cut Analysis (win rate by channel, Aero fit, deal size, post-close adoption)
9. Winning Playbook (Keep/Stop/Start framework)
10. Footer with run manifest

File lands at `Revenue Reviews/Closed Won Analysis/{Period}_Closed_Won_Analysis.html` and is published to GitHub Pages at `closed-won/{filename}`.

## Skills

- **`closed-won-setup`** — one-time installer. Verifies MCP connections, confirms AE Forecast tab, drops spec into working folder, registers the `mixmax-closed-won-analysis-report` scheduled task.
- **`closed-won-runbook`** — reference for ad-hoc generation, thematic categorization logic for wins, SVG pie chart specs, per-deal deep-dive protocol, and troubleshooting.

## Dependencies

- **`mixmax-publishing-core`** — required (GitHub Pages publishing config)
- **Google Sheets / Chrome MCP** — to read the AE Forecast - This Year tab from Gen 1
- **Amplitude MCP** — project 130895 (Mixmax App Prod) for product-usage deep-dives
- **Mixmax MCP** — for meeting transcript searches
- **Notion MCP** (optional) — for posting summaries
- **Slack MCP** (optional) — for DM delivery

## Data Source

Gen 1 Google Sheet → AE Forecast - This Year tab (gid=1450719288):
- Column C: Record Type (Net New / Expansion / Conversion)
- Column D: Opportunity Owner
- Column E: Account Name
- Column F: Stage (filter: "Closed Won")
- Column G: Close Date (determines period)
- Column M: Amount
- Column W: Opportunity Source
- Column X: Website
- Column Y: Win/Loss Details
- Column Z: Win/Loss Reason
- Columns AA-AB: Aero Account Fit, Aero Product Fit

Record types: "Mixmax - Net New - Direct Sales", "Mixmax - Expansion - Direct Sales", "Mixmax - Conversion - Direct Sales"

## Install

1. Install `mixmax-publishing-core` and run `publishing-config-setup`.
2. Install this plugin.
3. Run `closed-won-setup`.
4. Trigger `mixmax-closed-won-analysis-report` from the scheduled tasks panel, specifying the period (e.g., "Q1 2026").
5. Recommended cadence: monthly (first week of new month) + quarterly (first week after quarter close).
