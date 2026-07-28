---
name: superhuman-docs-design
description: Build beautiful, well-designed documents and pages in Superhuman Docs (Coda). Design principles, the app-like powers (columns, callouts, card/board views, conditional formatting, covers/icons), publishing modes, anti-patterns, and how to build each via the Docs MCP. Trigger on "build a Superhuman Doc", "make this doc less boring", "design a Coda page", "beautify this doc", or any Superhuman Docs / Coda authoring task.
---

# Building beautiful Superhuman Docs

Superhuman Docs (formerly Coda) is a canvas, not a word processor. A beautiful doc = a strong first screen, clear hierarchy, generous and consistent whitespace, restrained color, and a few app-like moments. **Core rule: let the content supply the color and energy; keep the structure calm and consistent.**

## Design principles
1. **Nail the first screen (hero).** Cover photo, title (+ icon only if meaningful), subtitle, then an orienting element (a purpose callout or a table of contents). Never open on a wall of text.
2. **Cover photo = welcome mat + link-unfurl.** Pick something specific to the doc; favor abstract/high-contrast/patterned over literal; avoid generic stock (laptops, handshakes); confirm it reads well center-cropped.
3. **Icon only if it adds meaning**; otherwise none. Do not put a generic icon on everything.
4. **Whitespace is a feature.** Add consistent extra spacing above/below blocks and keep the amount identical throughout so it reads as rhythm, not randomness.
5. **Restraint with color.** Never color body text. Emphasize with bold/italic/highlight. In a headline, color at most one word. Let images, colored chips, charts, and one key button carry the color. Gray is a valid way to de-emphasize a heading.
6. **Consistency.** One content alignment (usually Standard), one type system, uniform spacing across every page. Mixing alignments makes the nav jump.
7. **Scannability.** Break long prose with headings-that-group, images, dividers, and pull-quotes. Validate hierarchy by turning on the Table of Contents: if the auto-outline reads sensibly, your headings are right.
8. **Typography with purpose.** Standard font for docs with tables; serif for text-heavy intro pages. No ALL CAPS. Reserve "Large" text for pages with little copy.

## The powers that make a doc feel like an app
- **Cover + icon + subtitle header system.** Subtitle doubles as the search metadata and the URL-unfurl line, so it is often the first sentence anyone reads.
- **Columns / side-by-side layout (biggest unlock).** Breaks the top-to-bottom waterfall that makes docs feel like plain documents. Put parallel things side by side (text + image, two tables, two checklists, caption + visual, a mood board). Use a blank/empty column to offset content instead of always centering.
- **Callouts.** The fastest way to look intentional. One must-read callout per page (a caveat, setup instruction, or the page purpose). Set a style, color, and icon.
- **Dividers.** Underused. Isolate conceptual sections; responsive inside columns.
- **Interactive tables + multiple views.** The same table shown as grid, **card**, **board** (kanban), or **detail**. Cards are attractive and give click-to-expand. Hide non-essential columns per view.
- **Conditional formatting.** Auto-color rows/cells by rule (e.g., overdue = red). Add a small color "key" above the table.
- **Buttons.** Real actions (add row, notify, advance, run a Pack action). One colored primary, the rest white; add an icon only if the icon alone communicates it; avoid red/orange unless destructive.
- **Charts + embeds.** Live color and dimension; URL cards for clean references.
- **Canvas columns + subpages.** A page or whole table inside a single row; nest pages for a wiki/hierarchy.
- **Collapsible sections.** Only collapse content you are fine with people skipping; default to open.
- **AI columns / Docs AI.** Generate or summarize per row from a prompt.

## Layout patterns
- **Hero:** cover, then title (+ icon), then subtitle, then an orienting callout or TOC.
- **Section headers group, not decorate.** Add an emoji to key headers in long pages.
- **Columns for anything parallel;** blank column to offset. Adjust width with the handle.
- **Cards** for browsable/gallery/options; **board** for status/stage; **table** for dense data (hide extra columns).
- **One callout per page** for the must-read; **dividers + whitespace** between sections.

