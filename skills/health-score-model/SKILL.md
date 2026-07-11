---
name: health-score-model
description: Build a health-score model for a book of business you can actually defend. It picks the inputs, sets the weights, draws the green/yellow/red thresholds, and assigns a specific action to each tier so the score drives work, not just a color. Built for B2B customer success teams, customizable to your CRM and product analytics. Trigger on "build a health score", "score my book", "why is this account yellow", "health model for renewals", "what makes an account red", or any book-of-business scoring.
---

# Health Score Model

## What this does
Builds a health-score model for a whole book of business: the inputs that actually predict retention, the weight each one carries, the thresholds that split green from yellow from red, and the one specific action attached to each tier. The output is a scored book where every color tells the CSM what to do next, not just how to feel.

## What you'll need
You do not need to connect anything to get value today. Bring your account list and the skill runs now. Connect the tools below and it pulls the rest and adds signals you cannot paste by hand.

- Works today with: your accounts and whatever signals you have, usage, support load, sponsor status, renewal date, last touch. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads the book, ARR, renewal dates, and open cases automatically.
- Sharper with a product-analytics tool: real adoption becomes the strongest input instead of a guess.
- Sharper with a support or ticketing tool: turns ticket volume and sentiment into a real risk input.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your book with whatever signals you have. The skill builds and applies the full model today on your real accounts. No connection required.
- **Connect your tools**: the same skill pulls usage, cases, and dates automatically and adds signals you cannot paste by hand. Same model, less effort, sharper.
- **Just exploring**: no book yet? Get the framework, the exact inputs it reads, the default weights, and a worked example on sample accounts, so you can see the shape before you feed it.

Every run ends with the one input that would most improve the model, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org scoring a renewal book. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| ADOPTION input | usage signal and weight | product analytics, weight 40% |
| RELATIONSHIP input | sponsor / champion status and weight | multi-thread count, weight 20% |
| SUPPORT input | ticket load and sentiment and weight | ticketing tool, weight 15% |
| ENGAGEMENT input | last touch, QBR cadence and weight | activity dates, weight 15% |
| COMMERCIAL input | renewal proximity, growth and weight | ARR trend, weight 10% |
| THRESHOLDS | green / yellow / red cutoffs | 70+ green, 40-69 yellow, <40 red |
| TIER ACTIONS | the one move per tier | green nurture, yellow plan, red escalate |

Pick inputs you can actually see. A model with a 40% weight on a signal you never measure is a model that lies confidently.

## The method

### Pick the inputs
Choose four to six signals that predict retention for your product: adoption, relationship depth, support health, engagement cadence, commercial trend. Fewer strong inputs beat many weak ones. Any input you cannot measure gets dropped or flagged, never faked.

### Set the weights
Weight by predictive power, not by what is easy to pull. For most B2B SaaS, adoption carries the most and commercial the least, because usage moves first and the renewal number moves last. State the weights out loud so anyone can challenge them.

### Draw the thresholds
Green, yellow, red are decisions about attention, not math for its own sake. Set cutoffs so green means "leave it running," yellow means "there is a plan," red means "escalate this week." Re-tune once you see the spread; if 80% of the book is red, the thresholds are wrong, not the book.

### Action per tier
Each tier gets exactly one default action. Green: nurture and look for expansion. Yellow: a written recovery plan with an owner. Red: escalate, involve a leader, set a save play in motion. A score with no action is a dashboard nobody uses.

### Explain every score
Every account shows the two inputs pulling it up and the two pulling it down. A CSM should never ask "why is this yellow." The model answers before they ask.

## Quality gates
- Every input is measurable, or it is dropped from the model and noted.
- Weights are stated and sum to 100. No hidden factors.
- No account gets a color without the top reasons for it shown.
- Thresholds are sanity-checked against the book's spread, not set once and forgotten.

## Output (example)
```
BOOK HEALTH · 5 sample accounts
Account      Score   Tier     Up                 Down
Account A    82      GREEN    adoption, sponsor  none material
Account B    61      YELLOW   adoption           champion quiet
Account C    58      YELLOW   engagement         support spike
Account D    34      RED      none material      no usage, no sponsor
Account E    73      GREEN    adoption, growth   one open case

Tier actions:
  GREEN  (A, E): nurture, scout expansion.
  YELLOW (B, C): written recovery plan, owner named, this week.
  RED    (D):    escalate to leader, open a save play now.
```

## Where the numbers come from
The scores, weights, and thresholds come from the inputs you paste or the tools you connect. Nothing above is a real customer number; it is illustrative. The default weights (adoption 40, relationship 20, support 15, engagement 15, commercial 10) are a starting point tuned for one SaaS book, not a law. When an input is missing, the model redistributes weight and tells you which signal would sharpen the score.

## Make it yours
Fork it. Change the inputs, the weights, the cutoffs, the action per tier. The point is not to run someone else's health score. It is to run one you can defend in a QBR and act on the same day. Built by an operator. Customize it, break it, make it better.
