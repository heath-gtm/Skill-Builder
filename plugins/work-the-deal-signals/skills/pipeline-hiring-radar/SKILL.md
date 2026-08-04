---
name: pipeline-hiring-radar
description: Read job postings at accounts already in your pipeline as deal signals, not prospecting fodder. Four reads per posting (problem hire, owner hire, leadership change, freeze or takedown), each tied to a named deal and converted into one dated move. Built for AEs and CSMs, customizable to your product and CRM. Trigger on "what are my accounts hiring for", "job postings at my accounts", "hiring signals on my pipeline", "read this job posting as a deal signal".
---

# Pipeline Hiring Radar

## What this does
Watches job postings at the accounts already in your pipeline and customer book, and reads each one as a deal signal. A posting can mean the timing just got better, a new stakeholder is about to arrive, the decision dynamics are about to shift, or the budget is about to disappear. This skill makes the read, ties it to the specific deal or renewal it affects, and names one dated move on that deal. It is not a prospecting tool. If the account is not already in play, it is out of scope. Where trigger-outreach takes any buying signal and writes a timely cold-ish touch for new accounts, this skill is scoped to accounts already in play and its output is a deal move, not an outreach sequence.

## What you'll need
You do not need to connect anything to get value today. Bring your account list and the skill runs now. Connect the tools below and it pulls postings automatically instead of you checking careers pages by hand.

- Works today with: your open-opp and renewal account list, plus a manual careers-page check on the top 10. Paste the postings you find.
- More powerful connected to an enrichment tool with job-postings data (Clay, Common Room): postings arrive on their own, across the whole book.
- Sharper with a CRM: deal stage, close date, and renewal date attach to each read automatically.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a posting it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste your in-play account list and whatever postings you found on their careers pages. The skill runs the full read today. No connection required.
- **Connect your tools**: the same skill pulls postings from a jobs-data source and deal context from your CRM automatically. Same output, less effort, wider coverage.
- **Just exploring**: no accounts yet? Get the four reads, the exact fields the radar uses, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, an account to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS seller with a mixed book of opps and renewals. Set these to your world:

| Set this | What it is | Default / Example |
|---|---|---|
| PROBLEM keywords | role keywords that mean your problem | "revenue operations", "sales enablement", "data quality" |
| OWNER titles | the titles that would own your product | Head of RevOps, Director of Sales Ops |
| CHECK cadence | how often the radar sweeps | weekly (re-tune to your cycle length) |
| ACCOUNT scope | which accounts are in play | open opps, active trials, renewals inside 6 months, expansion targets |

The scope rule is the whole skill. Open opps, active trials, renewals inside 6 months, and named expansion targets are in. Everything else is out, no matter how interesting the posting.

## The method

### Read 1: They are hiring for the problem you solve
A posting that describes the pain your product removes is a timing signal. Someone got budget to fix the problem, and headcount is the expensive way to fix it. The move belongs on the live deal: raise the posting's problem statement in your next call and position against the cost of the hire, not against a competitor.

### Read 2: They are hiring the role that would own your product
A posting for the title that would run your tool means a new stakeholder is entering the deal. Get there first. If the deal closes before they start, you want the incumbent tool to be yours. The move: ask your contact who is hiring for it and what the new owner will walk into, and get your product into the onboarding conversation.

### Read 3: A leadership change posting
A VP or C-level posting at an in-play account means the decision dynamics are about to shift. Your current buyer may lose authority, your deal may get re-litigated, your renewal may get re-evaluated by someone with no history with you. The move: pressure-test the deal's approval path now, before the new leader lands, and get the business case in writing.

### Read 4: A hiring freeze or posting takedown
Postings that vanish, or a public freeze, are budget risk on the deal. If they stopped hiring for the problem, they may stop buying for it too. The move: qualify the budget directly this week, and if it is a renewal, move the value conversation up before the cut list gets written.

## Quality gates
- A posting is a hypothesis, not a fact. Verify before you act on it. Postings go stale, get reposted by agencies, and sit open for roles already filled.
- Never quote a posting back to a prospect verbatim in a way that reads as surveillance. Reference the problem, not the paragraph.
- Tie every read to a named deal or renewal, or it does not count. A signal with no deal attached is trivia.
- One move per read, with a date on it. A read that ends in "monitor" is not a read.

## Output (example)
```
PIPELINE HIRING RADAR · sample data · 4 in-play accounts
Account     Deal / Stage       Posting seen           Read              Move (dated)
Acme Corp   Opp / Proposal     Sr RevOps Manager      Owner hire        Ask contact who owns onboarding, by Fri
Northwind   Renewal / 90 days  VP Sales (new role)    Leadership shift  Get business case in writing, this week
Vertex      Opp / Eval         "fix pipeline data"    Problem hire      Position vs cost of hire, next call Tue
Blend Labs  Trial / Active     3 postings pulled      Freeze risk       Qualify budget directly, call Wed

Out of scope this run: 2 postings at accounts with no open deal. Logged, not read.
```

## Example chat
Here is the skill running on a real book, start to finish.

**You:** What are my accounts hiring for? Here's my open-opp list, and I checked the careers pages on my top 10. [pastes list and postings]

**Claude:** Ran the four reads on the 6 postings that map to in-play accounts.
```
Account     Deal / Stage       Posting              Read
Northwind   Renewal / 90 days  VP Sales (new role)  Leadership shift
Vertex      Opp / Eval         Sr RevOps Manager    Owner hire
```
The one that matters: Northwind is hiring a new VP Sales 90 days from renewal. Whoever lands will re-evaluate every tool in the stack with zero history with you. The move: get the renewal business case in front of your current buyer in writing this week, so the new VP inherits a documented decision, not an open question.

**You:** Read this posting at Vertex as a deal signal. It's for a Senior RevOps Manager.

**Claude:** Owner hire. That title would own your product day one, which means a new stakeholder enters your eval mid-deal. Two things before you act: verify the posting is live and recent, not a repost, then ask your contact directly who is running the hire and what the new person walks into. Do not mention you saw the posting. The move: propose that your pilot results become part of the new hire's onboarding packet, dated to your Thursday call. One sharpener: connect Clay or Common Room so the radar sweeps the whole book weekly instead of your top 10 by hand.

## Go further
The read is step one. Here is where an operator takes it once the manual version proves out.

- **Automate the sweep.** Connect Clay's job-postings enrichment or Common Room so every in-play account is checked on your cadence, not just the 10 you have time for.
- **Schedule the radar.** Set up a scheduled Claude task to run the sweep every Monday and post the reads that touched a named deal to your Slack channel before pipeline review.
- **Attach reads to the record.** Push each read into the Salesforce opportunity as a logged signal, so the deal history shows what you saw and when you moved.
- **Watch the people, not just the postings.** LinkedIn shows when the owner-hire role gets filled. The start date of that person is a calendar event on your deal.

The radar is only as good as its refresh rate. Automate the sweep, keep the judgment.

## Make it yours
Fork it. Change the keywords, the titles, the cadence, the scope rule. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
