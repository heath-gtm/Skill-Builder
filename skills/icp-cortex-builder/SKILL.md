---
name: icp-cortex-builder
description: Build the ICP Cortex, the four foundational blocks everything else in your GTM is based on, from the decks, docs and tables that describe your company. Four plain files your whole team and every AI tool can read from. Finds where your existing documents contradict each other first, makes a human resolve each conflict, then writes the files and sets up how people and agents reach them. Built for any GTM team whose ICP exists in six places and agrees with itself in none. Trigger on "turn my ICP doc into something my AI can use", "convert my decks into context", "build my ICP Cortex", "build my company context", "the foundational blocks", "my AI does not know our ICP", "where should our ICP live", "centralize our GTM context", "my reps AI keeps guessing", or any question about storing company context for AI to read.
---

# ICP Cortex Builder

## What this does
Builds the ICP Cortex: the four foundational blocks everything else in your GTM is based on. Takes what you already have, the ICP deck, the positioning doc, the persona tables, the Notion database nobody updates, and turns it into four plain text files that a human and an AI read the same way. The first thing it does is not write anything. It finds where your own documents disagree with each other, because that is the real problem and nobody has looked. Then a human picks a winner on every conflict, and only then does it write. The output is four files, one home for them, and a named path for your reps, your team and your agents to reach them.

This is a one-time conversion. Run it once per company, not once per quarter.

**What ships with this skill.** `templates/` holds the five documents with their headers, their guiding questions, and the prompts that fill the hardest one. Copy them into whichever tool your team edits in. They are markdown so they paste cleanly into a Google Doc, a Notion page or a text file.

## What you'll need
Your existing documents. That is the whole prerequisite. No connector, no repo, no engineer.

- **Works today with**: paste or attach everything that claims to describe who you sell to. The deck, the doc, the old deck, the one in someone's Drive. The skill works from what you give it.
- **Better with your Drive or Notion connected**: it finds the copies you forgot about, which is where most of the contradictions live.
- **Sharper with a CRM**: it checks your written ICP against what actually closed, and flags the claims your own pipeline does not support.
- **Just exploring**: no documents yet? It runs in reverse and interviews you for the four answers directly.

## How this runs at your connection level
The skill never pretends a document said something it did not. Every claim it writes into a file is traceable to a source you gave it, or it is marked as a gap for you to fill. A gap is a question, not a guess.

- **Bring your documents**: full conversion, contradictions surfaced, four files written.
- **Connect Drive or Notion**: it sweeps for duplicates first, so you resolve conflicts you did not know you had.
- **Connect a CRM**: it tests your written beliefs against closed-won and closed-lost and tells you which ones your data contradicts.

## Customize this for yourself

| Set this | What it is | Default / Example |
|---|---|---|
| HOME | the one place the files live | the tool your team already edits in |
| FILES | the four questions you answer | sell / fit / not-fit / score |
| OWNER | who approves a change to each file | named person, written in the file |
| SURFACE | where your team actually reads it | the shared AI project they work in |
| CHECK | the monthly question with a known answer | "who do we disqualify" |
| TRIGGER | the condition that means you outgrew HOME | an agent has to read it with nobody there |

The files are yours. The skill's job is to make them findable, readable, and honest, not to hand you someone else's ICP.

## The method

### Gather everything, curate nothing
Collect every artifact that claims to describe who you sell to. Do not decide what is current. Do not leave out the old one. The out-of-date deck is evidence, and someone on your team is still using it.

Put it all in one conversation. Expect six to twenty documents. If you only find one, go look again.

### Find the disagreements before you write anything
This is the step that matters and the step everyone skips. Do not ask for a summary. Ask one question:

**"Where do these documents contradict each other?"**

You will get a list. Company size bands that do not match. A persona in the deck that is absent from the doc. A disqualifier in one place that is a target segment in another. Four files with the same title and different content.

This list is the actual state of your company's context. Nobody has seen it before, including the person who wrote the documents.

### A human resolves every conflict
Not the AI. You. Go down the list and pick a winner on each one, out loud, with a reason. This takes about twenty minutes and it is the only part of this process that cannot be delegated.

Where you genuinely do not know, write "undecided" and move on. An undecided field that is labeled is safe. An undecided field that reads like a decision is what makes AI output confidently wrong.

### Write one file per answer
Four files. Plain text or markdown. Named as the question they answer, not as a category.

A file is addressable. A folder is searchable. You want the path to be the answer so nobody ever has to search.

