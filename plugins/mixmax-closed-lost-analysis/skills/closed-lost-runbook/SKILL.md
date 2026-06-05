---
name: closed-lost-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting
  the Mixmax Closed Lost Analysis report. Use whenever the user asks
  "how do I run the closed lost report", "regenerate the closed lost
  analysis", "what goes in the loss patterns", "how are loss themes
  calculated", "add a new deal to the closed lost report", or any
  question about the closed lost methodology, deal deep-dive protocol,
  competitive intelligence, preventability verdicts, or output format.
---

# Closed Lost Analysis Runbook

Reference runbook for generating, regenerating, or troubleshooting the Mixmax Closed Lost Analysis report.

---

## Report Overview

The Closed Lost Analysis produces a single self-contained HTML report combining:

1. **Executive Summary** — total deals lost, ARR lost, by channel/segment/rep
2. **Loss Reason Summary** — table of loss reasons + deal count + ARR
3. **Thematic Categorization + SVG Pie Chart** — themes by ARR share
4. **Competitive Intelligence** — losses by named competitor, win rate vs each competitor
5. **By Channel Breakdown** — Inbound, Outbound, Product
6. **By Rep Breakdown** — loss count + ARR per rep
7. **By Stage Lost** — at what stage did we lose (Discovery, Demo, Trial, Negotiation, etc.)
8. **Per-Deal Deep Dives** — each deal gets a card with Amplitude usage, meeting intelligence, preventability verdict, and "What to Fix"
9. **Cross-Cut Analysis** — loss rate by channel, by Aero fit, by deal size, by stage, by competitor
10. **Lessons Learned** — Keep/Stop/Start framework focused on process gaps, competitive responses, product gaps
11. **Footer** with run manifest

---

## Data Sources

| Source | What it provides | Tool |
|--------|-----------------|------|
| Gen 1 Sheet — AE Forecast - This Year tab | Deal list, Amount, Close Date, Owner, Record Type, Source, Win/Loss reasons, Aero scores | Chrome MCP / Google Sheets |
| Amplitude (project 130895) | 6-month product-usage deep-dive per account: did they trial? what features did they try? | Amplitude MCP |
| Mixmax Meetings | Historical meeting transcripts for each account (search by title + domain) — what happened in the sales process | Mixmax MCP |

---

## Thematic Categorization Logic for Losses

The report infers broader themes from the detailed Win/Loss Reason and Win/Loss Details fields. Use this mapping as a starting point, but always review and adjust based on the actual data:

| Theme | Typical Win/Loss Reasons | Color |
|-------|-------------------------|-------|
| **Competitor Won** | Named competitor selected, chose competitor tool, lost to [competitor name] | #dc2626 (red) |
| **No Decision / Went Dark** | Prospect stopped responding, no decision made, went silent | #9ca3af (gray) |
| **Budget / Timing** | Budget constraints, not the right time, pushed to next year, freeze | #f59e0b (amber) |
| **Product Gaps** | Missing features cited, product didn't meet requirements, feature gap | #3b82f6 (blue) |
| **Pricing Objection** | Our pricing was the blocker, too expensive, cheaper alternative | #8b5cf6 (purple) |
| **Internal Solution** | Built or chose internal tool, went with in-house solution | #06b6d4 (cyan) |
| **Champion Left** | Sponsor departed during cycle, champion changed roles, reorg | #ec4899 (pink) |
| **Bad Fit / Not ICP** | Shouldn't have been in pipeline, wrong segment, not ideal customer | #84cc16 (lime) |

### Mapping rules:
- **Named competitor in Details** (e.g., "chose Outreach", "went with Salesloft") = Competitor Won
- **"No response"** or **"went dark"** or **"ghosted"** = No Decision / Went Dark
- **"Budget"** or **"timing"** or **"next year"** or **"freeze"** = Budget / Timing
- **"Feature"** or **"missing"** or **"doesn't support"** = Product Gaps
- **"Price"** or **"expensive"** or **"cost"** in Details = Pricing Objection
- **"Internal"** or **"built their own"** or **"in-house"** = Internal Solution
- **"Champion left"** or **"sponsor"** or **"reorg"** = Champion Left
- **Record type mismatch** or **"not ICP"** or **"bad fit"** = Bad Fit / Not ICP
- If Win/Loss Details mention multiple factors, assign to the primary driver

