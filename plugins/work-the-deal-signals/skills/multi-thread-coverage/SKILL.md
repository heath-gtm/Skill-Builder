---
name: multi-thread-coverage
description: Turn "who do we actually know in this deal?" into a buying-committee coverage map, a coverage score per deal by stage, and a concrete widening play for every missing role. Built for B2B sales teams, customizable to your stages and your committee model. Trigger on "buying committee coverage", "single-threaded deals", "who else should be in this deal", "widen the deal", "map the committee".
---

# Multi-Thread Coverage

## What this does
Maps the buying committee every live deal should have at its stage, checks who is actually engaged, scores the gap, and hands you the widening play for each missing role. Deal-health analysis flags single-threading as one risk state among eight and gives you a verdict; this skill goes one level deeper on that single dimension with the full committee map, a coverage score by stage, and the concrete play per missing role. It ends with a per-deal move list, not a warning.

## What you'll need
You do not need to connect anything to get value today. Bring your deals and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a deal export with the contacts and roles on each deal, plus last-activity date per contact. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads contact roles and activity across the whole pipeline automatically.
- Sharper with conversation intelligence (Gong, Fathom, Fireflies): who actually attended calls beats who is listed in the CRM.
- Sharper with your email tool: real two-way threads, not logged touches.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a contact it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your export (deals, contacts, roles, last activity per contact). The skill maps and scores every deal today. No connection required.
- **Connect your tools**: the same skill pulls contact roles, call attendance, and email threads automatically. Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the committee model, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| REQUIRED ROLES by stage | who the committee should include at each stage | Early: champion. Mid: + economic buyer, technical evaluator. Late: + end users, procurement/legal |
| ENGAGED window | days of real two-way activity that count as engaged | 30 (re-tune to your cycle) |
| YOUR stage names | map your stages to early / mid / late | Discovery, Evaluation, Proposal, Contracting |
| CONTACT ROLES | where roles live in your CRM | OpportunityContactRole |
| ACTIVITY sources | what counts as two-way | replied emails, call attendance, meetings held |

The committee model is a default, not a law. If your motion has no procurement step, delete the row. If security review is its own gate, add the role.

## The method

### Define the committee the deal should have
Every stage carries a required-roles list. Early stage needs a champion. Mid stage adds the economic buyer and a technical evaluator. Late stage adds end users and procurement or legal. A deal is not judged against the full committee on day one. It is judged against what its stage requires.

### Map who is actually engaged
Engaged means real two-way activity inside the ENGAGED window: a reply, a call attended, a meeting held. A name sitting in the CRM with no activity is not coverage. Every contact gets a role, a last-activity date, and an engaged yes or no. Names with no role get flagged for the rep to assign, not guessed.

### Score the gap
Coverage score per deal: engaged roles over required roles for that stage. A Proposal-stage deal with an engaged champion and nothing else scores 1 of 4. The score is only as honest as the activity data behind it, so the source of each engaged call is shown.

### Name the single-thread risk plainly
If one person is the only engaged contact, say so in one sentence: this deal lives or dies with one inbox. No softening. The motion that changed our win rate was moving reps from reactive-to-reply to multi-threaded, multi-channel outreach on every live deal; single-threaded deals die far more often.

### The widening play per missing role
Every missing role gets exactly one of three plays, in this order of preference:
- **Intro path through the champion.** If the champion is engaged, ask them to bring the missing role in. Draft the ask for the rep.
- **Content that earns the meeting.** No warm path? Send the missing role something worth their time: a business case for the economic buyer, an architecture doc for the technical evaluator, a rollout plan for end users.
- **Direct approach when there is no path.** Cold but targeted: a short note that names the deal context they already know exists. Last resort, still better than silence.

### The per-deal move list
Every run ends with a ranked move list: deal, missing role, chosen play, and the specific first step. One move per gap. No deal leaves the run without its next action or an explicit "coverage is full, hold."

## Quality gates
- No contact counts as engaged without a two-way activity and its date shown.
- Coverage scores name the missing roles, never just the fraction.
- The single-thread call is one plain sentence, not a paragraph of hedging.
- Every widening play names a real person or says plainly that no path exists yet.

## Output (example)
```
COMMITTEE COVERAGE · 3 live deals (sample data)
Account     Stage      Coverage   Engaged                     Missing
Acme Corp   Proposal   4/4        Champ, EB, Tech, Users      none. hold
Vertex      Eval       1/3        Champion only               EB, Tech eval
Northwind   Proposal   1/4        Tech eval only              Champ, EB, Users

Single-thread risk: Vertex and Northwind each live or die with one inbox.

Move list:
  1. Vertex. EB missing. Intro path: ask the champion to bring
     their VP into the pricing conversation. Draft ready.
  2. Vertex. Tech eval missing. Content play: send the security
     overview to the engineer who attended call one.
  3. Northwind. Champion missing at Proposal stage. That is the
     deal-killer. Direct approach to the original requester today.
```

## Example chat
Here is the skill running on a pipeline export, start to finish.

**You:** Map committee coverage on my open deals, here's the export. [pastes CSV]

**Claude:** Mapped all 3 against the stage-based committee model.
```
Account     Stage      Coverage   Missing
Vertex      Eval       1/3        Economic buyer, tech evaluator
Northwind   Proposal   1/4        Champion, EB, end users
```
The catch: Northwind is at Proposal with only a technical evaluator engaged. No champion, no economic buyer. That deal lives or dies with one inbox, and it is the wrong inbox for this stage.

**You:** What's the widening play on Vertex?

**Claude:** Two gaps, two plays. Economic buyer: your champion replied twice this week, so use the intro path. Here is the ask, one paragraph, framed as helping the champion sell internally. Technical evaluator: no warm path, so run the content play. Send the architecture doc to the engineer who joined the first call and went quiet. One sharpener: connect Gong so call attendance counts toward engaged automatically instead of you pasting it.

## Go further
The map is step one. Here is where an operator takes it once the manual version proves out.

- **Make the CRM tell the truth.** Sync the map back to Salesforce OpportunityContactRole so every engaged contact has a role and the coverage score is computable on every deal, every day.
- **Count call attendance automatically.** Connect Gong so who actually attended each call feeds the engaged check, and a champion who stopped showing up gets caught the same week.
- **Find the missing role before you need the intro.** Use LinkedIn Sales Navigator to identify the likely economic buyer and technical evaluator at the account before asking the champion for the path.
- **Track the two-way, not the sent.** Connect your email tool so engaged means replied threads, not outbound volume. Then post each week's move list to the team's Slack channel so the widening work is visible.

A map that refreshes weekly beats a perfect map from last month. Automate the refresh.

## Make it yours
Fork it. Change the required roles, the stages, the engaged window. The point is not to run someone else's committee model. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
