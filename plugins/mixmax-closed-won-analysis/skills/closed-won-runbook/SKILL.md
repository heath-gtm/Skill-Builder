---
name: closed-won-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting
  the Mixmax Closed Won Analysis report. Use whenever the user asks
  "how do I run the closed won report", "regenerate the closed won
  analysis", "what goes in the winning patterns", "how are win themes
  calculated", "add a new deal to the closed won report", or any
  question about the closed won methodology, deal deep-dive protocol,
  or output format.
---

# Closed Won Analysis Runbook

Reference runbook for generating, regenerating, or troubleshooting the Mixmax Closed Won Analysis report.

---

## Report Overview

The Closed Won Analysis produces a single self-contained HTML report combining:

1. **Executive Summary** — total deals won, ARR booked, by channel/segment/rep
2. **Winning Patterns Summary** — table of win reasons + ARR
3. **Thematic Categorization + SVG Pie Chart** — themes by ARR share
4. **By Channel Breakdown** — Inbound, Outbound, Product, Expansion
5. **By Rep Breakdown** — deal count + ARR per rep
6. **By Segment** — Net New vs Expansion vs Conversion
7. **Per-Deal Deep Dives** — each deal gets a card with Amplitude usage, meeting intelligence, and "What Worked" verdict
8. **Cross-Cut Analysis** — win rate by channel, by Aero fit, by deal size
9. **Winning Playbook** — Keep/Stop/Start framework
10. **Footer** with run manifest

---

## Data Sources

| Source | What it provides | Tool |
|--------|-----------------|------|
| Gen 1 Sheet — AE Forecast - This Year tab | Deal list, Amount, Close Date, Owner, Record Type, Source, Win/Loss reasons, Aero scores | Chrome MCP / Google Sheets |
| Amplitude (project 130895) | 6-month post-close product-usage deep-dive per account: MAU trend, feature usage, event volumes | Amplitude MCP |
| Mixmax Meetings | Historical meeting transcripts for each account (search by title + domain) | Mixmax MCP |

---

## Thematic Categorization Logic for Wins

The report infers broader themes from the detailed Win/Loss Reason and Win/Loss Details fields. Use this mapping as a starting point, but always review and adjust based on the actual data:

| Theme | Typical Win/Loss Reasons | Color |
|-------|-------------------------|-------|
| **Price/Value** | Better pricing, cost savings vs incumbent, ROI-driven | #22c55e (green) |
| **Product Fit** | Feature match, solves specific workflow pain, product-led conversion | #3b82f6 (blue) |
| **Speed to Value** | Fast implementation, quick time-to-value, POC success | #8b5cf6 (purple) |
| **Competitive Displacement** | Displaced competitor, won head-to-head eval, switching from incumbent | #dc2626 (red) |
| **Executive Sponsorship** | Champion-driven, exec sponsor, top-down mandate | #f59e0b (amber) |
| **Channel/Partner** | Partner referral, channel-sourced, ecosystem play | #06b6d4 (cyan) |
| **Expansion/Land-Expand** | Existing customer expansion, seat growth, upsell, cross-sell | #ec4899 (pink) |

### Mapping rules:
- **"Product Fit"** reasons = Product Fit theme (they chose us because our product matched their needs)
- **"Price"** or **"Cost"** mentions in Win/Loss Details = Price/Value theme
- **"Speed"** or **"Fast"** or **"POC"** mentions = Speed to Value theme
- **Competitor name in Details** with "switched from" or "replaced" = Competitive Displacement
- **"Champion"** or **"VP"** or **"CRO"** = Executive Sponsorship
- **"Partner"** or **"Referral"** in Source = Channel/Partner
- **Record Type containing "Expansion"** = Expansion/Land-Expand
- If Win/Loss Details mention multiple factors, assign to the primary driver

### When to create new themes:
- If 3+ deals share a pattern not covered above (e.g., "Multi-Threading", "Technical Win", "Migration Ease")
- Always keep total themes to 8 or fewer for chart readability

---

## SVG Pie Chart Specifications

The pie chart is an inline SVG (no JavaScript dependencies). Requirements:

