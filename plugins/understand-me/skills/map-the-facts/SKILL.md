---
name: map-the-facts
description: >
  Stage 1 of Show Me You Understand Me. Finds the right person at a target
  account and enriches CONTEXT (not just contact data) from four sources:
  company signals, job postings, tech stack / product usage, and role+persona
  pain. Writes into the shared context-model schema, nothing invented. Data-first
  and tool-optional: works from what you paste, gets deeper with Deepline /
  Amplitude connected. Trigger on "map the facts on", "research this account",
  "pull context on", "enrich context for", "what do we know about {person}".
---

# Map the Facts

Stage 1 of the relevance engine. Contact enrichment tells you where to send an email. Context enrichment tells you what to say. This skill does the second one.

## What this does

Takes a person or an account plus a target role and hands back a populated context record: observable facts about their world, pulled from four sources, each with a receipt and a so-what. It is not personalization trivia. It is relevance, the raw material stage 2 needs to name a real crack. Works from what you paste. Gets deeper with tools connected. Nothing invented.

## What you'll need

You don't need to connect anything to get value today.

- Works today with: a name and company, or an account plus a target role. Paste what you already know. A scored account, a trigger, notes from a call, a careers page you read.
- More powerful connected to Deepline: people-find plus firmographic, job-posting, and tech-stack enrichment, so the four sources fill from live data instead of what you happened to paste.
- Sharper with Amplitude and Octave: Amplitude adds real product usage on existing users into source 3. Octave persona plays sharpen source 4.

No tools connected? The skill says what to connect and stops. It does not guess.

## How this runs at your connection level

- **Bring your data**: paste what you know. A scored account, a trigger, notes from a call, a careers page you already read. The skill structures it into the four sources and reasons over it. Works with zero tools.
- **Connect your tools**: Deepline for people-find, firmographic, job-posting, and tech-stack enrichment (route through the deepline-gtm skill). Amplitude for product usage on existing users into source 3. Octave persona plays to sharpen source 4.
- **Just exploring**: run it on a single named prospect. Watch it pull four sources into one schema and tell you where the signal is real and where it is thin, before you wire anything.

Every run ends by naming where the signal is thin and what to connect to make it live.

## Customize this for yourself

This was built for one outbound sales motion. Set these to your own:

| Knob | Default | Change it when |
|---|---|---|
| Sources pulled | All four | You already have strong company + job signals and want a fast pass |
| Richest-source-first | On (job postings led hard) | The account is an existing user and product usage is the sharper signal |
| Confidence floor to keep an observation | Medium | You are in early exploration and want to see every weak signal too |
| Product-usage pull | Off for prospects, on for users | You have Amplitude connected and the account is in your book |

## The method

Read `references/context-model.md` first. That schema is the contract you write into.

You are not collecting personalization trivia (school, hometown, a recent post). You are collecting relevance: the observable facts that let stage 2 name a real crack. Every fact you keep must earn its place by pointing at a possible problem.

**Inputs.** Minimum: a person (name + company) or an account + a target role. Better: the scored account and trigger from the Account Scoring Engine. Optional: connected tools. If you have only a company and a role family, first identify the right person (the one who owns the problem you solve), then proceed.

For each of the four sources, pull observations into `context.<source>[]` as `{observation, raw, crack_signal, confidence}`. `observation` is the fact. `crack_signal` is the so-what. Always keep the receipt in `raw`.

1. **Company signals.** Funding, headcount trend, exec moves, launches, reorg, press. Ask: what changed that the old setup was not built for?
2. **Job postings.** Open roles on the team you sell to, the tools and duties named, how many, how long open. Ask: what are they hiring their way out of? This is usually the richest source. Pull it hard.
3. **Tech stack / product usage.** Named tools, integrations, and for existing users the adoption signal (what they use, what they own but never touched, WAU trend). Ask: where is the gap between what they bought and what they wanted?
4. **Role + persona pain.** Cross-reference their title against `references/crack-library.md`. This is the durable hypothesis that sources 1-3 make specific and current.

**Tool-optional execution.**
- **No tools:** ask the user for what they know, then run WebSearch/WebFetch on the newsroom, careers page, and LinkedIn. Structure whatever comes back. Empty fields stay empty.
- **Deepline connected:** people-find, firmographic, job-posting, and tech-stack enrichment.
- **Amplitude connected:** for existing users, pull adoption tiers and WAU trend into source 3.
- **Octave connected:** persona plays enrich source 4.

Never let a missing tool stop the stage. The schema fills from whatever source can fill it.

**The non-negotiable.** Nothing invented. If you cannot find a real fact for a source, leave it empty and say so. A thin-but-true record beats a full-but-fabricated one, because stage 2 builds the crack on `evidence_ids` that trace back to a real `raw` receipt. Set `provenance.nothing_invented = true` only if it is actually true.

