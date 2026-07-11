---
name: icp-interview-finder
description: Your customer-interview target finder. Connect a CRM with your customer book and an ICP definition, and turn "who should I interview to validate the ICP, test the positioning, learn how they found us?" into a ranked slate of customers, each with a verdict, a three-bullet why, and one named buying-committee recipient ready for a CSM-mediated intro. Trigger on "find customers to interview", "ICP validation interviews", "test our positioning with customers", "who in my book matches the ICP", "build a customer research slate", "find reference customers", "validate the ICP with real customers".
---

# ICP Interview Finder

## What this does
Turns your customer book plus an ICP definition into a ranked slate of customers to interview. It scores every paying customer against the ICP you provide, ranks them, and returns a prioritized slate. Each customer gets a verdict, a three-bullet why grounded in real data, and one named buying-committee recipient so a CSM can make a warm intro. The slate ships in two tiers, a small Priority set you book first and a larger backup set, plus a watchlist of who it considered and dropped, with reasons.

## What you'll need
Two required inputs. A CRM with your customer book (who is a customer, who owns the relationship, firmographics, revenue, the contact graph). And an ICP definition (a URL or path to your canonical ICP doc; the skill reads the actual criteria from it, it does not bake in a rubric). If either is missing, stop and ask. Optional: a product-usage source, a meeting-history source, a publishing target, an outreach drafter.

## Customize this for yourself
| What to set | What it means | Default |
|---|---|---|
| CRM | Which system holds your book and contact graph | Whatever CRM you connect |
| Your ICP criteria | Size band, geography, tech stack, industry weights | Read from the ICP doc you provide |
| Book owner field | The field that marks an account as on someone's managed book | The owner field |
| How many to surface | Slate size, split Priority and backup | 5 to 7 Priority, 13 to 15 backups |
| ICP-match threshold | The composite cutoff | 78, or whatever your ICP doc names |

## The method
1. Resolve the ICP doc. Extract the size band and ceiling, primary geography, primary stack, industry set, anti-pattern verticals, and the current positioning sentence verbatim. Missing pieces: stop and ask.
2. Pull the customer book. Every paying customer on a managed book, with the fields the score needs.
3. Score every account against the ICP using the bands you extracted: a weighted composite of size, geography, stack, CRM, industry, and fit. Modifiers: tenure bucket (2 to 5 years is the freshest buyer memory), high product engagement, size out of band (flagged), anti-pattern vertical (dropped to watchlist), no senior contact (hygiene flag).
4. Pull buying-committee contacts for the top accounts. The most senior still-active contact per account; no senior contact is a hygiene flag, not a silent drop.
5. Write the Priority tier as briefs (verdict, three-bullet why, named next move with the CSM who introduces). Backups render as a compact table.
6. Build the watchlist: every account that scored above the threshold but did not make the slate, with the reason.
7. Verdict taxonomy: Interview-Priority, Interview, Interview-if-capacity, Skip-this-round.

Every account on the slate must be able to answer the five interview questions: how did you find us, what did you almost pick instead, react to this positioning sentence, what outcome are you getting you could not get elsewhere, would you recommend us and to whom. Too new to answer two or four reliably means demote to backup.

## Output (example)
```
Customer Interview Targets - ICP Validation Round
49 managed customers - 24 ICP-match - 20 slate - 6 priority

PRIORITY (book first)
1 - Northwind Logistics - ICP 100 - Priority
   200 emp - US - Professional Services - full primary-stack match - 5yr+
   WHY
   - Sweet-spot size, top-converting industry, the exact ICP shape
   - 5+ year customer with 5 renewals; long enough memory to compare positioning
   - High product engagement; can speak to outcomes, not just intent
   NEXT MOVE
   CSM intros the Founder. Frame: "we're rewriting how we describe who we sell
   to, and you're the case study."

WATCHLIST (scored well, skipping)
- Cedar Retail Co (82) - anti-pattern vertical per the ICP doc
- Summit Holdings (78) - above the size ceiling
```

## Make it yours
Read the ICP doc as the source of truth; do not bake in a band or vertical. Two-tier output is the point. Every Priority account names a recipient. The watchlist is the audit trail. Swap the CRM, rewrite the criteria, change the slate size; keep the spine. Built by an operator. Customize it, break it, make it better.
