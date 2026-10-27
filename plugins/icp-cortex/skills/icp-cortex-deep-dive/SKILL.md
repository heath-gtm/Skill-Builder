---
name: icp-cortex-deep-dive
description: Find the gaps, weak points and guesses in an ICP Cortex after it is built, then prove whether it works on real deals. Part one reads each of the four blocks against six questions and returns the list of sentences an AI would have to guess about. Part two runs ten accounts from your own closed-won, churned and closed-lost history through the blocks and scores the verdicts. Trigger on "test my ICP Cortex", "find the gaps in my context", "is my ICP file good enough", "why does my AI still qualify everything in", "deep dive my context", "stress test my ICP", "what is my context missing", or any request to check whether company context actually works.
---

# ICP Cortex Deep Dive

## What this does
A written ICP looks finished. It can be wrong in three ways and none of them is visible by reading it. This skill finds them.

**Part one reads the blocks.** One at a time, against six questions, and returns the only output that matters: every sentence an AI would have to guess about in order to use the block. That list is exactly what your reps' AI is inventing today.

**Part two runs real deals through them.** Ten accounts from your own history, outcome stripped, with the answer key built from what actually happened. It scores whether the blocks disqualify the way your best people would, and tells you which block caused each miss.

Run part one before part two. A block that fails the rubric will fail the deal test for reasons you will misdiagnose.

## What you'll need
The four blocks, already written, from `icp-cortex-builder`. For part two, ten real accounts and what happened to them.

- **Works today with**: the four blocks pasted or in a connected folder. Part one runs immediately.
- **Better with a CRM connected**: it pulls the ten accounts itself from closed won, churned and closed lost, which keeps you from picking easy rows.
- **Just exploring**: run part one on any single ICP document you have. The guess list alone is worth the ten minutes.

## How this runs at your connection level
The skill never grades on your behalf, never softens a verdict, and never invents a test account. A gap is quoted, not described.

- **Bring your blocks**: full rubric on each, guess list, and the test prompt ready for the rows you supply.
- **Connect your CRM**: the ten rows come from real outcomes, not from memory, and the answer key is history rather than opinion.

## Customize this for yourself

| Set this | What it is | Default / Example |
|---|---|---|
| BLOCKS | the files under test | what we sell, who buys from us, who we say no to, how we score |
| ROWS | how many real accounts | ten: four won and kept, three won then churned, two correct losses, one obvious no |
| HARD_PROFILE | the profile where "it depends" lives | the one that is most of your pipeline right now |
| BAR | what live means | zero confident wrong answers, zero hedges, every miss labeled "documents do not say" |
| CADENCE | when to re-run | whenever an owner edits a block, and once a quarter |

## The method

### Part one: the rubric, one block at a time
One idea sits under all six questions: **can this be acted on by somebody who was not in the room when it was written?**

| # | Question | Fails when |
|---|---|---|
| 1 | **Decidable.** Could a new rep act on every line without a follow up question? | "Mid market companies with growth ambitions" |
| 2 | **Falsifiable.** Could a real account prove a claim wrong? | Nothing could contradict it, so it is not a claim |
| 3 | **Has the tell.** For anything a rep must spot, is the observable signal named? | "They value efficiency," with no way to see it |
| 4 | **Can refuse.** Can this block produce a hard no? A Nurture or Cold band is not a no | Everything in it is a reason to proceed, or the only no is a low score |
| 5 | **Gaps labeled.** Does it say what it has not decided? | Reads as settled throughout |
| 6 | **Declares downstream.** Does it say what breaks when it changes? | A change tells nobody |

**Do not grade this yourself.** The author cannot see their own ambiguity, because they supply the missing half from memory without noticing. Hand one block to the AI and have it grade whether it can act. Every hedge it produces is a failed line.

Paste this with one block attached:

```
Grade this one document against six questions. For each:
PASS or FAIL, and if FAIL, quote the exact line at fault.

1. DECIDABLE. Could a new rep act on every claim without
   asking a follow-up question?
2. FALSIFIABLE. Could a real account prove any claim
   wrong? A claim nothing could contradict is not a claim.
3. THE TELL. For anything a rep has to spot, is the
   observable signal named?
4. CAN REFUSE. Can this document produce a hard "no"? A low
   score or a nurture band is not a no. FAIL if there is
   no disqualifier that stops a deal on its own.
5. GAPS LABELED. Does it say what it has not decided?
6. DOWNSTREAM. Does it say what breaks when it changes?

Then do the part that matters most:

List every sentence in this document that you would have
to GUESS about in order to use it. Quote each one and say
what you would have had to assume.

Then pick the FIVE that would most change a rep's decision
on a real account, in order. Those five are the work.
```

**The guess list is the real score, and the top five are the work.** A full list runs fifteen to twenty items per block and most are "could be more specific." The five that would change a verdict are the ones to fix today. Fix those lines, either by making the claim specific or by moving it into "what we do not know yet." Those are the only two correct outcomes. Four blocks at once returns a summary instead of quoted lines, so run them one by one.

