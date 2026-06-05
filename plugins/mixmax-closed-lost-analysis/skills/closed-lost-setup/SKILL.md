---
name: closed-lost-setup
description: >
  Set up the Mixmax Closed Lost Analysis workflow. Use when the user says
  "set up closed lost analysis", "configure closed lost report", "install
  closed lost analysis", "create the closed lost analysis task", "how do I
  run the closed lost report", or "I just installed the
  mixmax-closed-lost-analysis plugin".
  Guides the user through connecting required tools, verifying the
  AE Forecast tab, and registering the scheduled task.
---

# Closed Lost Analysis Setup

One-time setup skill for the Mixmax Closed Lost Analysis workflow.

---

## What this does

1. Verifies all required MCP connections are active
2. Confirms the AE Forecast - This Year tab exists in Gen 1
3. Drops the canonical spec and task prompt into the user's working folder
4. Registers a manual-trigger scheduled task: `mixmax-closed-lost-analysis-report`

---

## Prerequisites

Before running setup, the user MUST have:

- **`mixmax-publishing-core`** plugin installed and `publishing-config-setup` completed (PAT validated)
- **Google Sheets MCP** (or Chrome MCP) connected — to read the AE Forecast tab
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

### STEP 2 — Verify AE Forecast - This Year tab

Navigate to or fetch the Gen 1 sheet and confirm:
- Sheet ID: `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY`
- Tab: "AE Forecast - This Year" (gid=`1450719288`)
- Required columns: Account Name (E), Stage (F), Close Date (G), Opportunity Owner (D), Record Type (C), Amount (M), Opportunity Source (W), Website (X), Win/Loss Details (Y), Win/Loss Reason (Z), Aero Account Fit (AA), Aero Product Fit (AB)
- Confirm that rows with Stage = "Closed Lost" exist and have populated Close Date values

### STEP 3 — Drop spec + task prompt into working folder

Copy from plugin references:
```
${CLAUDE_PLUGIN_ROOT}/references/closed_lost_spec.md
  → Revenue Reviews/specs/closed_lost_spec.md

${CLAUDE_PLUGIN_ROOT}/references/closed_lost_task_prompt.md
  → Revenue Reviews/specs/closed_lost_task_prompt.md
```

### STEP 4 — Register scheduled task

Use the Scheduled Tasks MCP to create:

```
Name:        mixmax-closed-lost-analysis-report
Description: Generate the Mixmax Closed Lost Analysis report
Schedule:    manual (no cron — user triggers on demand)
Prompt:      Read and follow Revenue Reviews/specs/closed_lost_task_prompt.md
```

### STEP 5 — Confirm

Tell the user:
- Setup complete
- They can trigger `mixmax-closed-lost-analysis-report` from the scheduled tasks panel
- Recommended cadence: monthly (first week of new month) and quarterly (first week after quarter close)
- First run: specify the period (e.g., "Q1 2026", "March 2026") when triggering
