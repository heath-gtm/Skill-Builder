---
name: discovery-framework
description: Turn a discovery call into a qualification scorecard instead of a pile of notes. Runs the call against MEDDPICC (or your own framework), captures the problem, the quantified pain, the decision process, the economic buyer, and the champion, then names the gaps you still have to fill. Built for B2B sales teams, customizable to your methodology and your CRM. Trigger on "run discovery", "qualify this call", "what did I miss on this deal", "MEDDIC check", "is this qualified", or any post-call qualification pass.
---

# Discovery Framework

## What this does
Takes what you learned on a discovery call and lays it out on a qualification framework, one field at a time. It captures the problem in the buyer's words, the impact and quantified pain, how they actually buy, who signs, and who is fighting for you inside. Then it does the part reps skip: it names what you still do not know and what to ask next.

## What you'll need
You do not need to connect anything to get value today. Bring your call notes and the skill runs now. Connect the tools below and it pulls the call for you and fills more of the frame automatically.

- Works today with: your notes, a transcript, or a rough recap you paste in. Even bullet points work. The skill maps them onto the framework and shows the holes.
- More powerful connected to a meeting or transcription tool: it reads the call directly, pulls the buyer's own quotes, and stops you from scoring pain you only imagined.
- Sharper connected to a CRM: it writes each field back to the opportunity and checks the qualification against the stage the deal claims.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the notes you give it today and gets sharper as you connect tools. It never scores a field you did not actually earn on the call. An empty field is a question for next time, not a guess.

- **Bring your data**: paste your notes or a transcript. The skill runs the full qualification pass today and returns the scorecard plus the gap list. No connection required.
- **Connect your tools**: the same skill reads the call itself, pulls direct quotes, and writes the fields back to the deal. Same output, less typing, harder to fool.
- **Just exploring**: no call yet? Get the framework, the exact fields it scores, and a worked example on a sample call, so you can see the shape before your next one.

Every run ends with the one question that would most change the deal if you got it answered.

## Customize this for yourself
This was built for a B2B SaaS org running MEDDPICC. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| FRAMEWORK | your qualification methodology | MEDDPICC, MEDDIC, BANT, your own |
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| MEETING source | where calls are recorded | your meeting or transcription tool |
| STAGE field | the opportunity stage | Opportunity.StageName |
| PAIN fields | where impact and metrics live | your custom qualification fields |
| CHAMPION test | what proves a champion is real | acts when you are not in the room |
| QUANTIFY unit | how you size pain | hours, dollars, headcount, churn |

Run any framework you like. The skill scores "what did the buyer actually tell you," so point it at your fields, not anyone else's.

## The method

### Score every field, name every gap
Each framework field gets one of three states: EARNED (the buyer said it, and you can quote it), ASSUMED (you inferred it, not confirmed), or MISSING. Assumed and missing are the deal risk. The output leads with them, not with the fields you already have.

### Problem before solution
Capture the problem in the buyer's language first, before any product talk. If you cannot write the problem as a sentence the buyer would agree with, you do not have discovery, you have a pitch.

### Quantify the pain
Pain without a number is a nice-to-have. Push for the metric: hours lost, dollars leaking, deals slipping, the cost of the status quo. If the number is not there yet, mark it MISSING and make it the next call's job. An illustrative example: "roughly 6 hours a week per rep on manual list building" is a quantified pain, "it is a pain" is not.

### Decision process and economic buyer
Map how they buy, not just who likes you. Who signs, what the steps are, what has killed a deal like this before, whether you have met the person who controls the budget. Liking you is not access.

### Champion versus contact
A contact takes your call. A champion sells for you when you are not there and has something to gain if this lands. Test it: have they given you something that cost them anything, an intro, a proof point, an internal date. If not, mark champion ASSUMED.

## Quality gates
- No field scored EARNED without a quote or a specific fact behind it.
- Quantified pain is a number with a unit, or it is MISSING, never "significant."
- Champion is not marked real until they have taken one action for you unprompted.
- The gap list is ranked by deal impact, not by framework order.

## Output (example)
```
DISCOVERY SCORECARD · illustrative deal
Field                   State     What we have
Metrics (pain)          EARNED    ~6 hrs/wk/rep on manual prospecting
Economic Buyer          ASSUMED   VP Sales named, not yet met
Decision Criteria       EARNED    Must cut ramp time, integrate with CRM
Decision Process        MISSING   No steps, no timeline captured
Identified Pain         EARNED    Reps miss quota in first two quarters
Champion                ASSUMED   Enthusiastic, no action taken yet
Competition             MISSING   Not asked

Top gaps to close next call:
  1. Decision process. Get the actual steps and dates to signature.
  2. Meet the economic buyer. A named VP you have not met is not access.
  3. Test the champion. Ask for one internal intro and see what happens.
```

## Where the inputs come from
The three states (EARNED, ASSUMED, MISSING) and the champion test (one unprompted action) are the defaults that keep reps honest. The framework fields are yours to swap. If you run BANT, score BANT. The discipline does not change: earn the field or flag it. The fields are yours.

## Make it yours
Fork it. Change the framework, the fields, the champion test. The point is not to run someone else's methodology. It is to run yours, and to stop scoring pain you never heard. Built by an operator. Customize it, break it, make it better.
