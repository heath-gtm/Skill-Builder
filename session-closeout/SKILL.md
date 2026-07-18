---
name: session-closeout
version: 1.0.0
description: >
  Built GTM session close-out and QA. Run at the end of any working session, or
  mid-session before a risky handoff, to lock the work up: verify every change is
  committed, pushed, and green; confirm the deploy is live and runs without this
  machine; verify the work functionally; AND run the Skills + Schedules Impact
  Review so no skill, scheduled task, or process doc is left stale by what
  changed this session. Trigger on "close out the session", "session QA",
  "lock it up", "wrap up and QA", "close-out checklist", "are we good to close",
  "run the close-out", or any end-of-session request to review and finalize work.
license: MIT
compatibility: cowork claude-code opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
---

# Session Close-Out (Built GTM)

Close the session on a good note. Nothing half-shipped, nothing stale, and the next session resumes instantly.

---

## 1. Ship state

- Every change committed and pushed. Show `git status` clean and confirm the branch is not behind.
- Typecheck or build passes. Never claim verified if you could not actually run it. Say what you verified and what you could not.
- The deploy reached READY, not ERROR. If you could not confirm, say so plainly instead of assuming.
- Zero literal em dashes in anything committed.

## 2. Runs without this machine

Audit that what you built runs on its own in production: APIs, CI, env vars. NOTHING may depend on this session, a local script, a session-only CLI, or a desktop agent doing the work by hand. If something only works because you ran it here, that is a finding, not a feature.

## 3. Functional and visual verification

Verify the actual behavior, not just that the code compiles. Where there is a UI, look at it. Where there is a loop, run one pass end to end.

---

## 4. Skills + Schedules Impact Review (REQUIRED)

This is the step that gets skipped and causes drift. Any session that changes a process, a template, a workflow, or a data model leaves encoded copies of the OLD process behind. Find them and fix them.

Ask, and answer explicitly:

1. **What process, template, rule, or data model changed this session?** Write it in one line.
2. **Which skills encode that process?** Search the skills repo (`heath-gtm/Skill-Builder`) and the installed skill list for anything describing the old behavior. A skill that describes a superseded model is now actively wrong, not merely outdated.
3. **Which scheduled tasks or launchers encode it?** List scheduled tasks and read the SKILL.md of any that touch the changed area. Launchers that hand an agent a stale process will reproduce the stale process.
4. **Which process docs or memory files encode it?** The canonical spec, the design system doc, and the relevant memory entries.
5. **For each hit, decide: update, supersede, or retire.** Never leave two live copies of a process. If two files disagree, name which one wins, in the file itself.

Then follow the update protocol:

- **Update the GitHub repo FIRST.** The repo is the source of truth for skills. Commit the change there.
- **Then hand Heath a manual copy** to save and replace his local copy, since plugin and scheduled skill files are read-only from the session.
- **Say exactly which files he needs to replace, and where they go.**

Report the review as a short table: what changed, what it impacted, what you updated, what still needs his hand.

---

## 5. Handback

Close with:
- A short summary of the outcome, not a recap of every step.
- Live links to what shipped.
- Open items, honestly stated, including anything you could not verify.
- The rollback path.
- Updated memory or context notes so the next session resumes cold-start-free.
