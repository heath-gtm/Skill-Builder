# Closed-Won Replication

> Turn your last N wins into a scored lookalike target list with a first-touch angle per account. Extracts the win profile from closed-won deals, behavioral and situational signals first, keeps only the traits that separate wins from losses, scores net-new accounts against the profile, and writes the shared-situation opener for each one. Built for B2B revenue teams, customizable to your CRM and enrichment stack. Trigger on "replicate my closed won", "build a win profile", "lookalike accounts from wins", "clone my best customers", "who looks like my last ten wins".

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/closed-won-replication && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/closed-won-replication/SKILL.md -o ~/.claude/skills/closed-won-replication/SKILL.md && echo "Installed closed-won-replication. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/closed-won-replication/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Closed-Won Replication

## What this does
Takes your last N closed-won deals and turns them into a win profile, then into a scored list of net-new accounts that match it, each with a first-touch angle you can send this week. Where closed-won-analysis is the retro that tells you why you won, this skill consumes that read and produces the forward artifact: the scored lookalike list and the per-account opener. The profile is not just firmographics. It is what was true at the account before the deal started: what they were hiring for, what tool they were replacing, what changed. Those are the signals a rep can actually act on.

## What you'll need
You do not need to connect anything to get value today. Bring your wins and losses and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: your last 10 to 20 closed-won deals and a comparable closed-lost set, exported from your CRM. Include industry, size, deal size, source, the incumbent tool if you have it, and any notes on what was happening at the account. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads wins and losses automatically and pulls the fields you forgot to export.
- Sharper with an enrichment tool (Clay, Common Room): sources the lookalike candidates and fills the behavioral signals, hiring, stack, recent changes.
- Sharper with product analytics if you are PLG: adds pre-sale usage as a profile signal, which is often the strongest one you have.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a signal it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your won and lost exports. The skill builds the profile, scores any account list you give it, and drafts the angles today. No connection required.
- **Connect your tools**: the same skill pulls wins and losses from the CRM, sources lookalike candidates through your enrichment tool, and scores them automatically. Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org sourcing outbound from a win profile. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| N_WINS | how many wins to profile | last 15 (10 to 20 works) |
| LOSS_SET | the losses to contrast against | closed-lost, same window, same segment |
| LOOKALIKE_SOURCE | where candidate accounts come from | Clay table, Common Room, a list you paste |
| SCORE_THRESHOLD | minimum score to make the list | 70 of 100 (re-tune to your volume) |

The loss set is not optional. Without it you cannot tell a win signal from a coincidence, and the profile becomes a description of your market, not your winners.

## The method

### Win-profile extraction (behavior first)
Read every win and pull two layers. The firmographic shape: segment, size, industry, region. Then the layer that matters more: the behavioral and situational signals present before the deal started. What roles were they hiring for. What tool were they replacing. What changed at the account, a new leader, a funding round, a stack migration. When we backtested our scoring model against real won and lost deals, the strongest single predictor of a win was a behavioral signal at 3.56x lift; the firmographic fit score everyone trusted came in at 1.13x. The profile weighs behavior over firmographics because the data votes that way.

### Signal vs coincidence (wins against losses)
A trait counts only if it appears in wins meaningfully more than in losses. "Most of our wins are mid-market" is noise if most of your losses are too. Run every candidate trait through the contrast: share of wins that show it, share of losses that show it, and the ratio. Keep the traits that separate. Drop the rest, even the ones the team believes in.

### Lookalike list build (source and score)
Source candidate accounts that match the profile from LOOKALIKE_SOURCE, excluding current customers and open pipeline. Score each one against the profile, weighting the traits by how strongly they separated wins from losses. Every score shows its inputs: which traits the account hit, which it missed, and where each read came from. Accounts above SCORE_THRESHOLD make the list.

