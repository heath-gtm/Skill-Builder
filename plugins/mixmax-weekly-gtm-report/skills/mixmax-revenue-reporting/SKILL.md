---
name: mixmax-revenue-reporting
description: >
  Ground truth for analyzing and narrating Mixmax revenue from the Weekly RevOps Report
  (Gen 1) Google Sheet. Always use this skill for any weekly, monthly, or quarterly
  revenue wrap-up, pacing forecast, pipeline review, bookings or ARR analysis, Customer
  Success or renewals review, or rep performance callout. Trigger on phrases like
  "weekly revenue wrap-up", "monthly revenue report", "quarterly wrap-up", "how are we
  pacing", "MTD", "pipeline review", "renewals review", "how are reps doing", "run the
  weekly/monthly/quarterly report", or any mention of Mixmax ARR, NRR, GRR, SCS, SQL,
  SQO, MQL, PQL, OQL, bookings, or channel performance (Inbound, Outbound, Product,
  Expansion). Also trigger when the user references the Weekly RevOps Report sheet, Gen
  1, or any summary tab (Monthly/Quarterly Revenue Summary, Monthly/Quarterly Bookings
  Summary, Rep Summary, CS Summary). Authoritative source for Mixmax metric definitions,
  sheet schema, reporting rules, drill-down logic, and output formatting.
---

# Mixmax Revenue Reporting

You are the ground truth for Mixmax revenue analysis. This skill exists because revenue reporting is where hallucinations cost the most — a confidently wrong number in a wrap-up erodes trust in every future report. Your job is to make accuracy automatic.

When this skill triggers, you are working from the **Weekly RevOps Report Google Sheet** ("Gen 1"). This is the only authoritative source. Everything else is reference material.

---

## The accuracy contract

Before you narrate a single number, internalize these five rules. They are non-negotiable because they are where most revenue-reporting hallucinations originate.

1. **Every number must trace to a specific cell.** If you cannot point to a tab and a row, do not report the number. Say "data unavailable" instead of guessing.

2. **Period verification runs first, always.** Every summary tab has an "As of" date and a "For the Month of" / "For the Period of" date. Read them. Echo them at the top of every output. If they don't match what the user is asking for (e.g., they asked for April but the period is set to March), stop and flag it. Do not analyze.

3. **Read pre-calculated forecasts — never invent new ones.** The sheet already computes EOM Forecast, Projected vs Target, and Projected % to Target. Use those cells. Do not run your own pacing math on top of them.

4. **Never narrate error cells.** `#DIV/0!`, `#REF!`, `Error`, `#N/A`, `#VALUE!` — skip them silently or note "data unavailable for this metric." Never include them verbatim in the output.

5. **Monthly and quarterly periods never mix in the same section.** If you're analyzing a month, read from Monthly tabs only. If you're analyzing a quarter, read from Quarterly tabs only. Crossing streams produces wrong numbers that look right.

---

---

## Canonical extraction & reconciliation protocol (v2 — 2026-04-14)

The five rules above define *accuracy intent*. The ten rules below define the *mechanics* that make accuracy deterministic rather than aspirational. These were codified after the April 14, 2026 weekly run, where ad-hoc extraction produced reconciliation gaps that had to be caught by spot-check instead of by the pipeline itself.

### 1. Canonical extractor: openpyxl over the XLSX, never the natural-language renderer

When snapshots exist, always pull data via `download_file_content` (Drive MCP, MIME `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`) and parse with `openpyxl`. Do **not** use `read_file_content` — its natural-language rendering silently drops rows, merges cells, and reformats numbers. Only fall back to gviz CSV (Chrome MCP `javascript_tool` + `/gviz/tq?tqx=out:csv&gid={gid}`) when the snapshot is unavailable.

### 2. Manifest reconciliation gate (Step 2.5 — hard stop)

Every snapshot has a `Manifest` tab that declares expected row counts per data tab. After loading the workbook, compare `ws.max_row` (adjusted for header) against the Manifest count for each tab you intend to read. Any mismatch >1 row is a **fail-loud** condition — abort the run and surface the delta in the report. Do not proceed to analysis on a workbook that doesn't reconcile against its own Manifest.

### 3. Period verification is a fail-closed guard, not advisory

The period-verification protocol above is not "flag and continue" — it is "abort and surface." If the sheet's `For the Month of` / `For the Period of` does not match the user's requested period, halt. Do not fall through to analysis with a warning.

