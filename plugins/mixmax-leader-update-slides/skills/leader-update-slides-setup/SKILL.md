---
name: leader-update-slides-setup
description: >
  Install the `leader-ceo-updates` scheduled task that produces the monthly +
  quarterly Update Slides for the Mixmax CEO's board deck. Use whenever the
  user says "set up Update Slides", "install leader CEO updates",
  "configure board update slides", "create the leader-ceo-updates task",
  "set up the monthly slide brief workflow", or "I just installed the
  mixmax-leader-update-slides plugin". Verifies dependencies (publishing
  config, base reports), bundles the canonical spec into the user's working
  folder, and registers a manual-trigger scheduled task.
---

# Leader Update Slides — Setup

This skill is a one-time installer for the Update Slides workflow. It registers a manual-trigger scheduled task (`leader-ceo-updates`), drops the canonical spec into the user's working folder, and verifies the dependencies that the runbook needs at runtime.

## What this sets up

- `Revenue Reviews/specs/CEO_Update_Addendum.md` — copied from the plugin bundle into the user's working folder so the runbook can read it without referring back to `${CLAUDE_PLUGIN_ROOT}`.
- `Revenue Reviews/Leader Weekly/Update Slides/Sales/` and `Revenue Reviews/Leader Weekly/Update Slides/CS/` — folders created if they do not already exist.
- A scheduled task with `taskId = leader-ceo-updates` (manual trigger).

## Prerequisites

Before running, verify:

1. **`mixmax-publishing-core` is installed** and the user has run `publishing-config-setup` at least once (so `Revenue Reviews/specs/github_publishing_config.md` exists with a real PAT, not placeholders). If not, stop and direct the user to install/run that plugin first.
2. **A working folder is selected** in Cowork.
3. **Notion + Slack MCPs are connected** (Notion is required for distribution; Slack is optional — the runbook will draft messages inline if Slack is disconnected).
4. **A base monthly or quarterly report has been approved** at least once (this is for context — Update Slides inherit numbers; they never re-derive metrics).

## Workflow

### Step 1 — Verify dependencies

Read `Revenue Reviews/specs/github_publishing_config.md`. If missing or placeholder, stop and tell the user to run `publishing-config-setup` first.

Confirm with the user:
- The Notion parent page ID for "Leader Weekly Workflow" (where Sales + CS Update Slides child pages will be appended).
- The Slack DM target IDs for Heath (Sales) and Heather (CS). Defaults are `U07CAK8C0CW` and `D0A70RNQKM2` respectively per the spec — confirm these are still correct.

### Step 2 — Place the canonical spec

Copy `${CLAUDE_PLUGIN_ROOT}/references/CEO_Update_Addendum.md` to `Revenue Reviews/specs/CEO_Update_Addendum.md` in the user's working folder. If the file already exists and differs from the bundled version, ask the user whether to overwrite (they may have local edits worth preserving).

### Step 3 — Create the output folders

Ensure these directories exist (create if missing):
- `Revenue Reviews/Leader Weekly/Update Slides/Sales/`
- `Revenue Reviews/Leader Weekly/Update Slides/CS/`

### Step 4 — Register the scheduled task

Use `mcp__scheduled-tasks__create_scheduled_task` with:

- `taskId`: `leader-ceo-updates`
- `description`: `Leader Update Slides — generates Sales + CS slide-by-slide briefs (HTML, one section per slide) for the CEO's monthly/quarterly board deck. Lives under Leader Weekly. Manual trigger after the base monthly/quarterly revenue report is approved. Uses dynamic GitHub publishing config (specs/github_publishing_config.md).`
- No `cronExpression`, no `fireAt` (manual trigger only).
- `prompt`: the full task prompt below.

If a task with this ID already exists (visible from `list_scheduled_tasks`), use `mcp__scheduled-tasks__update_scheduled_task` to update its `prompt` and `description` instead of creating a duplicate.

#### Task prompt to register

Use the contents of `${CLAUDE_PLUGIN_ROOT}/references/leader_ceo_updates_task_prompt.md` as the `prompt` argument.

### Step 5 — Confirm

Tell the user:
- The task is registered. They can fire it from the Cowork scheduled-tasks panel by clicking "Run Now" on `leader-ceo-updates`.
- The expected output: two HTML files per run (`{period}.html` in Sales and CS folders), pushed to GitHub Pages and announced in Notion.
- The trigger flow: run the monthly or quarterly base report first, get APPROVAL GATE #1, then fire `leader-ceo-updates` and pass the period label (e.g., `2026-04` for April monthly, `2026-Q2` for Q2).

## Rotation / re-install

Running this skill again is safe — it idempotently updates the existing scheduled task and respecter local edits to the spec file (asks before overwriting).
