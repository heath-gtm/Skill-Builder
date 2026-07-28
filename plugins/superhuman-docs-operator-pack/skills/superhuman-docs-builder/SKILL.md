---
name: superhuman-docs-builder
description: The engineering companion to superhuman-docs-design: how to actually build a document in Superhuman Docs (Coda) through the Docs MCP. Tool inventory and build order, the gotchas that bite (batch caps, row-as-array writes, the date format token, select-vs-checkbox, card-face hiding, canvas-in-a-cell), Coda Formula Language traps, and the two-pass handoff to the human UI finishing pass. Trigger on "build this doc via the MCP", "create the tables and views", "the MCP call failed", "how do I add a timeline or progress or card view", "why did my table write break", "seed the rows", or any hands-on Superhuman Docs / Coda MCP build task.
---

# Building in Superhuman Docs through the MCP

This is the mechanics companion to `superhuman-docs-design` (which is the taste). Design decides what to build; this decides how to build it without the calls failing. Core stance: the MCP builds the substance (pages, tables, views, formulas, content); a human finishes the composition (columns, text sizes, bands, AI columns, dependencies, publish). Never pretend the API does the last 10 percent.

## Pre-flight
1. Confirm the Docs MCP is connected and call `tool_guide` (topics: getting_started, page, table, formula) once to confirm current tool shapes.
2. `document_create` for a new doc; keep the returned docId and browserLink. Title the first page with `page_update` (an H1 in content does not set the page title).
3. If you have a doc URL, `url_convert` decode it to the superhuman:// URIs; pass `scope` matching the next tool.
4. Response URIs are doc-relative (pages/..., tables/..., canvases/...); rebuild a full URI by prepending `superhuman://docs/{docId}/`.

## The tools
- **page_update:** coverPhoto.url + showCoverPhoto, icon + showIcon, subtitle + showSubtitle, pageWidth, title, showAuthor.
- **content_modify** (insert_element / replace / delete / set_collapsible): blockTypes markdown, callout, codeblock, divider, image. Inline color `<color:Red>...</color>` and highlight `<color: bg:Yellow>...</color>`. Inline live values `<formula>...</formula>`.
- **table_create / table_columns_manage:** typed columns; **rows are arrays of cell values in column order.**
- **table_view_manage:** viewLayout card / board / detail / timeline / calendar / chart; groups; sorts; conditionalFormats; hideColumnIds; chartOptions.
- **table_rows_manage / table_rows_read; content_read; search; name_match.**

## Gotchas that will bite you (learned the hard way)
- **content_modify batches cap at 10 operations.** Split larger edits. Send ops in document order; do deletes before inserts.
- **insertPosition uses the element id** as it appears in page markdown (`grid-...`, `cl-...`, `eca-...`), NOT the full table URI.
- **Table rows are arrays**, values in column order, not objects keyed by column name.
- **Date column format token is `dp`**, not `date`. Cells as ISO strings like `2026-09-08`.
- **Select pills:** define options as `{name, color}`; cell values must match an option name exactly (case-sensitive). For a real **checkbox**, use format `check` and write booleans (a select holding true/false is a different, wrong thing).
- **Simple-card / rich-detail:** in a card view, `hideColumnIds` hides fields from the card FACE but they still appear when the card is opened. That is how you get a minimal face with depth in the detail.
- **Ordering several inserts at one anchor:** put them in one batch in document order; consecutive inserts after X auto-reorder to X, A, B, C.
- **Canvas-in-a-cell:** to fill a rich detail body, `table_rows_read` the row for the cell's canvas URI, then `content_modify` that URI like any page.
- **Timeline** needs start + end date columns (or start + duration); group by a phase select column; a row with a start and no end renders as a milestone.
- **Live counts:** `<formula>[Build Tasks].Filter(Done).Count()</formula> of <formula>[Build Tasks].Count()</formula>`.
- **Verify by reading back;** the MCP cannot see its own render, so `content_read` after a build and open it in Chrome.

## Coda Formula Language (CFL) traps
CFL is its own dialect. Functions you will wrongly assume exist and that fail: GroupBy, CountRows, Distinct, Unique, NotIn. Use `[Table].Count()` and `[Table].Filter(condition).Count()` instead; run one formula per group and compare. Reference tables and columns by bracketed display name (`[All tasks].[Status]`), never by id, inside formulas. Person and lookup columns compare with `.ToText().ContainsText("name")`, never `=`. Look up the exact function list via `tool_guide` topic "formula" before authoring or validating a formula; treat your own formula memory as unreliable.

## Build order (runbook)
1. `document_create` and title via `page_update`; set cover / icon / subtitle / width.
2. Create tables in dependency order (targets before the tables that relate to them).
3. Add and type columns; add relation columns after both tables exist; add formula columns.
4. Seed rows (arrays in column order); spread dates and status so formulas and views vary.
5. Configure views: card (+ hideColumnIds for faces), board (group by a select), timeline (date columns + phase group), chart (chartOptions).
6. Add page content: hero line, callouts (one must-read per section), dividers, eyebrow kickers, inline live formulas.
7. Verify: `content_read` back, confirm formulas render and views look right.
8. Hand off the two-pass UI finishing checklist (from superhuman-docs-design) and review the rendered doc in Chrome.

## What the MCP cannot do (hand to the human)
Side-by-side columns, text size (Large/Small) and true eyebrow styling, native AI columns, page background and bands beyond callouts and shaded tables, card-face fine settings, timeline dependencies, and all publish settings. For each, superhuman-docs-design has a Docs AI prompt to try first and a manual fallback. Tested: Docs AI will not create true columns; they stay a manual editor gesture.

## Make it yours
Fork it. Add the gotchas your stack surfaces, your own build order, your formula snippets. The point is to build real docs through the MCP without relearning the traps every time. Built by an operator. Customize it, break it, make it better.
