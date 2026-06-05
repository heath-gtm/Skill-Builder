---
name: ae-pipeline-setup
description: >
  Set up the Mixmax AE Pipeline Analysis workflow. Use when the user says
  "set up AE pipeline analysis", "configure pipeline analysis", "install
  AE pipeline", "create the AE pipeline task", "how do I run a pipeline
  analysis for an AE", or "I just installed the mixmax-ae-pipeline-analysis
  plugin". Guides the user through connecting required tools, verifying
  the AE Forecast tab, and registering the scheduled task.
---

# AE Pipeline Analysis Setup

One-time setup skill for the Mixmax AE Pipeline Analysis workflow.

---

## What this does

1. Verifies all required MCP connections are active
2. Confirms the AE Forecast - This Year tab exists in Gen 1
3. Drops the canonical spec and task prompt into the user's working folder
4. Registers a manual-trigger scheduled task: `ae-pipeline-analysis-report`

---

## Prerequisites

Before running setup, the user MUST have:

- **Google Sheets MCP** or **Chrome MCP** — to read Gen 1 data
- **Amplitude MCP** — to pull product-usage / trial data (project 130895)
- **Mixmax MCP** — to search meeting transcripts and check sequence enrollments
- **Gmail MCP** — to search email threads and identify engaged contacts
- **Octave MCP** — to generate strategic outreach plays, enrich companies, and find contacts
- **GitHub publishing config** — `Revenue Reviews/specs/github_publishing_config.md` must exist with valid PAT

---

## Setup Steps

### Step 1 — Verify MCP connections

Check that the following tools respond:
- `query_amplitude_data` (Amplitude)
- `meetings` or `search_meeting_summaries` (Mixmax)
- `gmail_search_messages` (Gmail)
- `generate_email`, `generate_call_prep`, `enrich_company`, `find_person` (Octave)
- Chrome MCP `javascript_tool` OR Google Drive MCP (for sheet reading)

If any are missing, tell the user which connector to install and stop.

### Step 2 — Verify the AE Forecast tab

Read a sample from Gen 1 Sheet ID `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY` AE Forecast - This Year tab (gid `1450719288`) to confirm:
- The tab exists and has data
- Opportunity Owner column is populated
- Account Name, Stage, Amount, and Close Date columns have values
- Stage values include non-closed stages (not just Closed Won / Closed Lost)

### Step 3 — Copy specs to working folder

Copy from the plugin's `references/` folder:
- `ae_pipeline_analysis_spec.md` → `Revenue Reviews/specs/`
- `ae_pipeline_analysis_task_prompt.md` → `Revenue Reviews/specs/`

If files already exist, ask the user if they want to overwrite.

### Step 4 — Verify publishing config

Read `Revenue Reviews/specs/github_publishing_config.md`. Confirm:
- `GITHUB_PAT` is set (not placeholder)
- `GITHUB_OWNER` and `GITHUB_REPO` are set

If missing, tell the user to run the `publishing-config-setup` skill first.

### Step 5 — Register the scheduled task

Create a manual-trigger scheduled task:
- **taskId:** `ae-pipeline-analysis-report`
- **description:** "AE Pipeline Analysis — on-demand deep-dive into any AE's full open pipeline with deal tiering (Must-Win/Should-Win/Long-Shot), Amplitude trial usage, meeting intel, Gmail engagement, sequence status, and Octave strategic plays per deal. Published to GitHub Pages."
- **prompt:** (see task prompt file for full content)
- No cron — manual trigger only

### Step 6 — Create output directory

Ensure `Revenue Reviews/AE Pipeline Analysis/` exists.

### Step 7 — Confirm setup

Print:
- All MCP connections verified
- AE Forecast tab confirmed
- Specs copied to working folder
- Scheduled task registered
- Output directory ready
- "Setup complete. To run: trigger `ae-pipeline-analysis-report` and specify the AE name."
