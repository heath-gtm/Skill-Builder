---
name: superhuman-docs-builder
description: The engineering companion to superhuman-docs-design: how to actually build a document in Superhuman Docs (Coda) through the Docs MCP. Tool inventory and build order, the gotchas that bite (batch caps, row-as-array writes, the date format token, select-vs-checkbox, card-face hiding, canvas-in-a-cell), Coda Formula Language traps, and the two-pass handoff to the human UI finishing pass. Trigger on "build this doc via the MCP", "create the tables and views", "the MCP call failed", "how do I add a timeline or progress or card view", "why did my table write break", "seed the rows", or any hands-on Superhuman Docs / Coda MCP build task. v5 adds the AI layer (AI columns/blocks/chat + the computed-cell fallback; Coda AI does NOT browse the web), MCP-native reactions, wiki/KM + nested multi-page builds, and the bespoke-overlay model (template-first base, then charts/rich-detail/reactions via the MCP + one UI columns pass). Also triggers on "add collaborator reactions", "AI column", "build a wiki or hub", "multi-page or nested subpages", "add a chart", "checkbox column broke", "formula shows a stale value".
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

## Every build ships as three things
A build is not done when the doc exists. It ships as three artifacts, in order:
1. **The build.** The substance created through the MCP: pages, tables, views, formulas, content.
2. **The eval.** An end-to-end check that it actually works. Read the structure back with content_read, run formula_execute on every live formula, confirm the views render, confirm links resolve, and open the rendered doc in Chrome from the account that owns it for a visual pass. Log pass, warn, or block per element.
3. **The report.** A handoff that lists the eval results and the exact step-by-step UI finishing instructions (each UI-only touch with a Docs AI prompt to try and a manual fallback), plus the publish and share steps. The human runs the report to bring the doc to the finish line.
Never hand over just the build. The eval catches the broken formula, and the report catches the ten percent only a human can finish.

## Make it yours
Fork it. Add the gotchas your stack surfaces, your own build order, your formula snippets. The point is to build real docs through the MCP without relearning the traps every time. Built by an operator. Customize it, break it, make it better.

---

# v5 additions — AI layer, reactions, wiki/KM, multi-page builds, the bespoke overlay

Everything below was tested against the live Docs MCP while building a 4-page "Build Planner V2" doc. Where a claim is marked TESTED, it was verified in that build.

## The AI layer — build AI-native, know what the API can and can't do

Coda has five AI surfaces. Match each to the job; only some are reachable through the MCP.

- **AI column** (per-row generation, auto-populates new rows). Reference same-row fields with `@[Column]`; `=` opens the formula builder. Proven prompts: "write a sales email from each title," "rate 1–5," "prioritize High/Med/Low from the due date." **MCP status: UI-only to create a *live* one.** Build-time move = the **computed-cell fallback**: write the summary/label into a plain `none`/`canvas` cell yourself so the doc ships complete; flag "convert to a live AI column" for the UI pass.
- **AI Chat / Ask-the-doc** (grounded side panel; Context = no context / page / doc / selection). Live on every doc, no build step — the doc's job is to be *answerable* (clean headers, named tables, one fact per cell). Seed a callout of 3–4 starter questions so the reader knows it's queryable.
- **AI blocks** (`/Summarize`, `/Find action items from`, `@`-referencing tables/pages). UI-only as *live* blocks — build the summary/action-items yourself as a callout/table now, flag the live swap.
- **AI Assistant** (first drafts, "create a table…") and **AI Reviewer** (comment-rail feedback) — human aids after handoff, not build targets.

