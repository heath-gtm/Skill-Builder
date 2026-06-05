---
name: churn-analysis-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting
  the Mixmax Churn Analysis report. Use whenever the user asks "how do
  I run the churn report", "regenerate the churn analysis", "what goes
  in the thematic categorization", "how are churn themes calculated",
  "add a new account to the churn report", or any question about the
  churn analysis methodology, account deep-dive protocol, or output
  format.
---

# Churn Analysis Runbook

Reference runbook for generating, regenerating, or troubleshooting the Mixmax Churn & Downgrade Analysis report.

---

## Report Overview

The Churn Analysis produces a single self-contained HTML report combining:

1. **Executive Summary** — headline numbers, key narrative
2. **Churn Reason Summary** — raw reasons from Win/Loss fields, tabulated by logos + PCV
3. **Thematic Categorization + SVG Pie Chart** — inferred themes with ARR-share visualization
4. **Managed vs Non-Managed Split** — side-by-side comparison cards
5. **Managed Account Deep Dives** — per-account cards with Amplitude usage, meeting intelligence, preventability verdict
6. **Non-Managed Account Deep Dives** — same format, lighter data (no CSM meetings expected)
7. **Cross-Cut Analysis** — by preventability, usage classification, feature adoption, pricing impact, meeting coverage
8. **Recommendations** — prioritized action items

---

## Data Sources

| Source | What it provides | Tool |
|--------|-----------------|------|
| Gen 1 Sheet — Churn Analysis tab | Account list, PCV, Close Date, CSM, Win/Loss reasons, Aero scores | Chrome MCP / Google Sheets |
| Amplitude (project 130895) | 6-month product-usage deep-dive per account: MAU trend, feature usage, event volumes | Amplitude MCP |
| Mixmax Meetings | Historical meeting transcripts for each account (search by title + domain) | Mixmax MCP |

---

## Thematic Categorization Logic

The report infers broader themes from the detailed Win/Loss Reason and Win/Loss Details fields. Use this mapping as a starting point, but always review and adjust based on the actual data:

| Theme | Typical Win/Loss Reasons | Color |
|-------|-------------------------|-------|
| **Competitive Loss** | Selected Competitor, New DM chose competitor, Remained with Incumbent | #dc2626 (red) |
| **Acquired / M&A** | Company was acquired | #f59e0b (amber) |
| **Consolidation** | Tool Consolidation (NOT competitor — consolidating to existing stack) | #3b82f6 (blue) |
| **Self-Serve / No Contract Lock** | Self-Serve/MtM, month-to-month cancellation | #8b5cf6 (purple) |
| **Lack of Adoption** | Lack of adoption, Non-Responsive, No champion | #06b6d4 (cyan) |
| **Business Closed** | Business decreased/closed | #84cc16 (lime) |
| **Product Gaps** | Product Gaps (explicit) | #ec4899 (pink) |
| **Bad Fit** | Bad fit, Not ICP | #9ca3af (gray) |

### Mapping rules:
- **"Remained with Incumbent"** = Competitive Loss (they evaluated us and chose to stay with existing tool)
- **"Non-Responsive"** = Lack of Adoption (they stopped engaging — adoption failure)
- **"No champion"** = Lack of Adoption (no internal advocate — adoption failure)
- **"New DM chose different tool"** = Competitive Loss (decision-maker change leading to competitor win)
- If Win/Loss Details mention specific competitors → Competitive Loss
- If Win/Loss Details mention CRM migration or stack consolidation → Consolidation
- If Win/Loss Details mention budget cuts or layoffs → can create separate theme if volume warrants

### When to create new themes:
- If 3+ accounts share a pattern not covered above (e.g., "Budget Cuts", "Layoffs", "Seat Cleanup")
- Always keep total themes to 8 or fewer for chart readability

---

## SVG Pie Chart Specifications

The pie chart is an inline SVG (no JavaScript dependencies). Requirements:

