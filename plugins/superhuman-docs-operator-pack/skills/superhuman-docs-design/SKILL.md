---
name: superhuman-docs-design
description: Build beautiful, senior-level documents and pages in Superhuman Docs (Coda). The full design system: composition and visual hierarchy, a restrained color and background system, section and divider rhythm, a type scale, an anti-bullet doctrine, the simple-card / rich-detail pattern, timelines and progress visuals, the two-pass MCP-then-UI build model with an explicit UI finishing checklist, and an AI-reviews-it-in-Chrome step. Trigger on "build a Superhuman Doc", "design a Coda doc or page", "make this doc less boring", "beautify this doc", "de-bullet this", "lay out this section", or any Superhuman Docs / Coda authoring or design task.
---

# Building beautiful Superhuman Docs

Superhuman Docs (formerly Coda) is a canvas, not a word processor. Senior design is contrast and restraint: one focal point per screen, big type jumps, color used as a signal not decoration, a repeated section rhythm, and generous consistent whitespace. **Core rule: content supplies the color and energy (images, chips, charts, one button); structure stays calm; default to a designed layout instead of a bullet list.** A page is read in a Z or F pattern, so decide what the eye hits first and make everything else recede.

## Read first: the two-pass build model
You cannot build a senior doc through the MCP alone, and the MCP cannot see its own rendered output. So every build is two passes plus a review:
- **Pass 1, MCP (substance):** pages, cover/icon/subtitle, headings, callouts, dividers, tables and all their views, conditional formatting, inline formulas, canvas-in-a-cell content, seeded data.
- **Pass 2, editor UI (composition), about 10 minutes:** side-by-side columns, background bands, text sizes and eyebrow labels, card-face polish, live AI columns, timeline dependencies, publish settings. These are editor gestures the API cannot do. The explicit checklist is at the end of this skill.
- **Pass 3, AI review in Chrome:** open the live doc URL in a browser, screenshot and read the rendered page, critique it against this skill, then fix. Never trust a build you have not looked at.

## First screen (the hero lockup)
cover photo, then icon (only if it adds meaning), then H1 title, then subtitle, then one orienting element (a thesis callout or the table of contents). Never open on a wall of text.
- **Cover = welcome mat and URL unfurl.** Specific to the doc, not generic stock; avoid literal laptop/handshake shots; favor high contrast, colors, or patterns; it may be center-cropped, so check the crop.
- **Subtitle sells the doc.** One or two sentences; it doubles as the Google metadata and the text in the link unfurl, so it is often the first thing anyone reads.
- **Byline on.** Credit the maker; it adds authority and trust.

## Layout and visual hierarchy
- **One focal point per screen.** One thing wins above the fold; never two competing heroes.
- **Grid thinking (think in 12 units).** Three reusable splits: **50/50** (comparison, before/after), **66/34 main + rail** (body plus a margin rail for metadata, notes, status, or a CTA; the workhorse editorial layout), **75/25** (content plus a thin sidebar). Put the most important column **first** in source order so it survives mobile reflow.
- **Big jumps, not nudges.** Make one thing clearly big and the rest small; 1 to 2 unit differences read as mistakes.
- **Left-align body and hold it.** Center only tiny hero lockups (title plus subtitle plus one line), never paragraphs. Mixed alignment is the top amateur tell.
- **Whitespace is the cheapest luxury signal.** One consistent extra-space amount, applied identically, reads as rhythm.

Named patterns: **Hero Lockup** (first screen), **Main + Rail 66/34** (reports, planners, briefs), **Split Compare 50/50** (before/after, A vs B), **Card Wall** (a table in card view for peer items), **Zebra Sections** (alternating full-width band and plain canvas for long docs), **Kicker Stack** (eyebrow, H2, body: the standard section opener).

## Color and background system
- **60 / 30 / 10.** About 60% neutral canvas, 30% secondary neutral (gray tints, rails, table shading), 10% accent plus semantic. Color should feel scarce.
- **One accent, rationed.** A single hue, only on what the reader should notice or act on: the hero callout, key links or buttons, one active label, the closing CTA. Everywhere means nowhere.
- **Semantic color is fixed and literal.** Red = risk / overdue / blocked, Amber = caution / at-risk / pending, Green = good / done / on-track. Never reuse a semantic hue as the brand accent.
- **Color comes from content.** Bring color in through images, multicolored chips, charts, and key buttons. Do not color paragraph text (use the highlighter, or bold and italics). In a headline, color at most one word (it is already bold and big). Gray is a color, and it is the right way to make a heading recede.
- **Backgrounds and bands: there is no native page-background color in Coda.** Build bands from **full-width callouts** and **shaded grids or table rows**. Use a pale fill with dark text and a saturated hue only as a thin edge or icon. Tint about one section in five; reserve a genuinely saturated band for one or two real moments (the thesis, the CTA). Light canvas by default for reading; dark canvas only for short presentation-style pages, and never mix within a doc.

