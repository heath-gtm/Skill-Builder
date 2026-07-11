# Closed-Lost Analysis

> Turn a graveyard of lost deals into a fix list. Reads your closed-lost deals, sorts the loss reasons into clean buckets (no decision, price, competitor, timing, fit), pulls the competitive intel, and separates the losses you could have prevented from the ones that were never yours. Each theme comes with the specific fix. Built for B2B revenue teams, customizable to your CRM and your sales process. Trigger on "why do we lose", "categorize our losses", "which losses were preventable", "who are we losing to", "what's our biggest loss reason", or any lost-deal post-mortem.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/closed-lost-analysis && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/closed-lost-analysis/SKILL.md -o ~/.claude/skills/closed-lost-analysis/SKILL.md && echo "Installed closed-lost-analysis. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/closed-lost-analysis/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Closed-Lost Analysis

## What this does
Reads your closed-lost deals and tells you why they died, in buckets you can act on: no decision, price, competitor, timing, or fit. It pulls the competitive intel out of the losses, then splits them into two piles that matter more than the total: the losses you could have prevented, and the ones that were structural and never yours to win. Each theme ends with the fix. The point is not to feel bad about the number. It is to stop losing the same deal twice.

## What you'll need
You do not need to connect anything to get value today. Bring your lost deals and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a list of your closed-lost deals, with segment or size, stage at loss, deal size, the loss reason (if captured), the competitor (if known), and any loss notes. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads all of the above automatically, across every lost deal in the window you pick, including the raw loss notes.
- Sharper with a meeting or transcript tool: reads what the buyer actually said before they went dark, so "no decision" gets a real cause.
- Sharper with a product-analytics tool: on lost trials, shows whether they ever reached first value, which separates a product gap from a sales gap.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a loss reason it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your lost-deal list (a CRM export, a closed-lost CSV). The skill runs the full analysis today on your real deals. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (raw loss notes, buyer objections, trial behavior). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| LOST filter | how you mark a loss | Stage = Closed Lost |
| WINDOW | the loss-date range to analyze | trailing 4 quarters |
| REASON field | your loss-reason picklist | Closed Lost Reason |
| NOTES field | free-text loss notes | loss description, next-step notes |
| COMPETITOR field | who you lost to | competitor on the deal |
| STAGE_AT_LOSS field | how far it got before dying | stage when marked lost |
| SEGMENT fields | how you group accounts | industry, employee count, region |
| MIN_SAMPLE | fewest losses before a theme counts | 5 (raise if you lose a lot) |

Run any loss taxonomy you like. The skill sorts your losses into your buckets and names the fix per bucket, so point it at your fields, not anyone else's.

## The method

### Loss categorization (clean buckets)
Sort every lost deal into one primary reason: NO_DECISION (they picked nothing, status quo won), PRICE (budget or value gap), COMPETITOR (they picked someone else), TIMING (real but not now), or FIT (never a match). When the reason field is blank, read the notes or the transcript to place it. Report the share and the lost deal size behind each bucket, so a common reason and an expensive reason are both visible.

### Competitive intel pull
For every COMPETITOR loss, pull who won and, where the notes say so, why. Roll it into a per-competitor view: how often they beat you, at what stage, in which segment, and the reason that keeps repeating. This is the sheet your reps wish they had before the next competitive deal.

### Preventable vs structural split
Split every loss into two piles. PREVENTABLE: the deal was winnable and something in the motion lost it (single-threaded, slow follow-up, wrong persona, weak business case, late competitor entry). STRUCTURAL: it was never yours (no budget, no real need, wrong segment, a feature you do not build). This split matters more than the raw count, because only one pile is yours to fix.

### The fix per theme
Every theme ends with a specific, do-this-next fix, not a platitude. NO_DECISION driven by no compelling event points to earlier qualification of the trigger. PRICE losses that cluster at one tier point to packaging. A competitor winning late points to multi-threading sooner. Name the change, not the feeling.

## Quality gates
- No theme reported below MIN_SAMPLE. A single bad-luck loss is not a trend.
- Every loss lands in exactly one primary bucket, so shares add up and nothing is double-counted.
- Preventable is only claimed with a reason from a field, a note, or a transcript, never a hunch.
- Competitive claims name the source. No invented win reasons for the other side.

## Output (example)
```
CLOSED-LOST ANALYSIS · 41 losses, trailing 4 quarters

Loss reasons
Bucket         Share   Lost $     Note
No decision    37%     $520K      Status quo, no compelling event
Competitor     27%     $410K      Lost late, after Solution Validation
Price          20%     $300K      Clustered at the mid tier
Timing         10%     $140K      Real, revisit next cycle
Fit            6%      $70K       Wrong segment, disqualify earlier

Preventable vs structural
  Preventable: 54%  (no-decision + late competitor losses)
  Structural:  46%  (timing, fit, no-budget)

Who we lose to
Competitor     Losses   Wins late?   Segment
Rival A        8        Yes, 6 of 8  mid-market
Rival B        3        No           enterprise

Fixes:
  1. No decision. Qualify the compelling event before Stage 3, or park it.
  2. Rival A. Multi-thread by Stage 2. They win by out-flanking a single champion.
  3. Price at the mid tier. Revisit packaging, not discounting.
```

## Where the numbers come from
MIN_SAMPLE (5) and the trailing-4-quarter window are defaults, not laws. They suited a mid-market SaaS cycle with steady loss volume. If you lose a small number of large deals, widen the window so the buckets are not built on three data points. The preventable-vs-structural split is always grounded in your own notes and fields, so the fix list is yours, not a benchmark's.

## Make it yours
Fork it. Change the buckets, the split rules, the sample floor. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
