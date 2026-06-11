---
name: strategic-plan-structure
description: The mandatory structure for any leadership-facing strategic plan. Two bets max. Named team. Reads without scrolling. Use whenever the user asks for "a plan," "a 90-day plan," "a strategic plan," "a board update with a plan," "a leadership doc," "what we're going to do about X" — or anything that will be presented to a CEO, board, or exec team as "here's the plan." Trigger on "write the plan," "structure my plan," "tighten my plan," "the CEO wants the plan," or any leadership-strategy document where the test is "does the reader understand the plan in 30 seconds." Also fire as the mandatory structure for any pasted strategic doc being tightened by /heath-no-fluff or /heath-voice-humanizer.

license: MIT
compatibility: cowork claude-code
---

# strategic-plan-structure

The forcing function for leadership-facing strategic plans. Locked 2026-06-09 after CEO feedback to Heath: "I bring thrash to the room. My reports are so in-depth, people feel like I don't actually have a plan because I am just throwing so much at them. Solve 1–2 problems first, then optimize."

## The test

A leadership-facing strategic plan passes if it answers, in 30 seconds of reading:

1. **What are we committing to?** (the number)
2. **What's the plan?** (two bets)
3. **Who's doing what?** (named team)
4. **What does winning look like?** (Day-90 evidence)

If the reader has to scroll to find the plan, the plan failed. If the reader can't tell who owns each bet, the plan failed. If there are more than 2–3 bets, **the plan is thrash** — not a plan.

## The 30-second test in practice

Open the document. Set a 30-second timer. After 30 seconds, ask:
- Can I name the commit number?
- Can I name the two bets?
- Can I name the people who own each bet?

If any answer is "no," the doc is too deep, too wide, or buried. Cut.

## The mandatory structure

Every leadership strategic plan follows this exact order. Do not add sections. Do not reorder. Do not add an "executive summary" that just precedes the plan — the plan IS the executive summary.

### 1. Page hero (above the fold)

One line. The strategic motion. Examples:
- "Find it. Convert it. Grow it."
- "Save the renewals. Grow the book."
- "Ship one product. Land 30 customers."

### 2. Commit banner (above the fold, not a section, not collapsible)

One banner row containing:
- **The headline target** (H2 / annual / whatever the period is) with the binary verdict ("exceed or miss")
- **The 90-day commit** (or whatever the planning period is) — usually two numbers (e.g., $700K pipeline / $350K bookings)
- **The verdict line** — what failure looks like

This is NOT a numbered section. It's a banner. It sits at the top so the reader sees the commit before anything else.

### 3. The plan sentence (one paragraph, two lines max)

Literally one sentence that says: **"The plan is N bets. Each one has [problem / bet / moves / team / wins]."**

Followed by a second line that says: "Everything else is in service of the N. If a play is not feeding one of these bets, the play is wrong."

This sentence does the work of a 30-page strategy doc. It says: *we focused, we picked, we resisted the urge to do everything.*

### 4. The bets (2 max, 3 absolute ceiling)

**Hard rule: maximum 2 bets, 3 absolute ceiling.** The CEO's exact feedback was "solve 1–2 problems first, then optimize." If you have 4 bets, the plan is reactive — you're trying to solve everything because you can't decide which thing matters most.

Each bet is one card. Same template every time:

- **Bet header** — Bet number + name (e.g., "Bet 1 · Build the Pipeline Engine")
- **The problem** — the specific pain this bet solves. With numbers. No more than 2 sentences. Red accent.
- **The bet** — the call itself. One sentence. The strategic intent.
- **The 2 moves** — exactly 2 moves per bet. More than 2 means the bet is actually a portfolio. Each move has: a verb-led headline, an owner name, a measure with a date.
- **The team** — every role that contributes to THIS bet, in 1–2 lines. Names not titles.
- **Won at Day 90** — 3–5 bullets. The evidence that says "we won this bet."

If a bet doesn't fit on one card without scrolling inside the card, it's two bets pretending to be one. Split it or cut it.

### 5. How we execute (the team section)

The CEO feedback emphasized this: **"lean into the team to make it happen."** A strategic plan that doesn't name the team is one person trying to do everything.

This section has:
- A short lede ("Two bets. One team.")
- A grid of named roles, one row each. Each row says: **role name → what they own in each bet**.
- A rhythm line at the bottom: weekly cadence in one sentence. Detailed ownership lives in Notion (or wherever the user runs RACI).

