---
name: attribution-model
description: Pick the attribution model that fits the question, then build it. First touch, last touch, or multi-touch, each with its blind spots named out loud, turned into an honest channel-contribution read. Built for B2B RevOps and marketing teams, customizable to your CRM and your channel taxonomy. Trigger on "build attribution", "which channels drive pipeline", "first vs last touch", "how should we credit marketing", "what's working in our funnel", or any attribution diagnostic.
---

# Attribution Model

## What this does
Helps you choose an attribution model that answers the question you actually have, then builds it from your touch data. First touch to see what starts deals, last touch to see what closes them, multi-touch to spread credit across the journey. Whichever you pick, it names the model's blind spots up front and turns the result into a channel-contribution read that says where pipeline comes from without pretending to a precision the data does not support.

## What you'll need
You do not need to connect anything to get value today. Bring a touch export and the skill runs now. Connect the tools below and it reads the full journey automatically and grounds the credit split in every touch, not just the ones you remembered to paste.

- Works today with: a CSV or paste of deals with their touches, each touch carrying channel or source, timestamp, and the deal it maps to, plus outcome and amount.
- More powerful connected to a CRM: it reads campaign membership, lead source, and opportunity touches automatically across the whole funnel.
- Sharper with a data warehouse: it can stitch web, ad, and CRM touches into one journey and run true multi-touch instead of a single-field proxy.
- Sharper with a BI tool: pushes the channel-contribution read into a dashboard the whole team reads the same way.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the touches you give it today and gets more powerful as you connect tools. It never credits a channel on data it cannot see. A missing touch is a stated limit, not an invented one.

- **Bring your data**: paste or upload your touch export. The skill builds the full model today on your real journeys. No connection required.
- **Connect your tools**: the same skill reads the whole journey automatically and runs true multi-touch instead of a first-or-last proxy. Same output, less effort, more honest.
- **Just exploring**: no data yet? Get the framework, the model tradeoffs, the blind-spot list, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a touch source to connect or a channel to clean up.

## Customize this for yourself
This was built for a B2B SaaS org attributing pipeline across marketing and sales touches. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | a CRM (Salesforce, HubSpot, Pipedrive) |
| WAREHOUSE | optional journey source | a data warehouse (Snowflake, BigQuery) |
| MODEL | the attribution model | first touch, last touch, linear multi-touch |
| CHANNEL taxonomy | how you group touches | paid, organic, outbound, events, referral |
| TOUCH source | where touches live | campaign membership, lead source, tasks |
| CREDIT basis | what you attribute | pipeline created, or closed-won revenue |
| WINDOW | the lookback for a journey | touches within 90 days before the deal |

Pick the model to fit the question, not the other way around. If you want to know what fills the top of the funnel, first touch. What tips the close, last touch. How the whole journey contributes, multi-touch. Each answers a different question and lies about the others.

## The method

### Model selection
State the question, then pick the model, then name what it will hide. First touch over-credits the top and ignores everything that closed the deal. Last touch does the reverse. Multi-touch spreads credit but leans on complete journey data you may not fully have. Choose deliberately and print the tradeoff, so nobody reads the output as the whole truth.

### Credit assignment
Assign credit by the chosen model. First and last touch give one channel the whole deal. Linear multi-touch splits it evenly across touches in the window. Always state the credit basis, pipeline created or closed revenue, because a channel that sources cheap pipeline and a channel that sources deals that close are not the same channel.

### Blind-spot ledger
Every model ships with its blind spots listed beside the result. Single-touch models cannot see assists. Multi-touch cannot tell a decisive touch from a passing one. Offline and word-of-mouth touches are invisible to all of them. Naming the blind spots is what makes the read trustworthy instead of a story.

### Channel-contribution read
Roll credit up to the channel taxonomy and report each channel's share, alongside its cost where you have it. The honest output is not "this channel drives X percent of revenue" full stop. It is "under last touch, credited on closed revenue, this channel takes X percent, and here is what that model cannot see."

### Cross-check
Where you can, run the same deals under a second model and show where the two disagree. A channel that looks huge on first touch and tiny on last touch is doing top-of-funnel work. The gap between models is itself a finding.

## Quality gates
- The model is named, and its blind spots are printed beside every result.
- Credit basis (pipeline vs closed revenue) is stated. No ambiguous "contribution."
- Offline and untracked touches are acknowledged as invisible, never silently zeroed into someone else's credit.
- No single model is presented as the truth. The read carries its own caveats.

## Output (example)
```
ATTRIBUTION · last touch · credited on closed-won revenue · trailing 2Q
Channel        Credited revenue   Share   Note
Outbound       $1.20M             38%     closes deals, first-touch share is lower
Paid search    $0.70M             22%     
Events         $0.55M             17%     under-credited here, strong on first touch
Referral       $0.48M             15%     
Organic        $0.26M             8%      

Blind spots of this model: assists get no credit, offline touches invisible, one touch takes the whole deal.
Cross-check: under first touch, Events jumps to 26%. Events start deals that outbound closes.
```
Illustrative figures. Your run reports your real touches.

## Where the numbers come from
The lookback window (90 days) and the linear split for multi-touch are defaults, not laws. They suited a mid-market SaaS journey. If your cycle is longer or your touches sparser, widen the window or simplify the model. The model choice and credit basis are yours, and they decide what the numbers mean.

## Example chat
**You:** Which channels are actually driving our pipeline? Here's our touch export for the last two quarters. [pastes CSV]

**Claude:** Built it under last touch, credited on closed-won revenue, since that's the question you asked (what closes deals, not what starts them).
```
Channel        Credited revenue   Share   Note
Outbound       $1.20M             38%     closes deals, first-touch share is lower
Events         $0.55M             17%     under-credited here, strong on first touch
Referral       $0.48M             15%
```
Blind spot to know before you present this: under first touch, Events jumps to 26%. That's not a contradiction, it means Events starts deals that outbound closes, and last touch alone would make you cut a channel that's actually doing real top-of-funnel work.

**You:** So which model do I actually report to the board?

**Claude:** Report both lines, not one. "Last touch says outbound closes 38%, first touch says events starts 26% of that same pipeline" is a more honest sentence than picking the flattering model. One sharpener: connect your CRM so the touches come from campaign membership directly, this run leaned on your CSV so anything you didn't export (like a webinar touch nobody logged) is invisible to both models.

## Go further
Running one model by hand shows the shape. Here's the version that keeps both reads current.

- **Automate the dual-model refresh.** Connect Salesforce or HubSpot campaign data to a scheduled Claude task that recomputes first touch and last touch every week and flags any channel where the two models disagree by more than 10 points.
- **Stitch the full journey.** Pull web, ad, and CRM touches into Snowflake or your warehouse so multi-touch stops being a proxy and becomes a real stitched journey.
- **Push it to a dashboard everyone reads the same way.** Send the channel-contribution read into your BI tool so marketing and sales stop arguing over two different spreadsheets.

The model choice stays a decision you make. The refresh doesn't have to be.

## Make it yours
Fork it. Change the model, the channel taxonomy, the credit basis, the window. The point is not to run someone else's attribution. It is to run yours, with the blind spots named, so the channel read is honest instead of flattering. Built by an operator. Customize it, break it, make it better.