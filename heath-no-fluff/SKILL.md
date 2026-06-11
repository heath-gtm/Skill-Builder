---
name: heath-no-fluff
description: Cut any document to its essential core, HUMANIZE THE NUMBERS, restructure verdict-first as a 5-minute read, and rewrite in Heath's voice. A number alone is data; a number attached to a behavior is a story — round to human scale ("~70%", "1 in 2"), turn rates into daily rituals, keep exact figures in the evidence layer. Fire on "this is too long", "cut this down", "humanize the numbers", "explain it like I'm 5", "make this land", "remove the fluff", "say more with less", or any pasted doc needing a cleaner version. ALSO handles EXPLAINER MODE for docs that explain how something works (a score, model, system, process): restructure around the reader's four questions (what is it / where's the data / how does it add up / what do I do with it), add a trust contract and one worked example, close with an execution bridge — fire on "make this digestible", "rep-facing", "explain how this works". Also fire proactively on any reader-facing doc with a naked statistic, a buried verdict, or prose-buried lists.

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

**Pass 10 — Thrash filter (for leadership-facing strategic plans).** Locked 2026-06-09 after CEO feedback to Heath: "I bring thrash to the room. My reports are so in-depth, people feel like I don't actually have a plan. Solve 1–2 problems first, then optimize." Refined 2026-06-11 (departments-not-names + index registration). If the document is a strategic plan (90-day plan, quarterly plan, leadership brief, board update), apply these five hard cuts:

1. **The 1–2 problem rule.** If the plan responds to more than 2 problems, the plan is reactive. Pick the 1–2 problems whose math actually moves the headline number; let the rest go to receipts. If you cannot cut to 1–2, the user has not picked yet — flag this explicitly: "This reads as 4 priorities. The CEO's feedback was solve 1–2 first. Which two?"

2. **The 30-second test.** After the cut, a reader should be able to answer four questions in 30 seconds: *what are we committing to* (the number), *what's the plan* (the bets), *who's doing what* (the team), *what does winning look like* (Day-90 evidence). If any answer is buried, surface it. If any is missing, demand it from the user.

3. **Show the team, by DEPARTMENT — never by individual name.** Use "Sales," "Customer Success," "Revenue Operations," "Sales Operations," "Marketing," "Revenue Leadership" — not "Gabrielle," "Heath," "Lana." Individual names belong in Notion (RACI), not in leadership-facing plans. Locked Heath preference 2026-06-09. If the draft uses individual names in the body, swap them all to department labels before shipping.

4. **Strategic plan = tight + Deep Dive.** A strategic plan ships in two files: the tight plan (15–25KB, 2 bets max, reads without scrolling) AND a Deep Dive companion (full receipts + Speaking Points block for the presenter to defend the plan live). The tight plan is for the room; the Deep Dive is for the conversation. See [[strategic-plan-structure]] for the full pattern.

5. **Register the doc in the index manifest.** Every HTML doc pushed to a GitHub Pages reporting repo must be added to that repo's `reports.json` (or equivalent index) in the SAME commit cycle as the doc itself. If you skip the manifest, the doc doesn't show up on the dashboard — it exists at a URL but nobody finds it. Heath flagged this 2026-06-11 after Path to Revenue v4.0 sat live on Pages but wasn't on the dashboard. For strategic plans this means three entries: Plan + Deep Dive + Deck. See [[strategic-plan-structure]] §"Publishing checklist" for the entry shape.

When Pass 10 fires, the cut list calls out: "Strategic-plan thrash cuts: removed N bets, moved depth to Deep Dive companion, converted individual names to departments, registered N files in reports.json."

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
- Corporate-ops verbs as action headlines: "Activate," "Stand up," "Operationalize," "Roll out," "Cascade," "Implement" — used as the lead verb of an action. See the action-verb rule below.

### Action verbs — strategic intent, not corporate operations

**A number alone is data; a verb alone is structure. An action item lives or dies on its lead verb.** Action items in a do-this block lead with strategic human verbs that sound like a leader giving direction, not a project manager filing a ticket. The specific number or structural detail (the 184, the 1:2:1, "in-house") lives in the WHY line or the measure-by-when, never in the headline.