- **Viewbox:** `0 0 420 420`
- **Radius:** 160px, centered at (210, 210)
- **Title:** "{Period} Churn — Share of ${total} PCV"
- **Center donut hole:** 52px radius white circle with total account count
- **Colors:** Use the theme color mapping above
- **Labels:** Show theme name + percentage on slices large enough (>5%). Smaller slices get labels outside or in legend only.
- **Legend:** 2-column grid below the chart

### Generating pie chart paths:

Each slice is an SVG `<path>` using arc commands. For a slice from angle `startAngle` to `endAngle` (in degrees, 0° = top/12 o'clock, clockwise):

```
startX = 210 + 160 * sin(startAngle * π/180)
startY = 210 - 160 * cos(startAngle * π/180)
endX   = 210 + 160 * sin(endAngle * π/180)
endY   = 210 - 160 * cos(endAngle * π/180)
largeArc = (endAngle - startAngle) > 180 ? 1 : 0

path = "M210,210 L{startX},{startY} A160,160 0 {largeArc},1 {endX},{endY} Z"
```

---

## Account Deep-Dive Protocol

For each churned account, the report runs three data pulls:

### 1. Amplitude Product-Usage Read
- **Lookback:** 6 months prior to churn close date
- **Metrics per month:** MAU, Sequence Activations, Sequence Emails Sent, Template Emails, Calendar Meetings, Email Tracking Views, 3rd-Party Integrations
- **Classify usage:** Heavy (>100 MAU or deep multi-feature), Moderate (10-100 MAU), Light (<10 MAU), Silent (0 MAU)
- **Identify trend:** Stable, Growing, Declining, Steep Decline, Late Spike

### 2. Mixmax Meeting Transcript Search
- **Search by:** account name in meeting titles AND attendee domain in events
- **Extract:** meeting date, attendees, classification, key themes, churn signals, action items
- **Build narrative:** connect meeting progression to churn outcome

### 3. Preventability Verdict
Based on usage + meeting intelligence + churn reason:
- **Not Preventable:** M&A, business closed, bad fit, active usage with pure procurement decision
- **Possibly Preventable:** Tool consolidation (could have defended with integration story), competitive loss with known product complaints
- **Preventable:** Lack of adoption (CSM intervention could have helped), dormant accounts not flagged, product trial failures not followed up

---

## Output File Conventions

```
Revenue Reviews/Churn Analysis/{Period}_Churn_Analysis.html

Examples:
  Q1_2026_Churn_Analysis.html
  March_2026_Churn_Analysis.html
  Q2_2026_Churn_Analysis.html
```

GitHub Pages path: `churn/{filename}`
Full URL: `${GITHUB_PAGES_URL}/churn/{filename}`

---

## Regenerating a Single Section

If you need to update just one part of the report:

1. **Re-run Amplitude for one account:** Use the Amplitude MCP to query the specific domain, then update that account's deep-dive card in the HTML.
2. **Re-run meeting search for one account:** Use Mixmax MCP `search_meeting_summaries` and `search_events` with the account name/domain.
3. **Update thematic categorization:** Adjust the theme mapping table, recalculate percentages, regenerate the SVG pie chart paths.
4. **Re-publish:** Read the updated HTML, base64 encode, PUT to GitHub Contents API with the existing SHA.

---

## Common Issues

| Issue | Fix |
|-------|-----|
| Amplitude returns no data for a domain | Try alternate domains (e.g., `attentivemobile.com` vs `attentive.com`). Check Amplitude `get_users` with domain filter. |
| Meeting search returns zero results | Normal for non-managed accounts. For managed accounts, check if CSM used non-Mixmax meeting tools. |
| Pie chart slices don't add up to 360° | Ensure percentages sum to 100% before converting to degrees. Use `percentage * 3.6` for degree conversion. |
| PCV totals don't match sheet | Verify Column F values. Some accounts may have $0 PCV (bad fit, free trials). |
