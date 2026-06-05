# Account Intelligence — Cowork Plugin for Mixmax AEs

A full 360-degree account intelligence agent for Mixmax AEs. Every output delivers company research, Amplitude product usage deep dives, power user identification, Mixmax meeting history, contact intelligence, and ready-to-use Octave engagement materials. 10 skills covering the complete AE workflow: deal reviews, prospect prioritization, call prep, meeting prep, multi-channel outreach, health monitoring, follow-ups, and more.

---

## How it works

Reps maintain a Google Sheet with three tabs: **Open Deals**, **Renewal Book**, and **Prospect Accounts**. The agent reads this sheet and cross-references with live data from Amplitude (product usage), Mixmax (meeting history), and Octave (company/contact enrichment) to produce actionable intelligence.

Reps talk naturally. "What should I focus on?" gets a daily briefing. "How's the Acme deal?" gets a deal review. "Who should I go after in outbound?" gets prospect recommendations. The orchestrator routes every request to the right skill automatically.

---

## The ten skills

| Skill | What it does |
|-------|-------------|
| `account-intelligence-orchestrator` | Conversational router + daily briefing. The front door. |
| `deal-intelligence` | 360-degree deal review with Octave engagement materials |
| `prospect-finder` | 360-degree prospect prioritization with ready-to-use outreach sequences |
| `weekly-meeting-prep` | Meeting prep (3 modes: weekly scan, single-company, product research) |
| `call-prep` | Full call preparation: discovery questions, objection handling, talking points |
| `octave-outreach-drafter` | Multi-channel messaging engine: email sequences, LinkedIn, call prep |
| `account-health-monitor` | On-demand account health diagnostics from Amplitude |
| `meeting-followup-generator` | Post-meeting follow-up emails and action items |
| `prospect-enrollment-check` | Verify someone isn't already in a Mixmax sequence |
| `weekly-meeting-digest` | Weekly roll-up across all meetings with themes and action items |

---

## The three prompts

| Prompt | Purpose |
|--------|---------|
| `01-setup-prompt.md` | Day-zero setup: connectors, skills, sheet, instructions |
| `02-task-prompts.md` | Rep reference card — all the ways to invoke skills |
| `03-scheduled-digest-prompt.md` | Monday 7am auto-digest covering meetings + deals + renewals + prospects |

---

## Required connectors

| Connector | Required? | What it provides |
|-----------|-----------|-----------------|
| Google Calendar | Yes | Meeting schedule, attendee lists |
| Amplitude | Yes | Product usage analytics |
| Mixmax | Yes | Meeting summaries, transcripts, sequence data |
| Octave | Yes | Contact enrichment, company research, outreach |
| Chrome MCP | Yes | Reads the rep's Google Sheet |
| Gmail | Recommended | Email thread context |
| Slack | Optional | Monday digest posting |

---

## Setup (15 minutes)

```
1. Create a new Cowork Project named "Account Intelligence"
2. Attach connectors: GCal, Amplitude, Mixmax, Octave, Chrome
3. Install the plugin
4. Open account-intelligence-template.xlsx, upload to Google Drive
5. Fill in your Open Deals, Renewal Book, and Prospect Accounts
6. Paste 01-setup-prompt.md into a fresh task, hit run
7. Answer the setup questions (sheet URL, Slack channel)
8. Smoke test: "What should I focus on today?"
```

---

## What reps type

| Intent | What to type |
|--------|-------------|
| Daily briefing | "What should I focus on today?" |
| Deal review | "Review my deals" or "How's the Acme deal?" |
| Find prospects | "Who should I go after in outbound?" |
| Meeting prep | "Prep me for my call with Datadog" |
| Call prep | "Call prep for my demo with Stripe" |
| Draft outreach | "Draft outreach to Sarah at Gamma Tech" |
| Account health | "How healthy is datadog.com?" |
| Follow-up email | "Write a follow-up from my call with Acme" |
| Weekly summary | "Summarize my meetings this week" |

---

## Iterating on the plugin

| Symptom | File to edit |
|---------|------------|
| Daily briefing missing a section | `account-intelligence-orchestrator/SKILL.md` — Daily Briefing Flow |
| Deal risk thresholds wrong | `deal-intelligence/SKILL.md` — Auto-Flag Risk Signals |
| Prospect scoring too aggressive | `prospect-finder/SKILL.md` — Prioritization Signals |
| Sheet columns don't match | `deal-intelligence/references/sheet-schema.md` — update the schema |
| Briefing missing Amplitude data | `weekly-meeting-prep/references/amplitude-event-registry.md` |
| Outreach tone wrong | `octave-outreach-drafter/SKILL.md` — engagement quality rules |
| Call prep questions too generic | `call-prep/SKILL.md` — quality rules |
| Health thresholds too sensitive | `account-health-monitor/SKILL.md` — scoring thresholds |
