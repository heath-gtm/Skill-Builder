---
name: account-scoring-model-builder
description: Design the composite account score your team ranks on. Picks the signals that actually predict a good-fit account, sets fair weights across channels, adds gates and escalators, defines the tier bands, and hands back a scorer spec you can run and defend. Built for any GTM team building an ICP or PQL score, customizable to your signals and motion. Trigger on "design my account score", "build a scoring model", "how should I weight these signals", "what makes a good-fit account", "set my ICP tiers", "build a PQL score", "make my scoring fair across channels", or any account-scoring-design question.
---

# Account-Scoring-Model Builder

## What this does
Designs the scoring model your team stack-ranks on, and makes it defensible. It helps you pick the signals that actually separate a good account from a bad one, weight them fairly so an inbound account and an outbound account can each earn their score, add the gates and escalators that stop junk from ranking high, and set the tier bands. The output is a scorer spec with the logic written down, so the score has a reason on every row instead of a black box nobody trusts. This designs the model; a scoring skill then runs it.

## What you'll need
You do not need to connect anything to get value today. Describe your ICP and your signals and the skill designs the model now. Connect your data and it grounds the weights in what actually converted.

- Works today with: a description of your ideal customer, the signals you can see (firmographic, product, intent, engagement), and what a win looks like. Paste it and go.
- More powerful connected to a CRM: it reads closed-won and closed-lost so the weights reflect what actually converts, not a guess.
- Sharper with a data warehouse: it backtests the model against a real cohort before you trust it.
- Sharper with enrichment or product data: it scores on real signal coverage instead of assuming every field is filled.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on what you describe today and gets sharper as you connect tools. It never claims a weight is validated when it is not, and never scores a blank field as a zero. A gap is a prompt, not a guess.

- **Bring your data**: describe the ICP, the signals, and a few real wins and losses. The skill designs the full model and tier bands today.
- **Connect your tools**: the same skill reads closed-won and closed-lost, so it can fit the weights to what actually converted and backtest before you ship.
- **Just exploring**: no data yet? Get the framework, the fairness rule, and a worked example, so you see the shape before you build.

Every run ends with the one thing that would sharpen the next build, a signal to add or a cohort to backtest against.

## Customize this for yourself
This was built to be motion-agnostic. Set these to your business:

| Set this | What it is | Default / Example |
|---|---|---|
| SIGNALS | the inputs you can actually see | firmographic, product usage, intent, engagement |
| CHANNELS | the ways an account reaches you | inbound, outbound, product-led |
| WEIGHTS | how much each signal counts | set by fit, retuned against wins |
| GATES | hard rules that cap or disqualify | not-our-motion, wrong region, competitor |
| ESCALATORS | signals that earn a top tier on their own | a dominant, high-intent signal |
| TIERS | the bands you route on | Hot / Warm / Nurture / DQ, or your own |
| COVERAGE_RULE | how missing data is handled | cap the score, never score blanks as zero |

The model is yours. The skill's job is to make it fair, defensible, and honest about what it cannot see, not to impose someone else's weights.

## The method

### Pick signals that separate, not signals that exist
A signal earns a place only if it actually differs between accounts that win and accounts that lose. Start from a handful of real wins and losses and ask what was true of the wins. Signals that look the same on both sides are noise, no matter how easy they are to pull.

### Weight fairly across channels
An outbound account and a product-led account show up on different signals. If the model only rewards product usage, outbound accounts can never score. Weight so every channel can reach every tier on its own strongest signals. Uncap the channels, then let the gates do the filtering.

### Add gates and escalators
Gates are hard rules: a wrong-motion or wrong-region account gets capped or disqualified no matter how good it looks. Escalators are the opposite: one dominant, high-intent signal can lift an account to the top tier on its own. Both keep the middle of the score honest.