## Quality gates

- [ ] Every kept fact points at a possible problem. Trivia dropped.
- [ ] Went past contact data. Email + title is not context.
- [ ] Every observation has a `raw` receipt behind it.
- [ ] Persona pain is labeled a hypothesis, not a fact, until sources 1-3 make it live.
- [ ] Nothing invented. Empty fields left empty and named out loud.
- [ ] `provenance.nothing_invented = true` set only if actually true.

## Output (example)

Jordan Ellis, VP Sales at Northwind (mid-market B2B SaaS, ~280 employees). Trigger: Series B announced 3 weeks ago. The four sources, receipts kept:

```json
{
  "context": {
    "company_signals": [
      {"id": "company-1", "source": "company_signal",
       "observation": "Series B ($40M) announced 3 weeks ago; CEO press quote about tripling new-logo revenue in 18 months",
       "raw": "press release + funding announcement",
       "crack_signal": "a growth number the current motion probably can't hit",
       "confidence": "high"}
    ],
    "job_postings": [
      {"id": "jobs-1", "source": "job_posting",
       "observation": "4 open SDR reqs, 1 AE req; reqs name high-volume outreach",
       "raw": "careers page", "crack_signal": "scaling bodies, not motion", "confidence": "high"},
      {"id": "jobs-2", "source": "job_posting",
       "observation": "No RevOps, enablement, or ops hire anywhere",
       "raw": "careers page", "crack_signal": "nobody is building the system the bodies will run", "confidence": "high"}
    ],
    "tech_and_product": [
      {"id": "tech-1", "source": "tech_product",
       "observation": "Stack shows CRM + a sequencer, no enrichment or intent layer named",
       "raw": "public stack signal", "crack_signal": "outreach is volume-first, not relevance-first", "confidence": "medium"}
    ],
    "role_persona_pain": [
      {"id": "role-1", "source": "role_pain",
       "observation": "Sales Leadership: pipeline is reactive, not manufactured; scaling heads to hit a number instead of scaling motion",
       "raw": "crack-library.md", "crack_signal": "durable persona tension, now made live by the reqs", "confidence": "medium"}
    ]
  }
}
```

Read: job postings are the richest source. Product usage is thin and labeled as such. Two sources plus a company signal converge. First instinct on the crack: scaling bodies without building the motion. Stage 2 will pressure-test that, not inherit it.

## Example chat

**You:** Map the facts on Jordan Ellis, VP Sales at Northwind. They just raised a Series B. No tools connected yet.

**Claude:** No tools, so I'll work from what's public plus what you know. I pulled the Series B ($40M, 3 weeks ago) and the CEO quote about tripling new-logo revenue in 18 months. Careers page shows 4 SDR reqs and 1 AE req, all naming high-volume outreach, and no RevOps or enablement hire anywhere. One thing I can't confirm without a receipt: their stack. I see a CRM and a sequencer referenced publicly but nothing on enrichment or intent. Do you know their stack, or should I leave source 3 thin and label it?

**You:** Leave it thin. That's all I've got.

**Claude:** Done. Record is populated: company signal (high), two job-posting observations (high), one thin tech observation (medium, labeled), and the Sales Leadership persona pattern from the crack library (medium, hypothesis until the evidence makes it live). Nothing invented, `provenance.nothing_invented = true`. Richest source is the job postings. My first instinct: they're scaling bodies without building the motion. I'm not committing to that. That's stage 2's job to test. Hand off to name-the-crack?

## Go further

Run once and it's a research pass. Wire it in and it's an engine.

- **Batch across a list.** Feed a scored list from the Account Scoring Engine and map the facts per person, flagging the thin ones for a human look instead of pretending.
- **Wire into the scoring engine.** Take the account and trigger straight from the Account Scoring Engine so stage 1 starts where scoring left off, no re-picking.
- **Schedule the enrichment refresh.** Re-pull Deepline job postings and Amplitude usage on a cadence so the context record ages out stale signals before stage 2 reasons on them.

## Where the numbers come from

The knobs and thresholds here are yours to set. The confidence floor, the source priority, and the product-usage default were tuned for one outbound motion, not handed down as law. Any real number in a run comes from a real place: the context record you paste, the four sources, or product data from a connected tool like Amplitude. The one thing that does not change is the logic. Nothing is invented, and every observation traces to a `raw` receipt, so a thin-but-true record always beats a full-but-fabricated one.

## Make it yours

Swap the four-source priority to your motion: if you sell to existing users, lead with product usage, not job postings. Point source 4 at your own `crack-library.md` so the persona patterns are yours, not generic. Set the confidence floor to how much guessing your team tolerates. Tighter floor, fewer but harder facts.