Restrained recipe (hex is design intent; in Coda pick the palest swatch consistently, since the palette is a fixed swatch set, not a hex field): canvas `#FFFFFF` or warm `#FAF9F7`; ink `#1A1A1A`; muted gray `#6B7280`; hairline `#E5E7EB`; section tint `#F7F5F2`; one accent (e.g. `#2563EB`) with tint `#EFF4FF`; semantic green `#15803D` on `#ECFDF3`, amber `#B45309` on `#FFF7ED`, red `#B42318` on `#FEF3F2`. Max about three fill colors visible on any one screen.

## Sectioning and dividers
Repeat one rhythm for every major section so the doc has a predictable beat:
```
[blank line]
EYEBROW LABEL          (small, uppercase, muted or accent)
## Section Title       (H2, optionally numbered 01 / 02 / 03)
one-line section summary (muted)
[content]
[blank line]
divider                (only between peer sections)
```
Weight ladder, lightest to heaviest: **whitespace** (between related subsections), **thin divider** (between peer sections), **eyebrow label**, **numbered sections**, **section-opener callout**, **full-width colored band** (one or two per doc, for the biggest moments). Do not stack separators at one boundary. Always turn on the **Outline / TOC** for any doc longer than two screens, and keep a consistent header-icon vocabulary. Collapse (fold) only content you are fine with people skipping, never the core narrative.

## Typography
Six roles only: **H1 / H2 / H3 / Body / Caption / Eyebrow.**
- **H1 exactly once** (the title). A second H1 means a new page.
- **Big jumps** between levels; if H2 and H3 look alike, the hierarchy collapses.
- **Line length 60 to 80 characters** (this is why main + rail matters; on full-width pages keep body in a column, not spanning the canvas).
- **Leading:** body 1.5 to 1.6, headings 1.2 to 1.3.
- **Emphasis** = bold on one phrase, or accent color. **De-emphasis** = muted gray and smaller (captions, metadata). De-emphasize as deliberately as you emphasize.
- John's rules: **Standard font for pages with tables, Serif for text-heavy intro pages**; **Large text only when the page has little copy**; **no ALL CAPS**; headers must **group information**, not decorate.
- Coda note: the canvas scale is fixed to heading levels, so keep the relationships (big jumps, loose body leading, muted secondary text) even though you cannot type arbitrary sizes. Text size (Large / Small) and the true eyebrow style are UI-only.

## The anti-bullet doctrine
A bullet list is the last resort; it flattens every idea to equal weight and hides structure. Name what the list really is and give it the right container:

| If the "list" is really... | Build it as... | With |
| --- | --- | --- |
| A comparison (options vs criteria) | Decision table, winner row shaded | Table + conditional formatting + pills |
| Steps / a process | Numbered sections, or a Step/Owner/Status table (board if a workflow) | Numbered headers, or table grid/board |
| Options being weighed | Decision table (rows=options, cols=criteria) | Table/grid + shaded verdict |
| Key-value facts / metadata | Two-column key-value grid (spec band) | Grid 2-col, or detail view |
| Pros / cons, before / after | Two-column contrast, gray vs color | Columns (UI) or grid |
| Features / capabilities | Card wall or a callout grid | Table card view, or columns + callouts |
| References / sources | References table (Source/Type/Finding/Link), card view | Table + link column + pills |
| Definitions / glossary | Definition table (term to meaning) | 2-col grid or table |
| A structured argument | Simple cards with rich detail, or a callout stack | Table in card view, or callouts |
| The overview / TL;DR | Summary grid + one high-contrast callout | Grid + callout |
| The one key claim | Pull-quote / accent-colored header | Quote block or header with one colored word |

A plain bullet or numbered list is right only when items are parallel, equal-weight, short, attribute-free, and not scanned against criteria (a quick checklist, a short ordered procedure, an inline "e.g., a, b, c"). The moment an item carries an attribute (status, owner, score, type, source), it is a table.

## The simple-card / rich-detail pattern
The senior way to show cards: a **minimal face, all depth in the detail.**
- **Face = identity plus state:** the display column (a label) and one colored select pill; one or two lines. Nothing else.
- **Detail = evidence plus input:** an AI summary, a canvas body, a small sources subtable, and any input fields (checkbox, date, person, text).
- **Build:** `table_create` with the face columns plus detail columns; `table_view_manage` to card layout with `hideColumnIds` covering every detail column (they vanish from the face but appear when a card is opened). For a rich body, read the row to get the cell's canvas URI and `content_modify` it like any page. An AI summary is a UI AI column, or write the text into a plain-text or canvas cell yourself.
Rule of thumb: put identity and state on the face; put evidence and input in the detail. Never explode the detail onto the page.

