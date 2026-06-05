---
name: revenue-reporting
description: >-
  Ground truth for analyzing and narrating Mixmax revenue from the Weekly RevOps Report (Gen 1) Google Sheet. Use for any weekly, monthly, or quarterly revenue wrap-up, pacing forecast, pipeline review, bookings or ARR analysis, revenue position / variance analysis, CS or renewals review, or rep performance callout. Trigger on 'weekly revenue wrap-up', 'monthly revenue report', 'quarterly wrap-up', 'how are we pacing', MTD, EOM forecast, revenue position, revenue variance, Total ARR, Direct Sales ARR, Self-Serve ARR, Net ARR Contribution, DS vs SS breakdown, renewals review, 'how are reps doing', 'run the weekly/monthly/quarterly report', or any mention of Mixmax ARR, NRR, GRR, SCS, SQL, SQO, MQL, PQL, OQL, bookings, or channel performance (Inbound, Outbound, Product, Expansion). Also trigger on the Weekly RevOps Report sheet, Gen 1, or any summary tab (Revenue Summary, Bookings Summary, Rep Summary, CS Summary). Authoritative for Mixmax metric definitions, sheet schema, reporting rules, and variance flagging.
---

# Revenue Reporting

You are the ground truth for Mixmax revenue analysis. This skill exists because
revenue reporting is where hallucinations cost the most — a confidently wrong
number in a wrap-up erodes trust in every future report. Your job is to make
accuracy automatic.

This skill consolidates the former `mixmax-revenue-reporting` (sheet schema,
metric definitions, reporting rules, extraction protocol, cadences) and
`revenue-analysis` (ARR position, DS/SS variance decomposition, EOM pacing,
variance flagging) into one canonical skill.

When this skill triggers, you are working from the **Weekly RevOps Report Google
Sheet** ("Gen 1"). This is the only authoritative source. Everything else is
reference material.

---

## The accuracy contract

Before you narrate a single number, internalize these five rules. They are
non-negotiable because they are where most revenue-reporting hallucinations
originate.

1. **Every number must trace to a specific cell.** If you cannot point to a tab and a row, do not report the number. Say "data unavailable" instead of guessing. In detailed analysis, include cell references (e.g., "B12: $2.5M Current Total ARR").

2. **Period verification runs first, always.** Every summary tab has an "As of" date and a "For the Month of" / "For the Period of" date. Read them. Echo them at the top of every output. If they don't match what the user asked for, stop and flag it. Do not analyze.

3. **Read pre-calculated forecasts — never invent new ones.** The sheet already computes EOM Forecast, Projected vs Target, and Projected % to Target. Use those cells. Never run your own pacing math on top of them.

4. **Never narrate error cells.** `#DIV/0!`, `#REF!`, `Error`, `#N/A`, `#VALUE!` — skip them silently or note "data unavailable." Never include them verbatim.

5. **Monthly and quarterly periods never mix in the same section.** Analyzing a month → Monthly tabs only. Analyzing a quarter → Quarterly tabs only. Crossing streams produces wrong numbers that look right.

---

## Canonical extraction & reconciliation protocol (v2 — 2026-04-14)

The five rules above define *accuracy intent*. The ten rules below define the
*mechanics* that make accuracy deterministic.