- **Viewbox:** `0 0 420 420`
- **Radius:** 160px, centered at (210, 210)
- **Title:** "{Period} Closed Won — Share of ${total} ARR"
- **Center donut hole:** 52px radius white circle with total deal count
- **Colors:** Use the theme color mapping above
- **Labels:** Show theme name + percentage on slices large enough (>5%). Smaller slices get labels outside or in legend only.
- **Legend:** 2-column grid below the chart

### Generating pie chart paths:

Each slice is an SVG `<path>` using arc commands. For a slice from angle `startAngle` to `endAngle` (in degrees, 0 = top/12 o'clock, clockwise):

```
startX = 210 + 160 * sin(startAngle * PI/180)
startY = 210 - 160 * cos(startAngle * PI/180)
endX   = 210 + 160 * sin(endAngle * PI/180)
endY   = 210 - 160 * cos(endAngle * PI/180)
largeArc = (endAngle - startAngle) > 180 ? 1 : 0

path = "M210,210 L{startX},{startY} A160,160 0 {largeArc},1 {endX},{endY} Z"
```

---

## Per-Deal Deep-Dive Protocol

For each Closed Won deal, the report runs three data pulls:

### 1. Amplitude Product-Usage Read (Post-Close Validation)
- **Lookback:** 6 months starting from close date (post-close usage validation — are they actually using it?)
- **Metrics per month:** MAU, Sequence Activations, Sequence Emails Sent, Template Emails, Calendar Meetings, Email Tracking Views, 3rd-Party Integrations
- **Classify usage:** Heavy (>100 MAU or deep multi-feature), Moderate (10-100 MAU), Light (<10 MAU), Silent (0 MAU)
- **Identify trend:** Ramping Up, Stable, Declining, Not Yet Active

### 2. Mixmax Meeting Transcript Search
- **Search by:** account name in meeting titles AND attendee domain in events
- **Extract:** meeting date, attendees, classification, key themes, buying signals, objections overcome
- **Build narrative:** connect meeting progression to close outcome — what happened in the sales process

### 3. "What Worked" Verdict
Based on deal data + meeting intelligence + usage validation:
- **Winning Channel:** Which source/channel drove this deal (Inbound, Outbound, Product-Led, Expansion, Partner)
- **Winning Play:** What was the key motion that closed it (POC, Executive alignment, competitive bake-off, land-expand, speed play)
- **Replicable Pattern:** Is this a repeatable play? What made it work? Can we do this again?
- **Post-Close Health:** Based on Amplitude — is the customer actually adopting? (Green = strong usage, Yellow = moderate, Red = low/silent)

---

## Output File Conventions

```
Revenue Reviews/Closed Won Analysis/{Period}_Closed_Won_Analysis.html

Examples:
  Q1_2026_Closed_Won_Analysis.html
  March_2026_Closed_Won_Analysis.html
  Q2_2026_Closed_Won_Analysis.html
```

GitHub Pages path: `closed-won/{filename}`
Full URL: `${GITHUB_PAGES_URL}/closed-won/{filename}`

---

## Regenerating a Single Section

If you need to update just one part of the report:

1. **Re-run Amplitude for one account:** Use the Amplitude MCP to query the specific domain, then update that deal's deep-dive card in the HTML.
2. **Re-run meeting search for one account:** Use Mixmax MCP `search_meeting_summaries` and `search_events` with the account name/domain.
3. **Update thematic categorization:** Adjust the theme mapping table, recalculate percentages, regenerate the SVG pie chart paths.
4. **Re-publish:** Read the updated HTML, base64 encode, PUT to GitHub Contents API with the existing SHA.

---

## Common Issues

| Issue | Fix |
|-------|-----|
| Amplitude returns no data for a domain | Try alternate domains (e.g., `attentivemobile.com` vs `attentive.com`). Check Amplitude `get_users` with domain filter. |
| Meeting search returns zero results | Check if sales used non-Mixmax meeting tools. Try broader search terms. |
| Pie chart slices don't add up to 360 degrees | Ensure percentages sum to 100% before converting to degrees. Use `percentage * 3.6` for degree conversion. |
| Amount totals don't match sheet | Verify Column M values. Some deals may have $0 Amount (trials, pilots). |
| Record Type filter misses deals | Check for variant record type names — filter on "Closed Won" stage, not record type. |