## Argument patterns (problem / root cause / solution, before/after, decisions)
Simple cards with rich detail (above) is the default. Others: **decision table** with a conditionally-formatted winner and colored pills (the most persuasive move); **callout stack** (claim, then evidence, then implication, each its own callout); **two-column contrast** (gray "before", full-color "after"); **pull-quote** (the one load-bearing sentence as a quote or big header with one accent word).

## References that click
Default to a **References table**: Source, Type (colored pill: Study / Survey / Interview / Data / Article), Key finding (one line), Link (a clickable URL or markdown link). Offer it in **card view** grouped by Type. Never fabricate a source or URL; verify a claim's source before it goes clickable, and if you cannot verify it, flag it or soften the claim.

## The two visuals
- **Timeline / gantt:** needs a **start and end date** per row (or start plus duration). Build the table with date columns, then a **timeline** view **grouped by phase**; a row with a start but no end renders as a **milestone**. Dependencies can only be wired in the timeline view in the editor.
- **Percent complete:** the primary readout is a **formula-driven Progress bar** column (a slider with displayType Progress, driven by `Round(Tasks.Filter(Done).Count() / Tasks.Count() * 100)`); pair it with a **big-number plus bar summary band** at the top of the section (inline `<formula>` tags). A **donut/pie** of done vs remaining is the dashboard option; a **percent-by-phase stacked bar** shows distribution.

## Navigation, usability, and fun
- **Navigation:** sidebar for wikis (many pages) and ordered processes (steps in order); top nav for fewer pages and distinct categories. Turning pages into top-nav tabs is what makes a multi-page doc feel like a website.
- **Scannability:** break walls of text with images, charts, dividers, headlines, and columns.
- **Interaction mode:** View (articles, manuals, reports), Play (interact but unsaved: calculators, quizzes, timers, checkboxes), Edit (saved contributions: voting, RSVP, add-a-row). Pick deliberately.
- **Make it fun:** interactive buttons, card click-to-expand, filters on tables, multicolored chips, a big button to move to the next section instead of a footer.

## Publishing frame
Set cover, subtitle, and byline first. Organize with nested pages and collapse the extraneous. Keep margins and alignment clean. Choose the interaction mode. Turn on discoverability with a doc category and the right audience for anything public; leave it off for shared-but-unlisted. Use a clean custom URL (or custom domain for brand-facing docs), and "allow others to copy" only for templates. Preview, then publish. The live doc is the deliverable; never print or PDF it.

## Start from a template (template-first)
Default to starting from a template, not a blank canvas. A template kills the blank-page stall, removes the format debate, and bakes in the hierarchy, color budget, and anti-bullet rules, so the builder spends cycles on the thinking, not the layout. The field agrees: focused single-purpose templates beat all-in-one sprawl.
Rule: **template for the frame, blank-minded for the content.** The template decides structure, section order, and which patterns to use. It never decides the substance. Use a template when the doc-type recurs and the reader expects a known shape (launch plan, QBR, account plan, weekly update). Go closer to blank when the doc is a one-off argument whose shape is the idea (a novel strategy memo).
The move that avoids generic output: after picking the template, run an **objective-first prune** - delete every section that does not ladder to this doc's purpose, and add the one section this situation demands. A template you never subtract from is a straitjacket; a template you always prune is a head start.
Starter set (full specs in `templates/`): Launch Plan, QBR, PRD / one-pager, Strategy Memo, Account Plan, Meeting Notes to Action Items, Weekly Update, Team Hub. Each maps to the pattern language (hero, main+rail, card wall, decision table, timeline, references).

## Building via the Superhuman Docs MCP (tool mapping)
- **page_update:** coverPhoto.url + showCoverPhoto, icon + showIcon, subtitle + showSubtitle, pageWidth (narrow/wide/full, kept consistent), title, showAuthor.
- **content_modify** insert_element: callout, divider, image, codeblock, markdown (headings, bold/italic, tables, lists). Inline color/highlight via `<color:Red>...</color>` and `<color: bg:Yellow>...</color>`. set_collapsible on headings/tables. Batches run in document order and are capped at 10 operations. Inline live values via `<formula>...</formula>`.
- **table_create / table_columns_manage:** typed columns (select pills with colors, checkbox, currency, date [format token dp], scale, slider displayType Progress, person, link, canvas, button). Rows are arrays of cell values in column order.
- **table_view_manage:** viewLayout card / board / detail / timeline / calendar / chart; groups (top grouping on a card view = kanban); sorts; conditionalFormats; hideColumnIds; extra tab views; chartOptions (pieDisplayMode Donut, stacking, series).
- **Populate a canvas-in-a-cell:** read the row for its canvas URI, then content_modify that URI.

