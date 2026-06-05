# Mixmax GTM Slides Plugin

**HTML content workbench (spec v5.3.0)** — an opinionated source-of-truth document the Mixmax CEO uses to write his board deck. Not a rendered presentation.

## What It Does

Produces a single-file HTML workbench (~10–18 MB) with **34 slide cards** organized into **13 narrative Parts** and surfaced via a **21-Section** sidebar (Revenue → Direct Sales → Self-Serve → Customer Success → Pipeline → Expansion → Risks → Plan → Appendix → Q&A → Close). Every content card now follows a **universal 7-block skeleton** — same shape on every slide, so the CEO reads top-to-bottom without re-orienting.

## The 7-block skeleton (every slide, v5.2+)

1. **Compact header** — slide number badge + section label + state-aware verdict pill (ok / watch / risk) + action bar (Preview · Copy Slide Template · Copy Narrative) + "Mark decided" toggle
2. **Stat cards row** — 3 compact KPI cards (label, value, signed delta, direction arrow) — read-the-call-at-a-glance
3. **Visual picker** — universal 3-tab chooser: *Cards only · Cards + Key/Second/Supporting · Chart + Cards* (replaces the old narrative-angle picker)
4. **Primary visual** — chart (`<img loading="lazy" decoding="async">`) or K/S/S drivers card (inline-editable on D1–D5)
5. **Anticipated Q&A** — collapsed by default, 3–5 Q&A pairs per slide
6. **Custom bullets box** — `contenteditable` scratchpad per slide with Copy + Clear buttons
7. **Slide divider** — purple→lime gradient, hard break before the next slide

Nothing renders outside this skeleton. No narrative-angle tabs, no stacked 4-pack, no hybrid-pane composer, no Q&A + stat-tile + comparison-strip duplication. The 7-block skeleton IS the slide.

## What's new across v5.0 → v5.3

### v5.0 — 13-Part taxonomy + Custom Bullets
- Slide flow reorganized into 13 narrative Parts with Part dividers carrying Part number + title
- `<section data-part="…">` anchors drive sidebar grouping
- **Custom Bullets box** introduced — contenteditable scratchpad per slide, Copy + Clear actions

### v5.1 — 21-Section flow + unified pickers
- Sidebar granularity increased from 13 Parts to **21 Sections** with `sidebar-group-{section-id}` anchors
- New slide IDs: **D1–D5** (Drivers: ARR waterfall, Bookings, Pipeline, Renewals, Expansion), **DS1** (Direct Sales by Segment), **SS1** (Self-Serve funnel), **E1** (Expansion attribution), **R1** (Renewals summary), **GAL** (Chart Gallery)
- **Unified bullet picker** — Key / Secondary / Supporting tabs in one component, same shape across every slide
- **Chart picker tabs** — Active chart drives Copy Image, with YoY / QoQ / MoM variants where data supports it
- Header chip copy: *"31 cards · 24 charts · 21 Sections · YoY/QoQ charts · Unified bullets · QA"*

### v5.2 — Universal 7-block skeleton
- Every legacy slide (01–24) and every v5.x-native slide (D1–D5, DS1, SS1, R1, E1, GAL) normalized onto the same 7-block shape
- **Compact header** (`slide-head-compact`): slide-num + slide-section + verdict-pill + slide-action-bar + decided-toggle in a single tag row
- **State-aware verdict pill**: `verdict-ok` (green), `verdict-watch` (amber), `verdict-risk` (red) — CSS vars drive the tint
- **3-stat-card row** (`STAT_CARDS` dict keyed by slide ID) — same 3-card shape everywhere
- **All-navy chrome** — `#1D1D53` as the dominant header tone, Mixmax magenta `#C53FDF` as the accent
- Legacy slide headers rewritten in place (`rewrite_legacy_slide_verdict`, `rewrite_new_slide_header`)

### v5.3 — Cover DA banner + universal visual picker + collapse-all + inline K/S/S
- **Data Accuracy banner §0** at the top of the cover (above the AI summary / action items) — 4-card grid: ARR Contribution, Bookings, Pipeline, Renewals — each card shows 3 metrics (actual, plan delta, segment split) with `is-negative` amber-red styling for misses. Source citation footer cites Gen 1 Quarterly Lookback tabs. Banner is also pinned open in the sidebar.
- **Universal visual picker** replaces the narrative-angle picker: 3 tabs — *Cards only · Cards + K/S/S · Chart + Cards* — preview pane above; Copy Slide Template reads the active tab
- **Collapse-all-on-load** — every sidebar group starts collapsed; CEO expands what they want. `aside.toc .sidebar-group[data-collapsed="true"] .sidebar-group-list { display: none }` gates the list; `sidebar-group-data-accuracy` is pinned open.
- **Inline-editable K/S/S drivers** — Key / Secondary / Supporting bullets on D1–D5 are `contenteditable="true"` with `data-default-html` snapshots and a per-column Reset button. Type a correction, copy to Slides, or Reset to rendered default.
- **Compact sidebar** — every group collapsed on load, `decided/total` chips, Board-only filter toggle still works

## Mixmax brand palette (CSS variables)

```
--mx-lavender:      #EEC3F6
--mx-magenta:       #C53FDF
--mx-magenta-dark:  #971AAE
--mx-navy:          #1D1D53
--mx-green:         #18A26A
--mx-amber:         #E8A13C
--mx-red:           #D63851
--mx-is-negative:   #B8344A   (DA banner miss tint)
```

## Skills

- **gtm-slides-setup** — First-time setup and scheduled task registration
- **gtm-slides-runbook** — Reference for running, regenerating, and troubleshooting v5.3.0

## Reference artifact

The Q1 2026 build is the v5.3.0 reference:
- Published: `https://heath-gtm.github.io/mixmax-revenue-reports/reports/gtm-slides/GTM_Q1_Workbench_v5.3.0.html`
- Local: `Revenue Reviews/Leader Weekly/GTM Slides/GTM_Q1_Workbench_v5.3.0.html`
- Builder chain (reference only — the task prompt regenerates from scratch):
  `build_workbench_v2_1.py` → `transform_v5.py` → `transform_v5_1.py` → `transform_v5_2.py` → `transform_v5_3.py` → `patch_v5_3_da_rebuild.py`

## Replaces

This plugin supersedes `mixmax-leader-update-slides` (v1.x), the v4.x narrative-picker approach, and every earlier rendered-PPTX approach. The HTML workbench is the canonical artifact — no PPTX is generated.

## Dependencies

- Approved Monthly or Quarterly Revenue Report (numbers are inherited, never re-derived)
- `mixmax-publishing-core` plugin (GitHub Pages publishing via git data API — Contents API chokes on files > 5 MB)
- Google Sheets or Chrome MCP (for snapshot data access)
- Notion MCP (for team page updates)
- Slack MCP (optional — degrades gracefully)
- Python 3.10+, `matplotlib`, `playwright` (for visual QA)

## ARR Display Rule

Total ARR may appear as a reference label only. NEVER show Total ARR as % to target. Target comparisons use Net ARR Contribution and segment breakdowns. This rule drives the Data Accuracy banner design — the ARR Contribution card shows Net ARR Contribution (not Total ARR) as the top-line metric.

## Version

3.0.0 (spec v5.3.0)
