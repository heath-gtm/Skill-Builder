---
name: sales-leader-weekly-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting the
  Mixmax Sales Leader Weekly report. Use whenever the user asks "how do I
  run the Sales Leader Weekly", "what goes in the must-win deals section",
  "regenerate just the rep health dashboard", "the coaching notes are too
  vague", or "how should I select the Top 5 must-win deals this week". Also
  use for ad-hoc one-off generations outside the scheduled task.
---

# Sales Leader Weekly — Runbook

This skill documents the Sales Leader Weekly workflow at a level useful for ad-hoc generation, troubleshooting, or single-section regeneration. For end-to-end automated runs, fire the registered `sales-leader-weekly-report` scheduled task.

## Where everything lives

- **Spec:** `Revenue Reviews/specs/sales_leader_weekly_spec.md`
- **Output folder:** `Revenue Reviews/Leader Weekly/Sales/`
- **Filename:** `Sales_Leader_Weekly_{YYYY-MM-DD}.html`
- **Published path:** `${GITHUB_PAGES_URL}/reports/leader-weekly/sales/{YYYY-MM-DD}.html`

## Selection heuristics

### Top-5 Must-Win deals
Score each open Sales-owned deal:
- +3 if Close Date within 14 days
- +2 if Close Date within 30 days
- +2 if amount ≥ top-quartile of open pipeline
- +2 if Forecast Category = Commit
- −2 if SCS = 0 (no engagement → not really winnable this week)
- +1 if stage age in current stage > 30 days (decision deal, needs intervention)
Pick top 5. Every Play column must specify a concrete intervention (1:1, exec call, re-stage decision). No "monitor" or "follow up" verbs.

### Top-10 Accounts
Mix of: must-win deal accounts, accounts with this-week meeting activity (Mixmax MCP), accounts with Amplitude usage spikes (`account-amplitude-crossref`), and re-engagement targets where Octave can help (`octave-messaging-suggestions`).

### Stuck deals
Filter: stage age > 30 days AND no SCS movement in last 14 days. Verdict per row: **Kill** (Closed Lost), **Re-stage** (move back to earlier stage), or **Rescue** (named exec play).

### Pull-in deals
Filter: Close Date within next 21 days AND SCS ≥ 60 AND not yet at Best Case forecast. These are the "could pull into this period with one more push" deals.

## Status badge thresholds (Rep Health Dashboard)

- CRUSHING — ≥110% of QTD attainment pace
- ON-PACE — 90–110%
- WATCH — 70–90%
- BEHIND — <70%

## Account Deep-Dive Protocol

When a named account in sections 2, 5, or 6 needs context:
1. Mixmax MCP — search recent meetings for the account domain.
2. `account-amplitude-crossref` — cross-reference the domain to active product users.
3. `octave-messaging-suggestions` — if rep needs to re-engage, generate the recommended outreach.
Combine all three into the row's "Why it matters" / "Recommended action" / "Sales Leader Play" cells.

## Single-section regeneration

If the user wants only one section rebuilt:
1. Read the current `Sales_Leader_Weekly_{date}.html`.
2. Replace the `<h2 id="...">` block (and following content up to the next `<h2>`) for that section.
3. Re-validate the QA gate items applicable to that section.
4. Show diff before publishing.

## Publishing

Use `mixmax-publishing-core`'s `publishing-config-reference` skill to load the config, then publish via the GitHub Contents API. Wait 30–90s for Pages rebuild.

## Common failure modes

- **Coaching notes too vague** → regenerate with specific deal names + specific behaviors. "Coach Karan on close plans" is not acceptable. "Karan's Vector Media deal has been at SCS 0 for 186 days — coach on identifying economic buyer in next 1:1 (Mon)" is acceptable.
- **Status badges miscalibrated** → recompute attainment using QTD elapsed days / total quarter days * full-quarter target.
- **Top-5 dominated by stale low-SCS deals** → those are stuck deals (section 6), not must-wins. Re-select.
