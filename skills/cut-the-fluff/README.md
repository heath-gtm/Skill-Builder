# Cut the Fluff

> Cut any document to its essential core, humanize the numbers, restructure verdict-first as a 5-minute read, and rewrite it in your own voice. A number alone is data; a number attached to a behavior is a story. Round to human scale ("about 70%", "1 in 2"), turn rates into daily rituals, keep exact figures in the evidence layer. Fire on "this is too long", "cut this down", "humanize the numbers", "make this land", "remove the fluff", "say more with less", or any pasted doc needing a cleaner version. Also handles Explainer mode for docs that explain how something works (a score, a model, a process): restructure around the reader's four questions, add a trust contract and one worked example, close with an execution bridge.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/cut-the-fluff && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/cut-the-fluff/SKILL.md -o ~/.claude/skills/cut-the-fluff/SKILL.md && echo "Installed cut-the-fluff. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/cut-the-fluff/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Cut the Fluff

## What this does
Cuts documents to their essential core, restructures them verdict-first, and rewrites them in a voice you define. Aggressive editing, not summarizing. Every sentence earns its place. Three jobs: compress a bloated document without losing a single number, humanize the numbers so they land as behavior, and restructure so a reader can act in five minutes. There is also an Explainer mode for documents that explain how something works.

## What you'll need
Just a draft to edit. Paste in the document, report, email, spec, or post. No connectors, no data sources, no setup. The method runs on the text you hand it.

## Customize this for yourself
Set these once and the output sounds like you, not a generic editor.

| What you set | What it controls | Example |
|---|---|---|
| Your voice | The tone of the rewrite | "Short sentences, no hedging, first person, admit the mistake before the lesson." |
| Your audience | Who reads the output, which decides what counts as fluff | "Time-poor execs" vs "frontline reps who need the how" |
| What counts as a receipt | The evidence a claim needs to make the top block | "A specific number, a named source, or a before/after pair." |
| Your kill list | Words you never want in your writing | Edit the default list below. |
| Your action verbs | The lead verbs your action items use | Swap the verb table for words that sound like you giving direction. |

## The method

### Humanizing numbers, the core move
A number alone is data; a number attached to a behavior is a story. Apply five rules to every figure in the narrative layer:
1. Round to human scale. About 70%, not 68.3%. The exact figure lives one click away in the evidence block.
2. No naked numbers. Every figure rides with the behavior that produces it or the consequence it causes.
3. Rates become frequencies. 47% becomes "about 1 in 2." 64% becomes "2 of every 3."
4. Weekly abstractions become daily rituals. 8.8 per week becomes "fewer than 2 a day."
5. One number per sentence. A before/after pair counts as one.

Worked example. Before: "Inbound holds 68% of closed volume and 78% of won dollars." After: "About 7 of every 10 closed deals, and nearly 8 of every 10 won dollars, ride on one channel."

### What fluffy looks like
1. Context bombing. Paragraph 1 explains why we are doing this at all. Cut it.
2. Methodology exposition. Nobody asked how. Lead with what you found.
3. Buried verdict. The conclusion is in paragraph 5. Move it to sentence 1.
4. Symmetric coverage. Three items get equal treatment when one is far more important. Weight to importance.
5. Over-qualified claims. Pick a lane.
6. Show-your-work tables. Trim to the load-bearing columns.
7. Same point three ways. State the finding once, with the number.
8. Boilerplate transitions. Delete "it is worth noting," "in conclusion," "building on the above."
9. Prose-buried lists. A sentence enumerating 3+ parallel actions. Break it into a list.
10. Administrative metadata. "Data sources," "build sequence," appendices. Cut or move to a literal appendix.

### The compression protocol
Work in sequence.
1. Find the verdict. One plain sentence. If you cannot, the document does not know either.
2. Find the evidence. The 2 to 4 facts that prove the verdict. Keepers.
3. Rebuild the structure. Verdict first. Evidence second. Context last.
4. Sentence-level cuts. Delete any sentence that does not change what the reader knows or does.
5. Voice pass. Apply your voice rules.
6. Formatting pass. Pull prose-buried lists into numbered lists.
7. Thrash filter (for strategic plans). If the plan responds to more than 2 problems, it is reactive. Pick the 1 to 2 whose math moves the number.

### Your voice rules
- Self-implicating first. "We built the wrong thing," not "the data showed underperformance."
- Failure-derived insights beat generic best practices.
- Plain declaratives over bumper-sticker aphorisms.
- Specific numbers beat vague magnitude.
- No bow-tied endings.

Kill list (edit for yourself): "delve," "leverage" as a verb, "impactful," "seamlessly," "robust," "actionable insights," "it is worth noting," "in conclusion," "the data shows," rule-of-three lists where only two items matter, sycophantic openers, hyphenated filler ("data-driven," "best-in-class"), corporate-ops verbs as headlines ("activate," "operationalize," "roll out").

### Action verbs, intent not operations
An action item lives or dies on its lead verb. Lead with verbs that sound like a person giving direction. The number or structural detail lives in the why line, never in the headline.

| Drop (corporate-ops) | Use (direction) |
|---|---|
| Activate | Go after |
| Stand up | Decide on |
| Operationalize | Run |
| Implement | Build / Ship |
| Roll out | Launch |
| Leverage | Use |

### Output contract
Produce four things: the "If you read nothing else, do this" block (story arc in 3 lines + numbered actions + deeper reads), the compressed document, the cut list (one line per major cut), and the word-count delta.

### The 5-minute-read structure
Lead with a block a reader finishes in 5 minutes and can act on: the story as an arc (3 lines), the numbered do-this list, deeper reads as links with a reason to click. Everything below is evidence, not argument.

### Explainer mode
For documents that explain how something works, restructure around the reader's four questions: What is it? Where does the data come from? How does it add up? What do I do with it? Two closers are mandatory: one worked example end to end, and an execution bridge (numbered steps or copy-paste prompts).

### The trust contract
For anything the reader acts on without re-deriving it, trust is the product. State what was done for them, keep caveats visible, hand over the conclusion and the next move, never the homework.

## Output (example)
Input (about 130 words of setup, methodology, and a hedged close describing dashboard 73% / editor 34% / sidebar 12% usage).

Output (about 80 words, ~60% reduction):
```
Dashboard-first is no longer our headline. It is confirmed. Nearly 3 of every
4 interactions happen there. The editor sees about 1 in 3 users weekly. The
sidebar, barely 1 in 8.

The sidebar is underperforming enough to warrant a discoverability fix, not
just more onboarding. The editor needs more digging before we draw a conclusion.
One principle follows: dashboard-first, everything else secondary until the
sidebar numbers move.
```
Cut list: deleted the purpose paragraph and the methodology line, cut "quite interesting" plus the restatement, rewrote the hedged close as a concrete principle, turned rates into frequencies.

## Make it yours
Set your voice, your audience, and what counts as a receipt. Edit the kill list and the verb table until the output reads like you. Run a real document through it and see what it cuts. Built by an operator. Customize it, break it, make it better.
