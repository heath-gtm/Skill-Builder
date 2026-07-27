---
name: event-taxonomy-builder
description: Build the canonical event taxonomy your product analyst runs on. Names the moments that actually signal value in YOUR product, tiers them by how reliable they are, rolls them into a short list of capabilities, and hands back a taxonomy doc plus an adoption rubric. Built for any product-led or hybrid GTM team, customizable to your product and analytics tool. Trigger on "what events signal value in my product", "build my event taxonomy", "which events are reliable", "define my product capabilities", "map events to adoption", "what should my product analyst measure", or any product-instrumentation or value-moment question.
---

# Event-Taxonomy Builder

## What this does
Turns "what should we actually measure?" into a taxonomy your team can trust. It interviews you about your product, names the events that signal real value (not vanity clicks), tiers each one by how reliably it means what you think it means, and rolls the whole set into a short list of capabilities an analyst can score. The output is the source of truth every downstream product read runs on, so two people asking "how are they using us?" get the same answer.

## What you'll need
You do not need to connect anything to get value today. Describe your product and the skill builds the taxonomy now. Connect your analytics tool and it reads your real event names and usage so the taxonomy reflects what is actually firing.

- Works today with: a plain description of your product, its core actions, and the outcomes a healthy customer reaches. Paste it and go.
- More powerful connected to a product-analytics tool: it reads your live event stream, so it names real events instead of ones you hope exist, and flags the ones that barely fire.
- Sharper with a data warehouse: it checks event volume and reliability across the whole base before it trusts an event.
- Sharper with your onboarding or activation docs: it maps the taxonomy to the journey you already designed.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on what you describe today and gets sharper as you connect tools. It never claims an event fires that it cannot see, and never treats a rare event as a reliable signal. A gap is a prompt, not a guess.

- **Bring your data**: describe the product and its value moments. The skill drafts the full taxonomy and adoption rubric today.
- **Connect your tools**: the same skill reads your live events and volumes, so the taxonomy is grounded in what actually fires, not a wish list.
- **Just exploring**: no product data yet? Get the framework, the tiering test, and a worked example, so you see the shape before you build.

Every run ends with the one thing that would sharpen the next build, an event to instrument or a tool to connect.

## Customize this for yourself
This was built to be product-agnostic. Set these to your product:

| Set this | What it is | Default / Example |
|---|---|---|
| ANALYTICS tool | your product-analytics connector | Amplitude, Mixpanel, PostHog, a warehouse, a CSV |
| VALUE_MOMENTS | the actions that signal real value | your own list (the skill helps you find them) |
| CAPABILITIES | how events roll up into features | 5 to 15 named capabilities |
| RELIABILITY_BAR | volume/consistency an event needs to be trusted | fires for most active accounts, most weeks |
| GRAIN | how you group users into an account | domain, workspace id, org id |
| ANTI_SIGNALS | events that look like value but are not | logins, page views, passive opens |

The taxonomy is yours. The skill's job is to help you find the 5 to 15 moments that actually predict retention and expansion in your product, and to throw out the ones that just look busy.

## The method

### Name the value moments
Start from the outcome, not the feature. Ask what a customer has to do repeatedly for the product to be working for them. Those repeated, outcome-linked actions are your candidate value moments. A click is not a value moment. A completed core action that ties to why they bought is.

### Tier every event by reliability
Every candidate event gets a tier: TIER 1 (fires cleanly, means exactly one thing, high volume), TIER 2 (useful but noisy or lower volume, use with care), TIER 3 (a trap, looks like value but is not, or double-counts a Tier 1). Name the traps out loud so no one builds a read on them later.

### Roll events into capabilities
Group the trusted events into a short list of capabilities, the features that actually signal value. Each capability maps to its raw events explicitly, so an analyst can score adoption per capability instead of drowning in event names.