**Worked examples — Heath called these out by name:**
- ❌ "Activate the 184 PQAs" → ✅ **"Attack our Product Leads"** (the 184 moves to the Why)
- ❌ "Stand up the 1:2:1 SDR pod" → ✅ **"Decide on Outbound Strategy"** (the 1:2:1 detail moves to the Why)
- ❌ "Operationalize the renewal motion" → ✅ **"Ship the renewal strategy"**
- ❌ "Roll out the routing SOP" → ✅ **"Write down how a lead becomes a deal"**

**The verb swap table:**

| Drop (corporate-ops) | Use (strategic-human) |
|---|---|
| Activate | Attack |
| Stand up | Decide on |
| Operationalize | Run |
| Implement | Build / Ship |
| Roll out | Launch |
| Drive | Lead |
| Leverage | Use |
| Cascade | Push |
| Onboarding | Help them land |
| Enable | Coach |

**Why this matters.** Corporate verbs telegraph "consulting deck." Strategic verbs telegraph "we're going to do this on Monday." The reader of a do-this block is making a decision about how to spend the next 30 minutes — the headline has to carry intent, not implementation. The 184, the 1:2:1, the percent, the date are all load-bearing; they live one click down inside the action, not at the front.

**How to apply.** Every action in the do-this block leads with a strategic human verb. Every play name in a deeper section follows the same rule. Specific numbers and structure stay in the WHY/measure-by-when lines beneath. Section headlines (Find / Convert / Grow / Build / Save) also pass this test.

## Output contract

**Explainer mode swaps the structure** (see below): the reader's four questions replace the verdict-first arc, and the end-to-end worked example plus the execution bridge are the closers. The voice rules, humanized numbers, trust contract, and cut passes still apply.

Always produce four things:

1. **The "If you read nothing else — do this" block** — generated for EVERY document reviewed, even if the original had nothing like it. Template:
   - The story arc (≤3 lines): *Where we are → Where we need to be → How to get there*, humanized numbers
   - The numbered actions — each verb-first with a **strategic human verb** (Attack / Decide / Ship / Save / Write — never Activate / Stand up / Operationalize; see "Action verbs" in the voice rules above), carrying its one proving number, its **owner**, and its **measure-by-when**. The specific number and structure live in the WHY/measure line, never in the headline.
   - Deeper reads — links with a one-phrase reason to click
   If the document doesn't support a do-this block (no actions derivable), say so explicitly — that is itself the finding.
2. **Compressed document** — the full rewritten output, ready to use
3. **Cut list** — a brief log of what was removed and why (one line per major cut, not per sentence)
4. **Word count delta** — `Original: N words → Compressed: M words (X% reduction)`

**Action cards vs lists — the formatting test:** formatting earns its place only when it adds a scannable dimension (owner, measure, deadline, status); boxes around the same sentences are fluff. Default = numbered list with owner + measure inline (preserves reading order). Upgrade to a card grid only when the block is a standing dashboard rather than a one-time read.

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
| Explainer / how-it-works (score, model, system, policy) | restructure, do not just cut — reader's four questions + worked example + execution bridge; depth behind toggles |
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

## Explainer mode — structure by the reader's questions

Some documents don't report a finding — they explain how something WORKS: a score, a model, a system, a process, a policy. For these, verdict-first becomes **question-first**. The reader of an explainer arrives with the same fixed questions every time, in the same order. Lead with those questions, answer each in one screen, push the math behind a toggle. Don't make them hunt for the shape of the thing — hand it to them in the order their head is already asking.

The reader's four questions (rename the labels to the domain — "score" becomes "policy", "verdict", "number", "decision"):