### 4. Contract-based cell extraction

Every summary-tab metric must be fetched through a named extractor bound to an explicit `(tab, row, column)` coordinate. Extractors return `None` on empty cells and on any error value (`#DIV/0!`, `#REF!`, `#N/A`, `#VALUE!`, `Error`). Downstream narrative code checks for `None` and prints `—` or "data unavailable" — it never prints the error glyph.

### 5. Header-row auto-detection for raw-data tabs

AE Forecast, Renewals, Prospect Accounts, and SQLs do not have a stable header row. Scan rows 1–3 for an anchor header string (e.g., `"Account Name"` for Prospect Accounts, `"Opportunity Name"` for AE Forecast). Bind all downstream column indices off the detected header row. Hard-coded `row=1` reads are banned.

### 6. Empty-row filtering by required-field presence

`ws.max_row` is unreliable on sparse tabs (Renewals in particular trails deleted rows). After header detection, iterate from `header_row + 1` to `ws.max_row`, and keep only rows where a required field (e.g., `Account Name` for accounts, `Opportunity Name` for deals) is non-empty. This is the canonical row count for analysis — not `ws.max_row`.

### 7. Pre-publish QA gate via `accuracy-reconciliation`

Before any publish action (GitHub push, Notion create, Slack draft), run the weekly/monthly/quarterly `accuracy-reconciliation` skill. It performs the cross-artifact spot-check: weekly vs live sheet, monthly vs the three weeklies of the month, quarterly vs the three monthlies. A failed reconciliation blocks publish.

### 8. Deterministic Top 10 account selector

Top 10 accounts are selected by a stable sort — no LLM re-ranking. Filter to `GTM Stage ∈ {Engaged, New}`, then sort:
1. `Aero Blended Score` descending
2. `# Open Opps` ascending (fewer open opps = higher priority)
3. `days_since_last_activity` ascending (more recent = higher priority)

Cap at 3 per channel to prevent single-channel dominance. This selector is deterministic — two runs against the same snapshot produce the same Top 10.

### 9. Drive connector primary; Chrome MCP gviz as documented fallback

Primary data path: Drive MCP `download_file_content` on the snapshot XLSX. Fallback path (if snapshot missing or corrupt): Chrome MCP `javascript_tool` → `fetch` against the gviz CSV endpoint per tab GID. The fallback is **documented**, not improvised — the tab-to-GID map lives in this skill, and any fallback triggers a note in the report preamble.

### 10. Stable skill invocation — no absolute session paths in scheduled tasks

Scheduled-task prompts and skill cross-references invoke skills **by name** (`Use the Skill tool with name="mixmax-revenue-reporting"`). They do **not** embed session-scoped absolute paths like `/sessions/{id}/mnt/.claude/skills/...` — those paths go stale between sessions and silently break the task. All path references in scheduled tasks must be workspace-relative or user-home-relative.

---


## How to use this skill

This skill is large by design. Reading the whole thing every time would be wasteful. Instead, load the sections you need for the task at hand.

### Always load first
- **This SKILL.md** — you're reading it now. Sets the rules and the map.
- **`references/sheet_schema.md`** — tells you exactly which tabs exist, what they contain, and which rows hold which metrics. Load this before reading any data.

### Load for specific tasks

- **For any wrap-up or analysis that uses terminology** (ARR, NRR, GRR, SCS, SQL, SQO, pipeline coverage, etc.) → load **`references/metric_definitions.md`**. Contains Mixmax-specific definitions, exact cell references, worked calculation examples, and edge cases. ~500 words per top metric.

- **For any wrap-up that applies "always report" / "flag only" logic** → load **`references/reporting_rules.md`**. Contains the thresholds and decision rules for Rep Summary, CS Summary, stage concentration, SCS scoring, and rep outlier detection.

- **When you need to investigate *why* a flagged issue exists** (e.g., an SCS-low deal, a stuck-in-stage pipeline, a churning account) → load **`references/drill_down_map.md`**. Contains the decision tree for which raw-data tab to read for which investigation, and exactly which fields to pull.

- **When producing output** (any wrap-up, Notion post, or narrative) → load **`references/output_conventions.md`**. Contains number formatting rules, Notion markdown conventions, tone guidance per audience, and the three sample opening paragraphs (GTM / Company / Board).

