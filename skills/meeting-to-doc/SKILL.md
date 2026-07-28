---
name: meeting-to-doc
description: Turn a meeting transcript or notes into a structured Superhuman Docs (Coda) document with decisions captured and action items routed to owners. Pulls the transcript (from a meeting tool or pasted text), extracts decisions and next steps, and builds a clean doc: outcome up top, decisions callout, discussion, and an action-item table with owner and due date. Trigger on "turn this meeting into a doc", "write up the call", "capture the decisions and action items", "meeting notes to a doc", "recap this transcript", or any request to convert a conversation into a structured, owned record.
---

# Meeting to doc

Turn a conversation into an owned record. The value is not a transcript dump; it is the decisions made and the next steps with a name and a date on each.

## Inputs
A transcript or notes (pasted, or pulled from a meeting tool), the attendees, and the meeting purpose. If a meeting tool is connected, pull the transcript and summary; otherwise work from pasted text. Never invent a decision or an owner that was not in the source; mark anything unclear as [needs owner] rather than guessing.

## The build (uses the Meeting Notes to Action Items template)
- **Hero:** meeting name, date, attendees, and a one-line outcome (the single most important result).
- **Decisions:** a callout listing what was decided. Short declaratives, not a transcript.
- **Discussion:** the substance in a main+rail; the rail holds context, links, and open questions.
- **Action items:** a decision table with columns Action, Owner (person), Due (date), Status (pill). This is the point of the doc.
- **References:** the recording, related docs, the source transcript.

Build the substance through the MCP (superhuman-docs-builder), then finish in the UI and ship-check it.

## Routing the action items
Each action item gets one owner and a due date. If the connected stack allows, notify each owner; otherwise the owner column plus the share is the routing. Keep the human in control; do not auto-send on anyone's behalf without approval.

## Make it yours
Fork it. Point it at your meeting tool, set your action-item fields and your owners. The point is that every call leaves a record someone owns. Built by an operator. Customize it, break it, make it better.
