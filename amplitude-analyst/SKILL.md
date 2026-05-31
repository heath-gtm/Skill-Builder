---
name: amplitude-analyst
description: Your product usage analyst. Connect Amplitude — turns any "how are they using us?" question into a product engagement read: 11-capability adoption rubric, 12-week trend analysis, new user signals, Ghost-Active detection, Aero False-Negative detection, power-user identification, WAU/DAU at gp:domain grain. Use when a rep needs a single account's product story, finds expansion signals, surfaces new signups at customer accounts, or validates an Aero score. Trigger on "how is {account} using us?", "is {domain} active?", "find power users at {company}", "who signed up at customer accounts this week?", "is Aero right about {account}?", "is {account} ghost-active?", "what capabilities have they not adopted?", "show me onboarding gaps", "find product-qualified leads", "are they an Aero false negative?", or any product engagement question. Also fire when a CSM preps a QBR or a rep gets a meeting from a free account.
---

# Amplitude Analyst — your product usage analyst

**Required connector:** Amplitude (with appropriate read scope on the project — Mixmax production project is 130895).

**Optional dependencies:** Salesforce (for cross-referencing accounts to gp:domain — without it, the analyst works on bare domain inputs); Aero (for false-negative detection if Aero is connected).

## What this analyst answers

In plain English, the Amplitude Analyst answers questions like:

- "How is Acme Corp using Mixmax?" → 11-capability adoption tier card with 12-week trends
- "Is acme.com active?" → WAU/DAU + capability breadth + last-7-day activation status
- "Find power users at Datadog" → individual user IDs with breakdown of which capabilities each uses heavily
- "Who signed up at customer accounts in the last 14 days?" → new_users_14d list per domain, with activation status of each new signup
- "Is Aero right about Vortex?" → Cross-check Aero PES vs Amplitude reality. Ghost-Active detection (high `_active` but every capability zero) and Aero False-Negative detection (Aero PES floor but real adoption present)
- "What capabilities has acme not adopted yet?" → Untouched / Never-adopted list — the onboarding gap that drives consultative CSM outreach
- "Find product-qualified leads from the last 30 days" → Self-serve signups with high capability adoption that meet the PQL threshold
- "Show me onboarding gaps across HM's book" → For every account HM owns, surface the new users who haven't activated yet — the soft expansion conversation

## What it owns internally (the micro skills it composes)

The Amplitude Analyst is the product layer over these atomic skills:

- **D2 — Amplitude Product Engagement** — pulls the 11-capability rubric at gp:domain grain
- **A3 — Play Type Classifier (product side)** — uses Amplitude signals to inform ACTIVATE / CONVERT / EXPANSION / NURTURE play classification
- Override detection — Ghost-Active and Aero False-Negative (lock-in inherited from `product-engagement-story` skill)
- New-user signal computation (lock-in #18) — `new_users_14d`, `new_users_30d`, first-seen event analysis

## The 11-capability rubric this analyst tracks

1. **Email sends** — baseline activity
2. **Sequences** — outbound cadence usage
3. **Templates** — content reuse
4. **AI follow-ups** — Mixmax AI Compose for follow-ups
5. **AI Compose** — AI-drafted outbound
6. **Calendar enhancements** — meeting scheduling features
7. **Meeting Copilot — recording**
8. **Meeting Copilot — transcripts**
9. **Smart Send AI** — send-time optimization
10. **Sequence-server activations** — automated rep activation
11. **Baseline `_active`** — any product engagement at all (the "ghost-active" detector compares this against the other 10)

Per capability, the analyst returns:

- **Adoption tier:** Power / Established / Emerging / Dormant / Untouched / Never-adopted
- **12-week trend:** Rising / Flat / Declining / Collapsed
- **Last activation date**

## The quality gate this analyst guarantees

**Ghost-Active detection** — when an account looks healthy in the baseline `_active` metric but every other capability is zero, the analyst flags this. This is a classic CSM blind spot: a customer's seats are technically active (rep logs in once a week) but no value is being created.

**Aero False-Negative detection** — when an account's Aero PES score is at the floor (suggesting Aero thinks they're dead) but Amplitude shows real capability adoption, the analyst overrides Aero and promotes the account in any queue. The Daily Drop and Account Brief Pipeline both use this override; the analyst owns the detection.

