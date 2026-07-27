---
name: deal-intelligence
description: Walk into any deal review knowing what is actually known about the deal. Two modes: a numbers read that scores forecast quality, deal risk, velocity, and close-date accuracy, and a conversation read that turns a deal's meeting history into a deal-review brief on your qualification framework, with a qualification-vs-stage gap check that catches sandbagging. Built for B2B sales teams, customizable to your CRM and your sales process. Trigger on "how are my deals looking", "deal review", "forecast review", "what's closing", "is this deal real", "prep me for the deal review", or any single-deal or forecast diagnostic.
---

# Deal Intelligence

## What this does
Reads a deal, or your whole forecast, and tells you what is actually known versus what is being assumed. It runs in two modes. The numbers read scores forecast quality, deal risk, stage velocity, and close-date accuracy, and flags the deals that are quietly slipping. The conversation read takes a deal's meeting history and builds a deal-review brief on your qualification framework, then checks whether the deal is qualified for the stage it claims. Together they answer one question: is this deal real, and what do we do next.

## What you'll need
You do not need to connect anything to get value today. Bring your deal, or a pasted list of open deals, and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a pasted list or CSV of open deals, with stage, amount, close date, forecast category, last activity date, and the contacts on each. For the conversation read, paste the meeting notes or transcript for a single deal.
- More powerful connected to a CRM: it reads all of the above automatically, across the whole pipeline, plus your qualification fields.
- Sharper with a meeting or transcript tool: it pulls the deal's actual meeting history so the conversation read quotes what was said, not what was typed into a field.
- Sharper with a product-analytics tool: adds usage momentum on trials and evaluations.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your deal list, or paste one deal's meeting notes. The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the forecast and the meeting history automatically and adds signals you cannot paste by hand (live activity, product usage, transcript quotes). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| STAGE field | the opportunity stage | Qualification through Closed |
| FORECAST field | commit / best-case category | Commit, Best Case, Pipeline, Omit |
| QUALIFICATION framework | your methodology and its fields | MEDDIC, MEDDPICC, BANT, or your own |
| MEETING source | where the deal's conversations live | a meeting or transcript tool |
| STUCK_DAYS | days in one stage that mean stuck | 30 (re-tune to your cycle) |
| STALE_DAYS | no-meeting days that mean stale | 14 (re-tune) |
| CONCENTRATION cutoffs | single-deal and single-rep limits | 30% of pipeline, 50% per rep |

Run any methodology you like. The skill checks "is this deal qualified for the stage it claims," so point it at your qualification fields, not anyone else's.

## The method

The two modes compose. Run the numbers read to find the risky deals, then the conversation read to understand why and what to do.

### Mode A: the numbers read (is the forecast real?)
Score forecast quality and deal risk from a deal list.

**1. Forecast category distribution.** How much pipeline sits in Commit vs Best Case vs Pipeline vs Omit? Is Commit enough to cover the remaining target gap? Is Best Case realistic or inflated?

**2. Stage velocity and stuck deals.**
- Flag early-stage deals with close dates this period, at risk of not closing in time.
- Flag deals with no next step documented, likely stalled.
- Flag deals in the same stage past STUCK_DAYS.

**3. Concentration risk.**
- Any single deal over 30% of remaining pipeline, flag it.
- Any single rep holding over 50% of total pipeline, flag it.
- More than 60% of pipeline in early stages, flag the stage mix.

**4. Close-date accuracy.**
- Close dates in the past on deals still open, flag them.
- Close dates that have moved more than once, flag them.

**5. Deal-level detail table.** Account, owner, stage, close date, amount, forecast category, next step, and a risk flag. Red for commit or best-case stuck in early stages, past-due close dates, or no next step. Yellow for pipeline deals closing this period or large deals with no recent activity. Green for commit deals late-stage with a clear next step.

**6. Rep-level summary.** Per rep: total pipeline, pipeline by forecast category, deal count, average deal size, and largest deal as a concentration check.

Lead with the forecast gap: how much Commit plus Best Case covers versus the remaining target. Then name the top three riskiest deals with a specific reason each.

### Mode B: the conversation read (what do we actually know?)
Turn a deal's meeting history into a brief a rep or manager can walk into a review with, fully prepared, with evidence from actual conversations.

Structure every brief against your qualification framework (MEDDIC, MEDDPICC, or your own). For each element of your framework, pull evidence directly from the conversations and bind it to the matching field. Where a field is empty in the conversation, that is a qualification gap, not a formatting choice. Call it out and name the field.

