---
name: salesforce-analyst
description: Your deal analyst. Connect Salesforce — turns any "what's happening with this deal/account?" question into structured output: deal-risk classification, 4-source activity check, PLAN-vs-stage validation, Deal Health Summary, account context across 22 custom fields. Use when a rep or leader needs to understand a single account, audit a deal, prep for a pipeline review, or scan a book for risk. Trigger on "analyze {account}", "deal review on {opp}", "is {deal} healthy?", "what's stuck in my pipeline?", "deal autopsy on {closed lost}", "where am I missing PLAN coverage?", "show me at-risk renewals", "is this opp realistic?", "give me a deal health check", or any account / opp / pipeline diagnostic. Also fire when a leader walks into a 1:1 and says "review {AE}'s pipeline" or "what should I coach on?" Knows where to look in SFDC and what classifies as a real flag vs noise.
---

# Salesforce Analyst — your deal analyst

**Required connector:** Salesforce (Sales Cloud, Service Cloud, or any SFDC org with read access via the Salesforce MCP).

**Optional enrichment:** FullEnrich · Common Room · Octave. None required — Salesforce alone unlocks the full analyst capability.

## What this analyst answers

In plain English, the Salesforce Analyst answers questions like:

- "What's happening with Acme Corp?" → 60-second account summary with current state, last activity, PLAN gaps, risk flag
- "Run a deal review on the Acme renewal" → PLAN-based strategic read with risk classification + recommended next move
- "Is the customguide.com deal healthy?" → Deal risk verdict + 4-source activity audit + days dark
- "What's stuck in Karan's pipeline?" → Cross-deal Deal Health Summary with compound-risk Top 3 intervention priorities
- "Deal autopsy on Mirakl" → Closed-lost analysis with stage-by-stage timeline + champion analysis + preventability verdict
- "Where am I missing PLAN coverage?" → Pipeline-wide PLAN-vs-stage validation: every deal that's advancing without the discovery / leverage / decision-dynamics groundwork
- "Show me at-risk renewals closing in 30 days" → Renewal Slip Forecast with risk-adjusted ARR exposure
- "Is this opp realistic?" → PLAN-vs-stage check + activity recency + champion drop-off detection — surfaces deals where rep status doesn't match underlying signal

## What it owns internally (the micro skills it composes)

The Salesforce Analyst is the product layer over these atomic skills from the skill atlas (`Revenue Reviews/specs/skill_atlas.md`):

- **D1 — SFDC Account+Opp Pull** — 22 custom fields per lock-in #26 (current + forecasted ARR, the 4 PLAN Selling fields, tech stack, Decision Maker, Common Room enrichment)
- **A1 — Deal-Risk Classifier** (lock-in #16) — every open opp classified as AT_RISK / SLIP_RISK / GHOST / CHAMPION_DROP / STUCK / STALE / MOMENTUM / HEALTHY
- **A2 — Deal Health Summary** (lock-in #27) — 10-stat dashboard + compound-risk-scored Top 3 intervention priorities
- **A3 — Play Type Classifier** (lock-in #14 v7) — 8 plays: ACTIVATE / CONVERT / EXPANSION / RECOVERY / RENEWAL DEFENCE / COLD OUTBOUND / NURTURE / PASS
- **A5 — PLAN-vs-Stage Validator** (lock-in #26 + #27) — the "rep is BS'ing the deal" detector
- **O4 — SFDC Contact Write-Back** (lock-in #13) — when paired with enrichment data, creates/updates SFDC Contacts

## The quality gate this analyst guarantees

**Multi-source activity check (lock-in #16 v9.1 amendment)** — every "days since last activity" claim is computed as `MAX(Account.LastActivityDate, Opportunity.LastActivityDate, MAX Task.ActivityDate where AccountId/WhatId/WhoId matches AND Status='Completed', MAX Event.ActivityDate)`.

This solves the classic Salesforce reporting bug where Opp-level `LastActivityDate` is null because reps log emails/meetings at the Account or Contact level. Single-field reads systematically miss real activity. The Salesforce Analyst never makes this mistake.

Confirmed via the Daily Drop incident 2026-05-28: Guesty (HM had a meeting today + 6 reply emails) and Blend Labs (Petra Lovric replied yesterday) were falsely flagged as "zero activity" by a single-field check. With the multi-source check, both correctly classified as ACTIVE.

## Output format example

For "Analyze Acme Corp":

```
🎯 ACME CORP — Customer · $147.7K ARR · CSM: HM Pusztai

🚨 Verdict: REACH_OUT (RENEWAL DEFENCE play)
   Aero False-Negative confirmed: PES 28 but 351 active users + 7/10 capabilities adopted
   Last activity: TODAY (Account level) — 6 email replies from Megan Botting + meeting in 1h
   Days in current stage: 12d (Stage 7 — Almost Certainly Will)
   PLAN completeness: 4/4 — Problems · Leverage · Decision Dynamics · Next Steps all set
   
🧠 The PLAN
   PROBLEMS: Inbox plateau, no signal on adoption depth
   LEVERAGE: Multi-team rollout — Sales, RevOps, CS all on Mixmax
   DECISION DYNAMICS: Jim Coulon (CFO) signs · Sarah Chen (RevOps) champions
   NEXT STEPS: Finalize commercial terms by 6/15

🛠 Tech Stack: Gmail · Salesforce · Outreach
⭐ Decision Maker: Jim Coulon (CFO)
🔥 Hiring 14 sales reps at this account — expansion signal

Next move: HM's meeting at 12:30pm today. Stage 7 means commercial close is the gate; usage health is solid.

[Open in CRM ↗] [Full brief ↗]
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** (required)
- **W2 Leader Brief Generator** (required)
- **W3 Daily Drop** (required)
- **W4 Customer Strategy Suite** (required)
- **W5 Pipeline Analysis Manual** (required)
- **W6 Customer Interview Prioritizer** (required)
- Future workflows W7-W13 (all require)

## When NOT to use this analyst

- For product usage questions (use Amplitude Analyst instead)
- For "what did we last talk about" questions (use Conversation Analyst instead)
- For pure Salesforce CRUD with no analysis (use the Salesforce MCP directly)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.* (all 22 GTM custom fields per § 1)
- Opportunity.* (full set including PLAN fields, ForecastCategoryName, Channel__c)
- Contact.* (Email, Phone, MobilePhone, Title, LeadSource, LastActivityDate)
- Task / Event via salesforce_query_activities() (canonical 4-source check, § 8)
- OpportunityContactRole (multi-thread check, § 6 + § 10)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-ins #14 (play type), #16 v9.1 (multi-source activity), #19 (role boundaries), #26 (22 custom fields + PLAN Selling), #27 (Deal Health Summary). Read `Account Brief Pipeline/LOCKED_DESIGN.md` before any invocation.

## Shippable as

A connector-gated capability. Customer connects Salesforce → SFDC Analyst becomes available. Without the connector, the skill should respond "Connect Salesforce to enable deal analysis."