**Web research — the honest limit.** Coda AI has **no live internet access** (training data only, ~10k-word cap). **Never build an AI column that "looks up" or "researches" the web — it will hallucinate.** Route live external data through an **external workflow**: a doc **button** (Webhook/HTTP Pack) fires a Deepline/n8n/Make workflow → writes back into the row via the Coda API (`coda.io/apis/v1`, a Coda token as the workflow's secret). That is the correct home for web research.

## Reactions & collaborator input (build the spots in — MCP-native, TESTED)

- **Reaction column (TESTED MCP-native).** `format: {type:"reaction", imageIcon:"high-five", reactionDisplay:"People"}`. `reactionDisplay`: `People` (who — endorsement/sign-off), `Number` (tally — voting), `None`. Icons: `high-five`, `filled-like`, `fire-element`, `rocket`, `trophy`, `thumbs-down`.
  - **Gotcha:** a reaction column is interactive, **not value-writable** (`isWritable:false`) — create it, never seed it, and **exclude it from the `rows`/`columnIds` arrays**. Add it after seeding via `table_columns_manage` add if the table already has rows.
  - **Where:** an "Endorse" reaction (People) on a decisions/activations table; a "Vote" reaction (Number) on a requests/ideas backlog; a "Verified" reaction on a wiki article.
- **Reaction block** (`/reaction`, page-level) — UI-only; note it for the pass.
- **Interactive-verification unit (KM gallery):** pair a reaction with an **owner** (person col) and a **last-reviewed** date — vote + owner + freshness is the reusable KM contribution unit.

## Wiki & knowledge-management patterns (mostly MCP-native)

- **Page hierarchy (TESTED MCP-native).** `page_create` with `uri` = the **parent page URI** nests a subpage (top-level uses the doc URI); unlimited depth. `page_update` sets `parentPageUri`, `icon`, `showAuthor`, `showLastEdited`, `pageWidth`. UI-only leftover: turning top pages into **top-nav tabs**.
- **Home / hub page:** cover + one-line purpose, an escalation line, the information architecture, and link cards (`/link` in UI; MCP inserts markdown links, upgrade to cards in the pass). Hub archetypes: **Team Hub**, **Directory** (filterable index), **Request tracker** (intake + status + vote), **Curation repo** (title + type + source + freshness).
- **Discovery:** toggle the **Outline/TOC** on for anything over two screens (auto-built from H1/H2/H3 — another reason the section rhythm matters). Name tables and headers for what a person would search.
- **Attribution:** `showAuthor` + `showLastEdited` = the trust layer. Per-row freshness = owner (person) + last-reviewed (date) + a "Verified" reaction.

## Multi-page / nested-doc builds (TESTED recipe)

A whole multi-page doc builds through the MCP in one session. Recipe:

1. `page_create` the **parent hub** (uri = doc URI), then `page_create` each **subpage** with `uri` = the parent page URI to nest it. Set icons, subtitles, width in the create call.
2. Fill each page top-down (hero → sections → tables), one page at a time.
3. **Prefix every table name per page** (e.g. `V2 Build Tasks`) so name-based CFL references resolve unambiguously — two tables of the same name in one doc will break a `[Table]` reference.
4. **Live cross-page formulas** resolve by table name across the whole doc — a hub progress callout can read a table that lives on a subpage.
5. Reference: a full 4-page doc (parent + 3 subpages, ~10 tables, timelines, charts, a live progress formula) came in around **~27 write calls in one session**.

Ordering caveat: `page_create` nests correctly, but **`page_update position` does NOT reorder pages** — dragging in the sidebar is UI-only.

## The bespoke overlay — template-first is the base, always

The persuasive layer (the argument lockup, charts, rich-detail cards) is **not** a reason to hand-build a doc from scratch. It's an **overlay you add on top of a template-first base**, and most of it is MCP-native. So the rule is: **template-first for the recurring frame, then run the bespoke overlay** — never blank-mind the base.

The overlay, and how to build each piece:

- **Charts** (progress bar, donut) — MCP-native: `table_view_manage` add a view with `viewLayout: "bar chart" | "pie chart"`, set `chartOptions` (`xColumnIds`, `seriesColumnIds`, `stacking`, `pieDisplayMode`).
- **Rich-detail cards** (minimal face, depth on open) — MCP-native: add the detail columns, then `columnVisibility.hideColumnIds` on the card view. Populate an "AI summary" col with the computed-cell fallback.
- **Designed cards** (iterations, options) — MCP-native: `viewLayout: "card"`.
- **The only UI-only piece:** true side-by-side **columns** (e.g. Eigenquestion | How-to-read). Same one gesture whether the base was template-first or blank-minded — so it never favors blank-minding.

Bespoke-overlay checklist (run after the template-first base): charts on the board → rich-detail on the key card → a starter-questions callout for Ask-the-doc → reaction spots → then the single UI columns pass + publish.

## More gotchas learned the hard way (v5, TESTED)

- **Checkbox coercion.** `table_create` with `format: check` silently becomes a **true/false select**. Fix: create it, then `table_columns_manage` update the column to `check`, then write boolean cells.
- **select→check flips every non-empty cell to checked** (both "true" and "false" strings read truthy). After converting, explicitly set the false rows.
- **`content_read` returns a STALE formula cache** right after row writes. Confirm live values with **`formula_execute`**, not `content_read`.
- **`page_update position` does not move a page** (see multi-page recipe). Nesting via `page_create` parent works; reorder is UI-only.
- **Collision-safe table naming** in any multi-table/multi-page doc (see recipe).

## The action layer, relations, and self-serve (extras)

- **Buttons are the doc's verbs.** `format: button` with `actionFormula` (CFL, uses `thisRow`), `disableIfFormula`, `label`, `color`. This is the "Optimize in Claude" / "Enrich" pattern — pair a button with an external workflow for anything the API alone can't do.
- **Relation / lookup columns** (`format: lookup`, `objectId` = target table) keep "one governed surface" real: teams reference the same canonical rows instead of copying. Compare person/lookup values with `.ToText().ContainsText(...)`, never `=`.
- **Self-serve growth:** an add-a-row or duplicate-page button lets a wiki grow without you.
- **Conditional format vs. colored pills:** pills for *categorical* status (fast, free at `table_create`); `conditionalFormats` (via `table_view_manage`) for *computed* thresholds (overdue dates, score bands).

## Capability map — MCP-native vs UI-only (corrected)

| Capability | Status |
| --- | --- |
| Nested pages / hierarchy / icons / author / last-edited / width | **MCP-native** (`page_create` parent + `page_update`). UI-only leftover = top-nav tabs. |
| Reaction column | **MCP-native** (`format: reaction`; interactive, exclude from rows). |
| Charts (bar / pie / line / area) | **MCP-native** (`table_view_manage` chart layouts + `chartOptions`). |
| Card views + rich-detail (hideColumnIds) | **MCP-native.** |
| Checkbox column | MCP, but `table_create` coerces `check`→select; fix via `columns_manage`. |
| AI column / AI block (live) | **UI-only** to make live; ship the computed-cell fallback now. |
| Ask-the-doc / AI Chat | Live on every doc; design *for* it (structure + starter-questions callout). |
| Web research via Coda AI | **Not possible** — no internet; route through button → workflow → Coda API. |
| Side-by-side columns | **UI-only** (the one bespoke gesture; identical work regardless of base). |
| Page reorder | **UI-only** (`page_update position` no-ops). |
| Bands beyond callouts/shaded tables, text size, publish | **UI-only.** |