Both overrides log a row to `Revenue Reviews/aero_feedback_queue/{YYYY-MM}.tsv` (lock-in #8) for Heath to share with the Aero team.

## Output format example

For "How is Acme Corp using us?":

```
🔬 ACME CORP — Product Engagement Story (Amplitude · gp:domain)
   12-week window · Mixmax project 130895

📊 11-Capability Rubric
┌────────────────────────────────┬─────────────┬──────────┬─────────────┐
│ Capability                     │ Adoption    │ Trend    │ Last Active │
├────────────────────────────────┼─────────────┼──────────┼─────────────┤
│ Email sends                    │ Power       │ Rising   │ today       │
│ Sequences                      │ Established │ Flat     │ yesterday   │
│ Templates                      │ Emerging    │ Rising   │ 3d ago      │
│ AI follow-ups                  │ Dormant     │ Declining│ 18d ago     │
│ AI Compose                     │ Untouched   │ —        │ —           │
│ Calendar enhancements          │ Power       │ Rising   │ today       │
│ Meeting Copilot — recording    │ Established │ Rising   │ 2d ago      │
│ Meeting Copilot — transcripts  │ Established │ Flat     │ 2d ago      │
│ Smart Send AI                  │ Never-adopt │ —        │ —           │
│ Sequence-server                │ Established │ Flat     │ 5d ago      │
│ _active baseline               │ Power       │ Rising   │ today       │
└────────────────────────────────┴─────────────┴──────────┴─────────────┘

✅ NOT Ghost-Active — 7 of 10 capabilities show real activity
✅ NOT Aero False-Negative — Aero PES 99.7 matches Amplitude reality
👥 WAU latest: 351 · 4-week avg: 339 (Rising) · 12-week peak: 358
🆕 New users 14d: 8 signups · 5 activated within 7d · 3 still untouched

🧠 Story: Acme is a Power email + calendar user with rising AI follow-up + Meeting Copilot adoption. The onboarding gap is AI Compose + Smart Send. 3 new users from the last 14 days haven't activated — that's the CSM's consultative outreach.

Suggested play: EXPANSION (currently DS customer, healthy footprint, growing trend, with clear onboarding gaps for the new 3 users — soft expansion conversation embedded in the activation push).
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** (required for in-product briefs)
- **W3 Daily Drop** (required — new-user signal drives lead ranking)
- **W4 Customer Strategy Suite** (required)
- **W6 Customer Interview Prioritizer** (required — capability breadth scoring)
- **W7 Reference Customer Finder** (required — power user identification)
- **W9 Power-User Activation** (required — heavy individual user finder)
- **W10 Expansion Opportunity Scanner** (required — capability adoption jump detector)
- **W13 Quiet Quitting Detector** (required — declining usage signal)

## When NOT to use this analyst

- For deal / pipeline questions (use Salesforce Analyst)
- For "what did we say" questions (use Conversation Analyst)
- For accounts that aren't in Amplitude yet (cold prospects with no signups)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.Website (canonical → gp:domain join, § 10)
- Account.Aero_Product_Engagement_Score__c (override detection)
- Writes back: Product_Engagement_Verdict__c, Product_Engagement_Last_Run__c, Product_Engagement_Active_Latest__c, Aero_False_Negative__c (§ 1)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-ins #14 (play type override contract — Ghost-Active and Aero False-Negative), #18 (new user signal), and the override row format for `aero_feedback_queue/`. Read `Account Brief Pipeline/LOCKED_DESIGN.md` and the `product-engagement-story` SKILL.md before any invocation.

## Shippable as

A connector-gated capability. Customer connects Amplitude → Amplitude Analyst becomes available. Without the connector, the skill responds "Connect Amplitude to enable product usage analysis." Most powerful when paired with Salesforce Analyst — together they unlock account-level + product-level synthesis.
