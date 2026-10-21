---
name: discovery-prep-brief
description: >
  Stage 5 of Show Me You Understand Me, the human handoff. When a prospect
  replies or books, this generates the discovery brief that arms a rep to
  validate the hypothesis live and build rapport: what we hypothesized, what to
  confirm, the cracks to probe, and the human hooks to open with. Bridges the
  machine's relevance work into SMART Prospecting, SPRINT Discovery, and PLAN
  (Pinpoint the Problem / Line Up Priorities). Trigger on "prep me for the call",
  "discovery brief for {person}", "they replied, now what", "get me ready for
  {account}", or after assemble-and-sequence when a meeting is booked.
---

# Discovery Prep Brief

Stage 5. The machine owns relevance. The rep owns rapport. This is the seam. The brief does not replace discovery. It arms it, and it makes explicit which part is the human's job.

## What this does

Takes the full context record (context, crack, impact, message) and hands back the handoff block: a one-screen brief a rep reads in 60 seconds before the call. The hypothesis we sent, what to validate, the cracks to probe, the rapport hooks to open with, and the one thing not to do. It bridges the machine's relevance work into SPRINT Discovery and PLAN. The email named a crack in public. The call is where the rep confirms it, corrects it, or goes deeper.

## What you'll need

You don't need to connect anything to get value today.

- Works today with: the full context record, or the crack and impact you sent. Paste it and the skill builds the brief. Output is a one-screen read the rep can hold in a call.
- More powerful connected to Deepline: backfills a live rapport hook (a recent move, a shared background) so the human opener is real, not generic.
- Sharper with a meeting tool: Granola or your recorder feeds the call outcome back so the brief improves and the crack library learns.

No record connected? The skill says what to connect and stops. It does not guess.

## How this runs at your connection level

- **Bring your data**: paste the context record, or the crack and impact you sent. The skill builds the brief. Works with zero tools, output is a one-screen read the rep can hold in a call.
- **Connect your tools**: Deepline backfills a live rapport hook (a recent move, a shared background) so the human opener is real, not generic. Granola or a meeting tool feeds the call outcome back so the brief improves and the crack library learns.
- **Just exploring**: run it on a single replied prospect to see the seam. How a sent crack becomes a discovery plan a rep can walk in with.

Every run ends with the brief, and the next step: after the call, feed the real root cause back so the crack library learns.

## Customize this for yourself

This was built for one outbound sales motion. Set these to your own:

| Knob | Default | Change it when |
|---|---|---|
| Probe question count | 3-5 | A short intro call needs 3; a scoped discovery can hold 5 |
| Rapport-hook source | What's actually interesting in their situation | You have a real shared connection worth opening on instead |
| Framework depth | SPRINT + PLAN P and L only | Never run all of PLAN here. This is the first conversation, not the deal |
| Validate emphasis | The crack's disconfirmers | The reply already corrected the crack, so validate the correction instead |

## The method

Read `references/context-model.md`. Take the full context record (context, crack, impact, message). Write the `handoff` block.

**The core reframe.** The hypothesis we sent is now the hypothesis we test. A cold email that named a crack was a guess made in public. The call is where the rep confirms it, corrects it, or goes deeper. Either outcome is a win. A "no, actually it's..." is real discovery, and better than a "yes" because it is the truth. So the brief helps the rep walk in already understanding their world, so the conversation starts at the second question instead of the first.

**What the brief contains.**
1. **The hypothesis we sent.** The crack and framed question, verbatim, so the rep knows what the prospect already saw. Never contradict your own outreach on the call.
2. **What to validate** (`handoff.validate`). The specific things to confirm live. The crack's disconfirmers from stage 2 go here. "We guessed reporting is manual. Is that actually the bottleneck, or is it something upstream?"
3. **Cracks to probe** (`handoff.probe`). The discovery questions, drawn from SPRINT Discovery and PLAN's Pinpoint. Move from symptom to root cause. Use PLAN's Enhanced 3 Whys: symptom, then pattern, then root cause. Do not lead with the solution.
4. **Rapport hooks** (`handoff.rapport_hooks`). THIS is where the personal goes. The human openers you saved for the relationship: the shared context, the genuine curiosity, the thing that makes it a conversation between people. Explicitly not the insight. The insight was the email. Rapport is the room.
5. **Priority raw material.** The impact block, ready to become PLAN's Line Up Priorities (business priority + target date) once the problem is confirmed.

