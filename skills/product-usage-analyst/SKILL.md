---
name: product-usage-analyst
description: Turn "how are they using us?" into a product-engagement read. Adoption tiers per capability, a rising/flat/declining trend on every one, power-user identification, and a ghost-active check that catches accounts that look alive but create no value. Built for any product team, customizable to your product-analytics tool and your capability list. Trigger on "how is this account using us", "is this domain active", "find power users at this company", "what have they not adopted yet", "who signed up recently", "are they really engaged", or any product-usage question.
---

# Product-Usage Analyst

## What this does
Reads how an account actually uses your product and gives a plain read: which capabilities they have adopted, whether each one is rising or fading, and who the power users are. It turns "how are they using us?" into a product-engagement score you can act on, and it flags the accounts that look active on the surface but create no real value underneath.

## What you'll need
You do not need to connect anything to get value today. Bring a usage export and the skill runs now. Connect a product-analytics tool and it pulls the same data automatically and adds signals you cannot paste by hand.

- Works today with: a usage export by account, with a row per account and columns for each capability's activity count and a last-active date. Paste it or upload a CSV.
- More powerful connected to a product-analytics tool: it reads events automatically, at your chosen account grain, across the whole base.
- Sharper with a CRM: cross-references usage to the account record and its fit score.
- Sharper with a longer history: a full trend window instead of a single snapshot.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your usage export. The skill runs the full adoption read today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls events automatically and adds signals you cannot paste by hand (live trend, new-user first-seen dates, per-user breakdowns). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact columns it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a column to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS product with a handful of named capabilities. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| ANALYTICS tool | your product-analytics connector | Amplitude, Mixpanel, PostHog, a CSV export |
| ACCOUNT_GRAIN | how you group users into an account | email domain, workspace id, org id |
| CAPABILITIES | the features you want adoption on | your own list (see below) |
| TREND_WINDOW | weeks of history for the trend | 12 (re-tune to your cycle) |
| POWER_THRESHOLD | usage that counts as a power user | top decile of activity, or your own bar |
| NEW_USER_WINDOW | recency for "new signups" | 14 days |
| FIT_SCORE field | your account fit score, if you have one | any 0-100 fit or propensity score |

The capability list is yours. Point the skill at the 5 to 15 features that actually signal value in your product, not anyone else's.

## The method

### Adoption tier per capability
Every capability gets exactly one tier: POWER, ESTABLISHED, EMERGING, DORMANT, UNTOUCHED, NEVER-ADOPTED. Power means heavy, recent, repeated use. Untouched means they had it and stopped. Never-adopted means they never started. The Untouched and Never-adopted rows are the onboarding gap, the consultative outreach list.

### Trend per capability
Over TREND_WINDOW weeks, each capability is RISING, FLAT, DECLINING, or COLLAPSED. A high tier with a declining trend is an early quiet-quitting signal, worth more than the raw count.

### Power-user identification
Surface the individual users whose activity clears POWER_THRESHOLD, with which capabilities each one leans on. These are your expansion anchors and your reference candidates.

### Ghost-active check
When an account looks alive on the baseline "any activity" signal but every real capability is zero, flag it. This is the classic blind spot: seats are technically active (someone logs in) but no value is being created. Must show the per-capability zeros that prove it.

### Fit-score cross-check
If you carry an account fit score, compare it to what usage actually shows. When the fit score sits at the floor but adoption is clearly real, call it a false negative and promote the account. When the score is high but usage is a ghost, flag the mismatch the other way. The usage is the ground truth.

## Quality gates
- No GHOST-ACTIVE verdict without showing the per-capability zeros that prove it.
- Every "not adopted" surfaces capability by capability, named, never "low usage."
- Trend is over the full window, never a single week. Small samples lie.
- Never report a number the export does not contain. A missing column is a prompt, not a guess.

