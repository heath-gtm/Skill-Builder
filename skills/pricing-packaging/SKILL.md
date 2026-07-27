---
name: pricing-packaging
description: Reprice and repackage to de-risk revenue and capture the value you create. Moves you off a pure per-seat model, decides what to meter and what to bundle, sets the tiers, and models the impact on deal size, win rate, and free-to-paid. Trigger on "pricing", "repackage", "per-seat is capping us", "value-based pricing", "packaging and tiers", "monetize free users", "raise prices without losing deals", or any commercial-model question.
---

# Pricing & Packaging

## What this does

Turns "our pricing is leaving money on the table" into a concrete repackaging plan. It finds where your current model breaks (usually a pure per-seat license that bets revenue on headcount), decides what to charge for and what to bundle, sets the tiers and the value metric, and models the effect on deal size, win rate, and free-to-paid conversion before you change a thing. Reprice to de-risk, not just to raise the number.

## What you'll need

You do not need to connect anything. Bring what you sell and how you charge today and the plan runs. It gets sharper with real usage and deal data.

- Works today with: your current price list, your tiers, and a rough read on who buys what. Paste it.
- More powerful with a CRM: it reads real deal sizes, discounting, and win rates by segment.
- Sharper with a product-analytics tool: it sees which features drive value and who is stuck on free.

## How this runs at your connection level

Never reliant on a connector. It runs on what you tell it and gets more grounded as it sees real deal and usage data. It never claims a lift it cannot model from your own numbers. An assumption is labeled, not hidden.

## Customize this for yourself

| Set this | What it is | Example |
|---|---|---|
| Your value metric | The thing you charge for that scales with value | Seats, usage, outcomes, records, revenue processed |
| Your tiers | The packages a buyer chooses between | Starter, Team, Business, Enterprise |
| Your fence lines | What separates one tier from the next | Volume, features, support, security |
| Your guardrails | The moves you will not make | No surprise overages, no removing a feature customers rely on |

## The method

### 1. Find where the model breaks
Name what your current model bets on. A pure per-seat license bets revenue on the customer's headcount, so it caps you when they freeze hiring and it under-charges the accounts getting the most value. Say the failure out loud.

### 2. Pick the value metric
Choose what to charge for so the bill grows as the customer succeeds, not as they add chairs. The best metric is one the buyer already believes is fair and can predict.

### 3. Set the tiers and the fences
Decide what is bundled and what is metered, and draw clean fence lines between tiers so a buyer knows exactly why they move up. Bundle the things that drive adoption, meter the things that scale with value.

### 4. Handle the free base
If a large share of active users sit on free, decide what converts them: a usage ceiling, a value-gated feature, or a self-serve motion. Free is a funnel, not a leak, only if there is a path off it.

### 5. Model the impact before you ship
Estimate the effect on average deal size, win rate, and free-to-paid, using your own numbers. A reprice that lifts deal size but tanks win rate is a loss. Reprice to de-risk: bigger deals, held or better win rates, a smaller free base.

## Quality gates

- Every projected lift is modeled from your own deal or usage data, or clearly labeled an assumption.
- No move that creates a surprise bill or removes a feature customers depend on.
- The plan states the migration path for existing customers, not just new logos.
- If the change raises deal size but hurts win rate or retention, it does not ship.

## Output (example)

```
CURRENT: pure per-seat, revenue capped by customer headcount
VALUE METRIC: shift core to seats + a usage tier for the heavy accounts
TIERS: Starter (self-serve) / Team / Business / Enterprise, fences on volume + security
FREE BASE: ~40% on free, add a usage ceiling + one value-gated feature
MODELED IMPACT (from your data, illustrative):
- Average deal size: +25 to 35%
- Win rate: held (value-based framing, not a raw increase)
- Free-to-paid: single digits to low double digits
MIGRATION: grandfather existing seats 12 months, opt-in to new tiers
```

## Where the numbers come from

Your price list and tiers are yours. Deal sizes, discounting, and win rates come from your CRM when connected; feature value and free-user counts come from a product-analytics tool. Every projected lift is modeled from those numbers or labeled an assumption.

## Example chat

**You:** Our per-seat pricing is capping us. Customers freeze hiring and our revenue freezes with them. Help me reprice.

**Claude:** Here's where the model breaks and what to charge instead.
```
CURRENT: pure per-seat, revenue capped by customer headcount
VALUE METRIC: shift core to seats + a usage tier for the heavy accounts
TIERS: Starter (self-serve) / Team / Business / Enterprise, fences on volume + security
FREE BASE: ~40% on free, add a usage ceiling + one value-gated feature
```
The real problem isn't the price, it's the metric. Seats bet your revenue on their headcount decisions, not on the value they're actually getting, so the heaviest users and the frozen-headcount accounts pay the same.

**You:** Will this tank win rate if we push it out now?

**Claude:** That's exactly the check before this ships: I labeled the deal-size lift and the win-rate hold as modeled from your own numbers where you have them, and as an assumption where you don't. A reprice that grows average deal size but drops win rate is a loss, not a win, so that's the gate before anything goes to customers. Sharpener: connect the CRM so the win-rate and deal-size projections come from your real discounting history instead of the illustrative range above.

## Go further
The plan on paper is a hypothesis. Here's how an operator tests it before it touches a real quote.

- **Model the impact from real deals, not placeholders.** Connect the CRM so projected deal-size and win-rate shifts are computed from your actual discounting and close history, not an illustrative range.
- **Watch the free base convert in real time.** Connect a product-analytics tool so the usage ceiling and value-gated feature get tuned against who's actually stuck on free, not a guess at the 40%.
- **Pair the migration with the account list.** Feed the affected-accounts list into a business-case skill so existing customers get a grandfathering plan with names attached, not a generic policy memo.

Repricing is a bet. The connectors are what turn the bet into a number you can defend before you make it.

## Make it yours

Set your value metric, tiers, and fence lines in the table above. Run this before any pricing change, and pair it with a business case for the accounts a reprice affects most.
