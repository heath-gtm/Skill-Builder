---
name: mutual-action-plan
description: Generate a deal-specific Mutual Action Plan (MAP) — a.k.a. Trial Success Plan — for a Mixmax prospect. Produces a fully populated, Mixmax-branded .docx the rep can send directly to their champion. The MAP is the structured agreement on what gets evaluated, what success looks like, who does what, and by when. Trigger on "draft a MAP for [account]", "build a Mutual Action Plan", "create MAP", "trial success plan", "MAP template", "success plan for [account]", "build the MAP", "I need a MAP for [prospect]", or anytime a rep is entering Stage 3 (Validation / Business Case) at Mixmax and the deal requires a MAP. Also fire when a rep mentions a trial, pilot, or controlled evaluation that needs structure.
---

# Mutual Action Plan Skill

Generate a Mixmax Mutual Action Plan (MAP) — also called a Trial Success Plan — for a specific prospect, populated with their challenges, desired outcomes, success metrics, and a phased completion schedule. Outputs a Mixmax-branded `.docx` the rep can send directly to their champion.

## What is a MAP at Mixmax

A MAP is the structured agreement between Mixmax and a prospect that converts a Stage 2 / early Stage 3 conversation into a defensible Best Case deal. It documents:

- The specific business challenges the prospect is solving for (pulled from SPRINT discovery)
- The outcomes that define a successful evaluation
- The activities and milestones that will prove (or disprove) value
- The success metrics both sides will judge against
- The decision date and the path to signature

When the deal exit-criteria call for "MAP finalized — if required" (Stage 3 → 4), this is the artifact.

## When to use

Fire this skill when:

- A rep says "build a MAP for [account]" or "draft a Mutual Action Plan" or "trial success plan for [company]"
- A rep is heading into Stage 3 (Validation / Business Case) and the deal warrants a structured evaluation
- A rep is setting up a managed pilot or trial that needs documented success criteria
- A champion has asked for a written plan they can socialize internally
- Heath specifies an account that needs a Best Case-grade artifact

Do NOT fire for:
- Stage 0 / Stage 1 deals — they're too early for a MAP
- Closed Won deals (a MAP is a pre-signature artifact)
- Pure outreach / sequence drafting (use `octave-outreach-drafter` instead)

## Inputs to collect from the rep

Before generating, gather these. Use `AskUserQuestion` if anything is missing — don't guess.