- **Always skim before producing output** → load **`references/hallucination_traps.md`**. Short file listing the specific failure modes observed in Mixmax revenue reporting and how to avoid them. Worth re-reading every run.

### A good loading pattern

For a typical weekly wrap-up, you'd load:
1. SKILL.md (this file)
2. sheet_schema.md
3. metric_definitions.md
4. reporting_rules.md
5. output_conventions.md
6. hallucination_traps.md

And then `drill_down_map.md` only if flagged issues need investigation.

---

## The sheet at a glance

The Weekly RevOps Report Google Sheet has two kinds of tabs:

**Summary tabs (read these for reporting):**
- 📊 Monthly Revenue Summary
- 📊 Quarterly Revenue Summary
- 📞 Monthly Bookings Summary
- 📞 Quarterly Bookings Summary
- 🤑 Rep Summary
- 🤝 CS Summary

**Raw data tabs (read these only for drill-down investigation):**
- Rev Ops AE Forecast - This Year — deals AEs are managing
- Renewals - This Year — all CS renewals
- Total Prospect Account Engaged - Year — all prospect accounts with GTM stage, channel source, account status, Aero fit scores, prospecting notes, and website. Key tab for account-level pipeline analysis and prioritization.
- Rev Ops - SQLs - This Year — all opportunities created this year
- Looker Net New DS — Direct Sales Net New ARR breakdown
- DS - Primary — main Direct Sales and Self Serve revenue information
- Total ARR (Stripe) — total ARR
- Looker Net New SS — Self Serve Net New ARR breakdowns

For routine reporting, stay in the summary tabs. The raw tabs are for investigating specific flagged issues, not for re-deriving numbers the summary tabs already provide.

---

## Account GTM Stage Definitions

These stages describe where a prospect account sits in the GTM motion. They come from the "Total Prospect Account Engaged - Year" tab and are used for pipeline creation analysis and account prioritization.

- **New** — New account, not yet worked by an AE
- **Engaged** — AE activity in the last 14 days
- **Cold** — No AE activity in the last 14 days (needs re-engagement)
- **Nurture** — In nurture cycle, not actively worked
- **Disqualified** — Disqualified from the pipeline

## Account Status Definitions

These are the Salesforce account statuses. They provide finer-grained detail than GTM Stage and are used for drill-down analysis.

- **New** — New account
- **Qualified** — Qualified account, ready to work
- **Attempting Contact** — Trying to contact
- **Disqualified / 1. Bad company fit** — Does not fit ICP
- **Disqualified / 2. SPAM** — Spam account
- **Nurture / 1. Too small (SS)** — Too small for Direct Sales, route to Self-Serve
- **Nurture / 3. Product gaps** — Product doesn't meet their needs currently
- **Nurture / 7. No Interest** — No interest at this time

## Salesforce Account Links

When referencing any account in reports or analysis, always link to its Salesforce record. The URL format is:

`https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view`

Where `{AccountID}` is the Salesforce Account ID (e.g., `0011R00002uXwEKQA0`). Account IDs appear in the Rep Summary (Deals by Forecast Category section), AE Forecast, Renewals, and Total Prospect Account Engaged tabs.

Full schema — including row numbers, column meanings, and edge cases — lives in `references/sheet_schema.md`.

---

## The three cadences

You will see this skill invoked for three reporting cadences. Each is a separate Cowork with its own prompt, but all three share the same underlying rules from this skill.

### Weekly — audience is All GTM
- Purpose: live pacing check mid-month, tactical
- Reads: live sheet, no snapshot
- Tone: direct, candid, action-oriented
- Periods: Monthly Revenue Summary + Monthly Bookings Summary (current month MTD)

### Monthly — audience is All Company
- Purpose: closed-period retrospective of the month just completed
- Reads: monthly XLSX snapshot created by the Cowork *before* analysis
- Tone: accessible, contextual, connects the dots
- Periods: Monthly Revenue Summary + Monthly Bookings Summary (last completed month)
- Snapshot path: `~/Library/Mobile Documents/com~apple~CloudDocs/Anthropic/Revenue Reviews/Monthly Snapshots/`

### Quarterly — audience is Internal + Board
- Purpose: strategic review of the quarter just completed
- Reads: quarterly XLSX snapshot created by the Cowork *before* analysis
- Tone: formal, strategic, board-ready
- Periods: Quarterly Revenue Summary + Quarterly Bookings Summary (last completed quarter)
- Snapshot path: `~/Library/Mobile Documents/com~apple~CloudDocs/Anthropic/Revenue Reviews/Monthly Snapshots/` (quarterly files can live alongside monthly with Q-prefixed filenames)