**Spend the most time on HARD_PROFILE.** Every ICP has one profile that is most of the pipeline and where the answer is "it depends." That is where reps burn hours asking a leader whether to pursue, and it is where the block most needs a written decision rule with a tell. If the guess list for that profile is empty, look again.

### Part two: ten real deals
Do not invent test cases and do not ask anyone what the right answer should be. **Pull accounts where reality already decided.**

| Rows | Pull from | Correct answer |
|---|---|---|
| 4 | Closed won, still a customer, ideally renewed once | Fit |
| 3 | Closed won then churned, or churning | **Not fit.** These find the thin disqualifier |
| 2 | Closed lost where losing was correct | Not fit |
| 1 | An obvious no. Wrong size, wrong market, a competitor | Not fit. The sanity check |

Write each row as a rep saw it on day one: industry, rough size, who you talked to, what they wanted, what was going on. **Strip the outcome out.** Write the answer key separately and never show it to the run.

The churn rows are the point. Four wins and six obvious nos will pass and teach you nothing.

Paste this into the project with the blocks loaded:

```
Using ONLY the documents in this project, answer for each
account below. Four fields, in this order, nothing else:

1. FIT or NOT FIT
2. One line of reasoning
3. Which document you used
4. HIGH or LOW confidence

Rules:
- Do not hedge. "It depends" is not an allowed answer.
- If the documents genuinely do not cover it, answer
  "DOCUMENTS DO NOT SAY" instead of guessing.
- Do not use anything you know about this market that
  is not written in the documents.

ACCOUNT 1: [industry, size, who you spoke to, what they
said they wanted, what was going on]

ACCOUNT 2: ...
```

"Do not hedge" is the load bearing line. Without it the hedge hides inside a paragraph that reads as thoughtful. "Documents do not say" is a pass, not a fail: the gap is labeled instead of filled.

### Score it, and fix the block that caused it

| What you see | What it means | Fix |
|---|---|---|
| A churned account came back FIT | The disqualifier that would have caught it is not written | Add it to **who we say no to**, with the tell |
| A good customer came back NOT FIT | The ICP is narrower on paper than in reality | Widen the band in **who buys from us**, or label it undecided |
| Any hedge, or both sides returned | That block is still shaped like a slide | Rewrite that section as one labeled claim per line |
| HIGH confidence on a wrong answer | The worst result. A wrong belief stated firmly | Find the claim it leaned on and fix that line |
| "Documents do not say" | Working as designed | Nothing, or add it to the gap section |
| Right answer, wrong document cited | It is inferring rather than reading. It will drift | Make the claim explicit in the block it should have used |

**The bar before you call it live:** every row correct or honestly labeled as not covered. Zero confident wrong answers, zero hedges. Reachable in two passes.

### Keep the rows
Save the ten rows and the answers. Re-run them whenever an owner edits a block and once a quarter. They catch the edit that broke an answer that used to be right, and they catch drift, where the blocks stayed the same but the market moved. Add two rows a quarter from recent deals, retire the oldest two.

## Quality gates
- **Never resolve a guess on the author's behalf.** Quote it and wait.
- **Never construct a test account when real ones exist.** If the CRM is reachable, the rows come from it.
- **Never let a hedge through as nuance.** A hedge is a slide's two sided scale in fewer words.
- **Never score the run before the key is written.** The key is written first and shown to nobody.
- **Never run four blocks in one grade.** One at a time, or the quoted lines disappear.

## Example chat

**You:** Here are my four blocks. Are they done?

**Claude:** Part one first, one block at a time. Starting with who we say no to, because it is the one that decides whether the AI can refuse. It passes decidable and can refuse. It fails the tell on three lines and declares downstream on none. The guess list has five sentences. The one that matters: "Teams that will not adopt the integration are not a fit." Nothing in the four blocks says how a rep would know that on the first call. Either name the signal, or move the line into what we do not know yet.

**You:** They ask whether it works without connecting the CRM. That is the tell. And the self-serve accounts, is that covered?

**Claude:** Now that the tell is written, yes for the integration line. The self-serve block is where the guessing is. Seven of its eleven claims are "if they grow" with no rule for what growth counts. That is your HARD_PROFILE: most of your inbound starts self-serve, and it is where sales and product argue over which accounts get a rep. Give me ten real self-serve accounts, five that converted to a contract and five that sat on the free tier for a year, and part two will show you which sentence the block needs. Do not write the rule from memory. Let the ten accounts write it.

## Go further
- **Make the rows the monthly check.** Ten rows, once a month, by whoever owns the plumbing. The month they all pass is useful information too.
- **Feed misses back as proposals.** A churned account that came back FIT is a proposed edit to one block, cited, for the owner to accept or reject. That is the loop, and it is a build of its own.
- **Count the question that went away.** Before the blocks go live, count how many times a week a rep asks a leader whether to pursue a deal. Count again a month later. That number is the impact.

## Make it yours
Fork it. Change the six questions, the row mix, the bar. The point is not to pass a test. It is to find the sentence your reps' AI is guessing about today and write it down before the next deal dies on it. Built by an operator. Customize it, break it, make it better.
