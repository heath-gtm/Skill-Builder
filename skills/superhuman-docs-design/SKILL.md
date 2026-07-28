---
name: superhuman-docs-design
description: Build beautiful, high-impact documents and pages in Superhuman Docs (Coda). Design principles, an anti-bullet doctrine (default to layout, not lists), the app-like powers (columns, callouts, card/board views, conditional formatting, covers/icons), argument tables and cards, clickable references, section systems, publishing modes, and how to build each via the Docs MCP. Trigger on "build a Superhuman Doc", "make this doc less boring", "design a Coda page", "beautify this doc", "de-bullet this", or any Superhuman Docs / Coda authoring task.
---

# Building beautiful Superhuman Docs

Superhuman Docs (formerly Coda) is a canvas, not a word processor. A beautiful doc = a strong first screen, clear hierarchy, generous and consistent whitespace, restrained color, and a few app-like moments. **Core rule: let the content supply the color and energy (chips, tables, callouts, images), keep the structure calm and consistent, and default to a designed layout instead of a bullet list.**

## Design principles
1. **Nail the first screen (hero).** Cover photo, title (+ icon only if meaningful), subtitle, then an orienting element (a TL;DR callout, a summary grid, or a table of contents). Never open on a wall of text.
2. **Cover photo = welcome mat + link-unfurl.** Specific to the doc; abstract/high-contrast over literal; avoid generic stock; confirm it reads center-cropped.
3. **Icon only if it adds meaning**; otherwise none.
4. **Whitespace is a feature.** Consistent extra spacing above/below blocks, identical throughout, so it reads as rhythm.
5. **Restraint with color.** Never color body text. Color comes only from content: chips, conditional formatting, callout fills, charts, one accent word in a headline. Gray is a first-class way to de-emphasize.
6. **Consistency.** One alignment (usually Standard), one type system, uniform spacing across every page.
7. **Scannability.** Break long prose with headings-that-group, columns, images, dividers, and pull-quotes. Turn on the Table of Contents to check the auto-outline groups meaning.
8. **Typography with purpose.** Standard font for docs with tables; serif for text-heavy intros. No ALL CAPS. Reserve "Large" text for sparse pages.

## The anti-bullet doctrine (default to layout)
A bullet list is the last resort. It flattens every idea to equal weight and hides structure. Before writing a list, name what it really is and give it the right container:

| If the "list" is really... | Build it as... | With |
| --- | --- | --- |
| A comparison (options vs criteria) | Decision table, winner row shaded | Table + conditional formatting + select pills |
| Steps / a process | Numbered section blocks, or a Step/Owner/Status table (board if a workflow) | Numbered headers, or table grid/board |
| Options being weighed | Decision table (rows=options, cols=criteria) | Table/grid + shaded verdict |
| Key-value facts / metadata | Two-column key-value grid (spec band) | Grid 2-col, or table detail view |
| Pros / cons, before / after | Two-column contrast, gray vs color | Columns (2) or grid |
| Features / capabilities | Row of cards or a callout grid | Table Card view, or columns + callouts |
| References / sources | References table (Source/Type/Finding/Link), Card view | Table + URL column + pills |
| Definitions / glossary | Definition table (term to meaning) | 2-col grid or table |
| A structured argument | 3 narrative cards or a callout stack | Table in Card view, or columns + callouts |
| The overview / TL;DR | Summary table + one high-contrast TL;DR callout | Grid + callout |
| The one key claim | Pull-quote / accent-colored header | Quote block or header with one colored word |

A plain bullet or numbered list is the right call ONLY when items are parallel, equal-weight, short (a few words), attribute-free, and not scanned against criteria. Valid cases: a quick checklist, a short ordered procedure with no per-step metadata, an inline "e.g., a, b, c." The moment an item carries an attribute (status, owner, score, type, source), it is a table, not a bullet.

## Patterns for a structured argument (Problem/Root Cause/Solution, Before/After, decisions)
- **Three narrative cards (or a 3-row table in Card view):** one color-coded stage per card (red Problem, amber Root Cause, green Solution), read left-to-right as a causal chain. The cleanest way to show a 3-beat argument without sub-bullets.
- **Two-column contrast (Before/After, Old way/New way, Us/Them):** gray for the "before," full color for the "after," so the reader feels the delta.
- **Decision table:** rows = options, columns = criteria; conditional-format the winning row and disqualifiers; colored pills for categorical criteria. The single most persuasive move.
- **Callout stack:** claim, then evidence, then implication, each its own callout with escalating color/icon and white space between.
- **Pull-quote:** the one load-bearing sentence as a quote block or oversized header with a single accent word. Once per section.

## References that readers can click into
Default to a **References table**: columns Source, Type (colored pill: Study / Survey / Interview / Data / Article), Key finding (one line), Link (URL rendered as a clickable chip/unfurl). Offer it in **Card view** grouped by Type for an "evidence wall." It separates what a source says from where it lives, and the pills let a reader triage evidence quality at a glance.
Alternatives: a row of URL unfurl cards for 2 to 4 marquee sources; inline @-reference chips for sources cited repeatedly; an "Evidence" callout binding one stat to its source beside the claim; canvas-in-a-cell for a source that needs full notes.
Rule: never fabricate a source or a URL. Verify a claim's source before it goes clickable; if you cannot verify it, flag it or soften the claim.