### Set the adoption rubric
Define what POWER, ESTABLISHED, EMERGING, DORMANT, UNTOUCHED, and NEVER-ADOPTED mean for each capability, in your product's real numbers. This is the rubric every product read reuses, so adoption means the same thing every time.

### Flag the anti-signals
Call out the events that inflate a picture: logins, page views, passive opens, anything that rises when nothing of value happened. A baseline "any activity" signal is fine as a floor, never as proof of value.

## Quality gates
- Every trusted event has a named tier and a one-line reason. No untiered events in the taxonomy.
- Traps are named explicitly, not quietly dropped.
- Each capability lists the exact raw events it rolls up, never a vague label.
- The adoption rubric is in your product's real numbers, not borrowed defaults.
- No event is trusted on volume it does not have. A rare event is Tier 2 or 3, never Tier 1.

## Output (example)
```
EVENT TAXONOMY · [your product] · built [date]

Capability          Raw events (trusted)              Tier
Core action         action_completed                  1
Automation          rule_created, rule_ran            1
Templates           template_used                     2 (noisy: counts drafts)
AI assist           ai_compose_accepted               1
Integrations        integration_connected             2 (low volume)

TRAPS (do not build reads on these):
  - session_start   looks active, means nothing about value
  - page_view       inflates any "usage" number

Adoption rubric (Core action):
  Power >= 5 completions/week · Established 1-4 · Emerging <1 ·
  Dormant used then stopped 14d+ · Untouched never fired

Next: instrument ai_compose_accepted server-side; it is Tier 1 logic
but currently client-only, so ~15% of fires are lost.
```

## Example chat
Here is the skill building a taxonomy from a plain product description.

**You:** We're a scheduling tool. People connect a calendar, create booking pages, and get meetings booked. What should my product analyst measure?

**Claude:** Start from the outcome, which is a meeting actually booked, and work backward. Here's the first cut:
```
Capability        Trusted event            Tier   Why
Activation        calendar_connected       1      one-time, but the gate to all value
Core action       booking_page_created     1      the thing they came to do
Value realized    meeting_booked           1      the outcome; this is your north star
Sharing           page_link_shared         2      predicts bookings but noisy
```
The one I'd flag: do not measure `login` or `dashboard_view` as usage. A customer who logs in daily but never gets a meeting booked is not healthy, they just visit. That is the ghost-active trap, and building a read on logins is how teams miss churn.

**You:** We also have team plans. Does that change it?

**Claude:** It adds a grain question. Roll events to the workspace, not the person, so a team with one power booker and five dormant seats reads as partial adoption, not full. I'd add a `seats_active_ratio` capability at Tier 2. One sharpener: connect your analytics tool and I'll check real fire volumes, so I can confirm `meeting_booked` is clean and not double-firing on reschedules before you make it your north star.

## Go further
The taxonomy is step one. Here is where an operator takes it once it holds.

- **Wire it into a live product read.** Feed the taxonomy to a product-usage analyst skill so every account gets scored on your real capabilities, on demand or nightly from Amplitude or your warehouse.
- **Watch reliability drift.** Have a scheduled Claude task re-check event volumes weekly and flag when a Tier 1 event starts dropping fires, so instrumentation bugs surface before they corrupt every read.
- **Publish it as the shared source of truth.** Push the taxonomy to Notion or your docs so product, CS, and sales all score adoption the same way instead of arguing about definitions.

You define value once, and every downstream read inherits it.

## Where the numbers come from
The tiers, the reliability bar, and the adoption thresholds are yours to set. The examples here suited a weekly-rhythm SaaS product. If your product is used in bursts or on a monthly cycle, retune the thresholds. The logic, name the outcome, trust events by reliability, roll up to capabilities, does not change.

## Make it yours
Fork it. Change the value moments, the tiers, the capability list, the rubric. The point is not to measure someone else's product. It is to name what value looks like in yours, once, so every read agrees. Built by an operator. Customize it, break it, make it better.