**The bridge into the PLAN system.** Name the next framework so the rep knows where they are.
- The sent crack -> the opening hypothesis for SPRINT Discovery.
- Validate + probe -> PLAN's P: Pinpoint the Problem (root cause, not symptom; the Problem Iceberg).
- Impact / stakes -> PLAN's L: Line Up Priorities (business + target-date).
- Do not jump to A (decision dynamics) or N (next steps) in the brief. That is later in the deal. The brief's job is to make the first real conversation land.

**The rapport discipline.** Rapport is not a script and not trivia mining. The brief gives the rep permission and material to be human: what is actually interesting about this person's situation, a real question worth asking, the tone that fits. Tell the rep plainly: lead with curiosity about their world, not with the pitch, and not with the clever line from the email. The machine already spent the relevance. The rep's job is the relationship.

## Quality gates

- [ ] It's a discovery plan, not the email handed back.
- [ ] Probe questions start at the problem, not the solution.
- [ ] Rapport is genuine curiosity, resourced. Not trivia to recite.
- [ ] The brief runs SPRINT + PLAN P and L only. Not the whole of PLAN.
- [ ] The sent hypothesis is verbatim, so the rep never contradicts the outreach.
- [ ] Reads in 60 seconds. Hypothesis, validate, probe, hooks, one thing not to do.

## Output (example)

From Jordan Ellis / Northwind. Jordan replied. The brief:

```json
{
  "handoff": {
    "discovery_hypothesis": "Motion isn't built ahead of the SDR ramp (the sent crack).",
    "validate": [
      "Is it actually motion, or is it targeting/ICP?",
      "Confirm the ramp expectation the board set for the 5 new reps."
    ],
    "probe": [
      "What has to be true for the 5 new reps to hit ramp?",
      "Where does that break today?",
      "Is that a people thing or a system thing?"
    ],
    "rapport_hooks": [
      "Jordan came from a scaled org. Genuine curiosity about what they'd build differently this time. THIS is where the personal goes, not the email."
    ]
  }
}
```

Priority raw material: the 18-month 3x plan feeds PLAN's Line Up Priorities once the problem is confirmed. The probe moves symptom to root cause with the Enhanced 3 Whys and does not lead with the solution. The one thing not to do: don't re-pitch the clever line from the email. That was the relevance. The call is the relationship.

## Example chat

**You:** Jordan from Northwind replied to the sequence. Prep me for the call.

**Claude:** Here's the 60-second brief. The hypothesis you sent, verbatim, so you don't contradict it: "motion isn't built before the SDR ramp." What to validate: is it actually motion, or is it targeting and ICP? And confirm the ramp the board set for the 5 new reps. Probe, symptom to root cause: "What has to be true for the 5 reps to hit ramp?" then "Where does that break today?" then "Is that a people thing or a system thing?" Don't lead with the fix. Rapport hook: Jordan came from a scaled org, so open with genuine curiosity about what they'd build differently this time. That's the personal, and it opens the room. One thing not to do: don't re-pitch the clever line from the email. You already spent the relevance. This call is the relationship.

**You:** Should I bring up the 3x revenue target on the call?

**Claude:** Hold it. That's the priority raw material, and it's PLAN's Line Up Priorities, which comes after you've confirmed the problem, not before. If you open with the revenue number you're back to pitching. Run Pinpoint first: get Jordan to name where the ramp actually breaks. Once the problem is real and shared, then you line it up against the 18-month plan and it lands as urgency instead of a pitch. Right now your only job is to make the first real conversation land.

## Go further

One brief by hand arms one rep. Wired in, it closes the loop that makes the whole system smarter.

- **Batch across replies.** Generate a brief the moment any sequenced prospect replies, so every rep walks in armed instead of scrambling.
- **Wire into the meeting tool.** Pull the call transcript from Granola or your recorder after discovery so the real root cause is captured against the sent crack automatically.
- **Schedule the feedback write-back.** Write what discovery revealed back to `references/crack-library.md` (stage 6), so the pattern that predicted right gets sharper and the ones that missed get retired.

## Where the numbers come from

The probe count, the framework depth, and the rapport-hook source are yours to set, and the defaults here fit one outbound motion. The brief carries no invented numbers. The 3x plan and the 5 new reps come straight from the context record and the impact block, and they stay as priority raw material until the rep confirms the problem live. The logic that never changes: the sent hypothesis appears verbatim so the rep never contradicts the outreach, and rapport is resourced curiosity, never trivia to recite.

## Make it yours

Point the probe questions at your own discovery framework if it isn't SPRINT and PLAN. Set the rapport-hook source to what your reps actually open well on, curiosity or a shared connection. Tune the "one thing not to do" to your team's most common mistake, whether that's re-pitching, over-scoping, or leading with the solution. The brief should sound like your best rep's prep, not a generic checklist.