Each file opens with two lines: who owns it, and when it was last decided. Not a change log. Two lines.

Use the same four sections in all four documents, from `templates/`:

```
## The short answer          three sentences a new hire could repeat back
## What we believe           one labeled claim per line, no paragraphs
## What we do not know yet   explicitly undecided, labeled not hidden
## What this changes downstream   what becomes wrong when this changes
```

The last section is the one everyone skips. It turns each document into a declaration of its own blast radius, so changing a belief tells you what to go fix. The third is the one people resist. A labeled gap makes an AI say "your documents do not say." An unlabeled guess makes it answer confidently and wrong.

### Apply the new-hire test
Read each file and ask: would I hand this to someone on their first day and expect them to qualify a deal correctly.

If no, it is not done. The most common failure is a file that describes the ideal customer beautifully and never says who to walk away from.

## The four files

| File | The question it answers | What goes wrong without it |
|---|---|---|
| `what-we-sell.md` | What we sell, and against whom | AI writes copy for a product you discontinued |
| `who-buys-from-us.md` | Who is the right fit, and why | Every account looks qualified |
| `who-we-say-no-to.md` | Who is not a fit, and the tell | The expensive one. See below |
| `how-we-score.md` | What makes this a good lead | Marketing and sales disagree and neither knows it |

**The third file is the one nobody writes and the one that fixes the most.** An AI handed only an ICP will qualify everything in, because it has no basis to say no. Handed disqualifiers, it can refuse. That single file improves output more than the other three combined.

Sixteen-part frameworks collapse into these four. Most of the extra parts are one of three things: evidence that already lives in your CRM, something that changes monthly and is therefore not foundation, or a different view of one of the four.

## Enablement: three rungs, in order

Writing the files is half the job. Nobody reading them is the other half. Climb these in order and stop when it works.

### Rung one: yourself
The failure mode is forgetting. You will not remember to attach the files, and any system that depends on you remembering has already failed.

Load the context at the tool level, never at the conversation level. In Claude Code, that is a line in your project instructions. In Claude or ChatGPT, that is a project with the files loaded, and that project is where this work happens.

**The rule: never attach, always inherit.** If you are attaching a file, enablement is broken.

### Rung two: your team
Five to fifty people. The failure mode is copies drifting.

- One shared AI project. Everyone works inside it.
- One named person re-uploads when a file changes. Not a team. A person. If it is nobody, it is already dead.
- Staleness is silent, so detect it: once a month, ask the shared project your CHECK question. Wrong answer means the upload is stale. That is the entire monitoring system and it takes thirty seconds.

Most companies never need rung three. Be honest about whether you do.

### Rung three: your organization
Fifty plus, multiple teams, agents running in production. Copies stop working because you cannot re-upload to forty projects.

Now you need live reads, in order of effort:

1. Raw file URLs plus a token. Agents are happy, humans cannot use it, zero build.
2. A small internal site that rebuilds when a file changes. Humans get a URL, agents can fetch it. This is the right answer for most companies and almost nobody does it.
3. An MCP server. Agents get real tools instead of a wall of text. Most work, highest ceiling.

What makes it organizational is not the technology. It is two process hooks: a new hire gets the path on day one, and every new tool gets connected to it during setup. The market expectation now is that tools ship an MCP. If your context has an address, every tool you buy inherits your company's brain on day one instead of starting blank.

## Do not mirror. Migrate.
The most common mistake after this conversion is keeping the files in two places and syncing them.

Two copies that must agree is a job, and nobody runs it. Six weeks later they disagree and nothing tells you which is wrong. You have not built a backup, you have built a second source of truth with a delay.

**One home. Links everywhere else.** The other tool holds a link, not a copy. When you outgrow the home, move the files. Do not start mirroring them. If you genuinely need both, the copy is pulled automatically by a machine and no human ever touches it.

## The test that tells you what your format is actually doing
Run this once, at the start. Hold the tool constant and vary only the format. Same ten
accounts, same assistant, three sources: your existing deck, one plainly written document
saying the same thing, and the four documents once written. Score each on correct answers,
confident wrong answers, and "documents do not say."

**Do not assume the result.** What the test is for is finding the rows where the formats
disagree, because those are the rows where your documents contradict themselves or go
quiet. Those rows are the work. Whether you want an assistant that commits on a lean or one
that stops and asks is a choice you make, not a result the format decides for you.

