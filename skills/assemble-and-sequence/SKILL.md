---
name: assemble-and-sequence
description: >
  Stage 4 of Show Me You Understand Me. Assembles the message in the
  facts -> crack -> impact -> action structure (relevance, not personalization
  trivia) and designs the multi-touch cadence and channel mix around it. The
  action/CTA is matched to the crack's confidence and the relationship
  temperature. Sequencer-optional. Trigger on "assemble the message", "write the
  outreach", "build the sequence", "draft the email", "cadence for {person}",
  or after reveal-the-impact.
---

# Assemble and Sequence

Stage 4. Everything upstream was research and reasoning. This is where it becomes a message and a cadence. The structure is the point: facts -> crack -> impact -> action. That order is why it reads as understanding instead of pitching.

## What this does

Takes the crack and impact blocks and hands back the message block plus a 3-4 touch cadence. Four lines, in order, each doing one job, with a CTA matched to the crack's confidence and the relationship temperature. The goal is that they think "this person actually gets my world," not "this person did a lot of homework at me." Works as paste-ready copy. Builds into a sequence with your sequencer connected.

## What you'll need

You don't need to connect anything to get value today.

- Works today with: the crack and impact blocks from stages 2 and 3, plus the relationship state (cold or warm). Paste them and the skill assembles the four-line message and designs the cadence. Output is copy the rep can paste anywhere.
- More powerful connected to Octave: refines persona-aligned phrasing on the crack and impact lines.
- Sharper with your sequencer: builds the touches as an enrollable sequence mapped to the cadence (it checks enrollment first so you're not double-touching).

No sequencer connected? The skill says what to connect and stops. It does not guess.

## How this runs at your connection level

- **Bring your data**: paste the crack and impact blocks and the relationship state (cold or warm). The skill assembles the four-line message and designs the cadence. Works with zero tools, output is copy the rep can paste anywhere.
- **Connect your tools**: Octave refines persona-aligned phrasing on the crack and impact lines. Your sequencer builds the touches as an enrollable sequence mapped to the cadence (check enrollment first so you're not double-touching).
- **Just exploring**: run it on a single named prospect to see the four-line message and the same-crack-new-angle cadence before wiring a sequencer.

Every run ends with the message and cadence, plus the next step: refine the phrasing in Octave or build the touches in your sequencer.

## Customize this for yourself

This was built for one outbound sales motion. Set these to your own:

| Knob | Default | Change it when |
|---|---|---|
| Channel of touch 1 | Email | Their attention lives on LinkedIn, or you have a warm intro path |
| CTA friction | Matched to confidence + temperature | Never outrun the confidence. Raise only when the crack is high and warm |
| Cadence length | 3-4 touches | A short warm reconnect needs 2; a cold high-value target can hold 4 |
| Message length | Four lines | Never expand to a case study. If it reads like a report, cut |

## The method

Read `references/context-model.md`. Take the `crack` and `impact` blocks; write the `message` block and a cadence.

**The message structure.** Four lines, in order. Each does one job. Do not pad.
1. **Facts line.** The specific observation that proves you looked. Names a real thing from their world (a job posting, a signal, a stack). No flattery, no "I've been following your work for a while."
2. **Crack line.** The hypothesis, framed as a question. This is `crack.framed_question`. It invites a correction.
3. **Impact line.** The felt consequence. One line, a person in it, honest number or none.
4. **Action line.** The CTA, matched to temperature.

The whole thing is short. If it reads like a case study, cut it.

**Personalization vs relevance (the thesis, applied).** Do not open with personal trivia. Save the personal for rapport, which is the rep's job in stage 5. The opener's job is relevance, the facts line. A dog's name at the top is a wasted first impression. A real observation about their pipeline is not.

**The action line matches confidence AND temperature.** Pull `crack.confidence` and the relationship state.
- **High confidence + cold:** a specific, low-friction ask tied to the crack ("worth a 15-min look at how teams past that hiring wall handle it?").
- **Medium confidence:** softer, invite the correction ("if I've read that right, happy to share what worked. Did I read it right?").
- **Low confidence:** curiosity-first, no meeting ask yet ("curious how you're thinking about it, no pitch").
- **Warm / existing relationship:** you can skip straight to value. The crack is a reason to reconnect, not a cold hook.

Never ask for more than the temperature has earned. A high-friction ask on a low-confidence crack is the tell of automation.

**The cadence.** A single touch is a coin flip. The Love Test showed reactive reps average about 2 touches and lose. A real motion is multi-step and earns attention. Design the sequence around the same crack, not repeated nagging.
- **Touch 1:** the full facts -> crack -> impact -> action message.
- **Touch 2 (channel switch):** LinkedIn or call. A different angle on the same crack, or a proof point.
- **Touch 3:** a new piece of evidence for the crack, or a soft "worth a look?" bump.
- **Touch 4:** a genuine breakup that leaves the door open, not a guilt trip.
- Space by temperature. Every touch adds value, PLAN-style, never "just checking in."

**Tool-optional execution.**
- **No tools:** output the message and the cadence as copy the rep can paste anywhere.
- **Octave connected:** refine persona-aligned phrasing on the crack and impact lines.
- **Sequencer connected:** build the touches as a sequence mapped to the cadence, ready to enroll. Check enrollment first.

## Quality gates

- [ ] Relevance opens. No personalization trivia in the facts line.
- [ ] Four lines, not a report. Cut anything that reads like a case study.
- [ ] Crack line is a question, not a verdict. It invites a correction.
- [ ] Impact line has a person in it. No naked percentage.
- [ ] CTA matches confidence and temperature. The ask never outruns what you know.
- [ ] Cadence is the same crack, new angle each touch. Not the same message four times.

## Output (example)

From Jordan Ellis / Northwind. Crack confidence: high. Temperature: cold.

**Touch 1 (email):**
> Facts: Saw the Series B and the 4 SDR reqs, all high-volume outreach.
> Crack: Adding capacity fast. Usually the bottleneck for the growth number isn't headcount, it's whether the motion is built before the reps land. Is that the shape of it, or solved already?
> Impact: When it's not, new reps take an extra quarter to produce, which is real runway against an 18-month plan.
> Action: Worth 15 min on how teams past that wall build the motion first? No pitch if you've got it handled.

CTA matches high confidence + cold: specific, low-friction, with an out. Not personalization trivia in the opener. Relevance.

**Cadence:** T1 email (above). T2 LinkedIn, a proof point on motion-before-bodies. T3 new evidence (a relevant build/receipt) on the same crack. T4 genuine breakup. Same crack, new angle each touch.

## Example chat

**You:** Assemble the message for Jordan at Northwind. Cold outreach.

**Claude:** High-confidence crack, cold temperature, so the CTA gets a specific ask with an out, not a hard push. Four lines. Facts: "Saw the Series B and the 4 SDR reqs, all high-volume outreach." Crack, as a question: "Adding capacity fast. Usually the bottleneck isn't headcount, it's whether the motion is built before the reps land. Is that the shape of it, or solved already?" Impact, a person in it: "When it's not, new reps take an extra quarter to produce, which is real runway against an 18-month plan." Action: "Worth 15 min on how teams past that wall build the motion first? No pitch if you've got it handled." Want the cadence too?

**You:** Yeah. But can we open with the fact that Jordan came from a scaled org? Feels like a good hook.

**Claude:** That's a rapport hook, and it belongs in stage 5, not the opener. If I lead with "I saw you came from a scaled org," that's homework-at-them, and it burns the first line on trivia instead of relevance. The opener's job is to prove I understand their world right now: the Series B and the reqs. Save the "you've built this before" angle for the rep to open the actual call with. That's the personal, and it lands far harder in the room than in a cold email. Here's the cadence: T1 the email above, T2 LinkedIn with a proof point on motion-before-bodies, T3 a new receipt on the same crack, T4 a clean breakup. Same crack, new angle each touch.

## Go further

One message by hand is a draft. Wired in, it's a motion.

- **Batch across a list.** Assemble messages for every account that cleared stage 2 at medium-or-high confidence, and route the low-confidence ones to a human instead of enrolling them.
- **Wire into your sequencer.** Build the 3-4 touch cadence as an enrollable sequence, enrollment-checked, so the rep clicks once instead of pasting four times.
- **Schedule the reply handoff.** On reply, auto-trigger discovery-prep-brief so the rep is armed the moment the crack lands, not scrambling after.

## Where the numbers come from

The CTA ladder, the cadence length, and the four-line discipline are yours to set, and the defaults here fit one outbound motion. The "about 2 touches" figure comes from The Love Test, a real read on how reactive reps behave, not an invented stat. The "extra quarter" in the example is a labeled estimate carried through from stage 3, not a measured fact. The logic that never changes: the ask never outruns the crack's confidence, every touch adds real value, and nothing in the message is invented.

## Make it yours

Set touch 1 to the channel your buyers actually answer on. Point the phrasing pass at your own Octave persona so the crack and impact lines sound like your product's world. Tune the CTA ladder to your team's norms, because the ask a warm champion has earned is not the ask a cold VP has. Keep the four-line discipline no matter what. The structure is why it reads as understanding.
