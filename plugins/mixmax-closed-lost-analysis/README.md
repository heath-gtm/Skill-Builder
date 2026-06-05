# mixmax-closed-lost-analysis

Monthly and quarterly Closed Lost analysis for Mixmax GTM.

## What this plugin produces

A single self-contained HTML report per period (monthly or quarterly) that analyzes every deal that closed lost. Combines Gen 1 sheet data with Amplitude product-usage deep-dives and Mixmax meeting transcript intelligence. The counterpart to the Closed Won plugin — focused on learning from losses.

Sections:
1. Executive Summary (total deals lost, ARR lost, by channel/segment/rep)
2. Loss Reason Summary (raw loss reasons table)
3. Thematic Categorization + SVG Pie Chart (inferred themes by ARR share)
4. Competitive Intelligence (losses by named competitor, win rate vs each)
5. By Channel Breakdown (Inbound, Outbound, Product)
6. By Rep Breakdown (loss count + ARR per rep)
7. By Stage Lost (at what stage did we lose — Discovery, Demo, Trial, Negotiation)
8. Per-Deal Deep Dives (cards with Amplitude usage, meeting intelligence, preventability verdicts, "What to Fix" lessons)
9. Cross-Cut Analysis (loss rate by channel, Aero fit, deal size, stage, competitor)
10. Lessons Learned (Keep/Stop/Start framework — process gaps, competitive responses, product gaps)
11. Footer with run manifest

File lands at `Revenue Reviews/Closed Lost Analysis/{Period}_Closed_Lost_Analysis.html` and is published to GitHub Pages at `closed-lost/{filename}`.

## Skills

- **`closed-lost-setup`** — one-time installer. Verifies MCP connections, confirms AE Forecast tab, drops spec into working folder, registers the `mixmax-closed-lost-analysis-report` scheduled task.
- **`closed-lost-runbook`** — reference for ad-hoc generation, thematic categorization logic for losses, competitive intelligence protocol, preventability framework, SVG pie chart specs, per-deal deep-dive protocol, and troubleshooting.

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
- Column F: Stage (filter: "Closed Lost")
- Column G: Close Date (determines period)
- Column M: Amount
- Column W: Opportunity Source
- Column X: Website
- Column Y: Win/Loss Details
- Column Z: Win/Loss Reason
- Columns AA-AB: Aero Account Fit, Aero Product Fit

Record types: "Mixmax - Net New - Direct Sales", "Mixmax - Expansion - Direct Sales", "Mixmax - Conversion - Direct Sales"

## Loss Theme Categories

| Theme | Color | Description |
|-------|-------|-------------|
| Competitor Won | #dc2626 | Named competitor selected |
| No Decision / Went Dark | #9ca3af | Prospect stopped responding |
| Budget / Timing | #f59e0b | Budget constraints, not the right time |
| Product Gaps | #3b82f6 | Missing features cited |
| Pricing Objection | #8b5cf6 | Our pricing was the blocker |
| Internal Solution | #06b6d4 | Built or chose internal tool |
| Champion Left | #ec4899 | Sponsor departed during cycle |
| Bad Fit / Not ICP | #84cc16 | Shouldn't have been in pipeline |

## Install

1. Install `mixmax-publishing-core` and run `publishing-config-setup`.
2. Install this plugin.
3. Run `closed-lost-setup`.
4. Trigger `mixmax-closed-lost-analysis-report` from the scheduled tasks panel, specifying the period (e.g., "Q1 2026").
5. Recommended cadence: monthly (first week of new month) + quarterly (first week after quarter close).