**Do not run this as a tool comparison.** Testing your Drive against someone's Notion changes
two variables at once and you learn nothing about which one broke.

## The two tests
Run both before you call this done. Both take under two minutes.

**The qualifier test.** Give marketing's AI and sales's AI the same real account. Ask each to qualify it in or out, with the reason. Different answers means they are reading different context. The same answer with different reasons is nearly as bad.

**The disqualifier test.** Ask "what would make us walk away from this deal." A generic answer means there is no disqualifier file and the AI is improvising.

What failing looks like: a deck is mostly layout, so an AI reading its export sees the boxes and not the meaning, and a two-sided scale comes back as one flat list with both ends in it. A table or database view comes back as structure, column widths and empty cells, with the content buried. None of that is bad writing. It is a document written for a human in a meeting being read by a machine with nobody in the room.

## Quality gates
The skill refuses to do these things, and you should too.

- **Never write a claim no source supports.** A gap gets labeled as a gap, not filled with a plausible sentence.
- **Never resolve a contradiction on your behalf.** It surfaces conflicts and waits. The human decides.
- **Never produce more than four files on the first pass.** More files is the next problem, not this one.
- **Never recommend changing tools before changing format.** Drive is not the problem. Thirty formatted documents are the problem.
- **Never claim the context is live when it is a copy.** If someone re-uploads by hand, say so and name them.

## Example chat

**You:** I have an ICP deck, a positioning doc, two persona docs and a Notion table. Make me the files.

**Claude:** Before I write anything, these five sources disagree in four places. Your deck says 200 to 2000 employees. The Notion table says 500 plus. Your positioning doc names a "Head of RevOps" persona that appears in neither persona doc. And one of the two persona docs is dated eight months before the other with no note saying it was replaced, so I cannot tell which is current.

Pick a winner on each and I will write. The size band is the one that matters most, because every downstream score inherits it.

**You:** 200 to 2000 is right, the Notion table is old. Head of RevOps is real, add it. Use the newer persona doc.

**Claude:** Written. Four files. One flag worth your attention: none of the five sources says who you walk away from. Not one disqualifier anywhere. That is why your reps' AI qualifies everything in, and it is the single highest-leverage thing you are missing. I have left `who-we-say-no-to.md` as five questions instead of inventing answers. Fifteen minutes with your two best reps fills it, and they already know the answers.

## The loop that keeps it from going stale
Everything above gets you four documents that are true today. They were opinion when
you wrote them, the market moves, and nothing will tell you when they stop being true.
Staleness never throws an error. The assistant keeps answering confidently from a nine
month old belief and you find out when a deal dies.

So the last piece is a loop, and it has four parts.

**What feeds it.** What actually closed and what actually lost. Call transcripts. And the
observation nobody captures today: when five discovery calls in a row surface a pain that
appears nowhere in your documents, the documents are behind the market. A manager is the
only person positioned to notice that, which makes managers a sensor rather than an
audience.

**What it produces.** Proposed edits. Specific, cited, one per claim. "Three of the last
eight closed lost deals hit a pattern that is not in who-we-say-no-to. Here is the
proposed line."

**Who runs it, and who owns it.** These are two different jobs and conflating them is why
loops die.

| Job | Who | Why |
|---|---|---|
| Runs the extraction and proposes | Whoever owns the plumbing, usually RevOps | They are neutral between the teams, they already have the data, and they are the ones who notice the drift first |
| Approves or rejects the words | The named owner of that document | A belief needs an author. A document edited by consensus is owned by nobody |

**The gate that matters.** Proposals, never automatic edits. A document that rewrites
itself is a document nobody trusts, and the first silent wrong edit ends the whole
project. The owner clicks accept. That is the entire governance model and it needs no
committee.

Run it monthly. The month it produces nothing is useful information too.

## Go further
- **Put the monthly check on a calendar**, assigned to the OWNER, not to a team.
- **Give the files an address.** When something has to read them on a schedule with no
  human in the room, that is the trigger for rung three.
- **Point the loop at the gap list.** The "what we do not know yet" sections are a
  standing to-do list that most teams never revisit.

## Where this came from
This method came out of pointing AI at real GTM documents and watching what it did with slides and tables. The fix was not a better tool. It was four plain files and one person who owns each.

## Make it yours
Fork it. Change the four questions, the home, the owners. The point is not to run someone else's context. It is to have one version of your company that your team and your tools both read. Built by an operator. Customize it, break it, make it better.
