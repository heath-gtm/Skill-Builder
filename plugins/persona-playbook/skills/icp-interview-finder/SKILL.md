---
name: icp-interview-finder
description: Your customer-interview target finder. Connect a CRM with your customer book and an ICP definition, and turn "who should I interview to validate the ICP, test the positioning, learn how they found us?" into a ranked slate of customers, each with a verdict, a three-bullet why, and one named buying-committee recipient ready for a CSM-mediated intro. Trigger on "find customers to interview", "ICP validation interviews", "test our positioning with customers", "who in my book matches the ICP", "build a customer research slate", "find reference customers", "validate the ICP with real customers".
---

# ICP Interview Finder

## What this does
Turns your customer book plus an ICP definition into a ranked slate of customers to interview. It scores every paying customer against the ICP you provide, ranks them, and returns a prioritized slate. Each customer gets a verdict, a three-bullet why grounded in real data, and one named buying-committee recipient so a CSM can make a warm intro. The slate ships in two tiers, a small Priority set you book first and a larger backup set, plus a watchlist of who it considered and dropped, with reasons.

## What you'll need
You do not need to connect anything to start. Bring two things and the skill runs today: your customer book and your ICP definition. Connect a CRM and it pulls the book automatically.

- Works today with: (1) your customer list (who is a customer, who owns them, firmographics, revenue, key contacts) pasted or uploaded, and (2) your ICP definition, pasted as criteria or pointed to as a doc. The skill reads the criteria you give it; it never bakes in a rubric.
- More powerful connected to a CRM: the full customer book with owners, firmographics, revenue, and the contact graph, live.
- Sharper with a product-usage source, a meeting-history source, a publishing target, and an outreach drafter.

If you have neither a customer list nor an ICP definition, the skill gives you the framework and names the inputs it needs, then waits. It does not invent a customer or a criterion.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload what you have (a CSV or an export). The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (live activity, product usage, history). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.
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

## Example chat
Here is the skill running on a real customer book, start to finish.

**You:** Find me customers to interview for the ICP validation round. Here's our customer book and the ICP doc.

**Claude:** 49 managed customers, 24 matched the ICP, 6 made Priority.
```
1. Northwind Logistics - ICP 100 - Priority
   200 emp - US - Professional Services - full stack match - 5yr+
   WHY: sweet-spot size, 5+ year tenure, high product engagement
   NEXT MOVE: CSM intros the Founder
```
The catch worth flagging: Cedar Retail scored an 82, which would normally make the slate, but it's sitting in an anti-pattern vertical your ICP doc explicitly calls out. That's why the watchlist exists, a good score isn't the same as a good interview. One sharpener: connect a product-usage source so tenure isn't the only proxy for "can actually answer the five questions."

## Go further
The slate is step one. Here is where an operator takes it once the manual version proves out.

- **Refresh the slate every quarter automatically.** Run a scheduled Claude task against Salesforce each time the customer book changes, and re-rank against the same ICP doc.
- **Route the intro asks for you.** When a Priority account is confirmed, drop the CSM a Slack message with the named recipient and the one-line ask, ready to forward.
- **Feed the interviews back into the ICP.** Send the answers to the five questions into a knowledge-base or Notion doc so the next validation round starts from real quotes, not a blank page.

You built the slate once, now it restocks itself.


## Make it yours
Read the ICP doc as the source of truth; do not bake in a band or vertical. Two-tier output is the point. Every Priority account names a recipient. The watchlist is the audit trail. Swap the CRM, rewrite the criteria, change the slate size; keep the spine. Built by an operator. Customize it, break it, make it better.