## Sectioning: guide the reader
Establish one section rhythm and repeat it identically: a small gray **kicker label** (e.g., "SECTION 01 . THE THINKING") over a big header, then content, then a **line separator**, then white space. Number the sections. Put an Outline / Table of Contents block at the top and use it to verify headers group meaning. Collapse only optional depth (appendix, deep methodology), never the core narrative. Icon-tag section headers for wayfinding in a long, multi-page doc.

## Overview / summary without bullets
Open with a **TL;DR callout** holding 2 to 3 short declarative sentences (not bullets), plus a **2-column key-value summary grid** (Problem, Audience, Solution, Status, Owner, Next step) so a skimmer gets the verdict in five seconds and the metadata reads like a spec band. For a multi-part thesis, a **row of cards** (What / How / Solution). For a state report, a **status strip** of conditionally-formatted pills.

## The powers that make a doc feel like an app
- **Cover + icon + subtitle header system.** Subtitle is the search metadata and the URL unfurl line, often the first sentence anyone reads.
- **Columns / side-by-side layout.** Breaks the top-to-bottom waterfall. Parallel content side by side; a blank column to offset instead of centering; unequal widths for a "main + sidebar" read.
- **Callouts.** The fastest way to look intentional; one must-read per page; set style + icon + color.
- **Dividers.** Underused. Isolate sections; pair with white space.
- **Interactive tables + views.** Same table as grid, card, board (group to get kanban), detail, calendar, chart. Hide non-essential columns per view.
- **Conditional formatting.** Auto-color rows/cells by rule; add a small color key above the table.
- **Buttons.** Real actions; one colored primary, the rest white.
- **Charts + embeds; canvas-in-a-cell (a page/table inside a row); collapsible sections; AI columns.**

## Anti-patterns to fix
- Any bulleted list carrying attributes: convert to a table/grid/cards per the doctrine above.
- Wall of text first screen: cover + subtitle + TL;DR, then break with headings/columns/dividers/callouts.
- One top-to-bottom column: use columns; blank column to offset.
- Colored body text or whole headline: content carries color; at most one accent word.
- ALL CAPS: use a gray kicker label + big header instead.
- Generic stock cover; generic icon on everything; inconsistent spacing/alignment.
- Uncited claims: bind each to a References table row.
- Over-collapsing core narrative; all buttons colored; printing/PDF instead of sharing the live link.

## Building via the Superhuman Docs MCP (tool mapping)
- **page_update:** coverPhoto.url + showCoverPhoto; icon + showIcon; subtitle + showSubtitle; pageWidth (narrow/wide/full, consistent); title; showAuthor (byline).
- **content_modify** insert_element: callout (Info/Tip/Alert + icon + color), divider (Default/Thick/Dashed/Dotted/Wavy), image, codeblock, markdown (# headings, **bold**, *italic*, tables, - lists). Inline color/highlight via `<color:Red>...</color>` and `<color: bg:Yellow>...</color>`. set_collapsible on headings/tables; replace_element_text / delete_element for edits. Batch ops run in document order; to stack several blocks after one anchor, send them in order (they auto-reorder A,B,C after X).
- **table_create:** typed columns that carry design: select-list pills WITH colors, checkbox, currency, date, scale, slider displayType "Progress" (bar), person, link as Card/Embed, canvas (page-in-a-cell), button. Seed rows inline. Rows are arrays of cell values in column order.
- **table_view_manage:** viewLayout card/board/detail/calendar/chart; groups (top grouping on a card view = kanban board); sorts; conditionalFormats (condition like "Done = true"); hide columns; add extra views as tabs.
- **table_columns_manage:** add/retype columns and formulas.
- **Columns caveat:** the MCP cannot create side-by-side `/columns` blocks. To get the "three cards" effect for an argument or overview, build a TABLE and switch it to **Card view** (table_view_manage viewLayout card). Tables + card/board views are the column substitute. Arrange true columns in the editor only if needed.
- After changing a column type, rewrite affected cell values and verify with table_rows_read.

## Brand (for styled deliverables carrying the Superhuman look)
Origin system: warm cream chrome `#f7f5f2` framing a white paper canvas `#ffffff`; ink `#292827`; purple `#714cb6` (hover `#533192`) used sparingly; warm, brown-tinted neutrals; Super Sans (public fallback Inter); 4px grid; soft corners (8 to 16px; pills 999). Purple is a rationed accent, never on every element.

## Build checklist
1. Cover (specific, crop-tested) + icon (only if meaningful) + a 1 to 2 line subtitle.
2. First screen = hero + a TL;DR callout or summary grid or TOC; no opening text wall.
3. One alignment + uniform spacing across every page.
4. Default to layout, not lists: run every bullet list through the anti-bullet doctrine.
5. Arguments become narrative cards, a decision table, or a callout stack, never sub-bullets.
6. Every external claim gets a row in a clickable References table (verified source + link).
7. Section rhythm: gray kicker over big header, content, line separator, white space, repeated.
8. Color comes from content only (pills, conditional formatting, callout fills, one accent word).
9. Tables: conditional formatting + a color key; hide extra columns; card/board view where it fits.
10. Publish: pick the mode (View/Play/Edit), set cover/subtitle/byline + discoverability, preview, then ship.

## Make it yours
Fork it. Swap the brand block for your own palette and type, change the checklist to your house style, add the patterns your team reuses. The point is not to build someone else's doc. It is to build yours, faster and sharper, so the doc itself becomes the proof. Built by an operator. Customize it, break it, make it better.
