---
name: job-change-watchlist
description: The standing system that watches every contact who matters for a job change. Builds a tiered watchlist from engagement, role, and account value, picks a detection method per tier, runs a weekly diff that separates real moves from title cleanups, and routes every confirmed move to a named owner with a deadline. Trigger on "build a job-change watchlist", "track contact job changes", "who changed jobs this month", "monitor my contacts for moves".
---

# Job-Change Watchlist

## What this does
Builds and runs the standing system that watches your contacts for job changes. It decides who earns a watchlist slot, assigns each contact a tier, picks the cheapest detection method that works for that tier, and runs a weekly diff against the last known title and company. Every confirmed move gets routed to a named owner with a deadline. A champion who lands somewhere new is the warmest pipeline you will ever get, and this is the system that makes sure you hear about it first. What happens after detection, the outreach play itself, belongs to the champion-move-detection skill, which consumes this watchlist's alerts.

## What you'll need
You do not need to connect anything to get value today. Bring your contacts and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a contact export with name, title, company, segment, last-engaged date, and role (champion, user, buyer). Paste it or upload a CSV.
- More powerful connected to a CRM: it builds the watchlist from contact roles, account status, and closed-lost history automatically.
- Sharper with an enrichment tool (Clay, Common Room): scheduled refreshes catch moves without anyone checking manually.
- Sharper with Slack: routed alerts land in front of the owner the day the move is confirmed.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a move it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your contact export. The skill tiers the list, assigns detection methods, and gives you the weekly diff routine to run by hand. No connection required.
- **Connect your tools**: the same skill pulls contacts from your CRM, refreshes titles through enrichment on a schedule, and posts routed alerts to Slack. Same system, less effort, faster detection.
- **Just exploring**: no data yet? Get the tiering scheme, the detection ladder, and a worked example on sample contacts, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org with a customer base, open pipeline, and a closed-lost history worth mining. Set these to your book:

| Set this | What it is | Default / Example |
|---|---|---|
| TIER 1 threshold | who gets the closest watch | Champions at accounts over $25K ARR, engaged contacts on open deals |
| TIER 2 threshold | who gets the standard watch | Active users at customer accounts, buyers on deals closed-lost under 12 months |
| TIER 3 threshold | who gets the cheap watch | Everyone else with real engagement in the last 18 months |
| TIER 1 refresh | enrichment cadence for Tier 1 | Weekly |
| TIER 2 refresh | enrichment cadence for Tier 2 | Monthly |
| TIER 3 refresh | enrichment cadence for Tier 3 | Quarterly, plus bounce tripwires only |
| CUSTOMER moves route to | owner of a customer-contact move | The account's CSM, 2-business-day deadline |
| DEAL moves route to | owner of an open-deal-contact move | The deal's AE, same-day deadline |
| ALUMNI moves route to | owner of a past-champion move | Whoever owns new pipeline, 5-business-day deadline |

The thresholds are yours. A PLG motion might tier on product usage instead of ARR. The system does not change.

## The method

### Build the watchlist
Not every contact earns a slot. A slot costs refresh budget and reviewer attention, so gate on three things: engagement depth (they showed up to calls, replied, used the product), role (champion, active user, economic buyer), and account value (ARR for customers, deal size for pipeline, deal size at loss for closed-lost). Three source pools: champions and users at customer accounts, engaged contacts on open deals, and past champions at closed-lost accounts. Score each contact against the tier thresholds and assign exactly one tier.

### Choose the detection method per tier
Match the cost of detection to the value of the contact.
- Tier 1: scheduled enrichment refresh (Clay or Common Room) weekly, plus a manual LinkedIn check when a refresh looks off.
- Tier 2: enrichment refresh monthly, plus title-change diffs on every CRM sync.
- Tier 3: email bounce tripwires and quarterly refresh only. A hard bounce on a work email is a free, high-precision move signal. Never pay weekly refresh rates for Tier 3.

