---
name: cs-leader-weekly-setup
description: >
  Install the `cs-leader-weekly-report` scheduled task that produces the
  weekly CS Leader brief for Mixmax. Use whenever the user says "set up CS
  Leader Weekly", "install cs-leader-weekly-report", "configure the CS
  Leader weekly task", "create the CS leader weekly task", or "I just
  installed the mixmax-cs-leader-weekly plugin". Verifies dependencies,
  drops the spec into the user's working folder, and registers a
  manual-trigger scheduled task.
---

# CS Leader Weekly — Setup

This skill is a one-time installer for the CS Leader Weekly workflow. It registers a manual-trigger scheduled task (`cs-leader-weekly-report`), creates the output folder, and verifies dependencies.

## What this sets up

- `Revenue Reviews/Leader Weekly/CS/` — folder created if missing.
- `Revenue Reviews/specs/cs_leader_weekly_spec.md` — copied from the plugin bundle.
- A scheduled task with `taskId = cs-leader-weekly-report` (manual trigger).

## Prerequisites

1. **`mixmax-publishing-core` is installed** and `publishing-config-setup` has been run (so `Revenue Reviews/specs/github_publishing_config.md` exists with a real PAT). If not, stop and direct the user to install/run that plugin first.
2. **A working folder is selected** in Cowork.
3. **Most recent quarterly + quarter-ahead reports are available**, plus a fresh weekly snapshot.
4. **Notion + Slack MCPs connected** (Slack optional — runbook drafts inline if disconnected).
5. **Skills used during generation** (`renewals-management`, `mixmax-revenue-reporting`, `account-amplitude-crossref`, `octave-messaging-suggestions`, plus the monthly variant of `customer-success`) are available either as standalone Cowork skills or via the `mixmax-monthly-gtm-report` plugin. Install upstream plugins first.

## Workflow

### Step 1 — Verify dependencies

Read `Revenue Reviews/specs/github_publishing_config.md`. If missing/placeholder, stop.

Confirm with the user:
- Path to the most recent approved quarterly report.
- Path to the most recent Quarter-Ahead report.
- Slack DM target ID for Heather (default `D0A70RNQKM2`).

### Step 2 — Place the spec

Copy `${CLAUDE_PLUGIN_ROOT}/references/cs_leader_weekly_spec.md` to `Revenue Reviews/specs/cs_leader_weekly_spec.md`. Ask before overwriting.

### Step 3 — Create output folder

Ensure `Revenue Reviews/Leader Weekly/CS/` exists.

### Step 4 — Register the scheduled task

Use `mcp__scheduled-tasks__create_scheduled_task` (or `update_scheduled_task` if the ID exists) with:

- `taskId`: `cs-leader-weekly-report`
- `description`: `Weekly cross-period CS Leader report — MTD NRR/GRR, must-save accounts, renewal 30/60/90 pipeline, expansion plays, CSM book health, Q-ahead red flags. Synthesizes latest quarterly + quarter-ahead + weekly snapshot. Publishes to GitHub Pages via dynamic publishing config.`
- No `cronExpression`, no `fireAt` (manual trigger).
- `prompt`: contents of `${CLAUDE_PLUGIN_ROOT}/references/cs_leader_weekly_task_prompt.md`.

### Step 5 — Confirm

Tell the user:
- Task is registered. Fire from the Cowork scheduled-tasks panel.
- Recommended cadence: every Friday afternoon or Monday morning.
- Output: a single `CS_Leader_Weekly_{YYYY-MM-DD}.html` file pushed to GitHub Pages and DM'd to Heather.
