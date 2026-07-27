---
name: renewal-negotiation
description: Walk into the renewal with a plan instead of a flinch. Build the value recap, the price and term options, the concession ladder, and the answer to "we want a discount" that protects net retention. Built for B2B customer success teams, customizable to your pricing and your process. Trigger on "prep a renewal negotiation", "they want a discount on the renewal", "renewal is coming up", "how do I hold price at renewal", "concession ladder", or any renewal-negotiation prep.
---

# Renewal Negotiation

## What this does
Prepares you for the renewal conversation before the customer sets the terms. It recaps the value they actually got, lays out the price and term options you can offer, builds a concession ladder so you give ground in order instead of in panic, and scripts the answer to the discount ask. The goal is not to win a fight. It is to protect net retention while keeping the customer glad they stayed.

## What you'll need
You do not need to connect anything to get value today. Bring the account and the skill runs now. Connect the tools below and it pulls the numbers automatically and adds signals you cannot paste by hand.

- Works today with: what you can describe. The current price and term, the renewal date, what they have achieved, how much they use it, and what they have signaled about budget or the discount ask.
- More powerful connected to a CRM: pulls the contract value, the renewal date, the history, and any expansion in play.
- Sharper with a product-analytics tool: turns "they get value" into the adoption numbers that make holding price defensible.
- Sharper with a meeting or email tool: surfaces what the customer has already said about price, so the ladder starts from reality.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a usage or value number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: describe the account, the current terms, and the discount pressure. The skill builds the full negotiation plan today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls contract value, adoption, and history automatically and adds signals you cannot paste by hand (real usage, prior commitments, expansion signals). Same output, less effort, sharper.
- **Just exploring**: no renewal yet? Get the framework, the concession ladder, and a worked example on sample data, so you can see the shape before you walk in.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org protecting net revenue retention. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | your CRM of choice |
| ANALYTICS | your product-analytics connector | a product-usage tool of your choice |
| PRICE field | the current contract value | ARR, list price, current term |
| TERM_OPTIONS | the shapes you can offer | 1-year, multi-year, monthly to annual |
| CONCESSION_LADDER | what you trade, in order | term for price, volume for rate, roadmap for logo |
| FLOOR | the price you will not go below | your NRR-protecting minimum |
| NRR_TARGET | the retention you are defending | net revenue retention goal |

Run any pricing model you like. The skill trades value for concessions in a set order, so point it at your own floor and levers, not anyone else's.

## The method

### Value recap first
Never open a renewal on price. Open on what they got. Lead with the adoption and the outcomes, so the number that follows sits on a foundation of value already delivered. A customer reminded of the value argues less about the price. Keep the exact figures ready and round to human scale when you say them out loud.

### Price and term options
Offer a shape, not a single number. A flat renewal, a multi-year at a better rate, a monthly-to-annual switch. Options give the customer a decision to make instead of a price to fight. The one you want them to pick sits in the middle, framed as the sensible choice.

### The concession ladder
Decide, before the call, what you will trade and in what order. Trade term for price. Trade volume commitment for a better rate. Trade a case study or a reference for a small credit. Every concession buys you something back. You never give a discount for nothing. Walk down the ladder one rung at a time, slowly.

### The discount answer
When "we want a discount" lands, do not flinch and do not fold. Acknowledge, re-anchor on value, then convert the ask into a trade from the ladder: "We can get closer to that number on a two-year term." A discount given freely trains the customer to ask again next year. A discount earned through a trade protects the relationship and the number.

### The floor and the walk line
Know the price you will not cross, tied to your net retention target. Below the floor, the renewal stops being worth the terms. Name it in prep so you do not discover it live. Most renewals never reach the floor. Knowing where it is keeps you calm above it.

## Quality gates
- The value recap comes before any price discussion. Always.
- No concession without something traded back. No free discounts.
- The floor is named in prep, before the conversation, tied to the retention target.
- Concessions come off the ladder in order, one rung at a time, never in a jump.
- Value claims are sourced from real adoption, never asserted to win the point.

## Output (example)
```
RENEWAL NEGOTIATION, prep
Current: 1-year, list price. Renewal in 45 days. Customer signaled a discount ask.

Value recap (lead here)
  Deeply adopted across the team, key workflow now runs on the product.
  Outcome they wanted is measurably closer (illustrative).

Options to present
  A) Flat 1-year renewal at list.
  B) 2-year at a modest rate improvement.   <- steer here
  C) Expanded seats at a volume rate.

Concession ladder (in order)
  1. Better rate ONLY in exchange for a 2-year term.
  2. Small credit ONLY in exchange for a case study.
  3. Volume rate ONLY in exchange for more seats.
  Floor: the NRR-protecting minimum. Do not cross it.

"We want a discount" answer
  "Understood. Given the value your team is getting, I can improve the rate
   on a two-year commitment. Want me to put that shape together?"
```
(All numbers and details are illustrative.)

## Where the numbers come from
The floor, the term options, and the ladder order are yours to set, tied to your net retention target. The example figures are illustrative, not benchmarks. Real levers come from your pricing and your margin. The structure does not change. The numbers are yours.

## Example chat

**You:** They're asking for a discount on the renewal. Current is 1-year at list, 45 days out. Help me prep.

**Claude:** Built the prep. Lead with value, not the number.
```
RENEWAL NEGOTIATION, prep
Value recap (lead here)
  Deeply adopted across the team, key workflow now runs on the product.

Options to present
  A) Flat 1-year renewal at list.
  B) 2-year at a modest rate improvement.   <- steer here
  C) Expanded seats at a volume rate.

Concession ladder (in order)
  1. Better rate ONLY in exchange for a 2-year term.
  Floor: the NRR-protecting minimum. Do not cross it.

"We want a discount" answer
  "Understood. Given the value your team is getting, I can improve the rate
   on a two-year commitment. Want me to put that shape together?"
```
The rule this enforces: no concession without something traded back. If you'd asked me to just build "the discount," I'd have pushed back and built the ladder instead, because a free discount trains them to ask again next year.

**You:** What if they push past option B and still want a flat discount, no term trade?

**Claude:** Then you move to rung two, a small credit only in exchange for a case study or reference, still a trade, never free. If they push past that, you're near the floor, and the floor is where you stop, not where you improvise. Sharpener: connect your product-analytics tool and I'll swap the "deeply adopted" claim for the real adoption numbers, so the value recap is exact instead of a description.

## Go further
The prep gets you into the room calm. Here is the version that keeps you calm every renewal, not just this one.

- **Trigger prep automatically at 45 days out.** Schedule a Claude task off your CRM's renewal-date field so the negotiation plan is built before the customer brings up price.
- **Ground the value recap in real usage.** Connect Amplitude so the adoption story pulls actual numbers instead of a CSM's memory of how the account is doing.
- **Log every concession given.** Write each trade back to Salesforce so next year's negotiation starts knowing exactly what was already given away.

You walk in with the ladder already built instead of improvising it live.

## Make it yours
Fork it. Change the ladder, the options, the floor. The point is not to run someone else's playbook. It is to run yours, faster, so you walk into the renewal calm and walk out with the number protected. Built by an operator. Customize it, break it, make it better.
