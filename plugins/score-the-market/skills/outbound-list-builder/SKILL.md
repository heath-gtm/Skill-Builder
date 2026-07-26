---
name: outbound-list-builder
description: Turn an ICP into a scored, prioritized target list. Firmographic and signal filters, a tiering rule, the personas to reach per account, and a plain reason each account earns its spot. Built for B2B outbound teams, customizable to your ICP and your data sources. Trigger on "build me a target list", "who should I prospect", "build a prospect list from my ICP", "which accounts first", "add personas to this list", or any list-building or account-prioritization task.
---

# Outbound List Builder

## What this does
Takes your ideal-customer profile and turns a raw pile of accounts into a ranked list you can work in order. It filters on the firmographics that define fit, layers on the buying signals that mean now, sorts everything into tiers, names the personas to reach at each account, and writes one line on why each account made the cut. You get a list you can defend, not a list you have to trust.

## What you'll need
You do not need to connect anything to get value today. Bring your accounts and the skill runs now. Connect the tools below and it pulls the accounts and signals automatically, and adds fit data you cannot paste by hand.

- Works today with: your ICP definition and a list of accounts (company name, domain, industry, size, and anything you already know). Paste it or upload a CSV.
- More powerful connected to a CRM: it reads your accounts, owners, and prior activity, so you never build a list that collides with an open deal.
- Sharper with an enrichment tool: fills firmographics, headcount, and technographic data on accounts you only have a name for.
- Sharper with a signal source: adds funding, hiring, and news triggers that separate "good fit" from "good fit, right now."

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the accounts you give it today and gets more powerful as you connect tools. It never invents a firmographic it cannot see. A missing field is a prompt, not a guess.

- **Bring your data**: paste or upload your accounts and your ICP. The skill runs the full filter, score, and tier on what you have today. No connection required.
- **Connect your tools**: the same skill pulls accounts from your CRM, fills the gaps from enrichment, and reads live signals. Same output, less typing, sharper ranking.
- **Just exploring**: no list yet? Get the framework, the exact fields it scores, and a worked example on sample accounts, so you can see the shape before you feed it.

Every run ends with the one thing that would sharpen the next run, a firmographic to add or a signal source to connect.

## Customize this for yourself
This was built for a B2B team running outbound against a defined ICP. Set these to your motion:

| Set this | What it is | Default / Example |
|---|---|---|
| ICP definition | who you sell to, in fields | industry, size band, region, model |
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| ENRICHMENT | firmographic / technographic source | any enrichment tool |
| SIGNAL sources | the triggers that mean "now" | funding, hiring, tech change, news |
| FIT filters | the hard gates an account must pass | headcount 50-500, cloud stack, US |
| PERSONAS | the roles you sell to per account | economic buyer, champion, user |
| TIER cutoffs | the score bands that split the list | A / B / C |
| EXCLUDE rules | who never belongs on the list | open deals, current customers, competitors |

Point it at your ICP, not anyone else's. The skill scores fit against the profile you give it, so the list is only as good as the definition behind it.

## The method

### Fit filter (hard gates first)
Run the firmographic gates before anything else. An account that fails a hard gate is out, no matter how strong its signals. Size, industry, region, and business model are gates. Everything else is a scoring input. This keeps the list honest and small.

### Fit score (0-100)
Each account that clears the gates gets a fit score built from weighted firmographics: how close to the center of the ICP on size, industry, model, and stack. State the weights so the score is readable, not a black box. Two accounts with the same score should look alike on paper.

### Signal layer (fit plus timing)
On top of fit, add timing. A recent funding round, a burst of relevant hiring, a new product launch, a job posting for a role your product serves, or a technology change are all reasons to move an account up the list this week. Signal never overrides a failed gate. It reorders the accounts that already fit.

### Tiering
Sort into tiers off the combined fit-plus-signal score. Tier A is fit and a live signal, work now. Tier B is strong fit, no signal yet, work steadily. Tier C is edge-of-ICP, work only when capacity allows. The tier tells the rep how hard to lean, not just who to call.

### Personas per account
For each account name the roles to reach, not just one contact. An outbound touch that hits one person is one point of failure. Map the economic buyer, the likely champion, and the day-to-day user for each account, so multi-threading is built into the list, not bolted on later.

### The reason line
Every account carries one plain sentence on why it is here: the fit plus the signal, in words a rep can repeat. If an account cannot earn a reason line, it does not belong on the list.

## Quality gates
- No account on the list without a reason line a rep could say out loud.
- Hard gates run before scoring. A failed gate is never scored around.
- Signals reorder accounts that already fit. A signal never promotes a non-fit.
- Excluded accounts (open deals, customers, competitors) are dropped before tiering, not after.
- A fit score always shows the weights behind it. No number without its inputs.

## Output (example)
```
TARGET LIST · 6 accounts scored (illustrative)
Account       Fit   Signal              Tier   Personas
Northwind     92    Series B, 30d ago    A      VP Sales, RevOps Lead, SDR Mgr
Acme Corp     88    Hiring 4 AEs         A      CRO, Sales Ops, AE
Vertex        81    none                 B      VP Sales, Enablement
Blend Labs    74    New product launch   B      Head of Growth, PMM
Cirrus        61    none                 C      Sales Lead
Delta Co      58    none                 C      Founder

Work order:
  1. Northwind. Fresh raise, full committee mapped. Lead now.
  2. Acme Corp. Hiring AEs signals a scaling team. Reach the CRO.
  3. Blend Labs. Launch gives a reason to reach out this week.
```

## Where the inputs come from
The tier cutoffs, the fit weights, and the signal window (recent means the last 30 to 60 days) are defaults, not laws. They suited a mid-market outbound motion. If your cycle runs longer or your ICP is narrower, retune them. The logic does not change. The thresholds are yours.

## Make it yours
Fork it. Change the gates, the weights, the tiers, the personas. The point is not to run someone else's ICP. It is to run yours, faster, so the list you work is a list you built. Built by an operator. Customize it, break it, make it better.
