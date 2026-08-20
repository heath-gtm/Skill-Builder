---
name: brand-voice-guide
description: Set your brand voice and tone so every AI output sounds like you, not like generic AI. Names the voice pillars, the tone by context, the words you use and the ones you never do, and gives sample lines the model can pattern-match. Feeds the voice layer of the context repo so every skill writes in your voice. Fire on "define our brand voice", "brand and tone", "how should we sound", "voice guide", "make it sound like us", or the start of building a GTM context repo.
---

# Brand Voice and Tone: sound like you, not like AI

## What this does
Turns "make it sound like us" into a guide a model can actually follow: the voice pillars, the tone by context, a do and do-not word list, and sample lines to pattern-match. Without this, every skill output drifts to generic AI voice. With it, the whole repo writes in your voice.

## What you'll need (reads)
A few things you have already published that sound right (a post, an email, a page) and a couple that sound wrong. Your positioning from the Positioning skill, so voice and message agree. No connectors required.

## The method
1. Name 3 to 5 voice pillars. Adjectives with teeth: "plain, not corporate", "receipts over adjectives", "direct, no hedging". Each gets a one-line rule.
2. Set the tone by context. How you sound in a cold email vs a nurture vs a landing page vs a support reply. Same voice, different dial.
3. Write the do and do-not word list. The words and phrases you use, and the ones you never do (the AI tells, the corporate filler, the cliches). This is the fastest guardrail.
4. Give sample lines. Two or three real lines that are unmistakably you, each next to its generic-AI counterpart, so the model can copy yours and avoid the other.
5. State the one test. The single check any draft must pass to sound like you, for example "would I actually say this out loud?".

## Failure points
- Vague adjectives ("professional yet approachable") that no model can act on.
- A do list with no do-not list, so the AI tells survive.
- No sample lines, so "our voice" stays a feeling instead of a pattern.

## The receipt (writes)
[your voice pillars, the do and do-not list, and 3 sample lines with their generic counterparts. This becomes the voice layer of context/positioning.md]

Example (illustrative):
- Pillars: plain over clever, receipts over adjectives, operator not vendor.
- Do: short declaratives, name the tradeoff, one idea per line.
- Do not: hype words, filler, "unlock / leverage / seamless", bow-tied endings.
- Sample line: "We cut prep from a day to an hour." (yours) vs "Our seamless solution unlocks unprecedented efficiency." (generic AI).

## Example chat
**You:** I need to define our brand voice so every AI draft stops sounding generic. We're plain-spoken, no corporate fluff.

**Claude:** Here's the voice layer.
```
Pillars: plain over clever, receipts over adjectives, operator not vendor.
Do: short declaratives, name the tradeoff, one idea per line.
Do not: hype words, filler, "unlock / leverage / seamless", bow-tied endings.

Sample line: "We cut prep from a day to an hour." (yours)
vs "Our seamless solution unlocks unprecedented efficiency." (generic AI)
```
The part that actually holds this together isn't the adjectives, it's the do-not list. A pillar like "plain, not corporate" is a feeling until you pair it with the exact words banned; that's what a model can actually pattern-match against.

**You:** What's the single test I should run any draft through?

**Claude:** "Would I actually say this out loud?" If a line only works on a page, it's not your voice yet, it's a draft wearing your name. One sharpener: paste two more real examples, one that landed and one that felt off, so the sample-line pairs get sharper than the illustrative ones above.

## Go further
Naming the pillars by hand is the foundation. Here's how it holds across every piece of content you ship.

- **Feed it into every generator.** Drop the voice layer into your CLAUDE.md or context repo so every skill, post-writer, newsletter, and comment generator inherits the same do/do-not list automatically.
- **Audit drafts against it before they publish.** Run a voice-checker pass on anything leaving the building (Ghost drafts, LinkedIn posts) and flag violations line by line instead of catching them after they're live.
- **Keep the sample lines current.** Add a scheduled Claude task that pulls your best-performing published lines monthly and refreshes the pattern-match examples so the guide doesn't calcify around old work.

Once the voice is written down, every draft can be checked against it instead of vibed into shape.

## Next move
Hand the voice to the Context Pack so CLAUDE.md carries it into every session. Built GTM. Approach, not receipts.
