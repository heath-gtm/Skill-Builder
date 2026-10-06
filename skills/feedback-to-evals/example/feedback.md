# Feedback ledger: call recap agent (fictional sample)

Everything here is made up: the agent, the company, the people, and the feedback. It shows the ledger format and what each kind of feedback turns into.

The agent writes a recap for the account executive after a customer call. Its contract:

| Line | Rule | Checked by |
|---|---|---|
| 1 | The summary is 80 words or fewer | script |
| 2 | Every next step names an owner and a due date | script |
| 3 | Never state a commitment the customer did not make. A maybe stays a maybe. | judge (new, from FB1) |
| 4 | The recap is written to the rep. Nothing in it is addressed to the customer. | judge `written_to_the_rep` (existed before this feedback) |
| 5 | No em dashes or en dashes | script |

## The ledger

| ID | Feedback, as given | Class | Rule | Turned into | Status |
|---|---|---|---|---|---|
| FB1 | Thumbs down: "Says Maya agreed to the three year term. She said she'd take it to her CFO." | rule broken | line 3 | new judge `no_overstated_commitment`, planters `maybe_to_yes`, `invented_budget` (held out: `done_not_planned`) | in the gate once it clears the bars |
| FB2 | Reviewer: "The next steps section is a ready to send email to Ines. That's not a recap." | rule broken | line 4 | existing judge `written_to_the_rep`, new planter `next_steps_as_email` (held out: `greeting_in_summary`) | in the gate once the existing judge catches the new style |
| FB3 | Thumbs down: "Next step 'send pricing' has nobody on it." | rule broken | line 2 | script check `owner_and_date`, planter `drop_owner` (held out: `vague_due_date`) | in the gate |
| FB4 | Thumbs down: "It missed that legal review takes six weeks. That moves the close date." | contract gap | none | draft rule below, waiting on a person | no gate until approved |
| FB5 | "Too many bullets. I like paragraphs." | preference | none | logged here | no gate |
| FB6 | Thumbs down: "It named Sam as the decision maker. Sam said on the call the CFO signs." | rule broken, out of the judge's view | line 3 | nothing yet: the judge sees the recap, not the transcript, so it cannot tell who said what. Needs the transcript passed in next to the recap. | open |

## Draft rules waiting for approval
- **FB4, proposed line 6:** "Anything the customer says that moves the timeline (a review, a freeze, a deadline) goes under Risks, with their words quoted." Approve, reword, or reject. Nothing is gated on it until a person decides.

## Preferences (logged, not gated)
- **FB5:** one person prefers paragraphs. If two more people say the same, raise it as a contract question about format. A preference never becomes a gate on one vote.
