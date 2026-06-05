# Account Intelligence — Sheet Schema Reference

Shared reference for all skills that read from the rep's Account Intelligence Google Sheet.
The sheet is a Google Sheet the rep maintains. Skills read it via Chrome MCP (`get_page_text`
or `read_page` on the open sheet tab) or via the Google Drive MCP if connected.

## How to Read the Sheet

### Option A: Chrome MCP (preferred — works if rep has sheet open)

1. Ask the rep for the Google Sheet URL (or find it in project instructions).
2. Use `navigate` to open the sheet URL appended with `#gid=` for the target tab:
   - Open Deals: `#gid=0`
   - Renewal Book: the second tab's gid (check the URL when on that tab)
   - Prospect Accounts: the third tab's gid
3. Use `get_page_text` to extract the tab contents as text.
4. Parse the tab-separated or comma-separated output using the column headers below.

### Option B: Google Drive MCP (if connected)

Use `read_file_content` with the file ID from the sheet URL.

### Option C: Rep pastes data

If neither MCP is available, ask the rep to copy-paste the relevant tab's data.

---

## Tab 1: Open Deals (gid=0)

| Column | Header | Type | Description |
|--------|--------|------|-------------|
| A | Deal Name | text | Name of the opportunity |
| B | Account | text | Company name |
| C | Domain | text | Company domain — KEY for Amplitude/Mixmax cross-ref |
| D | Stage | enum | Discovery, Evaluation, Proposal, Negotiation, Verbal Commit, Closed Won, Closed Lost |
| E | Close Date | date | Expected close date (YYYY-MM-DD) |
| F | ARR ($) | currency | Annual recurring revenue of the deal |
| G | Forecast Category | enum | Pipeline, Best Case, Commit, Closed Won, Omitted |
| H | Champion | text | Internal champion name |
| I | Champion Email | email | Champion's email address |
| J | Economic Buyer | text | Person with budget authority |
| K | Next Step | text | Immediate next action |
| L | Days in Stage | number | Days since last stage change |
| M | Last Meeting Date | date | Most recent meeting with this account |
| N | Risk Flag | enum | None, Stalled, Single-threaded, No next step, Pushed close date, Competitor, Budget risk |
| O | Notes | text | Free-form notes |

### Deal Risk Signals (derived)

When analyzing deals, flag these automatically:
- **Stalled**: Days in Stage > 21 AND stage is not Closed Won/Lost
- **No champion access**: Champion Email is blank
- **Single-threaded**: Only one contact listed (no Economic Buyer)
- **Slipping**: Close Date is within 14 days AND stage is Discovery or Evaluation
- **Missing next step**: Next Step is blank AND stage is not Closed Won/Lost

---

## Tab 2: Renewal Book

| Column | Header | Type | Description |
|--------|--------|------|-------------|
| A | Account | text | Company name |
| B | Domain | text | Company domain — KEY for Amplitude/Mixmax cross-ref |
| C | Renewal Date | date | Contract renewal date |
| D | Current ARR ($) | currency | Current annual contract value |
| E | Expected Outcome | enum | Flat Renewal, Expansion, Downgrade, Churn Risk, Churned |
| F | Seats | number | Current seat count |
| G | Primary Contact | text | Main relationship contact |
| H | Contact Email | email | Contact's email |
| I | Health Status | enum | Healthy, Watch, At Risk, Critical |
| J | Last QBR Date | date | Most recent QBR |
| K | Risk Notes | text | What's driving risk (if any) |
| L | Expansion Opportunity | text | Upsell/expansion potential |
| M | Days to Renewal | formula | =C[row]-TODAY() — auto-calculates |

### Renewal Risk Signals (derived)

- **Upcoming + unhealthy**: Days to Renewal < 60 AND Health Status is At Risk or Critical
- **No recent QBR**: Last QBR Date > 90 days ago AND renewal within 120 days
- **Churn risk + high ARR**: Expected Outcome is Churn Risk AND ARR > $30,000

---

## Tab 3: Prospect Accounts

| Column | Header | Type | Description |
|--------|--------|------|-------------|
| A | Account Name | text | Target company name |
| B | Domain | text | Company domain — KEY for Amplitude cross-ref |
| C | Channel | enum | Inbound, Outbound, Product, Expansion, Partner |
| D | Aero Fit Score | number | 0-100 fit score from Aero |
| E | GTM Stage | enum | Cold, Engaged, Meeting Set, Qualified, Disqualified |
| F | ICP Tier | enum | Tier 1, Tier 2, Tier 3 |
| G | Industry | text | Company industry |
| H | Employee Count | number | Company size |
| I | Key Contact | text | Primary target contact |
| J | Contact Title | text | Contact's job title |
| K | Contact Email | email | Contact's email |
| L | Last Activity | text | Description of most recent touchpoint |
| M | Last Activity Date | date | When last activity occurred |
| N | Sequence Enrolled | enum | Yes, No |
| O | Product Usage Signal | text | Amplitude-derived usage context |
| P | Notes | text | Free-form notes |

### Prospect Prioritization Signals (derived)

- **Hot product lead**: Channel = Product AND Aero Fit Score > 70 AND GTM Stage is Cold or Engaged
- **Re-engage**: Last Activity Date > 30 days ago AND GTM Stage is Engaged AND Sequence Enrolled = No
- **High-fit untouched**: Aero Fit Score > 80 AND GTM Stage is Cold AND ICP Tier is Tier 1
- **Already covered**: Sequence Enrolled = Yes (skip — they're in motion)

---

## Cross-Referencing with Live Data

The sheet provides the "what" — the rep's deals, renewals, and targets. Live MCPs provide the "so what":

| Sheet field | Cross-ref with | What it tells you |
|-------------|---------------|-------------------|
| Domain (all tabs) | Amplitude (project 130895) | Active users, feature adoption, WAU trend, engagement depth |
| Domain (all tabs) | Mixmax meetings | Recent meeting history, transcripts, action items |
| Champion Email / Contact Email | Mixmax sequences | Whether they're already being sequenced |
| Domain (all tabs) | Octave (enrich_company) | Company research, competitive intel, org chart |
| Contact Email | Octave (find_person, enrich_person) | Contact enrichment, LinkedIn, role context |

Always use the Domain column as the primary key for Amplitude and Mixmax lookups.
Filter Amplitude by `gp:email contains [domain]` and exclude test users (cohort `vbyym9zo`).
