---
name: name-the-crack
description: >
  Stage 2 of Show Me You Understand Me, and the whole moat. Reasons over a
  context record to name ONE credible crack, where the person's world likely
  breaks, and frames it as a question, never an assumed problem. Enforces the
  hypothesis-as-question guardrail and scores confidence. Uses the crack library
  to map role/persona to likely cracks, then grounds them in real evidence.
  Trigger on "name the crack", "what's the hypothesis", "where does their world
  break", "find the tension for {person}", or after map-the-facts.
---

# Name the Crack

Stage 2. This is where the system either proves it understands the person or exposes that it does not. Everyone can enrich a contact. This step turns facts into a hypothesis about where their world breaks. That is the thing that earns the reply.

## What this does

Takes the context record from stage 1 and hands back one crack: the tension between what the person is trying to do and what their current setup lets them do, framed as a question, scored for confidence, bound to real evidence. Not a pain you assume. A fault line the evidence points at. This is the moat. The rest is plumbing.

## What you'll need

You don't need to connect anything to get value today.

- Works today with: a populated context record from stage 1, or even a few facts you already trust. Paste them and the skill clusters the evidence and names the crack.
- More powerful connected to Octave: persona plays sharpen how the crack maps to the role, so the pattern reads like the buyer's world and not a generic template.
- Sharper with Deepline: backfill a thin source before you commit, so a low-confidence crack becomes a medium one instead of a guess.

No context connected? The skill says what to connect and stops. It does not guess.

## How this runs at your connection level

- **Bring your data**: paste a populated context record, or even a few facts you already trust. The skill clusters the evidence and names the crack. Works with zero tools.
- **Connect your tools**: Octave persona plays sharpen how the crack maps to the role. Deepline can backfill a thin source before you commit, so a low-confidence crack becomes a medium one instead of a guess.
- **Just exploring**: run it on a single named prospect to see the shape. One crack, framed as a question, with the confidence score that decides the whole downstream tone.

Every run ends with the crack's confidence score and its disconfirmers, the thing the rep would go back and validate to make it sharper.

## Customize this for yourself

This was built for one outbound sales motion. Set these to your own:

| Knob | Default | Change it when |
|---|---|---|
| Crack confidence threshold to ship | Medium | You'd rather hold and go back for evidence than send a soft crack |
| One crack vs shortlist | One | You're workshopping internally and want to see the candidates before picking |
| Lead-with-fact vs lead-with-crack | Follows confidence | You want to stay conservative and lead with the fact even on a high-confidence crack |
| Crack library source | `references/crack-library.md` | You've built your own validated pattern set and want to point at it |

## The method

Read `references/context-model.md` and `references/crack-library.md` first. Take the context record from `map-the-facts` as input.

**What a crack is.** The tension between what they are trying to do and what their current setup lets them do.
- Weak (assumed): "You're probably struggling with pipeline."
- Strong (evidenced): "You just opened three RevOps analyst reqs while your stack is still spreadsheet-plus-CRM, which usually means reporting is being done by hand and the new heads are a patch, not a fix."

The second names a crack because it is built on observations (`evidence_ids`) and it invites the person to confirm or correct.

**The guardrail (non-negotiable). Hypothesis-as-question, never assumed-problem.** Every crack must pass this three-beat test before it ships:
1. **Here's what's likely true.** Grounded in a real observation from the context record.
2. **Here's where teams like yours usually feel friction.** The crack, stated as a pattern, not a verdict.
3. **Does that land?** An explicit invitation to correct you.

If your crack cannot be said in that shape, it is an assumption. Rewrite it or drop it. Set `crack.failure_mode_checked = true` only after it passes. Banned openings: "I bet you're...", "I know you're dealing with...", "Like every {role}, you're...". These presume. They are the tell of a machine that did not actually look.

**Procedure.**
1. **Cluster the evidence.** Read all four context arrays. Which observations point at the same underlying tension? A crack supported by two or three sources at once is far stronger than one from a single fact.
2. **Draft candidate cracks.** For each cluster, write the underlying tension. Pull the persona-level pattern from the crack library to name it, then bind it to the specific evidence.
3. **Pick one.** One crack per person. The best crack is specific, evidenced by more than one source, and something they would nod at. Resist listing three. You dilute all of them.
4. **Frame it as a question.** Write `crack.framed_question`, the actual "does that land?" line in plain language.
5. **Score confidence.** high = multi-source, recent, specific. medium = single strong source. low = mostly persona pattern with thin live evidence (usually means go back to stage 1, or lead softer).
6. **Run the guardrail test.** Confirm the three beats. Flag any presumption.