### Handle missing data honestly
A blank field is not a zero. An account scored on two of six signals must not sit next to a fully-enriched account at the same number. Cap the score by coverage so a thin account cannot hide as a strong one. This is the single most common way scoring models lie.

### Set the tier bands and the reason string
Define the bands you route on and, for every account, require a short reason: the signals that drove the score. A score with no reason is a black box reps will ignore. A score with a reason is a score they will work.

## Quality gates
- Every signal in the model has a stated reason it separates wins from losses. No signal included just because it is available.
- Every channel can reach every tier on its own signals. No channel is structurally capped.
- Blank fields are never scored as zero; coverage caps the score.
- Every score carries a reason string naming its top drivers.
- Gates and escalators are explicit rules, not vibes buried in a weight.

## Output (example)
```
SCORING MODEL SPEC · [your org] · built [date]

Signal              Weight   Reason it separates
Fit (firmographic)  30       wins cluster in this size + segment
Product usage       25       active trial predicts close
Intent              20       repeat high-intent visits precede wins
Engagement          15       multi-thread predicts a real deal
Recency             10       fresh signal beats stale

GATES:      not-our-motion -> DQ · competitor -> cap at Nurture
ESCALATORS: >=3 high-intent sessions in 7d -> min Warm
COVERAGE:   score capped at 60 if <3 of 5 signals present

TIERS:  Hot >=85 · Warm 65-84 · Nurture 40-64 · DQ gated

Reason string (per account):
  "Hot 91 - strong fit + active trial + 4 intent sessions this week"
```

## Example chat
Here is the skill designing a defensible score from a rough ICP.

**You:** I want to score accounts Hot to Cold. We get inbound demo requests and we do outbound. Signals I have: company size, product trial usage, website intent, email engagement.

**Claude:** First fairness check: if trial usage carries most of the weight, your outbound accounts can never go Hot, because they have not tried the product yet. So I'd weight it like this and uncap the channels:
```
Fit (size/segment)  30    both channels have it
Intent (website)    25    the outbound tell
Product usage       25    the inbound/PLG tell
Engagement          20    multi-thread signal
```
Now an outbound account can reach Hot on fit + intent + engagement, and an inbound trial can reach Hot on fit + usage. The thing worth catching: score blanks honestly. An account you have size on but nothing else should cap around 60, not sit at Hot because one field was strong. Otherwise thin accounts crowd out real ones.

**You:** How do I stop competitors and wrong-fit from ranking high?

**Claude:** Gates. A competitor domain caps at Nurture, a wrong-region or wrong-motion account gets disqualified outright, regardless of the other signals. And add one escalator so you never miss a hot hand: three-plus high-intent sessions in a week floors the account at Warm even if fit is soft. One sharpener: connect your CRM and I'll fit these weights against your actual closed-won versus closed-lost, then backtest the model on that cohort so the numbers are earned, not guessed.

## Go further
The model is step one. Here is where an operator takes it once it holds.

- **Hand it to a scoring skill to run at scale.** Feed the spec to an ICP-scoring skill so every account in the CRM gets scored, tiered, and reasoned, on demand or nightly.
- **Backtest and retune quarterly.** Pull closed-won and closed-lost from Salesforce or Snowflake and re-fit the weights against what actually converted, so the model does not freeze at launch defaults.
- **Route on the tiers automatically.** Wire the bands into Salesforce and Slack so a Hot account alerts its owner the moment it crosses the line.

Design the model once, defend it with a real cohort, and let it run.

## Where the numbers come from
The weights, gates, escalators, and tier bands are yours to set. The examples here suited a hybrid inbound-plus-outbound motion. A pure product-led or pure enterprise motion weights differently. The logic, pick signals that separate, weight fairly, gate the junk, never score a blank as zero, does not change.

## Make it yours
Fork it. Change the signals, the weights, the gates, the tiers. The point is not to run someone else's score. It is to build a score your team trusts because they can see the reason on every row. Built by an operator. Customize it, break it, make it better.
