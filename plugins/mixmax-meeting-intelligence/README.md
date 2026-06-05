# Meeting Intelligence — Cowork Plugin

Six skills and three prompts that give Mixmax's GTM team data-driven customer intelligence across the full meeting lifecycle: prep, outreach, follow-up, and ongoing health monitoring.

---

## Why six skills, not one?

Cowork is a skill runner, not a prompt executor. The intelligence lives in the SKILL.md files. The prompts are just short task descriptions that tell Cowork *when* to use those skills.

Each skill handles one job well. They compose naturally in conversation — run a prep, then draft an outreach, then check enrollment before sending — but each can also work standalone.

---

## The six skills

| Skill | What it does | Typical trigger |
|-------|-------------|-----------------|
| `weekly-meeting-prep` | The orchestrator. Three modes: (A) scan calendar + prep all meetings, (B) single-company deep dive, (C) product research only | "Run my weekly prep" / "Prep me for Datadog" / "Product research on Gong" |
| `octave-outreach-drafter` | Turns briefing insights into 75-120 word outreach emails via SMART framework | "Draft outreach to TJ at Datadog" |
| `account-health-monitor` | Quick diagnostic: user retention, engagement depth, volume trends, churn signals | "How healthy is datadog.com?" |
| `meeting-followup-generator` | Post-meeting follow-up emails + structured action items from Mixmax summaries | "Write a follow-up from my Datadog call" |
| `prospect-enrollment-check` | Check if a contact is already in a Mixmax sequence before reaching out | "Is TJ Boskelly in a sequence?" |
| `weekly-meeting-digest` | End-of-week roll-up across all meetings: themes, action items, accounts needing attention | "Summarize my meetings this week" |

---

## The three prompts

### 1. `01-setup-prompt.md` — Run once, on day zero

One-time configuration. Verifies connectors (GCal, Amplitude, Mixmax, Octave, Gmail, Slack), installs all six skills, writes project-level instructions, optionally sets up the Monday digest.

### 2. `02-task-prompts.md` — The daily rep experience

Reference card showing every way reps can invoke the skills. Bookmark on the project's home tab. Not a prompt to paste — a cheat sheet to copy from.

### 3. `03-scheduled-digest-prompt.md` — Monday morning auto-prep

Runs every Monday 7am. Scans the week's calendar, finds external customer meetings, generates triage cards (not full briefings) for each, and posts a grouped digest to Slack. Reps reply in-thread for full briefings on specific accounts.

---

## The order of operations

```
Day 0 (you, 15 minutes):
  1. Create a new Cowork Project named "Meeting Intelligence"
  2. Ensure GCal, Amplitude, Mixmax, Octave connectors are attached
  3. Install the plugin (or unzip the skills package)
  4. Paste 01-setup-prompt.md into a fresh task, hit run
  5. Answer the setup questions as they come
  6. Smoke test: type "prep me for my call with {a customer you know}"
  7. Review the briefing — does the data look right?

Day 1 (each rep, 2 minutes):
  1. Join the shared project
  2. Type "run my weekly prep" — get briefings for the week
  3. Type "draft outreach to {person}" — get ready-to-send emails

Week 2 (scheduled digest starts firing):
  Monday 7am → Slack gets a triage digest
  Reps reply in-thread for full briefings on specific accounts
```

---

## Required connectors

| Connector | Required? | What it provides |
|-----------|-----------|-----------------|
| Google Calendar | Yes | Meeting schedule, attendee lists |
| Amplitude | Yes | Product usage analytics — the data backbone |
| Mixmax | Yes | Meeting summaries, transcripts, sequence data |
| Octave | Yes | Contact enrichment, company research, email drafting |
| Gmail | Recommended | Email thread context for relationship signals |
| Slack | Optional | Monday digest posting (not needed for individual runs) |

---

## The meeting lifecycle this plugin covers

```
BEFORE the meeting:
  weekly-meeting-prep → Full briefing with data + history + angles
  octave-outreach-drafter → Ready-to-send outreach to key contacts
  prospect-enrollment-check → Verify nobody's already emailing them

DURING the week:
  account-health-monitor → Quick health diagnostic on any account

AFTER the meeting:
  meeting-followup-generator → Follow-up email + action items

END OF WEEK:
  weekly-meeting-digest → Roll-up across all meetings
```

---

## Iterating on the plugin

After setup, if the output isn't quite right, **edit the SKILL.md files, not these prompts.** The prompts just route to skills; the logic lives in the skills.

| Symptom | File to edit |
|---------|------------|
| Briefing missing Amplitude data | `weekly-meeting-prep/references/amplitude-event-registry.md` — query construction guide |
| Outreach draft feels like a pitch | `octave-outreach-drafter/SKILL.md` — tone rules and SMART framework |
| Health score thresholds too sensitive | `account-health-monitor/SKILL.md` — scoring thresholds |
| Meeting history synthesis too thin | `weekly-meeting-prep/references/mixmax-meeting-search.md` — synthesis framework |
| Briefing template structure wrong | `weekly-meeting-prep/references/briefing-template.md` — exact template |
| Wrong domains excluded from calendar scan | `weekly-meeting-prep/SKILL.md` — exclusion list table |

Edit the file, save, and Cowork picks up the change on the next task. No re-setup required.

---

## One thing I'd encourage before you share with the team

Run each mode once manually:

1. `"Run my weekly prep"` — does the calendar scan find the right meetings?
2. `"Prep me for my call with {customer you know cold}"` — does the Amplitude data match what you'd expect?
3. `"Product research on {customer}"` — does the report surface the right insights?
4. `"Draft outreach to {person}"` — would you actually send this email?

Fix the ONE thing that's wrong in the skill file. Then share with the team. You'll save everyone from a bad first impression.
