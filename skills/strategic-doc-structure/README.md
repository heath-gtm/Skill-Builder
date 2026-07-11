# Strategic Doc Structure

> A forcing function for any leadership-facing strategic document. STEP 0 triages the doc type (Strategic Plan, Deep Dive, Deck, Methodology, Analysis Report, Playbook, Brief) and routes to the right template. Universal rules apply to all types: verdict first, departments not individual names, a vocabulary lock (action words not process words), motion verbs (finalize / attack / stop / ship / launch / re-engage / coach / close), and a closing the reader can reach fast. Strategic plans use 2 bets and 5-block bet cards. Trigger on "write the plan", "structure this doc", "audit this report", "tighten this analysis", "review this playbook", "is this thrash", "where should I put this".

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/strategic-doc-structure && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/strategic-doc-structure/SKILL.md -o ~/.claude/skills/strategic-doc-structure/SKILL.md && echo "Installed strategic-doc-structure. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/strategic-doc-structure/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Strategic Doc Structure

A forcing function for any leadership-facing strategic document. It stops one failure mode: a document so deep and wide the reader cannot tell what you are committing to. The fix is always the same. Pick what matters most, say it first, name who owns it, push the depth to a companion.

## What this does
Takes a strategic document and makes it land. Tells you what kind of doc you are writing, what the reader's one question is, and the structure that answers it fast. For strategic plans it enforces the hardest discipline: a maximum of two bets, a five-block bet card, named owners, and a closing the reader reaches in seconds. The output survives a 30-second skim and a five-minute read.

## What you'll need
Two things, no connectors. A draft, outline, or rough brain-dump. And a sense of who reads it and what decision or action it should produce.

## Customize this for yourself
| Slot | What it is | Make it yours |
|---|---|---|
| Your doc types | The kinds of leadership docs you ship | Add or rename to match what your team writes (QBR, board memo, launch plan). Keep the reader-question column. |
| Your vocabulary lock | The words you ban and the words you require | Ban process-words ("work streams," "tracks," "pillars"). Require motion verbs. Set your own lists. |
| Your audience | Who the doc names and how | Departments, never individuals, by default. Use your org's labels. |

## The method

### STEP 0, triage the document type
| Type | Reader's question | Template |
|---|---|---|
| Strategic Plan | "What are we committing to?" | 2 bets, 30-second read |
| Deep Dive | "Where is the depth behind the plan?" | Speaking points, receipts |
| Deck | "What does this look like presented?" | 7 to 8 slides, no new info |
| Methodology | "How does this model work?" | Trust contract + worked example |
| Analysis Report | "What did we find?" | Verdict + 3 findings + actions |
| Playbook | "What should I do tomorrow?" | Findings paired with actions |
| Brief | "Give me the 60-second take" | Verdict + 3-bullet why + named move |

If unsure, default to Analysis. Never force the Strategic Plan template onto a methodology or analysis.

### Universal rules, every doc type
1. Verdict first. The conclusion before the evidence.
2. Vocabulary lock. Motion verbs (finalize / attack / stop / ship / launch / re-engage / coach / close). Never "work streams," "build," or "optimize" in headlines.
3. Departments, not individual names, in the body.
4. Plain voice. Humanize numbers. No filler.
5. The closing is reachable. Short docs show it in the first screens; long docs show a table of contents early.

### Strategic Plan template
The test: in 30 seconds the reader answers what we are committing to (the number), what is the plan (two bets), who is doing what (named team), what winning looks like (the evidence at period end).

Structure (do not reorder): a one-line page hero (the strategic motion); a commit banner (target + binary verdict + what failure looks like); the plan sentence ("The plan is two bets..."); the bets (2 max, 3 ceiling), each a 5-block card:
- Bet header (number + name).
- The problem (specific, numbers, two sentences max).
- The bet (the call, one sentence).
- The 2 moves (exactly 2; verb-led headline + department owner + one line each).
- What we are going after (the GO list, 4 outcome-led bullets max, each opening with a motion verb and naming a campaign/cohort with sizes).
- What winning looks like (a one-line verdict + 3 to 5 measurable bullets).

Then: How we execute (departments grid + a one-sentence cadence line); the closing (standalone, restates the commit); receipts (one row of links).

Cut from the body and link instead: diagnosis sections, transformation tables, diagrams, deep-dive metric grids, operating-system sections, resourcing, appendices, already-shipped proof. The plan reads as a plan; the companion shows the data.

### The other templates
Deep Dive equips the presenter (speaking-point Q&A cards + "what is in field this week" + numbered depth). Deck mirrors the plan in 7 to 8 slides with no new info. Methodology answers four reader questions with a worked example. Analysis is verdict + exactly 3 stacked findings + one conclusion + 3 to 5 actions. Playbook pairs each finding with the action it produces plus a peer comparison. Brief is one screen: color-coded verdict + 3-bullet why + one named move.

## Output (example)
```
Bet 1 - Build the Pipeline Engine

THE PROBLEM
Sales created only a third of its own pipeline last quarter. When inbound
dipped, the quarter dipped with it.

THE BET
Sales owns pipeline creation. We stop waiting for leads and build our own.

THE 2 MOVES
1. Stand up the outbound motion     Owner: Sales
2. Fix the routing                  Owner: Revenue Operations

WHAT WE ARE GOING AFTER
- Attack the priority cohorts: Tier 1 named accounts (130), re-engage cold (800)
- Launch the weekly outbound cadence across the team
- Stop chasing unqualified inbound; route it to nurture
- Ship the new routing rules to production

WHAT WINNING LOOKS LIKE
"A sales org that creates its own pipeline."
- Sales-sourced pipeline at 50%+ of total
- Qualified-to-meeting conversion at 18%+
- Time-to-first-touch under 24 hours
```
No individual names, no tool versions, no charts, no third move. Everything deeper lives in the companion.

## Make it yours
Change the doc types to what your team ships. Set your own vocabulary lock. Decide whether your culture names departments or individuals. Keep the spine: triage the type first, lead with the verdict, name the owner, cap the bets, push depth to a companion. Built by an operator. Customize it, break it, make it better.
