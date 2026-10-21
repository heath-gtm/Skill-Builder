---
name: reveal-the-impact
description: >
  Stage 3 of Show Me You Understand Me. Takes the named crack and ties it to a
  consequence the person actually feels, business stakes plus personal stakes,
  quantified where honest, humanized always. Kills trivia: a crack with no
  impact is just a clever observation. Trigger on "reveal the impact", "so
  what", "what does this cost them", "quantify the crack", or after
  name-the-crack.
---

# Reveal the Impact

Stage 3. A crack tells them you noticed. Impact tells them why they should care. Without it you have written a smart observation that earns a "huh, true" and no reply. Impact is the difference between being interesting and being worth a meeting.

## What this does

Takes the named crack and hands back the impact block: the consequence the person actually feels, split into business stakes and personal stakes, quantified only where honest, humanized always. A number attached to a behavior is a story. A number alone is data. This stage turns the crack's cost into something the person feels in their actual week. Nobody feels a percentage.

## What you'll need

You don't need to connect anything to get value today.

- Works today with: the crack block from stage 2 and whatever you know about their goals. The funding target, the board pressure, the number they own. Paste it and the skill ties the crack to a felt consequence.
- More powerful connected to Amplitude: a real product-usage number to anchor the impact instead of an estimate.
- Sharper with Deepline: firmographic context confirms the business objective the crack threatens, the growth target or the headcount plan.

No data connected? The skill says what to connect and stops. It does not guess.

## How this runs at your connection level

- **Bring your data**: paste the crack block and whatever you know about their goals. The funding target, the board pressure, the number they own. The skill ties the crack to a felt consequence. Works with zero tools.
- **Connect your tools**: Amplitude gives you a real product-usage number to anchor the impact instead of an estimate. Deepline firmographic context confirms the business objective the crack threatens (the growth target, the headcount plan).
- **Just exploring**: run it on a single named prospect to see how a crack becomes a felt cost, with a person in the number, before you scale it.

Every run ends with the impact stated so a person feels it, and a note on whether the number is real, a labeled estimate, or none at all.

## Customize this for yourself

This was built for one outbound sales motion. Set these to your own:

| Knob | Default | Change it when |
|---|---|---|
| Quantify vs no-number | Quantify only on honest basis | You have no defensible number and a well-drawn consequence is enough |
| Estimate labeling | Always labeled and conservative | Never turn this off. An unlabeled estimate is a fabricated number |
| Business vs personal stakes emphasis | Both, personal weighted | You're writing to a champion who needs the business case to sell up |
| Impact length | One to two lines | Never expand to a paragraph. The message needs a line |

## The method

Read `references/context-model.md`. Take the `crack` block as input; write the `impact` block.

**The rule: nobody feels a percentage.** Reports are full of stats nobody feels. "68.3%" lands on no one. A number attached to a behavior is a story; a number alone is data.
- Data: "manual reporting costs ~15 hours a week."
- Felt: "that's two of your three new analysts spending their first quarter rebuilding the same dashboard by hand instead of the work you hired them for."

Same fact. The second one has a person in it.

**Two layers of stakes.** Fill both when you can.
1. **Business stakes** (`impact.business_stakes`): tie the crack to a company objective the context already surfaced. New funding leads to a growth number. New leader leads to a mandate. Churn signal leads to a retention line. This is what makes it a priority, not a nice-to-have. It is also the raw material for PLAN's Line Up Priorities later.
2. **Personal stakes** (`impact.personal_stakes`): what it costs this person in their role. The VP whose forecast is a guess is the one in the board meeting. The RevOps lead whose team is hand-jamming reports is the one who looks slow. Personal stakes are what actually move a human to reply.

**Quantify on a real basis, or don't.** Set `impact.quantified = true` only when you have a real basis: their context, a public benchmark you can cite, or a defensible estimate you label as one.
- Real basis: use the number, keep the receipt.
- Estimate: frame it as an estimate ("teams this size usually...") and keep it conservative. An inflated number is the same arrogance as an inflated crack.
- No honest basis: skip the number. A well-drawn consequence beats a fabricated figure. Never invent a metric to sound precise.

