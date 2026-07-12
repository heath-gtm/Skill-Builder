---
name: workspace-organizer
description: Make a messy repo, folder, or workspace navigable, without moving a thing until you approve. Propose a naming convention, a folder structure, an index or README, and a cleanup plan, shown as a plan first so you can see every move before anything happens. Trigger on "organize this folder", "this repo is a mess", "clean up my workspace", "come up with a naming convention", "where should this live", or any pile of files you can no longer find things in.
---

# Workspace Organizer

## What this does
Takes a workspace you have lost the thread of, a repo, a drive, a folder, and proposes a way to make it navigable: a naming convention so files are predictable, a folder structure so things have a home, an index or README so there is a front door, and a cleanup plan for what to archive or merge. It shows you the entire plan as a proposal. Nothing moves, nothing is renamed, nothing is deleted until you approve it, move by move.

## What you'll need
You do not need to connect anything to get value today. Show the skill what is in the workspace and it proposes the structure. Connect the tools below and it reads the real tree and can execute the approved plan.

- Works today with: a file listing, a directory dump, or a description of what is in there. It proposes a convention and a structure from that.
- More powerful connected to a repo or file store: it reads the actual tree, sizes, and dates, so the cleanup plan is grounded in what is really there.
- Sharper with a knowledge base or index: the new README links into the rest of your context, not just this folder.
- Sharper with git history: it can tell what is genuinely stale from what is just quiet.

## How this runs at your connection level
This skill is never reliant on a connector. It plans from what you show it and gets more precise as you connect the real workspace. It proposes every move; it executes none without approval.

- **Bring your data**: paste the file listing. The skill proposes the naming convention, structure, index, and cleanup plan today. No connection required.
- **Connect your tools**: it reads the true tree and, only after you approve, executes the moves it proposed, one batch at a time.
- **Just exploring**: nothing to organize yet? Get the convention template and a worked example, so you can see the target state before you commit.

Every run ends with the single highest-leverage move, usually the one folder whose fix unlocks the rest.

## Customize this for yourself
This was built for an operator whose workspace grew faster than its structure. Set these to your setup:

| Set this | What it is | Default / Example |
|---|---|---|
| WS_HOME | the workspace being organized | a git repo, a shared drive, a folder |
| NAMING | the convention to adopt | lower-kebab-case, date-prefixed for logs |
| STRUCTURE | the folder scheme | by type, by project, by lifecycle |
| INDEX | the front door | a README that maps the whole tree |
| ARCHIVE_RULE | what gets set aside | untouched > 180 days, superseded files |
| PROTECT | what must never move | anything you name here is off-limits |

The convention and structure are proposals, not decrees. Set the rules; the skill applies them consistently and shows you the result.

## The method

### Read the current state
Inventory what is actually there: the files, the rough types, the obvious duplicates, the folders that became junk drawers. If the real tree is connected, ground this in dates and sizes. If not, work from your listing, and say so.

### Propose a naming convention
One convention, applied consistently, beats five clever ones. Propose a single scheme, lower-kebab-case, date-prefixed logs, type or project prefixes, and show it against your actual filenames so you can see the before and after.

### Propose a folder structure
A home for each kind of thing, shallow enough to navigate and deep enough to separate. Show the proposed tree next to the current one. Every file in the plan has exactly one obvious destination.

### Draft the index
A README that maps the workspace: what each folder holds, where to put a new file, what the conventions are. The index is what keeps the structure from decaying the week after you build it.

### Plan the cleanup, do not perform it
List what to archive, merge, or delete, each with a reason and its current path. This is a plan, presented for approval. Nothing is touched. You approve moves in batches, and a protected path is never in the plan at all.

## Quality gates
- Nothing is moved, renamed, or deleted without your explicit approval, batch by batch. The default action is to propose, never to execute.
- Every proposed move shows its source path and destination. No file changes location invisibly.
- Nothing is ever deleted outright when it can be archived instead. Destructive moves are the last resort and always named as such.
- Protected paths are excluded from the plan entirely. What you mark off-limits is never proposed for a move.

## Output (example)
```
WORKSPACE PLAN · /projects (proposal, nothing moved yet)

NAMING CONVENTION (proposed)
  lower-kebab-case; logs get a YYYY-MM-DD prefix
  before: Final_v2 NOTES.docx   after: onboarding-notes.md

STRUCTURE (proposed tree)
  /projects
    /active        (current work)
    /reference     (facts, specs, playbooks)
    /archive       (superseded, kept for history)
    README.md      (the map)

CLEANUP PLAN (approve per batch, nothing runs yet)
  ARCHIVE  Final_v2 NOTES.docx        (superseded, 210 days untouched)
  MERGE    notes.md + notes-copy.md   (near-duplicate; keep notes.md)
  KEEP     /billing                   (PROTECTED, excluded from all moves)

DO THIS FIRST
  Adopt the naming convention on /active. It makes the rest self-sorting.

(this is a plan. approve moves in batches; nothing has changed.)
```

## Where the inputs come from
ARCHIVE_RULE (180 days) and the naming scheme are defaults, not laws. A fast project archives sooner; a records-heavy one keeps more. The one rule that never bends is that the skill proposes and you dispose, no move happens without your yes. Change the thresholds. Keep the approval gate.

## Make it yours
Fork it. Change the structure to by-project or by-lifecycle, tighten or loosen the archive rule, add a "do not touch" list as long as you like. Cut what does not fit. The point is a workspace you can find things in, reorganized on your terms and never behind your back. Built by an operator. Customize it, break it, make it better.
