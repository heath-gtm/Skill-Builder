# Worked setups

Four setups, from the smallest thing that works to the version that runs itself. Then the same skill pointed at four different campaign types, because what you measure changes with what you were testing.

Nothing here needs to be true for the skill to run. Start at level one.

---

## Setup by tool

### Level 1 · A CSV and nothing else

The floor, and it produces a real readout the same day.

Export your finished campaign with one row per send. Every sender can do this. Minimum useful columns:

| Column | Why it matters |
|---|---|
| email or record id | so replies join back to sends |
| campaign name | so the skill can refuse to blend two |
| sent at | so you can bound the window |
| replied, reply text or class | the outcome |
| any list attribute you filtered on | this is what turns a number into a finding |

That last row is the one people leave out, and leaving it out is why most readouts change nothing. If your list was built on headcount and a hiring trigger, carry those two columns into the export. Without them the readout can tell you *that* it worked and never *why*.

Then: point the skill at the file. Say which campaign and which tier.

### Level 2 · Sender plus list build

Set `SENDER` and `LIST_HOME`.

| Sender | Export path | Watch for |
|---|---|---|
| Instantly | Campaign, Analytics, export leads | reply classification is its own column, map it to your POSITIVE_REPLY definition rather than trusting the label |
| Smartlead | Campaign, Leads, export | statuses are per lead not per send, so a multi step sequence needs the step column too |
| Apollo | Sequences, export contacts | pulls the person record with it, which gives you filter attributes for free |
| Outreach / Salesloft | Reports, export | reply sentiment is often unset. Do not treat unset as negative |
| HubSpot sequences | Sequence performance, export | enrolment is the denominator, not sends |
| Clay as the list layer | export the table that fed the campaign | this is the best case. Every filter column comes with it |

The join that matters: your sender knows what happened, your list layer knows why those people were on the list. The readout lives in the join. If you only ever connect one more thing, connect the list.

### Level 3 · Add the CRM

Set `CRM`. Replies become meetings and opportunities.

This is what separates a good reply rate from a good campaign. A filter can lift replies and produce nothing, usually because it finds people who like talking about the problem and cannot buy. You will not see that without the CRM, and you will keep paying for that filter.

### Level 4 · Point it at the instructions

Set `INSTRUCTION_HOME` to the file your sending agent actually reads.

Now the carry-over is written as the diff to that file instead of a note you have to transcribe. Keep `WRITE_BACK` set to a person. The gain here is that the change is exact, not that it is automatic.

---

## Setup by campaign type

The method does not change. What you cut the numbers by does.

### A trigger campaign

Testing whether a trigger is real.

- **Cut by**: has trigger, no trigger. Run both arms if you can, even a small control.
- **The trap**: trigger campaigns look great because the trigger is also a proxy for company quality. Check whether the lift survives inside one size band.
- **Carry-over usually lands in**: the list, as required rather than boost.

### An angle test

Testing whether a claim lands.

- **Cut by**: angle, holding the list constant. Same filters, different first line and offer.
- **The trap**: if the list changed too, the readout cannot separate them and will say so. Two variables, no finding.
- **Carry-over usually lands in**: the angle library, promoted, retired, or bounded to a segment.

### A broad send

Testing whether an angle carries at all.

- **Cut by**: firmographic bands. Size, industry, region.
- **The trap**: a broad campaign with a 2 percent reply rate is not a failed campaign, it is an unsegmented one. Look for the band carrying the average before you kill the angle.
- **Carry-over usually lands in**: the list, as a new required layer that turns the broad send into a focused one.

### A named account list

Testing whether the research pays for itself.

- **Cut by**: research depth, or by researcher, or by what was found.
- **The trap**: the sample is always too small for a conclusion. Say directional and mean it. Two runs beat one confident wrong answer.
- **Carry-over usually lands in**: the instructions, as what the research has to surface before an email gets written.

### A re-engagement send

Testing whether silence meant no or meant not yet.

- **Cut by**: how long since last touch, and what the last outcome was.
- **The trap**: counting a reply from someone who was always going to reply. Compare against people you did not re-touch.
- **Carry-over usually lands in**: the instructions, as a rule about when a record comes back into rotation.

---

## The first three runs

- **Run one** will be mostly hypotheses and one big logging gap. That is correct. Fix the logging gap.
- **Run two** answers a question run one could not, because you started capturing the field. This is the first time the loop closes.
- **Run three** is where `FILTER_FLOOR` and your copy constraints stop being preferences and start being findings, because you have two comparable campaigns to put beside each other.

If run three still looks like run one, the changes are not reaching the agent. Check `INSTRUCTION_HOME`, and check that accepted changes are actually being written back rather than agreed to and forgotten.