1. **What is it?** The output, first and biggest — one number, verdict, or one-line answer. Visual, not buried in prose. If there is a scale or set of outcomes, show the ladder.
2. **Where does it come from?** The inputs and sources, as scannable cards, each tied to the exact question it answers ("hiring data, are they growing sales?"). Not a methodology dump — a trust map.
3. **How does it add up?** The mechanism. ELI5 sentence first (the rule already holds), the real math behind a "show me the math" toggle. The skimmable reader never opens it; the skeptic always can.
4. **What do I do with it?** The reader's payoff — the context, the angle, the next move this unlocks. An explainer that stops at "now you understand" stopped half-way.

Two closers are mandatory in explainer mode:

- **One worked example, end to end.** A single real case run through all four questions — the actual number, where its data came from, how it added up, what to do about it. Abstract explanations get doubted; a concrete case is where trust is won. (e.g. one account: "Score 100. Here is the data. Here is the math. Here is your opener.")
- **The execution bridge.** End on "here is how you act on this today" — numbered steps or literal copy-paste prompts, not a summary. The best explainer hands the reader the next action with the friction already removed (e.g. score then brief then draft then launch, as three prompts they can paste).

Test: read only the four answer-headers and the worked example — could the reader use the thing? If no, an answer is missing a sentence, not the reader missing a section.

## The trust contract — earn the right to be executed on

A reader only executes on an output they trust. For anything the reader is meant to act on without re-deriving it — a score, a lead list, a recommendation, an enriched record — trust is the product, and you build it on purpose:

1. **State what was done FOR them, up front.** "We checked 9 sources, cross-validated the CRM against the truth, and only spend on accounts you will touch." This is the permission slip to stop re-checking and start acting. Without it, a careful reader re-verifies everything and the document saved them nothing.
2. **Keep the caveats visible, never buried.** "When the data is thin, the score says so." A limitation you can see reads as a system you can trust; a limitation you hide reads as a black box. Surfacing the honest edge is what makes the confident parts believable.
3. **Hand over the conclusion and the next move — never the homework.** If the reader has to assemble the answer from parts, the document did not finish its job. The deliverable is the verdict plus the action, with the parts one click away for anyone who wants to audit.

This is the difference between a document that informs and one that gets acted on. The tone is "we have your back": the work was done, here is the result, here is how to use it. Reassurance is not fluff — it is what converts a correct document into an executed one.

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

## Make this presentable — the deck view

Trigger on "make this presentable", "slide view", "deck this", "give me something to drive the convo". Any document that has a do-this block is ~20 minutes from a presentation, because the block maps onto slides 1:1:

1. **The arc → 3 slides** (Where we are / Where we need to be / How to get there) — one humanized headline number per slide.
2. **Each numbered action → 1 slide**, or one "the moves" slide with owners inline when there are ≤5.
3. **One proof slide** — the single trendline or comparison that says "this is achievable" (e.g., "we already hit the target rate twice").
4. **Closer = deeper reads** — the link list as the final slide.

Rules: **8–12 slides, one idea each**; humanized numbers only (exact figures live in the linked doc — the deck never carries precision the document must defend); **every slide links to its evidence anchor** so a challenge in the room is one click from the source; the deck is an HTML page on the same Pages site (arrow-key/space navigation, dots, print = one slide per page for the PDF handout); the source document gets a **"▶ Present"** button in its sticky header. Deck inherits the report's CSS variables; the accordion/sticky-header validator warnings don't apply to deck format.

The deck is a VIEW of the document, never a fork — it is regenerated from the do-this block after any revision, and its QA line states which report rev it mirrors.

## Anti-patterns

Do not do these:

- **Don't summarize into bullet points** unless the original was bullets. Preserve the document's form — compress its words. (Exception: Pass 6 — sentences that *enumerate* 3+ parallel items become lists; narrative stays prose.)
- **Don't lose the numbers.** If the original says "42%," the compressed version must say "42%." Vague compression is worse than no compression.
- **Don't invent.** If the verdict isn't explicitly stated, find the strongest implicit one and flag it: "Reading the verdict as: [X]. If that's wrong, correct me."
- **Don't compress tables of data.** Threshold tables, weight matrices, event registries — these are already compressed. Leave them. Cut the prose around them.
- **Don't add new structure.** Don't introduce headers that weren't in the original just because they'd organize your output better. Restructure what exists; don't redesign.