1. **Canonical extractor: openpyxl over the XLSX, never the natural-language renderer.** When snapshots exist, pull via `download_file_content` (Drive MCP, MIME `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) and parse with `openpyxl`. Do **not** use `read_file_content` — it silently drops rows, merges cells, reformats numbers. Fall back to gviz CSV only when the snapshot is unavailable.

2. **Manifest reconciliation gate (Step 2.5 — hard stop).** Every snapshot has a `Manifest` tab declaring expected row counts. Compare `ws.max_row` (adjusted for header) against the Manifest per tab. Any mismatch >1 row is **fail-loud** — abort and surface the delta.

3. **Period verification is a fail-closed guard, not advisory.** If the sheet's period doesn't match the requested period, halt — do not fall through with a warning.

4. **Contract-based cell extraction.** Every summary-tab metric is fetched through a named extractor bound to an explicit `(tab, row, column)` coordinate. Extractors return `None` on empty/error cells; narrative code prints `—` or "data unavailable", never the error glyph.

5. **Header-row auto-detection for raw-data tabs.** AE Forecast, Renewals, Prospect Accounts, SQLs lack a stable header row. Scan rows 1–3 for an anchor string (e.g., `"Account Name"`, `"Opportunity Name"`). Hard-coded `row=1` reads are banned.

6. **Empty-row filtering by required-field presence.** `ws.max_row` is unreliable on sparse tabs. After header detection, keep only rows where a required field is non-empty. That is the canonical row count.

7. **Pre-publish QA gate via `accuracy-reconciliation`.** Before any publish (GitHub push, Notion create, Slack draft), run the weekly/monthly/quarterly `accuracy-reconciliation` skill. A failed reconciliation blocks publish.

8. **Deterministic Top 10 account selector.** Stable sort, no LLM re-ranking. Filter `GTM Stage ∈ {Engaged, New}`, then sort: (1) Aero Blended Score desc, (2) # Open Opps asc, (3) days_since_last_activity asc. Cap 3 per channel.

9. **Drive connector primary; Chrome MCP gviz as documented fallback.** Primary: Drive MCP `download_file_content` on the snapshot XLSX. Fallback: Chrome MCP `javascript_tool` → `fetch` the gviz CSV per tab GID. The fallback is documented (GID map below), not improvised, and triggers a note in the report preamble.

10. **Stable skill invocation — no absolute session paths in scheduled tasks.** Invoke skills by name (`Use the Skill tool with name="revenue-reporting"`). Never embed session-scoped paths like `/sessions/{id}/...` — they go stale. All path references must be workspace- or home-relative.

---

## How to use this skill

Large by design — load the sections you need.

**Always load first:** this SKILL.md and `references/sheet_schema.md` (tabs, contents, which rows hold which metrics).

**Load for specific tasks:**
- Terminology in any wrap-up (ARR, NRR, GRR, SCS, SQL, SQO, coverage…) → `references/metric_definitions.md`
- "Always report" / "flag only" logic → `references/reporting_rules.md`
- Investigating *why* a flagged issue exists → `references/drill_down_map.md`
- Producing output → `references/output_conventions.md`
- Always skim before output → `references/hallucination_traps.md`

A good weekly pattern: SKILL.md → sheet_schema → metric_definitions → reporting_rules → output_conventions → hallucination_traps, plus drill_down_map only when investigating.

---

## The sheet at a glance

**Summary tabs (read for reporting):** Monthly Revenue Summary, Quarterly Revenue Summary, Monthly Bookings Summary, Quarterly Bookings Summary, Rep Summary, CS Summary.

**Raw data tabs (drill-down only):** Rev Ops AE Forecast - This Year, Renewals - This Year, Total Prospect Account Engaged - Year, Rev Ops - SQLs - This Year, Looker Net New DS, DS - Primary, Total ARR (Stripe), Looker Net New SS.

For routine reporting, stay in the summary tabs.

### GID reference (gviz CSV export)

| Tab | GID |
|---|---|
| Monthly Revenue Summary | 586801175 |
| Quarterly Revenue Summary | 2066645768 |
| Monthly Bookings Summary | 1201655554 |
| Quarterly Bookings Summary | 1160215217 |
| Rep Summary | 1461552329 |
| CS Summary | 1594569652 |

Template gviz URL:
```
https://docs.google.com/spreadsheets/d/1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY/gviz/tq?tqx=out:csv&gid={GID}
```
Use JavaScript fetch via Chrome MCP's `javascript_tool`; store in `window.__` variables and retrieve in chunks via `.substring()` if truncated.

---

## The period-verification protocol

First thing in any task. Every time.

1. Open the sheet (or snapshot XLSX).
2. Read "As of" and "For the Month of" / "For the Period of" from the relevant summary tab(s) (exact cells in `references/sheet_schema.md`).
3. Echo at the top of your output:
   > **As of:** [date] · **Period covered:** [period] · **Cadence:** [Weekly | Monthly | Quarterly] · **Audience:** [All GTM | All Company | Internal + Board]
4. If the period doesn't match the request — stop. Tell the user the sheet is set to [X] but they asked for [Y].
5. If "As of" is >3 business days old, flag staleness.

---

## Key revenue metrics (revenue-position analysis)

### Total ARR (top-level)
Current, Target, Variance ($ and %), % to Target.

### Direct Sales (DS) channel
Current, Target, Variance, % to Target, plus the **4-component breakdown**: Net New Business, Expansion, Downgrade, Churn (each Current / Target / Variance).

### Self-Serve (SS) channel
Current, Target, Variance, % to Target, plus the **7-component breakdown**: Net New SS, Reactivation, Upgrade, Seat Expansion, Seat Contraction, Downgrade, Churn (each Current / Target / Variance).

### Net ARR Contribution
Current (closed to date), Target, Forecast, Projected vs Target.

### EOM Forecast & pacing
EOM Forecast and Projected % to Target — ALWAYS read from the sheet, never calculate. Monthly / quarterly / YTD pacing as relevant.

---

## The three core definitions (never blur these)

- **Target** = the company's committed number for the period (set by leadership). The goal.
- **Forecast** = what the team is committing to based on current visibility (rep roll-ups + CS forecast). The commitment.
- **Current** = what has actually closed / is in the system as of the As-Of date. The reality.

"We're at $X" is ambiguous — always specify which of the three.

---

## Revenue-position analysis framework (five steps)

1. **Headline.** Lead with Total ARR vs target — above, below, or on target.
2. **Breakdown by channel.** DS vs SS — which is driving the gap (or surplus)?
3. **Drill into driver.** For the channel with the biggest variance, analyze the specific sub-channel breakdown (e.g., DS Churn vs New Business, SS Upgrade vs Reactivation).
4. **Forecast comparison.** Current vs Forecast vs Target — are we tracking to close the gap by EOM?
5. **Forward outlook.** What does EOM Forecast say about where we land? Quantify projected variance at close.

### Variance flagging rule
- Flag any metric where variance exceeds **10% of target**.
- Color code: **red** for >10% gap, **yellow** for 5-10%, **green** for on/above target.

---

## The three cadences

### Weekly — audience All GTM
Live pacing check mid-month, tactical. Reads the live sheet (no snapshot). Tone: direct, candid, action-oriented. Periods: Monthly Revenue + Monthly Bookings (current month MTD).

### Monthly — audience All Company
Closed-period retrospective. Reads the monthly XLSX snapshot created *before* analysis. Tone: accessible, contextual. Periods: Monthly Revenue + Monthly Bookings (last completed month). Snapshot path: `~/Library/Mobile Documents/com~apple~CloudDocs/Anthropic/Revenue Reviews/Monthly Snapshots/`.

### Quarterly — audience Internal + Board
Strategic review. Reads the quarterly XLSX snapshot created *before* analysis. Tone: formal, board-ready. Periods: Quarterly Revenue + Quarterly Bookings (last completed quarter). Snapshot path: same folder, Q-prefixed filenames.

Which `reporting_rules.md` rules apply to which cadence is specified in each Cowork prompt, not here. This skill is cadence-agnostic.

---

## Post-snapshot reset process (Monthly)

After a Monthly wrap-up (snapshot taken, charts generated, HTML built), reset the sheet forward and capture incoming targets. Not optional.

1. **Switch all 4 summary tabs to the new month** via the data-validation dropdowns:
   - Monthly Revenue Summary — single dropdown near "For the Month of"
   - Monthly Bookings Summary — single dropdown in the header row
   - Rep Summary — two dropdowns (start + end); set both to the 1st of the new month
   - CS Summary — two dropdowns (E3 and F3); set both to the 1st of the new month
   Use Chrome MCP `find` to locate the combobox by cell reference, click to open, screenshot the list, click the target month, verify by screenshot.
2. **Capture new-month targets** via gviz CSV and save to markdown:
   - Monthly Revenue Summary — *contribution* targets (not Total ARR targets): Total Net ARR, Total Net DS Contribution, Total Self-Serve ARR Contribution; DS breakdown (Net New Business, Expansion, Downgrade budget, Churn budget); SS breakdown (Net New SS, Reactivation, Upgrade, Seat Expansion, Seat Contraction, Downgrade, Churn)
   - Monthly Bookings Summary — Bookings targets (Total, New Business, Expansion); Pipeline targets by channel (Total, Inbound, Outbound, Product, Expansion); Activity targets (Accounts Engaged, Meetings Booked, SQLs, SQOs)
   - CS Summary — NRR/GRR by segment (All / CSM Owned / VSB Owned): # Accounts, At Risk, Forecasted ARR, NRR %, GRR % (ARR Retention), GRR % (Client Retention); Renewals Summary (Previous Contract, Current ARR, Forecasted ARR, ARR Impact $, NRR Target)
3. **Save targets file** to `Monthly Report/[Month]_[Year]_Targets.md`.
4. **Verify** with a screenshot of each tab (no `$0` / `#DIV/0!` in key cells).

---

## Account GTM Stage & Status definitions

GTM Stage (from Total Prospect Account Engaged tab): New, Engaged (AE activity last 14 days), Cold (no AE activity last 14 days), Nurture, Disqualified.

Account Status (Salesforce, finer grain): New, Qualified, Attempting Contact, Disqualified / 1. Bad company fit, Disqualified / 2. SPAM, Nurture / 1. Too small (SS), Nurture / 3. Product gaps, Nurture / 7. No Interest.

Account links: `https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view` (IDs appear in Rep Summary, AE Forecast, Renewals, Total Prospect Account Engaged).

---

## Revenue narrative & HTML output

### Narrative guidelines
- **Headline first.** On/above: "We are on track to hit our revenue target. Total ARR is $X (Y% to target)." Below: "We are tracking below our monthly target by $X (Z% gap)."
- **Quantify** gaps in both dollars and percentages.
- **Attribute** to specific channels/sub-channels ("shortfall driven by DS Churn ($300K) and lower SS Net New ($150K)").
- **Forward-looking:** lead with Current then pivot to Forecast and EOM.
- **Tone by audience:** Weekly (GTM) — blunt, action-oriented. Monthly (company-wide) — accessible, context for non-GTM readers.

### HTML formatting
- Currency `$X,XXX`; percentages with 1 decimal.
- Color coding: **Green** `#00AA00` on/above target; **Yellow** `#FFCC00` watch zone (5-10% below); **Red** `#CC0000` >10% gap.
- Standard variance table:

| Metric | Current | Target | Variance ($) | Variance (%) |
|--------|---------|--------|--------------|--------------|
| Total ARR | $2,500K | $2,750K | -$250K | -9.1% |
| DS ARR | $1,500K | $1,750K | -$250K | -14.3% |
| SS ARR | $1,000K | $1,000K | $0K | 0.0% |

Color-code the Variance columns by the thresholds above. Lead with a 2-3 sentence narrative, follow with the table, include a forward-looking Forecast/EOM statement, close with action recommendations if variance exceeds thresholds.

### Sample opening paragraphs (illustrative, not templates)

**Weekly (All GTM):**
> **Week of April 6, 2026 — mid-month pacing check.** We're 7 working days into April with 15 to go. Bookings are at $17.9K against a $165K target — light, but the team forecasts $125K by EOM, which would close us to 76% of target. The gap is a New Business story: $0 booked so far, $156K remaining. Pipeline to close sits at $127K ($101K New Business, $26K Expansion). 64% of open pipeline is stuck in Scoping/Demo — focus pull-forward conversations there this week.

**Monthly (All Company):**
> **March 2026 Revenue Wrap-Up.** March closed $439K below our Total ARR target of $8.94M, landing at $8.50M — a 4.9% gap driven almost entirely by Direct Sales (9.2% under plan). Self-Serve held the line (+0.6%). The story is churn: $273K in DS churn against an $85K target. On the bright side, Expansion Bookings came in nearly 2x target and reactivations added $58K we hadn't forecasted.

**Quarterly (Internal + Board):**
> **Q1 2026 Revenue Performance Review.** Q1 closed at Total ARR $8.50M against $8.94M, a $440K (4.9%) shortfall concentrated in Direct Sales ($4.54M vs $5.00M, −9.2%); Self-Serve delivered $3.96M vs $3.93M (+0.6%). Three drivers: New Business at 48% of target, Churn 19.9% above plan, Downgrades 7.5% above plan. Offsetting: Expansion at 180% of target, SS Reactivation at 141%.

---

## When something isn't covered

If asked to report on something not in the summary tabs and not obviously in a raw tab, do **not** invent a source:

> "I don't see [X] in the Weekly RevOps Report Gen 1 sheet. The closest related data is [Y]. Want me to report on that instead, or point me to where [X] lives?"

It is always better to ask than to fabricate.

---

## Scope boundaries

**Covers:** revenue position (Total ARR, DS ARR, SS ARR), channel-level variance, Forecast vs Current vs Target, EOM forecast and pacing, variance flagging; plus the full Gen 1 sheet schema, metric definitions, reporting rules, and cadence mechanics.

**Other skills handle:** pipeline creation & account strategy → `pipeline-intelligence`; deal management & velocity → `deal-intelligence`; renewals & retention → `renewals-management`; product metrics & activation → `amplitude-analyst` / `amplitude-guide`; pre-publish QA → `accuracy-reconciliation`.

---

## A note on iteration

When this skill gets something wrong, tell the user which ref file is wrong and what the correction is, so the next iteration improves.
