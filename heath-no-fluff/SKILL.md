---
name: heath-no-fluff
description: Cut any document to its essential core, HUMANIZE THE NUMBERS, restructure verdict-first as a 5-minute read, and rewrite in Heath's voice. The core move: a number alone is data; a number attached to a behavior is a story. Round to human scale in narrative ("~70%", "1 in 2", "2 of every 3"), turn rates into frequencies and weekly targets into daily rituals ("fewer than 2 booked meetings a day"), keep exact figures one click away in the evidence layer so QA precision survives. Fire whenever Heath says "this is too long", "cut this down", "humanize the numbers", "too much to read", "explain it like I'm 5", "make this land", "tighten this up", "remove the fluff", or pastes a document/data block for a cleaner version. Also fire proactively on any reader-facing doc whose summary contains a naked statistic, a buried verdict, or prose-buried lists.

license: MIT
compatibility: cowork claude-code
---

# heath-no-fluff

Cut documents to their essential core, restructure verdict-first, rewrite in Heath's voice. Think of it as aggressive editing — not summarizing — where every sentence earns its place.

## Humanizing numbers — the core move

**A number alone is data; a number attached to a behavior is a story.** "Inbound holds 68% of closed volume" makes the reader do math. "Almost everything we close comes through inbound (~70%) — and we pay for it by burning 5–7 meetings per qualified deal" makes the reader wince. Every rewrite applies these five rules to every figure in the narrative layer:

1. **Round to human scale.** ~70%, not 68.3%. "About half," not 47.2%. The exact figure lives one click away in the evidence block — the narrative rounds, the QA trail stays precise. (This precision split is what keeps "humanized" from becoming "approximate.")
2. **No naked numbers.** Every figure rides with the behavior that produces it or the consequence it causes. If a number appears without a verb consequence, attach one or demote the number to the evidence layer.
3. **Rates become frequencies.** 47.2% → "about 1 in 2." 64% → "2 of every 3." 24.2% → "1 in 4." People feel frequencies; they compute percentages.
4. **Weekly abstractions become daily rituals.** 8.8 booked/week → "fewer than 2 booked meetings a day." 5.1 sourced/week → "1 sourced meeting a day." A ritual is adoptable; a weekly quota is negotiable.
5. **One number per sentence** (a before/after pair counts as one). Two parentheticals in a sentence = two supporting-data points pretending to be story.

Worked example — before: "Inbound holds 68% of closed volume and ~78% of won dollars. Target SQO blend: Inbound 45 / Product 40 / Outbound 15."
After: "~7 of every 10 closed deals — and nearly 8 of every 10 won dollars — ride on one channel. Spread it: half inbound, 40% product, 15% outbound. *Why this blend →*"

## What fluffy looks like

Nine patterns that bloat documents. Learn to spot them on sight:

**1. Context bombing** — Paragraph 1 explains why we're doing this at all. The reader already knows. Cut it.

**2. Methodology exposition** — "We pulled data from three sources and cross-referenced..." Nobody asked how. Lead with what you found.

**3. Buried verdict** — The conclusion appears in paragraph 5. Move it to sentence 1.

**4. Symmetric coverage** — Three items get equal paragraph treatment even though Item 1 is 10× more important. Weight coverage to importance.

**5. Over-qualified claims** — "It's possible that, in some cases, there may be an opportunity to consider..." Pick a lane: either it's true or it isn't.

**6. Show-your-work tables** — A 6-column table where only 2 columns matter. Either drop the table or trim to the load-bearing columns.

**7. Same point three ways** — State the finding once, with the number. Don't restate it in the chart title and again in the paragraph below.

**8. Boilerplate transitions** — "Building on the above," "It's worth noting that," "As we look ahead to," "In conclusion." Delete all of them.

**9. Prose-buried lists** — A sentence enumerating 3+ parallel actions, criteria, or items, glued together with commas and "and". The reader can't scan it, can't reference item 3, can't check items off. Break it into a numbered or bulleted list. (See "Formatting pass" below for the worked example.)

**10. Administrative metadata** — Sections like "Data sources," "Build sequence," "Brand guidelines," "Appendix A: methodology" that are relevant to the author but not the intended reader. When the audience is leadership, cut these entirely or move to a literal appendix. Do not just compress them — remove them.

## Five-pass compression protocol

Work in sequence. Don't skip passes.

**Pass 1 — Find the verdict.** What is the single most important thing this document says? Write it as one plain sentence. If you can't, the document doesn't know either — that's your first cut signal.

**Pass 2 — Find the evidence.** What are the 2–4 facts that prove the verdict? These are keepers. Everything else is scaffolding.

**Pass 3 — Rebuild the structure.** Verdict first. Evidence second. Context (if any) last. If the document has a methodology section longer than the findings, invert it.

**Pass 4 — Sentence-level cuts.** Remove every sentence that doesn't add new information. For each sentence, ask: "Does this change what the reader knows or does?" If no, delete it.

**Pass 5 — Voice pass.** Apply Heath's voice rules (below). The document should read like it was written by someone who knows the answer, not someone building a case.

