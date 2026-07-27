---
name: crm-field-library-builder
description: Build the canonical field library for your CRM. Names the fields that actually drive GTM decisions, locks a plain definition and query pattern for each, maps your stages to what has to be true at every one, and hands back a reference every rep, analyst, and skill can trust. Built for any team on Salesforce, HubSpot, or another CRM, customizable to your object model and process. Trigger on "build my CRM field library", "which fields actually matter", "define my stage matrix", "what does this field mean", "standardize our CRM definitions", "map fields for my analyst", or any CRM-hygiene or field-definition question.
---

# CRM Field-Library Builder

## What this does
Turns a messy CRM into a source of truth. It interviews you about your process, names the fields that actually drive decisions (not the 200 nobody fills), locks a plain-English definition and a query pattern for each, and maps your pipeline stages to what must be true at every one. The output is a reference every rep, analyst, and downstream skill reads from, so "what does this field mean?" has one answer instead of five.

## What you'll need
You do not need to connect anything to get value today. Describe your process and the skill builds the library now. Connect your CRM and it reads your real field names and fill rates so the library reflects what you actually have.

- Works today with: a description of your sales process, your stages, and the decisions you make from CRM data. Paste it and go.
- More powerful connected to a CRM: it reads your actual objects, field names, and fill rates, so the library names real fields and flags the dead ones.
- Sharper with your reporting: it ties each field to the report or metric that depends on it, so you know what breaks if it goes empty.
- Sharper with your process docs: it aligns the stage matrix to the methodology you already run.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on what you describe today and gets sharper as you connect tools. It never invents a field name it cannot see, and never assumes a field is filled when it is not. A gap is a prompt, not a guess.

- **Bring your data**: describe your process, stages, and the fields you lean on. The skill drafts the full field library and stage matrix today.
- **Connect your tools**: the same skill reads your real objects and fill rates, so the library names actual fields and flags the ones sitting empty.
- **Just exploring**: no CRM access yet? Get the framework, the definition template, and a worked example, so you see the shape before you build.

Every run ends with the one thing that would sharpen the next build, a field to standardize or a tool to connect.

## Customize this for yourself
This was built to be CRM-agnostic. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| OBJECTS | the records you run GTM on | Account, Opportunity, Contact, Lead |
| CORE_FIELDS | the fields that drive decisions | your own short list (the skill helps you find them) |
| STAGES | your pipeline stages | your real stage names |
| STAGE_TESTS | what must be true to be in a stage | your exit criteria per stage |
| ACTIVITY_SOURCES | where real engagement is logged | email, calls, meetings, product |
| OWNERS | who is accountable for each field | rep, manager, ops, system |

The library is yours. The skill's job is to cut the field sprawl down to the ones that actually change a decision, and to lock what each one means so a report never lies.

## The method

### Name the fields that drive decisions
Most CRMs carry hundreds of fields and use twenty. Start from the decisions you make, forecast, prioritize, route, renew, and keep only the fields those decisions depend on. Everything else is noise the library should not bless.

### Lock a definition and a query pattern per field
Every kept field gets a one-line plain definition (what it means, who sets it, when) and a query pattern (how a skill or report reads it reliably). No field enters the library without both. This is what kills the "it depends who you ask" problem.

### Build the stage matrix
Map every pipeline stage to what must be true to sit in it: the fields that must be filled, the activity that must exist, the exit test. A deal that fails its stage test is misstaged, and the matrix is what lets an analyst catch it.

### Define the activity formula
Name what counts as real engagement and from which sources, so "active" and "dark" mean the same thing everywhere. A single-source activity check lies; name the full set (email, calls, meetings, product) and how days-dark is computed.

### Flag the dead and the dangerous
Call out fields that are always empty (drop them), fields that mean different things to different teams (redefine them), and fields people game (add a guard). The library is as much about what to stop trusting as what to keep.

## Quality gates
- Every field in the library has a plain definition AND a query pattern. No entry with only one.
- The stage matrix has an explicit exit test per stage, never just a name.
- The activity formula names its sources; no single-source "active" claim.
- Dead and ambiguous fields are flagged, not silently included.
- No field is trusted on a fill rate it does not have. Low-fill fields are labeled, not assumed.

## Output (example)
```
CRM FIELD LIBRARY · [your org] · built [date]

Field                Definition                          Query pattern
Deal_Stage           where the opp sits in the process   Opportunity.StageName
Next_Step            the committed next action + date    Opportunity.Next_Step__c
Champion_Identified  a named internal advocate exists    Contact role = Champion
Last_Activity_Date   most recent real engagement         max(email, call, meeting)

STAGE MATRIX (exit tests):
  Discovery -> problem named + next step set + 1 meeting logged
  Validation -> champion identified + success criteria written
  Commit -> mutual plan + close date defended by activity

ACTIVITY FORMULA:
  active = any of {email reply, call connect, meeting held, product use}
  in last 21 days; else days-dark = today - last of those

FLAGGED:
  - Lead_Source (32% filled) -> unreliable for routing, fix or drop
  - "Engaged" (means 3 different things by team) -> redefine
```

## Example chat
Here is the skill turning a messy CRM into a trustworthy reference.

**You:** Our Salesforce has like 180 fields and reps fill maybe 20. Build me a field library that an analyst can actually trust.

**Claude:** The fix is not documenting all 180, it is blessing the ones that drive decisions and flagging the rest. Here's the core cut:
```
Field               Definition                     Owner    Query
Deal_Stage          stage in the process           rep      Opportunity.StageName
Next_Step           committed next action + date    rep      Next_Step__c
Amount              expected ACV                    rep      Opportunity.Amount
Last_Activity_Date  most recent real engagement     system   max(activities)
```
The thing worth catching: you have a "Priority" field filled on 11% of records. An analyst that trusts it will rank on garbage. I'd flag it as do-not-trust until fill rate clears the bar, or drop it. Same for any field where two teams disagree on the definition.

**You:** What about our stages? Reps sandbag everything in "Discovery."

**Claude:** That is a stage-test problem, so I'd write an explicit exit test per stage: no deal sits in Discovery without a named problem, a set next step, and one logged meeting. Once the matrix exists, an analyst can flag every deal that fails its own stage test, which is exactly how you catch the sandbagging. One sharpener: connect Salesforce and I'll pull real fill rates per field, so the library names your actual dead fields instead of me guessing which ones reps skip.

## Go further
The library is step one. Here is where an operator takes it once it holds.

- **Feed it to every analyst skill.** Point your deal-health, book-of-business, and forecast skills at the field library so they all read the same definitions and the same stage tests, no drift.
- **Run a nightly hygiene check.** Have a scheduled Claude task scan Salesforce or HubSpot against the library and DM owners in Slack the records missing a required field for their stage.
- **Version it when the process changes.** Keep the library in Notion or GitHub so a stage-model change updates one doc and every downstream skill inherits it.

Define the fields once, and every report and every skill stops arguing about what they mean.

## Where the inputs come from
The core-field list, the stage tests, and the activity window are yours to set. The examples here suited a mid-market sales process. If you run a longer enterprise cycle or a self-serve motion, retune the stages and the days-dark window. The logic, keep decision-driving fields, define them once, test the stages, does not change.

## Make it yours
Fork it. Change the objects, the fields, the stage matrix, the activity formula. The point is not to adopt someone else's schema. It is to make your CRM mean one thing to everyone who reads it. Built by an operator. Customize it, break it, make it better.
