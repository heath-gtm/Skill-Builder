---
name: renewal-health-analyst
description: Your per-renewal analyst. Connect Salesforce + Amplitude + Mixmax — turns any "will this renewal happen?" question into a per-deal verdict: renew y/n + value + conditions, champion stability check (still at company? still engaged?), PES adoption story for the pitch, commercial lever inventory, save-play prerequisites. Different from Book-of-Business (portfolio view) — this is per-renewal depth. Trigger on "will {account} renew?", "renewal verdict on {account}", "is {customer}'s renewal real?", "prep for {account} renewal", "what should I offer {account}?", "save play for {account}", "commercial levers on {customer}", "champion check on {account}", "renewal pitch for {customer}", or any single-renewal question. Also fire when a CSM is prepping a renewal conversation.
---

# Renewal-Health Analyst — your per-renewal companion

**Required:** Salesforce + Amplitude. **Optional:** Mixmax (champion-conversation depth), Intercom (support pulse).

## What this analyst answers

- "Will {account} renew?" — per-deal verdict + confidence
- "What value will they renew at?" — flat / upsell / downgrade prediction
- "Is the champion still there?" — LinkedIn + activity cross-check
- "What's the adoption story I bring to the pitch?" — PES (Product Engagement Story) summarized
- "What commercial levers can I pull?" — discount, term, expansion, multi-year inventory
- "What needs to happen before the renewal call?" — save-play prerequisites

## What it owns internally

- **Per-renewal verdict engine**: combines product adoption + champion stability + support sentiment + competitive intel
- **Champion stability check**: SFDC contact still active + LinkedIn current title + recent engagement
- **PES adoption story** (composes product-engagement-story skill): 11-capability adoption read framed for renewal pitch
- **Commercial lever inventory**: term length, discount headroom, expansion options, multi-year incentives
- **Save-play prerequisite checklist** (composes customer-battle-plan skill)

## Quality gates

**No renewal verdict without champion check.** If the named champion has left the company or hasn't engaged in 90 days, the verdict downgrades automatically.

**PES adoption story is named-capability.** Not "good usage" — instead, "uses Sequences (Power), Smart Send AI (Established), Meeting Copilot Recording (Emerging), but has not adopted AI Compose or Calendar Enhancements."

**Save plays are sequenced.** Day 0 / Day 7 / Day 14 with branch logic for responds / ghosts / rejects.

## Output format example

```
🎯 ACME CORP RENEWAL · Closes 2026-08-15 · $187K ARR

VERDICT: RENEW + EXPANSION POSSIBLE · Confidence: 78%

Champion stability:
  ✅ Sarah Chen still at Acme (verified LinkedIn 2026-05-28)
  ✅ Sarah engaged in 6 of last 12 weeks (above customer median)
  ⚠ Second-thread Mike Rodriguez left Acme March 2026 — single-thread risk

PES adoption story (for the pitch):
  Power:        Sequences, Smart Send AI
  Established:  Templates, Meeting Copilot Recording
  Emerging:     AI Compose
  Untouched:    Calendar Enhancements, AI Follow-ups
  → Story: "You've crushed core outreach + AI Send. The Calendar suite is 
            your next compounding lever."

Commercial levers available:
  • Multi-year (3-yr at flat = $561K committed) ← STRONGEST
  • 12% discount headroom (down to $165K)
  • Add Calendar bundle (+$48K expansion)
  • Annual prepay (5% off)

Save-play prerequisites:
  ☐ Re-thread to a second champion (Sarah's #2 left)
  ☐ Run a Calendar Enhancement demo
  ☐ Confirm budget cycle aligns with August close
  ☐ Pre-position the multi-year offer 30 days out

Recommended pitch: Multi-year + Calendar expansion. Project value: $609K over 3yr.
```

## Used by

- **CS-leader-weekly-report** workflow (must-save section)
- **CSM-book-of-business** workflow (renewal queue depth)
- **Daily-Sales-Assistant** workflow (renewal-day mode)
- Standalone for renewal conversation prep

## When NOT to use

- For portfolio-level book health (use Book-of-Business Analyst)
- For new-business deals (use Deal-Health Analyst)
- For multi-touch save sequence drafting (use Comms Analyst + customer-battle-plan)

## Inheritance from LOCKED_DESIGN.md

Lock-ins #7 (Renewal Defence play type), #14 v7 (Aero override), #28 (Deal Health Summary), product-engagement-story skill.

## Make.com / API packaging

**Input:** `{ account_id: string, mode: "verdict | pitch_prep | save_play_prereq | commercial_levers" }`

**Output:** `{ verdict, confidence, renewal_value_prediction, champion_check, pes_story, commercial_levers, save_play_prereqs }`

**Failure modes:** No Amplitude → falls back to qualitative PES read. No Mixmax → champion check is SFDC-only (lower confidence).

## Shippable as

Standalone connector-gated SKU. Make.com node. The CSM's pre-renewal-call companion.