### First-touch angle (the shared situation)
For each account on the list, write one opener built on the shared situation, not the shared logo. The shape is "companies that looked exactly like you chose us when X", where X is the situational signal the account matches: the hire, the replaced tool, the change. Never name a customer without written permission. The angle works because the situation is recognizable, not because the name is impressive.

## Quality gates
- A profile trait counts only if it separates wins from losses, not wins from thin air. Show the contrast for every trait that makes the profile.
- Every lookalike score shows its inputs: the traits hit, the traits missed, the source of each read. A bare number is not a score.
- Never name a customer in outreach without written permission. The default angle is the anonymous shared situation.
- No angle drafted from a signal the skill cannot source. A guessed situation is worse than a generic opener.

## Output (example)
```
WIN PROFILE · built from 15 wins vs 18 losses (sample data)

Trait                          In wins   In losses   Keep?
Hiring RevOps or SalesOps      67%       22%         YES (3.0x)
Replacing spreadsheet/DIY      53%       17%         YES (3.1x)
New sales leader < 6 months    40%       11%         YES (3.6x)
Mid-market, 100-500 staff      73%       61%         NO (1.2x, noise)

LOOKALIKE LIST · 3 of 41 candidates above threshold 70
Account     Score   Traits hit                      First-touch angle
Northwind   88      RevOps hire, DIY stack, new VP  New sales leader + spreadsheet ops
Vertex      79      RevOps hire, DIY stack          Hiring RevOps onto a manual stack
Acme        74      New VP, DIY stack               New leader inheriting DIY tooling

Next move:
  1. Northwind first. It hits all three separating traits.
  2. The angle for all three: "companies that looked exactly like
     you chose us when the new leader hit the spreadsheet wall."
```

## Example chat
Here is the skill running on a real export.

**You:** Here are my last 14 wins and 16 losses from Salesforce. Build the profile and tell me who to go after. [uploads CSVs]

**Claude:** Profile's built, and one trait your team trusts did not survive the contrast.
```
Trait                        In wins   In losses   Keep?
Replacing a legacy tool      57%       19%         YES (3.0x)
Hiring for ops roles         50%       13%         YES (3.8x)
Series B-D funded            71%       63%         NO (1.1x)
```
Funding stage is in nearly all your wins, and nearly all your losses. It describes your market, not your winners. The traits that separate are behavioral: the legacy replacement and the ops hire. Give me a candidate list, or connect Clay, and I'll score against these two plus the rest of the kept traits.

**You:** Score this list of 30 accounts from our Clay table.

**Claude:** Scored all 30, four clear the 70 threshold.
```
Account     Score   Traits hit                    Missing
Northwind   84      legacy tool, ops hire         no recent change signal
Vertex      76      ops hire, recent re-org       incumbent unknown
```
Northwind's angle writes itself: they posted a RevOps role last month and run the same legacy tool three of your wins replaced. The opener is the situation, "teams that looked exactly like you moved off that tool when the ops hire landed," no customer names unless you have written permission. One sharpener: add the incumbent-tool field to your Clay table, it is the thinnest read on this list.

## Go further
The list is step one. Here is where an operator takes it once the manual version proves out.

- **Refresh the list on a schedule.** Point a scheduled Claude task at Salesforce and your enrichment tool weekly, rebuild the profile as new wins close, and rescore the candidate pool so the list never goes stale.
- **Automate the sourcing.** Feed the kept traits into Clay, or run Ocean.io-style lookalike sourcing through your enrichment tool, so candidates arrive pre-matched to the profile instead of hand-picked.
- **Add the community layer.** Connect Common Room so the behavioral signals include who is showing up in your community and content before the deal exists, often the earliest separating trait you have.
- **Write the score back.** Push each account's score and traits-hit into a CRM field so reps see the why in the record, not in a doc they never open.

The profile decays as your product and market move. Rebuild it every quarter or it becomes last year's playbook.

## Make it yours
Fork it. Change the traits, the threshold, the source. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