Which rules from `reporting_rules.md` apply to which cadence is specified in each Cowork prompt, not in this skill. This skill is cadence-agnostic.

---

## Post-snapshot reset process (Monthly)

After completing a Monthly wrap-up (snapshot taken, charts generated, HTML report built), reset the sheet forward to the new month and capture incoming targets. This is a standard final step in the Monthly cadence — not optional. It ensures the sheet is ready for live weekly pacing and that the new month's targets are recorded before anyone changes them.

### When to run

Immediately after the Monthly wrap-up report is finalized and the XLSX snapshot is saved. Do not skip this step.

### Steps

1. **Switch all 4 summary tabs to the new month.** Each tab has data-validation dropdowns that control the reporting period. Change them from the just-completed month to the current (new) month:
   - 📊 Monthly Revenue Summary — single dropdown in the header row (near "For the Month of")
   - 📞 Monthly Bookings Summary — single dropdown in the header row
   - 🤑 Rep Summary — two dropdowns (start date and end date); set both to the 1st of the new month
   - 🤝 CS Summary — two dropdowns (E3 and F3); set both to the 1st of the new month

   **How to change dropdowns:** Use Chrome MCP's `find` tool to locate the data validation combobox by cell reference (e.g., "data validation dropdown in cell E3"), then click the ref to open it. Take a screenshot to see the month list, then click the target month. Verify with a screenshot that the value changed and data populated.

2. **Capture new-month targets.** Once all tabs are switched, extract the following targets via the gviz CSV endpoint (`/gviz/tq?tqx=out:csv&gid={gid}`) and save them to a markdown file:

   **From Monthly Revenue Summary — capture *contribution* targets, not Total ARR targets:**
   - Net ARR Contribution targets: Total Net ARR, Total Net DS Contribution, Total Self-Serve ARR Contribution
   - DS Channel breakdown targets: Net New Business, Expansion, Downgrade (budget), Churn (budget)
   - Self-Serve breakdown targets: Net New SS, Reactivation, Upgrade, Seat Expansion, Seat Contraction, Downgrade, Churn

   **From Monthly Bookings Summary — capture target vs forecast:**
   - Bookings targets: Total Bookings, New Business Bookings, Expansion Bookings
   - Pipeline targets by channel: Total, Inbound, Outbound, Product, Expansion
   - Activity targets: Accounts Engaged, Meetings Booked, SQLs, SQOs

   **From CS Summary — capture NRR/GRR by segment:**
   - Renewals Overview for All / CSM Owned / VSB Owned: # Accounts, At Risk, Forecasted ARR, NRR %, GRR % (ARR Retention), GRR % (Client Retention)
   - Renewals Summary: Previous Contract, Current ARR, Forecasted ARR, ARR Impact ($), NRR Target

3. **Save targets file.** Write to: `Monthly Report/[Month]_[Year]_Targets.md` (e.g., `Monthly Report/April_2026_Targets.md`)

4. **Verify.** Take a final screenshot of each tab to confirm dropdowns are set to the new month and data has populated (no `$0` or `#DIV/0!` in key cells that should have values).

### GID reference for gviz CSV export

| Tab | GID |
|---|---|
| Monthly Revenue Summary | 586801175 |
| Monthly Bookings Summary | 1201655554 |
| Rep Summary | 1461552329 |
| CS Summary | 1594569652 |

### Template gviz URL

```
https://docs.google.com/spreadsheets/d/1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY/gviz/tq?tqx=out:csv&gid={GID}
```

Use JavaScript fetch via Chrome MCP's `javascript_tool` to retrieve the CSV. Store in `window.__` variables and retrieve in chunks via `.substring()` if output is truncated (Google Sheets CSVs can exceed single-response limits).

---

## The period-verification protocol

This is the first thing you do in any Mixmax revenue task. Every time. No exceptions.

1. Open the sheet (or the snapshot XLSX).
2. Read the "As of" and "For the Month of" / "For the Period of" cells from the relevant summary tab(s). See `references/sheet_schema.md` for exact cell locations.
3. Echo them at the top of your output in this format:

   > **As of:** [date from sheet]
   > **Period covered:** [period from sheet]
   > **Cadence:** [Weekly | Monthly | Quarterly]
   > **Audience:** [All GTM | All Company | Internal + Board]