A general spine, adapt to your framework:
- **Problems / pain.** What specific, ideally quantified problems has the buyer named (revenue, cost, time, headcount, tooling pain)? Quote it and the meeting it came from. If absent, flag it.
- **Value alignment.** Has your value been tied explicitly to those problems, a business case or ROI the buyer agreed with? If you have demoed features but not aligned them to a problem, that is a gap.
- **Decision dynamics.** Who decides, on what criteria, through what process (procurement, legal, security, pilot, committee), and by when? Is the named decision maker identified and engaged? An absent or unengaged decision maker past discovery is a significant risk.
- **Champion.** Is someone internally advocating? Look for forward-looking questions ("how would we roll this out?") and volunteered intros. No champion is high risk.
- **Next steps.** Are there mutually agreed next steps with real dates? "Sometime next quarter" is a gap.

**Qualification-vs-stage gap check (the sandbagging catcher).** Compare framework coverage to the deal's current stage and name any missing field, never just "incomplete."

```
Stage claims Discovery      and the pain/problem field is empty      -> GAP (name it)
Stage claims Validation     and the value-alignment field is empty   -> GAP (name it)
Stage claims Proposal       and decision dynamics are unmapped       -> GAP (name it)
Stage claims Negotiation    and next steps have no date              -> GAP (name it)
Forecast = Commit           and ANY required field is empty          -> COMMIT_RISK
```

**Risk signals to surface.** Qualification gap for the current stage (name the field), a Commit deal missing any required field, a decision maker not identified or engaged past discovery, a stale deal (no meetings past STALE_DAYS with no clear next step), a competitor mentioned (quote it and the meeting), vague or dateless next steps, single-threading, and overdue action items.

**Next steps.** Close with two or three specific, prescriptive moves tied to the gaps. Example: "Problems are not quantified, book a follow-up to attach a number to the stated pain." "No named decision maker, get the champion to map the approval process and introduce the economic buyer."

Open the brief with a two-to-three-sentence executive summary: current state, biggest gap or risk, recommended next action. Use direct quotes from the conversations to keep it credible.

For a portfolio review across deals, give a shorter summary per account (exec summary, top gap, next step), a portfolio view (healthy / at-risk / stalled), and the patterns across the set (common objections, recurring gaps that signal a coaching opportunity).

## Quality gates
- No stale or dead verdict without showing the activity or meeting dates that prove it.
- Qualification gaps surface field by field, named, never "incomplete."
- Forecast accuracy is trailing-quarter, never trailing-week. Small samples lie.
- Every quoted claim in the conversation read is tied to the meeting it came from.

## Output (example)
```
DEAL REVIEW · Northwind · Proposal / $112K · Commit

Verdict: COMMIT_RISK. Committed for this period, but no named decision maker
and next steps have no date. This is a slip waiting to happen.

What we know (from the conversations):
  Problems   Strong. VP named a quantified pain in the last call.
  Value      Aligned. Buyer agreed the business case in the demo recap.
  Decision   GAP. No economic buyer identified. Champion is a manager.
  Champion   Present but junior. Asked "how would we roll this out?"
  Next steps GAP. "Circle back next month." No date, no owner.

Next moves:
  1. Get the champion to map the approval process and introduce the buyer.
  2. Set a dated next step before this deal stays in Commit.
  3. Pull it from Commit until the decision maker is engaged.
```

## Where the numbers come from
STUCK_DAYS (30), STALE_DAYS (14), and the concentration cutoffs (30% single deal, 50% single rep) are defaults, not laws. They suited a mid-market SaaS cycle. If your deals run longer, raise them. The logic does not change. The thresholds are yours.

## Example chat
Here is the skill running both modes on the same deal, start to finish.

**You:** How's my forecast looking this week? Here's the export.

**Claude:** Ran the numbers read first.
```
Forecast gap: Commit + Best Case covers 71% of the remaining target.
Top 3 riskiest: Northwind ($112K, Commit, no named decision maker),
Vertex ($67K, stuck 34 days), Halborn ($40K, close date already past).
```
Commit alone does not cover the gap, and your riskiest deal is sitting in Commit with a qualification field empty.

**You:** Pull the conversation read on Northwind, I've got the meeting notes. [pastes notes]

**Claude:** Mapped it to MEDDPICC.
```
Verdict: COMMIT_RISK. No named decision maker, next steps have no date.
Problems EARNED, Value EARNED, Decision GAP, Champion present but junior.
```
The insight: this deal was scored Commit on activity volume, not qualification, and the gap that matters, the decision maker, has been open since discovery. One sharpener: connect the CRM's qualification fields so future reads pull the framework state directly instead of re-scoring from notes each time.

## Go further
The read is step one. Here is where an operator takes it once the manual version proves out.

- **Run the numbers read every Monday automatically.** Schedule a Claude task against Salesforce to post the forecast-gap summary to the sales leader's channel before the pipeline review.
- **Feed the conversation read from real calls.** Connect Gong or another transcript tool so the qualification quotes come from the actual meeting, not a typed-up recap.
- **Turn commit-risk flags into action.** Have Slack notify the deal owner the moment a Commit deal loses a required qualification field, tied straight to the CRM field change.

Know what is real before the review, not during it.

## Make it yours
Fork it. Change the modes, the thresholds, the framework, the fields. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
