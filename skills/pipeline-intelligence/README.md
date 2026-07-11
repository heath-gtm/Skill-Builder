# Pipeline Intelligence

> Answer the three questions every pipeline review asks: do I have enough, who do I work next, and is this month's pipeline any good. Three modes: pipeline coverage and activity by channel, account prioritization into five ranked top-10 lists, and a monthly ICP-quality read that scores the new-deal cohort on a composite fit score and flags the misses. Built for B2B sales teams and managers, customizable to your CRM and your motion. Trigger on "how's my pipeline", "pipeline coverage", "pipeline by channel", "which accounts should I work next", "who do I go after", "re-engage cold accounts", "is this month's pipeline any good", "monthly pipeline analysis", or any coverage, prioritization, or pipeline-quality question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/pipeline-intelligence && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/pipeline-intelligence/SKILL.md -o ~/.claude/skills/pipeline-intelligence/SKILL.md && echo "Installed pipeline-intelligence. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/pipeline-intelligence/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Pipeline Intelligence

## What this does
Reads your pipeline and answers three questions. Do I have enough, coverage and activity by channel against target. Who do I work next, five ranked lists of the accounts worth a touch this week, each with a reason and an angle. Is this month's pipeline any good, a quality read that scores the new-deal cohort on a composite fit score, catches the accounts your scoring got wrong, and compares this month to a trailing baseline. Run coverage and prioritization together off a weekly snapshot; run the quality read once a month.

## What you'll need
You do not need to connect anything to get value today. Bring your pipeline or account list and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a pasted list or CSV of accounts or pipeline, with channel source, stage, status, a fit score or tier if you have one, and last activity date. For coverage, include your targets by channel.
- More powerful connected to a CRM: it reads accounts, opportunities, stages, and activity automatically across the whole book.
- Sharper with an ICP-scoring tool: adds an independent fit verdict so the monthly quality read can cross-check your own score and catch false negatives and false positives.
- Sharper with a product-analytics tool: adds usage signal on product-sourced accounts so expansion angles reference real behavior.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your account list or pipeline snapshot. The skill runs coverage, prioritization, and the quality read today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls accounts, opportunities, and activity automatically and cross-scores fit where a scoring tool is connected. Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a multi-channel motion. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| CHANNEL field | how you attribute source | Inbound, Outbound, Product, Expansion |
| STAGE field | your motion stage | New, Engaged, Cold, Nurture, Disqualified |
| FIT score | your account fit score and tiers | Excellent / Good / Moderate / Low |
| ICP cross-check | an independent fit verdict | your ICP-scoring tool (optional) |
| COVERAGE target | healthy pipeline-to-target ratio | 3x healthy, below 2x concerning |
| ENGAGED window | days of activity that mean engaged | 14 (re-tune to your cycle) |
| BASELINE window | trailing months for the quality trend | 3 (trailing-3-month average) |

Use whatever fit score you already trust. The quality read cross-checks it against an independent signal only if you connect one, otherwise it reports on the score you bring.

## The method

Pick the mode that matches the question. Coverage and prioritization usually run together off a snapshot. The quality read is a monthly deliverable.

### Mode A: pipeline coverage and activity
Do we have enough pipeline, and is it converting?

**1. Coverage and health.** Total pipeline created, current vs target. Pipeline by channel (Inbound, Outbound, Product, Expansion), each with current, target, variance. Coverage ratio, total pipeline over remaining target (healthy at 3x or more, concerning below 2x). Channel mix, balanced or over-reliant on one channel.

**2. Activity metrics.** Compare actual activity to target to find the bottleneck: accounts engaged, meetings booked, qualified leads, qualified opportunities, each current vs target vs percent to target, broken out by channel. Ask whether activity is converting to pipeline at the expected rate.

**3. Stage distribution.** Count accounts by stage (New, Engaged, Cold, Nurture, Disqualified) and break down by channel within each. Red flags: Cold outnumbering Engaged (a re-engagement problem), New accounts piling up without moving to Engaged (an activation problem), too many in Nurture (pipeline sitting idle).

**4. Engagement velocity.** How fast do New accounts become Engaged? What share of Engaged accounts reach an opportunity? Are Cold accounts being re-engaged or just accumulating?

### Mode B: account prioritization (the five lists)
Turn the account list into five ranked top-10 lists. Each list holds the top 10 accounts, and for each account give: account name, channel source, fit tier, status, notes, and a suggested engagement angle of one or two sentences drawn from the account's website (for product accounts, reference actual usage).

- **List 1, top 10 New accounts to go after.** Filter to New. Sort by account fit (Excellent to Good to Moderate), then channel diversity. Fresh accounts nobody has touched, best-fit first.
- **List 2, top 10 Cold accounts to re-engage.** Filter to Cold. Sort by fit, then how recently they went cold. They showed interest then fell off, re-engagement beats cold outreach because context exists.
- **List 3, top 10 Inbound accounts to prioritize.** Filter to Inbound. Sort by fit, then stage (Engaged to New to Cold). They raised their hand, best-fit first maximizes conversion.
- **List 4, top 10 Outbound accounts to prioritize.** Filter to Outbound. Sort by fit, then stage (New to Engaged to Cold). Outbound costs more effort per account, spend it on the highest-fit accounts.
- **List 5, top 10 Product accounts to prioritize.** Filter to Product. Sort by both product fit and account fit (a great product fit with poor company fit is still a poor bet). These accounts already use your product, the angle is expansion, reference real usage.

