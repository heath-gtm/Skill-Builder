# mixmax-leader-update-slides

End-of-month and end-of-quarter Update Slides for the Mixmax CEO's board/exec deck.

## What this plugin produces

Two slide-by-slide HTML briefs per close — one for Sales (Heath), one for CS (Heather). Each brief mirrors the deck the CEO writes himself, with one chart + drafted bullets + Writing Guidance per slide. The CEO copies what he wants and ignores what he doesn't.

- Monthly: 5 slides (TLDR, TOFU, Conversion, Bookings, Projects)
- Quarterly: 6 slides (the 5 above + Quarter-Over-Quarter Pacing + Year-Ahead Outlook)

Files land at:

- `Revenue Reviews/Leader Weekly/Update Slides/Sales/{period}.html`
- `Revenue Reviews/Leader Weekly/Update Slides/CS/{period}.html`

…and are published to GitHub Pages under `${GITHUB_PAGES_URL}/reports/leader-weekly/update-slides/{sales,cs}/{period}.html`.

## Skills

- **`leader-update-slides-setup`** — one-time installer. Bundles the spec into your working folder and registers the `leader-ceo-updates` scheduled task.
- **`leader-update-slides-runbook`** — reference for ad-hoc generation, single-slide regeneration, and back-period rendering.

## Dependencies

- **`mixmax-publishing-core`** — required. Provides the GitHub publishing config used to push to Pages.
- A previously-approved Mixmax Monthly or Quarterly Revenue Report. Update Slides inherit numbers; they never re-derive from the Gen 1 sheet.

## Install

1. Install `mixmax-publishing-core` first and run `publishing-config-setup`.
2. Install this plugin.
3. Run `leader-update-slides-setup`.
4. After every monthly or quarterly close (and only after the base report is approved), trigger the `leader-ceo-updates` scheduled task from the Cowork panel and pass the period label.

## Spec

Canonical spec ships in `references/CEO_Update_Addendum.md` and is copied into `Revenue Reviews/specs/CEO_Update_Addendum.md` at setup time. Edit the local copy for org-specific tweaks; the bundled copy is the upstream baseline.