### Run the weekly diff
Once a week, diff current title and company against last known. A real move is a company change, or a title change plus a domain change, or a hard bounce plus a LinkedIn mismatch. A title cleanup is the same person at the same company with a reworded title, "Sr. Manager" becoming "Senior Manager, Demand Gen." Cleanups update the record silently. Only real moves generate alerts.

### Route every move
Every confirmed move gets an owner and a deadline the day it is confirmed. Customer-contact moves route to the account's CSM, who now has both a retention risk at the old account and a warm door at the new one. Open-deal moves route to the AE, same day, because a deal just lost or gained a thread. Alumni moves route to whoever owns new pipeline. The alert carries the contact, the old and new company, the evidence, the owner, and the deadline. What the owner does next is the champion-move-detection play.

## Quality gates
- No move alert without evidence: the source, the old value, the new value, and the date detected.
- Title cleanups never generate alerts. Same company plus reworded title updates the record silently.
- Every alert has a named owner and a deadline. An unrouted alert is a dropped one.
- A bounce alone is a tripwire, not a confirmation. Confirm against a second source before routing.

## Output (example)
```
JOB-CHANGE WATCHLIST · weekly diff · 214 contacts watched (sample data)
Contact         Was                          Now                       Tier  Route
Dana Reyes      VP Ops, Northwind (cust)     VP Ops, Vertex Labs       1     CSM J. Park, 2 days
Sam Okafor      Dir Eng, Acme (open deal)    Dir Eng, Fabrikam         1     AE M. Cole, today
Lee Tran        Mgr RevOps, Contoso (lost)   Sr Dir RevOps, Globex     2     Pipeline: T. Nash, 5 days
Priya Nair      "Sr. Mgr" -> "Senior Manager", same company            2     Cleanup, no alert

3 moves routed. 1 cleanup absorbed. 2 Tier 3 bounces pending confirmation.
```

## Example chat
**You:** Build me a job-change watchlist from this contact export. [pastes CSV]

**Claude:** Tiered all 214 contacts. 31 in Tier 1 (champions at accounts over $25K plus engaged contacts on your 9 open deals), 88 in Tier 2, 95 in Tier 3. Detection plan: weekly enrichment refresh on Tier 1, monthly plus CRM title diffs on Tier 2, bounce tripwires only on Tier 3. One gap: 14 Tier 1 contacts have no LinkedIn URL on file, so a refresh cannot verify them. That is the first thing to fix.

**You:** Who changed jobs this month?

**Claude:** Two real moves and one cleanup in this month's diffs. Dana Reyes left Northwind, a customer account, for Vertex Labs: routed to the CSM with a 2-day deadline, because Northwind just lost its champion and Vertex Labs just gained one. Sam Okafor moved off your open Acme deal: routed to the AE, same day. Priya Nair's title change at Contoso is a rewording, same company, so the record updated silently with no alert. One sharpener: connect Slack so these route the day they are confirmed instead of waiting for the weekly review.

## Go further
The manual weekly diff proves the system. Here is where an operator takes it once it earns its keep.

- **Automate the refresh.** Put Tier 1 on a weekly Clay or Common Room enrichment run so title and company updates arrive without anyone checking profiles by hand.
- **Catch moves between refreshes.** Turn on Salesforce field history for contact Title and Email, so any change written by a sync or a rep becomes a diff the same day.
- **Route alerts where owners live.** Post each confirmed move to Slack, tagged to the CSM, AE, or pipeline owner, with the deadline in the message.
- **Schedule the diff itself.** A scheduled Claude task runs the weekly diff every Monday, absorbs the cleanups, and posts only the real moves.
- **Verify the ambiguous ones.** Keep LinkedIn Sales Navigator as the confirmation source when a bounce or a partial refresh needs a human-grade check before routing.

The watchlist is only as good as its refresh rate. Automate the refresh.

## Make it yours
Fork it. Change the tiers, the cadences, the routing owners. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