### When to create new themes:
- If 3+ deals share a pattern not covered above (e.g., "Security/Compliance", "Integration Gap", "Evaluation Fatigue")
- Always keep total themes to 8 or fewer for chart readability

---

## SVG Pie Chart Specifications

The pie chart is an inline SVG (no JavaScript dependencies). Requirements:

- **Viewbox:** `0 0 420 420`
- **Radius:** 160px, centered at (210, 210)
- **Title:** "{Period} Closed Lost — Share of ${total} ARR Lost"
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

For each Closed Lost deal, the report runs three data pulls:

### 1. Amplitude Product-Usage Read (Trial Validation)
- **Lookback:** 6 months prior to close date (did they trial the product? what features did they try?)
- **Metrics per month:** MAU, Sequence Activations, Sequence Emails Sent, Template Emails, Calendar Meetings, Email Tracking Views, 3rd-Party Integrations
- **Classify usage:** Heavy (>100 MAU or deep multi-feature), Moderate (10-100 MAU), Light (<10 MAU), Silent (0 MAU — never trialed or stopped early)
- **Identify trend:** Ramping Up, Stable, Declining, Never Activated
- **Key question:** Did they actually try the product, and if so, what did their usage pattern look like before they decided to walk away?

### 2. Mixmax Meeting Transcript Search
- **Search by:** account name in meeting titles AND attendee domain in events
- **Extract:** meeting date, attendees, classification, key themes, objections raised, competitive mentions, red flags
- **Build narrative:** connect meeting progression to loss outcome — what happened, where did it go wrong, what signals were missed?

### 3. Preventability Verdict
Based on deal data + meeting intelligence + usage validation:
- **Not Preventable:** Budget freeze, M&A, company went dark with no prior signals, genuinely bad fit
- **Possibly Preventable:** Competitor won but product gaps were cited (could we have addressed them?), champion left (could we have multi-threaded?), pricing objection (could we have offered alternatives?)
- **Preventable:** No decision after strong engagement (follow-up failure), product trial failure not addressed (support gap), objections raised in meetings but never resolved, deal stalled at stage with no action plan

### 4. "What to Fix" Lesson
Based on all evidence, one specific, actionable lesson from this loss:
- What process gap led to this loss?
- What competitive response is needed?
- What product gap was cited?
- What could the rep or team have done differently?

---

## Competitive Intelligence Protocol

For deals lost to named competitors:
- Track which competitor won each deal
- Calculate win rate vs each competitor (requires Closed Won data for comparison)
- Identify patterns: what do we lose to [Competitor X] on? (features, pricing, brand, existing relationship)
- Note competitive battlecard gaps
- Track frequency: which competitors appear most often in losses?

---

## Output File Conventions

```
Revenue Reviews/Closed Lost Analysis/{Period}_Closed_Lost_Analysis.html

Examples:
  Q1_2026_Closed_Lost_Analysis.html
  March_2026_Closed_Lost_Analysis.html
  Q2_2026_Closed_Lost_Analysis.html
```

GitHub Pages path: `closed-lost/{filename}`
Full URL: `${GITHUB_PAGES_URL}/closed-lost/{filename}`

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
| Amplitude returns no data for a domain | Try alternate domains (e.g., `attentivemobile.com` vs `attentive.com`). Check Amplitude `get_users` with domain filter. Some lost deals may never have trialed — that's valid data (Silent classification). |
| Meeting search returns zero results | Check if sales used non-Mixmax meeting tools. Try broader search terms. Some early-stage losses may have no meetings recorded. |
| Pie chart slices don't add up to 360 degrees | Ensure percentages sum to 100% before converting to degrees. Use `percentage * 3.6` for degree conversion. |
| Amount totals don't match sheet | Verify Column M values. Some deals may have $0 Amount (unqualified, early stage). |
| Record Type filter misses deals | Check for variant record type names — filter on "Closed Lost" stage, not record type. |
| No Win/Loss Reason populated | Flag these deals — they need rep follow-up. Categorize as "Reason Not Captured" and note in recommendations. |
| Competitor name inconsistencies | Normalize competitor names (e.g., "Outreach" vs "Outreach.io" vs "outreach"). Build a dedup mapping. |