**Procedure.**
1. Take the crack and ask the enhanced "so what" three times, PLAN-style: crack, then immediate cost, then business consequence, then what it means for this person.
2. Draft the business stakes, tied to a real objective from the context record.
3. Draft the personal stakes, in the person's own terms.
4. Decide on quantification: real number, labeled estimate, or none.
5. Humanize: rewrite so a person is in it, not just a metric. Round to human scale.
6. Pressure-test: would this person feel this, or just read it?

## Quality gates

- [ ] No naked statistic. Every number has a person in it.
- [ ] Both layers filled where possible. Personal stakes are what get the reply.
- [ ] Every number has an honest basis. Estimates labeled and conservative.
- [ ] Nothing invented to sound sharp. No number beats a fabricated one.
- [ ] It's a line or two, not a paragraph. Compressed for the message.
- [ ] Pressure-tested: this person would feel it, not just read it.

## Output (example)

From Jordan Ellis / Northwind. The crack: scaling SDR headcount without building the motion those reps will run.

```json
{
  "impact": {
    "business_stakes": "The Series B promised roughly 3x new-logo in 18 months. A reactive motion caps how fast new reps produce, so the number slips on the exact timeline the board is watching.",
    "personal_stakes": "Jordan is the one in the QBR explaining why 5 new reps haven't moved the number yet. The ramp looks like a hiring problem when it's a system problem.",
    "metric": "new reps on an unbuilt motion usually take 2-3 extra months to produce, which is most of a quarter of the runway you just raised (labeled estimate, conservative)",
    "quantified": true
  }
}
```

Humanized: a person is in it (Jordan in the QBR), not a naked stat. The number is labeled an estimate and kept conservative. Business stakes tie to the real objective the context surfaced (the 18-month 3x plan). Personal stakes are what actually move Jordan to reply. This compresses to one line in the message.

## Example chat

**You:** Take the Northwind crack and reveal the impact. Can we say it costs them a specific dollar amount?

**Claude:** I don't have an honest basis for a dollar figure. I'd have to invent their pipeline math, and a made-up number reads as guessing. So I'll draw the consequence instead and label the one estimate I can defend. Business stakes: the Series B promised roughly 3x new-logo in 18 months, and a reactive motion caps how fast the new reps produce, so the number slips on the exact timeline the board is watching. Personal stakes: Jordan is the one in the QBR explaining why 5 new hires haven't moved the number, and it looks like a hiring problem when it's a system problem. The one number I'll use, labeled: new reps on an unbuilt motion usually take 2-3 extra months to produce. That's most of a quarter of the runway they just raised.

**You:** Why lead with the QBR thing instead of the revenue number?

**Claude:** Because nobody replies to a revenue number. They reply to being seen. The 3x target is the business case, and it makes this a priority. But the QBR moment is the personal stake, the thing Jordan actually feels on a Tuesday. A person is in it. That's what earns the reply. The revenue number stays in as the business layer so the impact has both, but the felt line is the one that moves a human.

## Go further

One impact block by hand shows the shape. Wired in, it stops smart observations from dying without a reply.

- **Batch across a list.** Run stage 3 on every named crack and flag the ones where no honest number exists, so a human decides whether the consequence alone carries the message.
- **Wire into the product-usage read.** Pull the real Amplitude adoption number for existing accounts so the impact is anchored to their behavior, not an estimate.
- **Schedule the priorities handoff.** Write the business-stakes line straight into the discovery brief's priority raw material so it's ready for PLAN's Line Up Priorities the moment the problem is confirmed.

## Where the numbers come from

The quantify knob and the estimate-labeling rule are yours to set, and the defaults here fit one outbound motion. The 2-3 extra months in the example is a labeled, conservative estimate, not a measured fact, which is exactly how any estimate should read. A real number comes from a real place: their own context, a public benchmark you can cite, or product data from a connected tool like Amplitude. The logic that never changes: nothing is invented to sound sharp, and a well-drawn consequence with no number beats a fabricated figure every time.

## Make it yours

Anchor the business stakes to the objectives your buyers actually get measured on, not generic ones. Set the quantify knob to your team's tolerance for estimates. Some buyers want a number, some punish a made-up one harder than no number at all. Tune the personal-stakes voice to the title you sell to, because the QBR moment that lands on a VP is not the one that lands on an SDR leader.