Format names BIG (they're the load-bearing piece). Format ownership descriptions short.

### 6. The closing (standalone, not numbered, not collapsible)

The closing is the last thing the reader sees. It is:
- A pill-tagged closing block ("THE CLOSING")
- A bold three-line statement (e.g., "Same page. Own our parts. Get shit done.")
- The commit numbers restated with the verdict ("Exceed or miss")
- Signed off ("— Heath" or whoever)

This block is NOT collapsible. It's the closure. It bookends the commit banner at the top.

### 7. Receipts (one row, not a section)

A single row of links at the very bottom. Format:

```
Want the depth? · ⚙ Deep Dive — Speaking Points + Receipts →
Direct receipts · Pipeline Diagnosis · Multi-Channel Test · CSM Renewal Proactivity · ...
```

Not a section. Not collapsible. The Deep Dive link leads. Individual source-doc links follow.

## The Deep Dive companion (mandatory)

**Every strategic plan ships with a Deep Dive companion file.** Filename pattern: `<plan-filename>-deep-dive-<date>.html` next to the tight plan.

The Deep Dive is where ALL the depth lives:
- Speaking Points block at the top (see below)
- The full receipts: challenges, transformation tables, CORES deep-dives, KPI grids, all the plays, all the analysis
- Linked source documents inline

The tight plan is what the room sees. The Deep Dive is what the presenter uses during the conversation. Without the Deep Dive, the presenter is exposed when someone asks "wait, where did that number come from" — they can't reference depth they cut from the plan.

### Speaking Points block (mandatory inside the Deep Dive)

At the top of the Deep Dive, immediately after the binary banner, ship a **Speaking Points** block:

- Eyebrow pill: "SPEAKING POINTS"
- Headline: "If they ask — here's the data and the answer."
- Sub: "Use these during the conversation. Each card pairs a likely question with the answer + the load-bearing number behind it."

The block contains a grid of Q&A cards:
- **Q cards** — likely questions a leadership audience will ask, with the answer + the sourced data point + a "data" line citing the source
- **Objection cards** — likely pushback ("this is just 2 bets," "why isn't [team] central," "what about [alternative]") with the counter

A solid Speaking Points block has 8–12 cards. 60–70% Q cards, 30–40% Objection cards.

Card pattern:
```
Q · [question]
[Answer with strong tag on the load-bearing claim.] [Context sentence.]
data: [source doc] · [number]
```

This is what makes the difference between "I have a plan" and "I have a plan and I can defend every number live."

Both files share the same sticky header pattern:
- The tight plan links to the Deep Dive with a "⚙ Deep Dive" pill (amber accent)
- The Deep Dive links back to the tight plan with a "← The Plan" pill (green accent)
- Both link to the deck with "▶ Present"

The reader's mental model:
- "I want to know the plan" → open the tight plan
- "I want to defend the plan" → open the Deep Dive
- "I want to present the plan" → open the deck

## What MUST be cut

The reason most strategic plans fail the 30-second test is because they include reference material in the body. Move ALL of the following OUT of the strategic plan:

- **Diagnosis sections** ("the 11 challenges," "what's broken," "the state of the funnel") — these are receipts. Link to them.
- **Transformation tables** ("we are here / where we are going") — useful context but not the plan. Link to a separate doc if needed.
- **Bowtie diagrams, funnel SVGs, capability maps** — visual context. Belongs in receipts.
- **All CORES deep-dives** with KPI grids and play tiles — this is depth analysis. Belongs in a separate receipts doc.
- **Operating system / engine / infrastructure sections** — these are how the bets get executed; they live INSIDE each bet's "The team" or "Won at Day 90," not as their own sections.
- **AI-Native / funding / tooling sections** — same. These are how we resource the bets; they live inside the team section or in receipts.
- **Appendix with version history, ownership notes, what we're not doing** — keep version history in the file but at the very bottom of the source HTML, not in the rendered narrative. "What we're not doing" lives as a footnote in receipts.
- **Frameworks the reader doesn't need to learn** (Build/Fix/Enable, Leverage/Leaks/Motion, 5 Requirements, 3 P0 Foundations) — internal vocabulary. Use it once in the closing as a callback if at all; don't structure the doc around it.

## The thrash test

Before publishing, ask:

1. **Am I being reactive?** If the plan responds to >2 problems, it's reactive. Pick the two that matter most.
2. **Am I bringing thrash?** If a reader could come away with a different "main point" than I intended, the plan is too wide. Tighten the bets until the main point is unmissable.
3. **Did I name the team?** If the team section uses titles instead of names, fix it. Use real names.
4. **Can I read it without scrolling?** Open the doc. If the closing isn't visible on screen 2, cut more.

## Length targets

| Doc type | Target file size | Max screens |
|---|---|---|
| 90-day plan | 15–25KB HTML | 3 screens |
| Quarterly plan | 20–30KB HTML | 4 screens |
| Annual plan | 25–40KB HTML | 5 screens |
| Board update | 15–20KB HTML | 2 screens |

If the file is bigger, content was added that doesn't belong. The receipts are linked, not included.

## When NOT to use this skill

- Operational runbooks (those need depth)
- Methodology docs (those need depth)
- Analysis reports (those ARE the receipts)
- Post-mortems (different structure: timeline / what happened / what we learned)

This skill is for **strategic plans** — documents that say "here is what we are committing to and how we will execute." Not for documents that explain how things work or what we found.

## Anti-patterns

Things that look like a tight plan but aren't:

- **The "all the plays" doc dressed as a plan** — 8 plays organized into 3 themes is still 8 plays. Pick 2 bets and let the rest go to receipts.
- **The "every team has a section" doc** — Sales gets a section. CS gets a section. Marketing gets a section. RevOps gets a section. Each section has its own bets. That's 5 plans, not one. The team owns the SAME 2 bets together.
- **The "executive summary + full plan" doc** — if the exec summary is enough, the full plan is wasted text. If the full plan is necessary, the exec summary is window dressing. The plan IS the exec summary.
- **The "we'll figure out the team in Notion" doc** — naming the team is part of the plan. If you don't know who owns it, you don't have a plan; you have a strategy memo.
- **The "depth as proof of work" doc** — long ≠ rigorous. Brief ≠ shallow. The CEO doesn't reward depth; she rewards a clear bet on what matters.

## Worked example

See `mixmax-path-to-revenue-2026-05-31.html` v4.0 — built to this exact structure after the same CEO feedback this skill encodes. 19KB. Reads without scrolling. Two bets. Named team. The receipts link out.

## Reference

This skill was written 2026-06-09 after Heath's CEO gave the following feedback verbatim:

> "I bring thrash to the room. My reports are so in-depth, people feel like I don't actually have a plan because I am just throwing so much at them. Feels as though I am reactive right now and not driving GTM. Solve 1–2 problems first, then optimize. One thing I do want us to lean into more is the team to make it happen."

That feedback is the skill. If a strategic doc is being written and one of those four things is missing — focus, decisiveness, team, succinctness — the skill is doing its job.