## Output (example)
```
PRODUCT ENGAGEMENT · acme.com · 12-week window

Capability            Adoption      Trend       Last active
Core action           Power         Rising      today
Automation            Established   Flat        yesterday
Templates             Emerging      Rising      3d ago
AI assist             Dormant       Declining   18d ago
Advanced module       Untouched     -           -
Integrations          Never-adopt   -           -
_active baseline      Power         Rising      today

NOT ghost-active: 4 of 6 capabilities show real activity
Fit-score check: score 28 looks low, but adoption is real -> false negative, promote
Weekly actives: 351 latest · 339 four-week avg (Rising)
New users (14d): 8 signups · 5 active within 7d · 3 still untouched

Story: Power on the core action with rising template use. The gap is the
advanced module and integrations. 3 new users have not activated yet, that is
the onboarding conversation.
```

## Example chat
Here is the skill running on a real account, start to finish. You paste what you have; it does the read.

**You:** How is acme.com using us? Here's the 12-week export.
[pastes a CSV: one row per capability, activity counts, last-active dates, plus an _active baseline row and a fit score of 28]

**Claude:** Read's done. Acme is real, and your fit score is wrong about them.

```
PRODUCT ENGAGEMENT · acme.com · 12-week window
Capability          Adoption      Trend       Last active
Core action         Power         Rising      today
Automation          Established   Flat        yesterday
Templates           Emerging      Rising      3d ago
AI assist           Dormant       Declining   18d ago
Advanced module     Untouched     -           -
Integrations        Never-adopt   -           -
```

Four of six capabilities show real activity, so this is **not** ghost-active. Power on the core action, and template use is climbing. Two things stand out:

- **Fit-score false negative.** The score sits at 28 (floor), but adoption is clearly real. The usage is ground truth. I'd promote Acme and stop treating it like a cold account.
- **A quiet-quitting tell.** AI assist is Dormant *and* Declining. Not urgent yet, but that's the capability to ask about before it collapses.

**You:** Who are the power users?

**Claude:** Three clear the top-decile bar: j.reyes@acme.com (core action + automation, daily), m.okafor@acme.com (templates, rising fast, your reference candidate), and s.lin@acme.com (core action only). Reyes and Okafor are your expansion anchors. Want me to hand the two untouched capabilities (Advanced module and Integrations) over to the outreach skill as the onboarding-gap angle?

**You:** Yes.

**Claude:** Passing the named gaps to `trigger-outreach`. One sharpener for next time: this ran on a single snapshot with the fit score attached. Connect your product-analytics tool and I'll pull the live trend and each new signup's first-seen date automatically. Same read, no paste, and I can catch the AI-assist decline the week it starts.

## Where the numbers come from
TREND_WINDOW (12 weeks), NEW_USER_WINDOW (14 days), and the power-user cutoff are defaults, not laws. They suited a mid-market SaaS product with a steady weekly rhythm. If your product is used in bursts or on a monthly cycle, widen them. The logic does not change. The thresholds are yours.

## Go further
The read is step one. Here is where an operator takes it once the manual version proves out.

- **Score the whole base while you sleep.** Point a scheduled Claude task at Amplitude every night, run this read on every account, and write the product-engagement verdict and the false-negative flag straight back to Salesforce. You wake up to a scored book, not a to-do.
- **Catch only the flips.** Have the nightly run diff against yesterday and DM the account owner in Slack just the accounts that *changed*: a capability that started collapsing, or a fit-score false negative that just proved itself. No dashboard to check; the signal comes to the rep.
- **Close the loop to outreach.** Feed the Untouched and Never-adopted rows directly into a cold-email or trigger-outreach skill so the onboarding-gap list leaves as sent messages, not a spreadsheet nobody opens.

The stack is boring on purpose: Amplitude reads it, Claude scores it, Salesforce holds the verdict, Slack delivers the one line that matters. You built the read once; now it runs itself.

## Make it yours
Fork it. Change the capabilities, the tiers, the trend window. The point is not to run someone else's rubric. It is to see your own product's adoption story, faster. Built by an operator. Customize it, break it, make it better.
