---
name: sales-leader-weekly-setup
description: >
  Install the `sales-leader-weekly-report` scheduled task that produces the
  weekly Sales Leader brief for Mixmax. Use whenever the user says "set up
  Sales Leader Weekly", "install sales-leader-weekly-report", "configure the
  Sales Leader weekly task", "create the sales leader weekly task", or "I
  just installed the mixmax-sales-leader-weekly plugin". Verifies dependencies,
  drops the spec into the user's working folder, and registers a manual-trigger
  scheduled task.
---

# Sales Leader Weekly — Setup

This skill is a one-time installer for the Sales Leader Weekly workflow. It registers a manual-trigger scheduled task (`sales-leader-weekly-report`), creates the output folder, and verifies dependencies.

## What this sets up

- `Revenue Reviews/Leader Weekly/Sales/` — folder created if missing.
- `Revenue Reviews/specs/sales_leader_weekly_spec.md` — copied from the plugin bundle.
- A scheduled task with `taskId = sales-leader-weekly-report` (manual trigger).

## Prerequisites

1. **`mixmax-publishing-core` is installed** and `publishing-config-setup` has been run (so `Revenue Reviews/specs/github_publishing_config.md` exists with a real PAT). If not, stop and direct the user to install/run that plugin first.
2. **A working folder is selected** in Cowork.
3. **The most recent quarterly report has been generated** (or at least the most recent monthly + a fresh weekly snapshot). The Sales Leader Weekly synthesizes across these — it never re-derives from the Gen 1 sheet directly.
4. **Notion + Slack MCPs connected** (Slack is optional — runbook drafts inline if disconnected).
5. **Skills bundled with this plugin** (`deal-management`, `pipeline-building`, `mixmax-revenue-reporting`, `account-amplitude-crossref`, `octave-messaging-suggestions`) are available — the plugin ships skill stubs that point to the canonical implementations in `mixmax-weekly-gtm-report` / `mixmax-monthly-gtm-report`. If those plugins are not installed, install them first.

## Workflow

### Step 1 — Verify dependencies

Read `Revenue Reviews/specs/github_publishing_config.md`. If missing/placeholder, stop.

Confirm with the user:
- Path to the most recent approved quarterly report (e.g., `Revenue Reviews/Quarterly Report/CRO_Quarterly_Report_Q1-2026.html`).
- Path to the most recent Quarter-Ahead artifact (e.g., `Mixmax_Quarter_Ahead_Q2-2026.html`).
- Slack DM target ID for Heath (default `U07CAK8C0CW`).

### Step 2 — Place the spec

Copy `${CLAUDE_PLUGIN_ROOT}/references/sales_leader_weekly_spec.md` to `Revenue Reviews/specs/sales_leader_weekly_spec.md`. Ask before overwriting if a local edit exists.

### Step 3 — Create output folder

Ensure `Revenue Reviews/Leader Weekly/Sales/` exists.

### Step 4 — Register the scheduled task

Use `mcp__scheduled-tasks__create_scheduled_task` (or `update_scheduled_task` if the ID already exists) with:

- `taskId`: `sales-leader-weekly-report`
- `description`: `Weekly cross-period Sales Leader report — MTD pacing, must-win deals, rep health, quarter-ahead red flags, Monday coaching agenda. Synthesizes latest quarterly + quarter-ahead + weekly snapshot. Publishes to GitHub Pages via dynamic publishing config.`
- No `cronExpression`, no `fireAt` (manual trigger).
- `prompt`: contents of `${CLAUDE_PLUGIN_ROOT}/references/sales_leader_weekly_task_prompt.md`.

### Step 5 — Confirm

Tell the user:
- Task is registered. They fire it from the Cowork scheduled-tasks panel.
- Recommended cadence: every Friday afternoon or every Monday before the sales standup.
- Output: a single `Sales_Leader_Weekly_{YYYY-MM-DD}.html` file pushed to GitHub Pages and DM'd to Heath.