**Required:**
- **Customer company name** — e.g., "Quantum Metric"
- **Evaluation start and end dates** — e.g., "April 1 – April 30, 2026"
- **Decision date** — when the buying decision happens (often the same as end date)
- **Stakeholders / recipients** — 2–4 names with titles (champion + 1-3 stakeholders); these go in the "To:" block
- **Business challenges** — 4–7 specific challenges from SPRINT discovery (use the rep's actual notes, not boilerplate)
- **Desired outcomes** — 4–7 outcomes that define success for this customer
- **Trial activities** — 5–10 core evaluation activities (build from what the rep has already proposed)
- **Success metrics** — 4–7 metrics with Target / Signal (e.g., "Adoption rate → 90%+ of trial reps actively using Mixmax")
- **Phased schedule** — phase names + dates for IT/Admin setup, Kick-off, Check-ins, Wrap-up
- **Rep info** — Name, Title, Email, Phone

**Optional:**
- Champion name(s) for the opening salutation ("Dear [First Name]")
- Specific legal owner / integration stack to call out in IT & Admin setup

## How to gather inputs

1. **First, check meeting history.** If the user has the Mixmax Meeting Intelligence MCP connected, call `mcp__229af089-f88a-40ac-ae96-42d07e09ff31__meetings` (or equivalent) to pull recent meeting transcripts for the account. Most of the inputs above are buried in discovery notes.

2. **Second, check Salesforce.** Use `mcp__d50c041d-378a-4fbe-b287-5541902dd1b9__soqlQuery` to find the Opp record — Decision Maker, Champion, Renewal/Close dates, custom MAP-related fields.

3. **Third, ask the rep for what's missing.** Use `AskUserQuestion` with specific questions. Don't make the rep type a long brief — chunk it into 2-3 question blocks max.

4. **Confirm the inputs before building.** Show the rep a quick recap of every field you'll insert. Let them confirm or correct before the doc is generated. This is faster than fixing a fully-built MAP.

## Workflow

1. **Acknowledge the request** in one line. State which account.
2. **Pull existing context** (meetings, Salesforce, Notion) before asking for new info.
3. **Use `AskUserQuestion`** for genuine gaps. Pass already-known answers as defaults in the question text.
4. **Show the rep a recap** of every input that will populate the MAP.
5. **Generate the docx** by running `build_map.py` (see "Output spec" below) with a JSON inputs file.
6. **Present the file** via `mcp__cowork__present_files` so the rep can download and send.
7. **Note next steps**: send to champion, schedule MAP review call, surface back at Stage 3 exit gate.

## Output spec

The `build_map.py` script in this skill folder accepts a JSON inputs file and produces a Mixmax-branded `.docx`. It mirrors the canonical structure of the Mixmax & Quantum Metric Trial Success Plan (the reference doc reps have been using).

**Run it like this:**

```bash
python3 /path/to/this-skill/build_map.py \
  --inputs /tmp/map-inputs.json \
  --out "/path/to/working/folder/MAP-[CustomerName]-[Date].docx"
```

**JSON input shape** (all fields required unless marked optional):

```json
{
  "customer": "Acme Corp",
  "date_range": "April 1 – April 30, 2026",
  "decision_date": "April 30, 2026",
  "recipients": [
    {"name": "Jane Doe", "title": "VP Sales"},
    {"name": "Bob Smith", "title": "Director of Sales Enablement"},
    {"name": "Alli Park", "title": "Senior Manager, IT & Apps"}
  ],
  "salutation_first_names": "Jane, Bob, and Alli",
  "business_challenges": [
    "Manual processes slowing rep outreach...",
    "Salesforce data desync...",
    "Low engagement signal visibility..."
  ],
  "desired_outcomes": [
    "Automate follow-up so no deal goes cold...",
    "Eliminate manual Salesforce logging...",
    "Drive adoption across all reps..."
  ],
  "trial_activities": [
    "Install Mixmax across all trial reps and confirm Salesforce integration...",
    "Send at least 5 tracked emails and review engagement data...",
    "Set up scheduling links..."
  ],
  "success_metrics": [
    {"metric": "Adoption rate", "target": "90%+ of trial reps actively using Mixmax"},
    {"metric": "Salesforce sync accuracy", "target": "100% of activities logging correctly"}
  ],
  "schedule": [
    {
      "phase": "IT & Admin Setup",
      "date": "April 1–3, 2026",
      "activities": [
        "Confirm ToS items resolved with Legal",
        "Provision trial users and set up integrations",
        "Confirm Salesforce integration live"
      ]
    },
    {
      "phase": "Kick-Off Call — Rep Onboarding",
      "date": "Week of April 6, 2026",
      "activities": [
        "Walk reps through Mixmax functionality",
        "Set up trial users' scheduling links",
        "Send first tracked emails"
      ]
    }
  ],
  "rep": {
    "name": "Isabelle Tuomi",
    "title": "Account Executive",
    "email": "isabelle@mixmax.com",
    "phone": "647 988 3032"
  }
}
```

## Quality bar (the rep checks this before sending)

A high-quality MAP at Mixmax has:

- **Specific challenges** that match what was actually said in discovery — not generic boilerplate
- **Measurable success metrics** with targets a leader can defend in front of their own boss
- **A phased schedule** with dates, not "TBD" placeholders
- **Named owners** for each milestone (or at minimum, "Mixmax SE" vs. "Customer IT")
- **A decision date** that matches what the EB said live (not aspirational)
- **Specific Mixmax integrations** called out (Salesforce, Slack, calendar, Gong, LinkedIn — whichever apply to the stack the rep heard in discovery)

If any of the above is generic, send the rep back to discovery before generating. Better to delay the MAP than send a hollow one.

## Reference

- **Canonical example**: Quantum Metric Trial Success Plan (March 31, 2026) — the source pattern this template was modeled on
- **Mixmax Sales Process — Stage 3 (Validation / Business Case)**: this MAP is the deliverable that unlocks the Stage 3 → 4 exit
- **PLAN Selling (Track 6)**: the framework for navigating the buyer conversations that get the MAP returned with the champion's edits
- **Mixmax For Teams Trial Playbook (Notion)**: the operational detail behind the trial mechanics referenced inside the MAP

## Notes

- Always save the .docx to the user's working folder (not the scratchpad), so it persists outside the session
- File-name convention: `MAP-[CustomerName]-[YYYY-MM-DD].docx`
- After generating, optionally offer to draft a 3-sentence intro email the rep can paste above the MAP attachment
- This skill reads only. It does not write back to Salesforce. If the rep wants the MAP linked on the Opp record, use the Salesforce MCP separately to attach the file URL.
