---
name: build-signal-library
description: Build the signal library your AI-native GTM repo runs on, the file that turns your context brain from a reference doc into a system that acts. Define each signal with a detection method, a point value, a decay curve, combination bonuses, and a message hook, plus a performance-log stub so it becomes a learning system. Feeds context/signal-library.md. Fire on "build our signal library", "what signals should we track", "signal scoring", "signal decay", "signal combinations", "define our signals", or turning intent, usage, funding, or hiring into something a rep can act on.
---

# Build Your Signal Library: signals that fire, decay, and combine

## What this does
Turns "we should watch for funding" into a real signal library: each signal with how you detect it, what it is worth, how it decays, which combinations score higher, and the message hook that earns the reply. This is the file that makes your context repo act, not just describe. A list of alerts that is never scored or decayed is not a signal library.

## What you'll need (reads)
Your ICP definition (from Define Your ICP), so signals are scored against real fit. And whatever you know about the moments that precede a deal: funding, a new hire, a product-usage spike, a competitor switch, intent. No connectors required to design it; connect your data sources when you want to detect them live.

## The method
1. List the moments that precede a deal. The events that mean now, not someday: a new RevOps hire, a Series B in the last 60 days, a usage spike, a competitor renewal coming up. Start with 5 to 8, not 30.
2. Give each a detection method. How you actually see it: a Crunchbase alert, a job-board scrape, a product-usage threshold, an intent feed. A signal you cannot detect is a wish.
3. Score each in points, against fit. The same signal on a Tier 1 account is worth more than on a Tier 3. Points, not vibes.
4. Set a decay curve. A funding round from 150 days ago is not the signal it was at 10 days. Decay the points over time so your active list reflects real urgency, not old history. This one step fixes the list that quietly fills with stale accounts.
5. Add combination bonuses. Two signals together tell you more than either alone. A Series B plus a new RevOps hire is not a 65-point account, it is an 80-point account: budget exists and someone is rebuilding. Write the pairs that matter and the bonus each earns.
6. Write a message hook per signal. The one line that makes the outreach obviously about them, tied to the signal that fired.
7. Leave a performance-log stub. A column for meetings generated per signal, empty for now. Episode 4 fills it, and the library starts to learn which signals actually pay.

## Failure points
- A signal you cannot detect, so it never fires.
- No decay, so the active list is a lie full of six-month-old events.
- Scoring every signal the same regardless of fit, so Tier 3 noise floats to the top.
- Thirty signals nobody maintains instead of eight that work.

## The receipt (writes)
[your signal library: 5 to 8 signals with detection, points, decay, combination bonuses, and hooks, plus an empty performance log. This becomes context/signal-library.md]

Example (illustrative):

| Signal | Detection | Points | Decay | Combo | Hook |
|---|---|---|---|---|---|
| New RevOps hire | job-title change | +30 | 90 days | +15 with fresh funding | "Saw you just brought RevOps in-house" |
| Pricing page revisited 3x | product or web analytics | +20 | 14 days | +20 with an active trial | "Noticed the team back on pricing" |
| Series B raised | funding source | +25 | 120 days | +15 with headcount growth | "Congrats on the round" |

Performance log: empty until outcomes come back in Episode 4.

## Example chat
**You:** We should be tracking signals like funding rounds and new hires. Help me build a real signal library, not just a list of alerts.

**Claude:** Built the first pass, five signals with the parts that make it actually usable.
```
Signal              Detection          Points  Decay     Combo
New RevOps hire      job-title change   +30     90 days   +15 with fresh funding
Pricing page x3       product analytics +20    14 days   +20 with active trial
Series B raised        funding source    +25    120 days  +15 with headcount growth
```
The part most lists skip: decay. A Series B from 150 days ago isn't the signal it was on day 10, and without decay your "hot" list quietly fills with stale accounts nobody should be prioritizing anymore.

**You:** What about when two signals hit the same account?

**Claude:** That's the combo bonus. A Series B plus a new RevOps hire isn't a 65-point account, it's an 80-point account, because budget exists and someone is actively rebuilding the stack. One sharpener: leave the performance log empty for now, but wire it up once outreach starts landing, that's what turns this from a static list into a system that learns which signals actually book meetings.

## Go further
Defining the signals is the design work. Here's how they start firing on their own.

- **Detect them live.** Connect Clay or a Crunchbase feed for funding, a job-board scrape for hires, and Amplitude for usage spikes, so each signal fires the moment its detection method sees it instead of you checking manually.
- **Score and decay automatically.** Run a scheduled Claude task nightly that recalculates every account's score against the decay curve, so the active list always reflects real urgency, not last month's snapshot.
- **Close the loop with performance data.** Feed booked-meeting outcomes back from Salesforce into the performance log so the library learns which signals actually convert, and the weak ones get retired.

A signal library that decays and learns is worth more than a longer list of alerts.

## Next move
Score the accounts your signals fire on, then wire the freshest one to a motion before it goes stale. Built GTM. Receipts only.