**Pass 6 — Formatting pass.** Scan every paragraph for prose-buried lists: 3+ parallel actions, steps, criteria, or named items chained inside one sentence. Pull them out into a numbered list (use bullets only when order truly doesn't matter). Keep the framing sentence before the list and the consequence/payoff sentence after it as prose.

Worked example — before:

> Tracking is necessary, but it is the enabler, not the crux. The crux is behavior and focus: keep the Stage 0→1 gate hard, refuse low-quality noise from channels that haven't earned a meeting, narrow the focus, diversify the pipeline beyond inbound, and force a clean qualify-in / qualify-out decision on every deal. Those moves can start Monday.

After:

> Tracking is necessary, but it is the enabler, not the crux. The crux is behavior and focus:
>
> 1. Keep the Stage 0→1 gate hard
> 2. Refuse low-quality noise from channels that haven't earned a meeting
> 3. Narrow the focus
> 4. Diversify the pipeline beyond inbound
> 5. Force a clean qualify-in / qualify-out decision on every deal
>
> Those moves can start Monday.

Boundary rule: this converts *enumerating sentences* into lists. It does NOT convert narrative paragraphs into bullets — that anti-pattern still holds. The test: if the clauses are parallel and independently actionable/checkable, list them; if they build an argument, leave them as prose. In HTML output, emit a real `<ol>`/`<ul>`, not line breaks.

## Heath's voice rules (baked in — do not delegate to humanizer)

Apply these on Pass 5 without exception:

**Tone and structure:**
- Self-implicating first: if something failed, say "we built the wrong thing" not "the data showed underperformance"
- Failure-derived: insights that cost something to learn are more valuable than generic best practices
- Plain declaratives over bumper-sticker aphorisms: "Templates drove 3× conversion" not "Templates are a game-changer"
- Specific numbers always beat vague magnitude: "42%" not "a significant portion"
- No bow-tied endings: don't wrap up with "Overall, this demonstrates..." — end on the last real point

**Kill list — delete these on sight:**
- Em dashes (—) used for dramatic effect: rewrite as two sentences
- "Delve," "leverage" (as verb), "impactful," "seamlessly," "robust," "transformative," "actionable insights"
- "It's worth noting that," "importantly," "notably," "it should be emphasized"
- "In conclusion," "to summarize," "in summary," "as we look ahead"
- "This analysis reveals," "the data shows," "our research indicates"
- Rule of three lists where only two items matter
- Sycophantic openers: "Great question," "Absolutely," "Certainly"
- Hyphenated compound adjectives used as filler: "data-driven," "best-in-class," "cutting-edge"

## Output contract

Always produce three things:

1. **Compressed document** — the full rewritten output, ready to use
2. **Cut list** — a brief log of what was removed and why (one line per major cut, not per sentence)
3. **Word count delta** — `Original: N words → Compressed: M words (X% reduction)`

Format the cut list as:
```
CUTS:
- [Section/pattern] → [what you did]: [one-line reason]
```

Example:
```
CUTS:
- "Background" section → deleted: audience already knows the context
- Methodology paragraph → deleted: findings speak for themselves
- 6-column table → trimmed to 3 columns: only channel, WAU, and trend were load-bearing
- 3 "it's worth noting" phrases → deleted: boilerplate
- Conclusion paragraph → deleted: verdict was already in para 1
```

## Target compression

| Document type | Target |
|---|---|
| Narrative report / analysis | 40–55% of original |
| Executive brief / leadership update | 35–50% of original |
| Technical spec / scoring methodology | 50–65% prose reduction (preserve data tables and threshold values) |
| Email / Slack message | 30–50% of original |
| LinkedIn draft | 40–60% of original |

**Important on specs:** Preserve the DATA (weights, thresholds, formulas, event names). Cut the PROSE scaffolding around it aggressively. A spec can lose 50% of its words while keeping 100% of its information.

## HTML report mode

If the input is an HTML report and the request is to compress it, compress the *prose content* — do not restructure the HTML layout. Output the compressed prose inline (not as a new HTML file) unless explicitly asked for HTML output.

## Worked example

**Input (259 words):**
> This document provides an overview of the key findings from our recent analysis of the product surfaces in use by our GTM team. The purpose of this analysis was to understand which surfaces are being actively used, which are underperforming, and where there may be opportunities to improve adoption across the team.
>
> We looked at usage data across three primary surfaces: the inbox, the sidebar, and the compose window. The data was pulled from Amplitude over a 90-day period and cross-referenced with our internal tracking systems to ensure accuracy.
>
> What we found is quite interesting. The inbox is by far the most used surface, with approximately 73% of all interactions happening there. The sidebar, while available, is seeing much lower engagement — around 12% of users interact with it on a weekly basis. The compose window falls somewhere in between, at roughly 34% weekly engagement.
>
> Based on these findings, it seems clear that inbox-centric design should remain our primary focus going forward. The sidebar may benefit from additional onboarding or discoverability improvements, and the compose window presents a mixed picture that warrants further investigation.

**Output (87 words, 66% reduction):**
> Inbox-centric is no longer our headline — it's confirmed. 73% of all interactions happen in the inbox. Compose is at 34% weekly engagement. Sidebar at 12%.
>
> The sidebar is underperforming enough to warrant a discoverability fix, not just more onboarding. Compose needs more investigation before we draw conclusions.
>
> One design principle follows from this: inbox-first, everything else secondary until sidebar numbers move.

**Cut list:**
```
CUTS:
- "Purpose" paragraph → deleted: setup the reader already has
- Methodology paragraph → deleted: 90-day Amplitude pull is standard
- "quite interesting" + restatement → deleted: just gave the numbers
- Hedged closing → rewritten as a concrete design principle
```

## The 5-minute-read structure (progressive disclosure)

Every multi-page report or decision document leads with a block a reader can finish in 5 minutes and act on. Structure, in order:

1. **The story as an arc, ≤3 short lines:** *Where we are → Where we need to be → How to get there.* One plain sentence per leg, the single most causal number in leg one (e.g. "AEs burn 5–7 meetings per inbound SQO, which eats the capacity for product and outbound"). If a sentence needs two parentheticals, it is two supporting-data points pretending to be story.
2. **The numbered do-this list.** The actions, each one line, hardest-hitting number inline.
3. **Deeper reads.** A short link list — companion pages, appendix, verification trail — each with a one-phrase reason to click ("why touchpoints are the gap", "every won deal, linked").

Everything below that block is evidence, not argument. The argument is complete in the 5-minute block; sections exist for the reader who wants to audit it. Tests:

- Can someone who reads ONLY the top block make the decision? If no, the block is missing a sentence — not the reader missing a section.
- Does any section below introduce a NEW conclusion? If yes, hoist it into the story; sections defend, they don't reveal.
- Is every deep-dive one click away with a stated reason to click? Bare links are dead links.

Companion documents follow the same rule recursively: each leads with its own verdict block and links back. The set forms a hub: 5 minutes on the main page, every detail reachable in one click.

## Action data vs supporting data — the highlight rule

All data is good data; **only the right data creates action.** Every document divides its numbers into two classes and treats them differently:

- **Action data** — the numbers that change what the reader does Monday (the gate standard, the meetings target, the trigger that tripped). These go in the top block, in bold, attached to a verb.
- **Supporting data** — everything that defends the action data (cohort tables, method notes, reconciliations). These go behind toggles, in collapsed sub-sections, or in linked appendices. Never deleted — demoted.

Test: if a number appears above the fold but no action changes when it changes, it is supporting data wearing action data's clothes. Demote it.

## Section anatomy — summary first, evidence behind toggles

A section a reader must scroll to understand is a failed section. Every long section follows this anatomy:

1. **One-line sub** + a 2–3 sentence "what this section is" paragraph.
2. **The actions/conclusions** — visible, never collapsed.
3. **Evidence in collapsed sub-blocks** (`<details>` in HTML), each with a one-line summary carrying the key numbers — readable without expanding.

Hero/directive blocks carry the verdict only: one bold number per item and a "See the math →" link to the evidence block — never the proof table itself. Duplicating the table in the hero is the same point twice (pattern #7).

## ELI5 the math, backlink the data, cut the author's notes

Three rules that came out of live presentation reviews:

**1. ELI5 before arithmetic.** Every model or formula gets one plain-language sentence explaining the mechanism BEFORE any table — written so a reader with zero context follows it ("a rep has fixed hours, so the only decisions are which doors to knock on and how good we are inside; meetings are the bill, not the goal"). Then show the table. A model whose intro needs the table to be understood is backwards.

**2. Every referenced number links to its source.** Any statistic, model output, or claim that lives in another section or page gets an anchor link to it at the point of mention ("47.2% SQO→win" → the funnel block; "45/40/15" → the blend justification). If a number can't be backlinked to a source block, it doesn't belong in the summary. This is also how stale numbers get caught — an unlinked number is an unaudited number.

**3. Cut the author's teaching notes.** Framings that taught the ANALYST something during the work ("treat X as time management, not allocation") do not belong in reader-facing actions — the reader needs the conclusion, not the analyst's correction history. If it shaped the model, it lives in the model's justification block; it is never an action item.

And one structural rule from the same review: **never present a target blend, ratio, or standard without its justification one link away** — "why this blend →" is mandatory next to any prescribed number.

## Anti-patterns

Do not do these:

- **Don't summarize into bullet points** unless the original was bullets. Preserve the document's form — compress its words. (Exception: Pass 6 — sentences that *enumerate* 3+ parallel items become lists; narrative stays prose.)
- **Don't lose the numbers.** If the original says "42%," the compressed version must say "42%." Vague compression is worse than no compression.
- **Don't invent.** If the verdict isn't explicitly stated, find the strongest implicit one and flag it: "Reading the verdict as: [X]. If that's wrong, correct me."
- **Don't compress tables of data.** Threshold tables, weight matrices, event registries — these are already compressed. Leave them. Cut the prose around them.
- **Don't add new structure.** Don't introduce headers that weren't in the original just because they'd organize your output better. Restructure what exists; don't redesign.