**Deterministic selector (for reproducible output off a snapshot).** Filter to stage in {Engaged, New}, then sort by (1) blended fit score descending, (2) open opportunity count ascending, (3) days since last activity ascending. Cap at three per channel so no single channel dominates. Two runs against the same snapshot produce the same top 10.

**Crafting angles.** Visit the account's website and write one or two sentences that reference something specific (industry, size, recent news, tech stack), connect it to a relevant value prop, and for product accounts reference which features they use and where the expansion opening is. Good: "Mid-market recruiting firm running high-volume outreach, position sequences as a way to scale candidate engagement without adding headcount." Bad: "They might benefit from us."

### Mode C: monthly ICP-quality read
How good is this month's pipeline? Answer three questions: is the volume real, is it good ICP, and what to keep doing vs fix. Build it from CRM ground truth, cross-scored against an independent fit signal if one is connected, compared to a trailing baseline, laid out as a leadership talking script.

**Cohort.** Score the new qualified-opportunity cohort for the target month (exclude renewals). Keep a parallel qualified-lead cohort to sanity-check funnel movement and catch opportunities created late-month that have not yet advanced. If your primary cohort field is inconsistently populated, fall back to created-date and document the fallback.

**Channel attribution.** Use one canonical channel field that rolls up to Inbound / Outbound / Product / Expansion. Do not mix in free-text or inconsistent source fields.

**Composite fit scoring.** Use two independent signals when available: your own account fit score, and an independent ICP verdict from a scoring tool (for example an ICP-qualification service). Grade the cohort:
- Top grade: the independent verdict is Strong, regardless of your own score.
- Mid grade: the independent verdict is Moderate, or Strong while your own score has no read.
- Off-ICP: the independent verdict is Weak or Bad at any score.

**Override flags, the highest-value output.** A false negative is your score Low while the independent verdict is Strong, you almost passed on a real fit. A false positive is your score High while the independent verdict is Weak or Bad, you prioritized a non-fit. Name each one at the deal level with the account and the dollar amount. If you only have one signal, say so and skip the cross-check.

**Trailing baseline.** Same cohort definition over the prior three months. Report per-month detail and the three-month average. Flag any anomalously low month and offer a trimmed-baseline alternative.

**Deal-health overlay.** For every target-month opportunity still open, compute days since it qualified, run the qualification-vs-stage gap check (see `deal-intelligence`), and surface concentration risk (which rep owns more than 40% of the cohort by amount).

**Velocity reality-check.** Compare target-month closed-won to pipeline created. If closed-won grew much slower than pipeline, flag it and note expected forward-quarter conversion (trailing win rate times cycle time).

**Report structure (nine sections, in order, the leadership talking script).**
1. At a glance: four metric cards (pipeline, closed-won, strong-fit percent, misclassified amount).
2. What the month proved: two callouts side by side, "keep doing this" and "fix this immediately," each naming specific accounts and amounts.
3. Channel breakdown: one card per channel with amount, opportunity count, strong-fit count, weak/bad amount, fit alignment, average deal size, closed-won, plus a short narrative.
4. Score vs independent verdict: a table of every account where the two disagree, flagged false negative or false positive, with a callout summarizing the systemic finding. This is the headline insight.
5. Every opportunity ranked by composite grade: a full sortable table with override flags inline.
6. Rep breakdown: per-rep cards plus a coaching callout naming the highest-leverage save or post-mortem.
7. Vs trailing average: per-month detail, average row, target-month row, delta row, with a callout if velocity drops despite volume rising.
8. Action plan: five to seven specific actions, each with a named owner and a due date. No abstractions.
9. Methodology: cohort definition, channel attribution, scoring rules, baseline definition, and a reconciliation block if your dashboard total differs from the report total.

## Quality gates
- Coverage claims show the ratio and the target behind them, never a bare "healthy."
- No fit claim in the monthly read without showing both signals, or a note that only one was available.
- Every false negative and false positive gets a deal-level call-out: the account, the amount, and what the disagreement means for action.
- A reconciliation block is mandatory when dashboard totals differ from the pulled totals. State the ground-truth figure first, then explain the difference.
- The baseline includes a trimmed alternative when one month had fewer than two opportunities.

## Output (example)
```
PIPELINE COVERAGE · this period
Channel     Created / Target   Coverage   Read
Inbound     $195K / $180K      1.1x       On pace, best-fit heavy
Outbound    $46K  / $90K       0.5x       Behind, activity is the gap
Product     $18K  / $25K       0.7x       Thin, expansion angle underused
Total                          2.4x       Adequate, outbound is the risk

WORK NEXT (top 3 of the New list)
  1. Acme Corp   Inbound   Fit: Excellent   Raised hand on pricing page
  2. Vertex      Outbound  Fit: Good        Hiring a sales team, strong signal
  3. Blend Labs  Product   Fit: Good        Using core features, expansion open

MONTHLY QUALITY · 1 flag worth the meeting
  False negative: Northwind. Your score Low, independent verdict Strong. $62K.
  You almost passed on a real fit. Re-open it.
```

## Where the numbers come from
The coverage bands (3x healthy, below 2x concerning), the Engaged window (14 days), the concentration cutoff (40% of the cohort by one rep), and the trailing baseline (3 months) are defaults, not laws. They suited a mid-market SaaS motion. If your cycle runs longer or your channels behave differently, re-tune them. The logic does not change. The thresholds are yours.

## Make it yours
Fork it. Change the modes, the lists, the fit score, the thresholds. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
