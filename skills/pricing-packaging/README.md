# Pricing & Packaging

> Reprice and repackage to de-risk revenue and capture the value you create. Moves you off a pure per-seat model, decides what to meter and what to bundle, sets the tiers, and models the impact on deal size, win rate, and free-to-paid. Trigger on "pricing", "repackage", "per-seat is capping us", "value-based pricing", "packaging and tiers", "monetize free users", "raise prices without losing deals", or any commercial-model question.

## Install

```bash
mkdir -p ~/.claude/skills/pricing-packaging && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/pricing-packaging/SKILL.md -o ~/.claude/skills/pricing-packaging/SKILL.md && echo "Installed pricing-packaging. Restart Claude Code."
```

Or download `SKILL.md` and drop it into `~/.claude/skills/pricing-packaging/`. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

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

## Make it yours

Set your value metric, tiers, and fence lines in the table above. Run this before any pricing change, and pair it with a business case for the accounts a reprice affects most.