## Capability map: MCP vs UI
MCP can do: pages and headers; cover/icon/subtitle/width; callouts (with color and icon) and dividers; markdown, inline color, inline formulas; set_collapsible; tables, typed columns, all view layouts, grouping, sorts, conditional formatting, hidden columns, extra views; canvas-in-a-cell population; writing computed text into a cell.
UI-only (the finishing pass): **side-by-side columns** (main + rail, unequal widths); **page background / section bands beyond callouts and shaded tables** (Coda has no page-background setting at all); **text size (Large/Small) and the true eyebrow style**; **native AI columns**; **card-face fine settings** (line count, cover layout, labels); the **row-layout arrangement** editor (you can still create a detail view and hide/reorder columns via MCP); **timeline dependencies**; all **publish settings**.

## Human in the loop: the UI finishing pass (try Docs AI first)
Some senior touches cannot be built through the MCP; a human applies them in the editor. For each, **try Docs AI first** by pasting the prompt below, then fall back to the manual gesture if Docs AI cannot do it. Verify the result by looking at the rendered doc (Pass 3). Record which touches Docs AI reliably handles so the finishing pass shrinks over time.

| UI-only touch | Why it matters | Docs AI prompt to try | Manual fallback |
| --- | --- | --- | --- |
| Side-by-side columns (main + rail) | The #1 senior move; breaks the vertical stack | "Rearrange this section into two side-by-side columns: a wide left column (about two-thirds) for the main content and a narrow right column (about one-third) for the callout and metadata." (Tested 2026-07: Docs AI declines this and confirms columns are UI-only.) | Type /columns, or drag one block beside another, then drag the divider for a 2:1 split |
| Large / hero text | Makes the title and the key number dominate | "Make the page title and the percent-complete number large display text." | Select the text, set size to Large |
| Native AI column | A live summary that refreshes as inputs change | "Add an AI column to this table that summarizes the Sources column in one sentence and updates when the sources change." | Add column, choose type AI, Summarize prompt referencing the field |
| Colored section band | A real background moment for the thesis or CTA | "Wrap this section in a full-width colored callout band as a section background." | Insert a full-width callout and set its color |
| Card-face polish | Keeps card faces minimal | "In this card view, show only the label and the status pill on the card face and set it to two lines." | Card view options: line count, cover image, hidden fields |
| Timeline dependencies | Moving one task shifts the ones after it | "In this timeline, make milestone B depend on milestone A so moving A shifts B." | Timeline view: draw the dependency between the two bars |
| Publish frame | Turns a draft into a product | "Publish this doc in View mode, show the cover and subtitle, and turn on discoverability under the chosen category." | Share, Publish tab: mode, appearance, discoverability, custom URL |

Rule: try Docs AI, look at the result, and if it did not land, do the manual gesture. The one touch that would change everything if Docs AI can do it is **side-by-side columns**, so test that first.

**Tested finding (columns).** Docs AI will not create true side-by-side columns; it confirms they are a manual editor gesture, so columns stay in the human pass. MCP approximation: a one-row, two-column **grid** whose cells hold text and callouts gives a genuine side-by-side layout, but a live card or table cannot be nested inside a cell (it renders as a placeholder), so a main + rail that must contain live tables stays manual.

## Pass 3: AI review in Chrome
Open the live doc URL in Chrome, screenshot each screen and read the rendered page, then grade it against this skill: one focal point per screen, color discipline (accent rationed, semantic only for status, pale fills), section rhythm repeated, type hierarchy with big jumps, card faces minimal, no walls of text, no orphaned bullets. Fix what the MCP can fix, list the UI items, and repeat until it passes.

## Build checklist
1. Hero: cover + (meaningful) icon + one-line subtitle; a thesis callout or TOC; no opening text wall.
2. One focal point per screen; one alignment; one spacing amount.
3. Section rhythm (eyebrow, H2, summary, content, divider) repeated identically.
4. Default to layout, not lists; run every bullet through the anti-bullet doctrine.
5. Cards: minimal face, rich detail; never explode detail onto the page.
6. Color from content; 60/30/10; one accent; semantic only for status; pale fills; bands from callouts.
7. Every external claim gets a verified row in a References table.
8. The two visuals where relevant: a real timeline and a progress readout, both off one data table.
9. Run the UI finishing pass, then review it in Chrome.
10. Publish: mode, cover/subtitle/byline, discoverability, clean URL.

## Make it yours
Fork it. Swap the color recipe for your palette, change the checklist to your house style, add the patterns your team reuses. The point is not to build someone else's doc; it is to build yours, faster and sharper, so the doc itself becomes the proof. Built by an operator. Customize it, break it, make it better.