4. If the period does not match what the user is asking for — stop. Do not analyze. Tell the user: "The sheet's period is currently set to [X], but you asked for [Y]. Please update the period selector in the sheet and rerun, or confirm you want me to analyze [X] instead."

5. If the "As of" date is more than 3 business days old, flag it: "Heads up — the sheet was last updated on [date], which is [N] business days ago. Numbers may be stale."

This protocol alone prevents the single most common category of revenue-reporting error: analyzing the wrong period with complete confidence.

---

## Output framing — the three core definitions

These three definitions appear in nearly every wrap-up. Get them right every time:

- **Target** = the company's committed number for the period (set by leadership)
- **Forecast** = what the team is committing to based on current visibility (rep roll-ups + CS forecast)
- **Current Bookings / Current ARR / Current [metric]** = what has actually closed / is actually in the system *as of the As-Of date*

Never blur them. "We're at $X" is ambiguous — specify whether that's current, forecast, or target. The narrative should always make it obvious which of the three any number refers to.

---

## Sample opening paragraphs per audience

These are illustrative — not templates to copy verbatim. They show the tone and depth each audience expects. Full examples live in `references/output_conventions.md`.

### Weekly (All GTM)

> **Week of April 6, 2026 — mid-month pacing check.** We're 7 working days into April with 15 to go. Bookings are at $17.9K against a $165K target — light, but the team is forecasting $125K by EOM, which would close us to 76% of target. The gap is a New Business story: $0 booked so far, $156K remaining to land. Pipeline to close sits at $127K, with $101K in New Business and $26K in Expansion. 64% of open pipeline is stuck in Scoping/Demo, which is where we need to focus pull-forward conversations this week.

### Monthly (All Company)

> **March 2026 Revenue Wrap-Up.** March closed $439K below our Total ARR target of $8.94M, landing at $8.50M — a 4.9% gap driven almost entirely by Direct Sales, which came in 9.2% under plan. Self-Serve held the line, closing 0.6% above target. The story for March is churn: we lost $273K in Direct Sales churn against a $85K target, more than tripling the planned impact. On the bright side, Expansion Bookings came in nearly 2x target, and reactivations added $58K we hadn't forecasted. Here's what drove the numbers and what it means for April.

### Quarterly (Internal + Board)

> **Q1 2026 Revenue Performance Review.** Q1 closed with Total ARR of $8.50M against a $8.94M target, a $440K (4.9%) shortfall. The underperformance was concentrated in Direct Sales, which finished Q1 at $4.54M against a $5.00M target (−9.2%), while Self-Serve delivered $3.96M against a $3.93M target (+0.6%). Three factors drove the Direct Sales gap: New Business Bookings closed at 48% of target ($86K of $180K), Churn ran 19.9% above plan ($565K of $257K target), and Downgrades ran 7.5% above plan. Offsetting these: Expansion Contribution delivered 180% of target, and Self-Serve Reactivation came in at 141% of target. The following sections detail the drivers, the forecast implications for Q2, and the corrective actions underway.

---

## When something isn't covered

If a user asks you to report on something that isn't in the summary tabs and isn't obviously in one of the raw data tabs, do **not** invent a source. Tell them:

> "I don't see [X] in the Weekly RevOps Report Gen 1 sheet. The closest related data I can see is [Y]. Want me to report on that instead, or can you point me to where [X] lives?"

It is always better to ask than to fabricate.

---

## A note on iteration

This skill is v1. It will get things wrong. When it does, tell the user which ref file is wrong and what the correction is, so the next iteration improves. The user has explicitly agreed to treat the first 2–3 runs as a deliberate refinement pass.

---

## Product data cross-reference (Amplitude)

The Gen 1 sheet is the source of truth for **financial outcomes** (ARR, bookings, deals, renewals). It is **not** the source of truth for **product behavior** (signups, activation, feature adoption, usage velocity, aha-moment progression, PQL signals).

**Rule:** any time a report section touches Self-Serve revenue drivers, Product-channel pipeline, activation/aha-moment trends, PQLs, or feature-adoption claims, **invoke the `amplitude-guide` skill** to pull the live product data. Do not derive product behavior from financial aggregates alone.

Applies to all three cadences — Weekly, Monthly, Quarterly. The `amplitude-guide` skill knows which events are reliable, how to build funnels, and how to cross-check Amplitude output against the sheet.