**Confidence changes the whole downstream tone.**
- **High:** you can lead with the crack directly.
- **Medium:** lead with the fact, offer the crack as "I'd guess this means..."
- **Low:** do not fake certainty. Lead with genuine curiosity about the fact, hold the crack lightly. A low-confidence crack sent as high-confidence is exactly the arrogance buyers punish.

## Quality gates

- [ ] It's a crack, not a pain. A specific tension the evidence shows, not generic persona pain.
- [ ] One crack, not three. No dilution.
- [ ] Passes the three-beat test: likely-true fact, pattern-not-verdict, explicit "does that land?"
- [ ] No banned opening. Nothing that presumes the problem.
- [ ] Confidence is honest, not inflated. `evidence_ids` trace to real observations.
- [ ] `crack.failure_mode_checked = true` only after the guardrail passes.
- [ ] Confidence sets the downstream tone. Low confidence leads soft, not sure.

## Output (example)

From Jordan Ellis / Northwind. The evidence clusters: funding pressure + SDR-only hiring + no ops hire + volume-first stack all point at one tension.

```json
{
  "crack": {
    "hypothesis": "Northwind is scaling outbound headcount to hit the Series B number, but nobody is building the motion those reps will run, so pipeline stays reactive and volume-dependent.",
    "framed_question": "Looks like you're adding SDR capacity fast for the growth plan. Usually the bottleneck there isn't headcount, it's whether the motion is built before the bodies land. Is that the shape of it, or have you already got that piece solved?",
    "evidence_ids": ["company-1", "jobs-1", "jobs-2", "tech-1"],
    "confidence": "high",
    "failure_mode_checked": true
  }
}
```

Why this crack over the others: it explains four observations at once, not one. What would disconfirm it: they've already hired an ops or enablement lead you couldn't see, or the reqs are backfill, not expansion. That disconfirmer becomes a thing the rep validates in stage 5. Passes the guardrail: here's what's likely true (hiring SDRs fast), where teams feel friction (motion not built), does that land.

## Example chat

**You:** Here's the context record on Jordan at Northwind. Name the crack.

**Claude:** Four observations cluster on one tension: the Series B growth number, the four SDR reqs, the missing ops hire, and the volume-first stack. Draft crack: they're scaling bodies to hit the number without building the motion those reps will run. That's supported by three sources plus the persona pattern, so confidence is high. Framed as a question so it invites a correction: "Looks like you're adding SDR capacity fast for the growth plan. Usually the bottleneck isn't headcount, it's whether the motion is built before the bodies land. Is that the shape of it, or solved already?" I'm holding at one crack. I could also name a targeting-quality crack off the thin stack signal, but that one only has a single source. Naming both would dilute the strong one. Want the single crack or the shortlist?

**You:** Single. But are you sure it's motion and not just that they hired too fast?

**Claude:** Not sure, and I'm not going to fake it. That's exactly the disconfirmer: it could be motion, or it could be targeting, or the reqs could be backfill I can't see. That's why it ships as a question, not a verdict, and it's the first thing the rep validates on the call. The evidence gives me high confidence there's a system gap. It doesn't tell me the gap is motion specifically. So the email names the shape and lets Jordan correct it. A "no, actually it's targeting" is a win. That's real discovery.

## Go further

One crack by hand proves the method. The value shows up at volume.

- **Batch across a list.** Run stage 2 on every mapped account and sort the output by confidence, so the high-confidence cracks go to send and the low ones go to a human queue instead of on autopilot.
- **Wire into the scoring engine.** Feed the account trigger from the Account Scoring Engine as the seed observation, so the crack is anchored to the reason the account scored in the first place.
- **Schedule the feedback write-back.** After discovery, write the real root cause back to `references/crack-library.md` so the library stops being generic persona pain and becomes your validated pattern set.

## Where the numbers come from

The confidence tiers and the ship threshold are yours to set, and the ones here suited one outbound motion. Confidence is not a formula. It is a plain read of how many real sources back the crack: high means multi-source, recent, and specific, medium means one strong source, low means mostly persona pattern with thin live evidence. Any fact the crack rests on traces to an `evidence_id` in the context record from stage 1. The logic that never changes: nothing is invented, and a crack that cannot be framed as a question is an assumption, so it gets rewritten or dropped.

## Make it yours

Point the skill at your own crack library so the patterns are the ones your reps have actually confirmed, not the starter set. Raise the confidence threshold if your buyers punish presumption harder than most. Tune the framed-question voice to how your team actually talks, blunt or warm, so the crack sounds like a person and not a template.
