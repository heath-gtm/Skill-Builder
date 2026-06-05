---
name: churn-analysis-setup
description: >
  Set up the Mixmax Churn Analysis workflow. Use when the user says
  "set up churn analysis", "configure churn report", "install churn
  analysis", "create the churn analysis task", "how do I run the churn
  report", or "I just installed the mixmax-churn-analysis plugin".
  Guides the user through connecting required tools, verifying the
  Churn Analysis tab, and registering the scheduled task.
---

# Churn Analysis Setup

One-time setup skill for the Mixmax Churn Analysis workflow.

---

## What this does

1. Verifies all required MCP connections are active
2. Confirms the Churn Analysis tab exists in Gen 1
3. Drops the canonical spec and task prompt into the user's working folder
4. Registers a manual-trigger scheduled task: `mixmax-churn-analysis-report`

---

## Prerequisites

Before running setup, the user MUST have:

- **`mixmax-publishing-core`** plugin installed and `publishing-config-setup` completed (PAT validated)
- **Google Sheets MCP** (or Chrome MCP) connected — to read the Churn Analysis tab
- **Amplitude MCP** connected — project 130895 (Mixmax App Prod)
- **Mixmax MCP** connected — for meeting transcript searches
- **Notion MCP** connected (optional) — for posting summary to Notion
- **Slack MCP** connected (optional) — for DM delivery
- **GitHub** access verified via publishing config

---

## Setup Steps

### STEP 1 — Verify MCP connections

Check that these tools respond:

```
Chrome MCP   → mcp__Claude_in_Chrome__navigate (or Google Sheets MCP)
Amplitude    → mcp__21ac7e4d-...__query_amplitude_data
Mixmax       → mcp__229af089-...__meetings
Notion       → mcp__7e606609-...__notion-search (optional)
Slack        → mcp__e42a8a14-...__slack_send_message (optional)
```

If any required MCP is missing, tell the user which connector to install and stop.

### STEP 2 — Verify Churn Analysis tab

Navigate to or fetch the Gen 1 sheet and confirm:
- Sheet ID: `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY`
- Tab: "Churn Analysis" (gid=`1283374228`)
- Required columns: A (Account Name), B (Domain), E (CSM), F (Previous Contract Value), R (Close Date), S (Downgrade Reason), T (Win/Loss Reason), U (Win/Loss Details), V-Z (Aero scores and additional fields)

### STEP 3 — Drop spec + task prompt into working folder

Copy from plugin references:
```
${CLAUDE_PLUGIN_ROOT}/references/churn_analysis_spec.md
  → Revenue Reviews/specs/churn_analysis_spec.md

${CLAUDE_PLUGIN_ROOT}/references/churn_analysis_task_prompt.md
  → Revenue Reviews/specs/churn_analysis_task_prompt.md
```

### STEP 4 — Register scheduled task

Use the Scheduled Tasks MCP to create:

```
Name:        mixmax-churn-analysis-report
Description: Generate the Mixmax Churn & Downgrade Analysis report
Schedule:    manual (no cron — user triggers on demand)
Prompt:      Read and follow Revenue Reviews/specs/churn_analysis_task_prompt.md
```

### STEP 5 — Confirm

Tell the user:
- Setup complete
- They can trigger `mixmax-churn-analysis-report` from the scheduled tasks panel
- Recommended cadence: monthly (first week of new month) and quarterly (first week after quarter close)
- First run: specify the period (e.g., "Q1 2026") when triggering