## Anti-patterns to fix
- Wall of text first screen: add cover + subtitle, then break with heading/image/divider/callout.
- One top-to-bottom column: use columns; blank column to offset.
- Colored body text or whole headline: bold/highlight; one word max; content carries color.
- ALL CAPS: use headings/bold/callout.
- Generic stock cover: doc-specific, abstract, high-contrast, crop-tested.
- Inconsistent spacing/alignment: one alignment (Standard), one spacing amount everywhere.
- Generic icon on everything: icon only when meaningful.
- Plain sprawling grid: conditional formatting + color key; hide columns; card/board view.
- Blocks crammed together: dividers + consistent whitespace.
- Over-collapsing to look tidy: only collapse skippable content.
- All buttons colored / random icons: one colored primary; icon only if self-explanatory.
- Printing/PDF a doc: publish or share the live link; the doc is the deliverable.

## Publishing
- Set the three header assets first: **cover** (unfurl), **subtitle** (metadata/unfurl), **byline** (maker credit + discoverability).
- Organize with nested pages; move extraneous content off the main path.
- Choose the interaction mode: **View** (read-only; articles/manuals), **Play** (interact but unsaved; calculators/quizzes/worksheets), **Edit** (saved table contributions; voting/brainstorm).
- Toggle discoverable (SEO/gallery) + category; show cover/subtitle; optional top-nav tabs; custom URL/domain; offer a "Copy this doc" button; preview, then ship (edits propagate in minutes; Google indexing about a week).

## Building via the Superhuman Docs MCP (tool mapping)
- **page_update** to set coverPhoto.url + showCoverPhoto; icon + showIcon; subtitle + showSubtitle; pageWidth (narrow/wide/full, keep consistent); title; showAuthor (byline).
- **content_modify** insert_element for callout (style Info/Tip/Alert/Critical + icon + color), divider (Default/Thick/Dashed/Dotted/Wavy), image, codeblock, markdown (# headings, **bold**, *italic*, - lists). Inline color/highlight via `<color:Red>...</color>` and `<color: bg:Yellow>...</color>`. set_collapsible on headings/tables; replace_element_text / delete_element for edits.
- **table_create** for typed columns that carry design: select-list pills WITH colors (status/category), checkbox, currency, date, scale/rating, slider with displayType "Progress" (a progress bar), person, link shown as Card/Embed, canvas (page-in-a-cell), button (actionFormula + color). Seed rows inline.
- **table_view_manage** for viewLayout card/board/detail/calendar/chart; groups (collapsible sections); sorts; conditionalFormats (auto-color rows/cells; condition like "Done = true"); hide columns; add extra views as tabs.
- **table_columns_manage** to add/retype columns and formulas.
- **Ordering tip:** to place several new blocks in a fixed order at one anchor, insert them in REVERSE order, each anchored "after {anchorId}", so each lands immediately after the anchor and pushes the prior insert down.
- **Columns / side-by-side layout:** not currently creatable through the MCP content blocks. Build the blocks with the MCP, then arrange them side by side in the editor (`/column` or drag one block beside another). Verify current MCP support before relying on it.
- After changing a column type, existing cell values may need rewriting (e.g., a select converted to a checkbox needs boolean values); verify with table_rows_read.

## Brand (for styled deliverables carrying the Superhuman look)
Origin system: warm cream chrome `#f7f5f2` framing a white paper canvas `#ffffff`; ink `#292827`; purple `#714cb6` (hover `#533192`) used sparingly; warm, brown-tinted neutrals (not blue-gray); Super Sans (public fallback Inter); 4px spacing grid; soft corners (8 to 16px; pills 999). Purple is a rationed accent, never on every element.

## Build checklist
1. Cover (specific, crop-tested) + icon (only if meaningful) + a 1 to 2 line subtitle.
2. First screen = hero + an orienting callout or TOC; no opening text wall.
3. One alignment + uniform spacing across every page.
4. Break long text (headings that group, images, dividers, pull-quotes).
5. Columns for parallel content; a blank column to offset.
6. One callout per page for the must-read; dividers between sections.
7. Color comes from content only (images, pills, charts, one key button).
8. Tables: conditional formatting + a color key; hide extra columns; card/board view where it fits.
9. Add at least one app-like moment (a button, a reaction, or a card view).
10. Publish: pick the mode (View/Play/Edit), set cover/subtitle/byline + discoverability, preview, then ship.

## Make it yours
Fork it. Swap the brand block for your own palette and type, change the checklist to your house style, add the patterns your team reuses. The point is not to build someone else's doc. It is to build yours, faster and sharper, so the doc itself becomes the proof. Built by an operator. Customize it, break it, make it better.
