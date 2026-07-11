---
name: daily-sales-assistant
description: Compose deal risk, pipeline, coaching, and conversation reads into one morning brief that names today's priorities. Runs in rep mode (your accounts today: risk flags, hot leads, follow-up drafts) or leader mode (your team today: coaching priorities, must-win status, per-rep gaps). Built for GTM teams, customizable to your stack and your cadence. Trigger on "morning brief", "what should I work on today", "today's priorities", "run my morning", "team morning brief", "pre-1:1 brief", or any rep or leader morning-priorities request.
---

# Daily-Sales-Assistant

## What this does
This is a workflow, not a single check. It composes the reads you would otherwise run one by one, deal risk, pipeline health, coaching signals, and conversation follow-ups, into one brief that opens your day. Rep mode answers "what are my three priorities today" and drafts the follow-ups. Leader mode answers "what does my team need today" with named coaching priorities and must-win deal status. One workflow, a different brief per role.

## What you'll need
You do not need to connect anything to get value today. Bring your book and the skill runs now. Connect the tools below and it composes the brief automatically each morning.

- Works today with: your open deals and today's meetings. Paste or upload a list with stage, amount, close date, last activity, and the contacts. A CSV is enough to produce a brief.
- More powerful connected to a CRM: it reads your whole book and pipeline coverage automatically.
- Sharper with a meeting or email tool: it adds today's meetings, prep links, and follow-up drafts.
- Sharper with a product-analytics tool: it adds usage signal to the hot-leads and expansion reads.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your book (a deal export, today's calendar). The skill composes the full brief today on your real numbers. No connection required.
- **Connect your tools**: the same workflow pulls deals, meetings, and drafts automatically and fires each morning without you asking. Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the sections each mode produces, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next brief sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B GTM team running a rep-and-leader cadence. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| MODE | which brief you get | rep (your accounts) or leader (your team) |
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| MEETING source | where today's meetings and threads live | your calendar, a meeting or email tool |
| FIRE_TIME | when the brief lands | 07:00 local, adjustable per user |
| DELIVERY | where it goes | a messaging DM or a channel |
| INCLUDE_DRAFTS | auto-draft follow-ups (rep mode) | true, drafts land for review, never auto-sent |
| PRIORITY_COUNT | how many top priorities to name | 3 |

Point it at your book and your calendar, not anyone else's. The workflow composes whatever reads you have wired up.

## The method

### Rep mode: your accounts today
Compose the reads that decide your day and rank them into three named priorities.
- **Hot leads**: who engaged or replied recently and has no follow-up yet.
- **At-risk deals**: the opps in your book that are slipping, stuck, or gone dark, with the multi-thread gaps.
- **Meetings today**: what is on the calendar and the prep link for each.
- **Drafted follow-ups**: the highest-priority gaps, drafted and dropped in your drafts folder for review.
- **Bonus**: one account that needs attention this week before it becomes a problem.

### Leader mode: your team today
Compose the reads that decide where your attention goes.
- **Coaching priorities**: named rep, named issue, tied to today's 1:1s.
- **Must-win deals**: status and flags across the team.
- **Pipeline coverage**: which channel is the gap and who owns closing it.
- **1:1s today**: each with a pre-1:1 brief.
- **Escalation**: anything that needs leadership today, honestly "none" when it is none.

### Prioritization is forecast-aware
The brief knows when today is the forecast call and leads with the deals that decide it. Priority is not the loudest item, it is the one that moves the number.

## Quality gates
- Drafts are review-first. Follow-up drafts land in a drafts folder, never auto-sent, unless the user explicitly opted in.
- Empty days surface honestly. Nothing critical means "nothing critical today, here is where to invest instead," never invented urgency.
- Every priority names the specific action and the specific account or rep, never "follow up on deals."
- Leader mode names the rep and the issue together, never a standings table with no next move.

## Output (example)
```
REP MODE · Monday June 1

TOP 3 PRIORITIES TODAY
  1. Reply to the Acme contact who said "interested" 2 days ago. Every day cools the reply.
  2. Prep the 2pm with Vortex, a $67K deal now at slip risk.
  3. Unstick Blend Labs: day 30, no touch sent, milestone missed.

HOT LEADS (5)
  Acme, replied 2d ago, no follow-up · Vortex, booked yesterday · Globex,
  opened 4 emails in 3d · Blend, clicked pricing yesterday · PGA, asked for info 5d ago

AT-RISK DEALS (3)
  Vortex, slip, champion dark (today's meeting is the test)
  Blend Labs, stuck, no next step set
  Globex trial, ghost, 47 days no activity (declare lost?)

MEETINGS TODAY
  10:00 pipeline review · 2:00 Vortex (prep link) · 4:30 Blend Labs intro

DRAFTED FOLLOW-UPS (in your drafts, review and send)
  To Acme: "Quick demo this week?" · To PGA: "Sending the resources"

BONUS
  Halborn: champion just changed jobs. Re-thread the backup contact this week
  or risk the renewal.
```

## Where the numbers come from
The three-priority cap, the 07:00 fire time, and the review-first draft rule are defaults, not laws. They suited a daily seller-and-leader rhythm. If your day starts earlier or you want five priorities, change them. The logic does not change. The settings are yours.

## Make it yours
Fork it. Change the modes, the sections, the delivery, the fire time. The point is not to run someone else's morning. It is to open yours with the next three moves already named. Built by an operator. Customize it, break it, make it better.
