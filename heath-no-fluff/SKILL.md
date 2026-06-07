---
name: heath-no-fluff
description: >
  Cut any document — report, analysis, brief, email, spec, or LinkedIn draft —
  to its essential core, restructure it verdict-first, and rewrite it in Heath's
  voice. Target: 40–55% of original length for narrative docs. Fire whenever
  Heath says "this is too long", "cut this down", "remove the fluff", "tighten
  this up", "make this more direct", "condense this", "shorten it", "too much
  detail", or pastes a document and asks for a cleaner version. Also fire
  proactively when you observe a document that buries its lead, spends more than
  one paragraph on setup before stating the main point, gives equal coverage to
  unequal findings, or has a methodology section longer than the findings section.
license: MIT
compatibility: cowork claude-code
---

# heath-no-fluff

Cut documents to their essential core, restructure verdict-first, rewrite in Heath's voice. Think of it as aggressive editing — not summarizing — where every sentence earns its place.

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

**9. Administrative metadata** — Sections like "Data sources," "Build sequence," "Brand guidelines," "Appendix A: methodology" that are relevant to the author but not the intended reader. When the audience is leadership, cut these entirely or move to a literal appendix. Do not just compress them — remove them.

## Five-pass compression protocol

Work in sequence. Don't skip passes.

**Pass 1 — Find the verdict.** What is the single most important thing this document says? Write it as one plain sentence. If you can't, the document doesn't know either — that's your first cut signal.

**Pass 2 — Find the evidence.** What are the 2–4 facts that prove the verdict? These are keepers. Everything else is scaffolding.

**Pass 3 — Rebuild the structure.** Verdict first. Evidence second. Context (if any) last. If the document has a methodology section longer than the findings, invert it.

**Pass 4 — Sentence-level cuts.** Remove every sentence that doesn't add new information. For each sentence, ask: "Does this change what the reader knows or does?" If no, delete it.

**Pass 5 — Voice pass.** Apply Heath's voice rules (below). The document should read like it was written by someone who knows the answer, not someone building a case.

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

## Anti-patterns

Do not do these:

- **Don't summarize into bullet points** unless the original was bullets. Preserve the document's form — compress its words.
- **Don't lose the numbers.** If the original says "42%," the compressed version must say "42%." Vague compression is worse than no compression.
- **Don't invent.** If the verdict isn't explicitly stated, find the strongest implicit one and flag it: "Reading the verdict as: [X]. If that's wrong, correct me."
- **Don't compress tables of data.** Threshold tables, weight matrices, event registries — these are already compressed. Leave them. Cut the prose around them.
- **Don't add new structure.** Don't introduce headers that weren't in the original just because they'd organize your output better. Restructure what exists; don't redesign.
