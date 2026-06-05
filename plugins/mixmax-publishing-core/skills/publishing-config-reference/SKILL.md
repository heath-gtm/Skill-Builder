---
name: publishing-config-reference
description: >
  Load and resolve the Mixmax GitHub publishing config (PAT, owner, repo,
  branch, derived API base, derived Pages URL, per-artifact path roots) from
  the user's working folder so any downstream task can publish HTML artifacts
  to GitHub Pages without hardcoding URLs or tokens. Use whenever a Mixmax
  task needs to push an HTML report to GitHub, build a "Published to" link,
  emit a Pages URL into Notion or Slack, or read the canonical PATH_* roots
  for weekly / monthly / quarterly / leader-update artifacts. Trigger on "load
  publishing config", "resolve GitHub publishing variables", "where do
  reports get pushed", "what's the GITHUB_PAGES_URL", or any task prompt that
  starts with STEP 0a.
---

# Mixmax Publishing Config — Reference & Loader

This skill is the runtime loader for the publishing config that `publishing-config-setup` provisions. Every Mixmax task that publishes to GitHub Pages calls this skill at STEP 0 to resolve the variables it needs.

## Where the config lives

`Revenue Reviews/specs/github_publishing_config.md` in the user's working folder. This is a YAML-in-markdown config maintained as the single source of truth.

## Variables this skill resolves

From the YAML config block:

- `GITHUB_PAT` — sensitive; never print, never commit.
- `GITHUB_OWNER`
- `GITHUB_REPO`
- `GITHUB_BRANCH` (default `main`)

Derived (always compute from the four above; never read from disk):

- `GITHUB_REPO_FULL = ${GITHUB_OWNER}/${GITHUB_REPO}`
- `GITHUB_API_BASE = https://api.github.com/repos/${GITHUB_REPO_FULL}`
- `GITHUB_PAGES_URL = https://${GITHUB_OWNER}.github.io/${GITHUB_REPO}`

Path roots (read directly from the config file's path block):

- `PATH_WEEKLY`
- `PATH_MONTHLY`
- `PATH_QUARTERLY`
- `PATH_UPDATE_SLIDES_SALES`
- `PATH_UPDATE_SLIDES_CS`
- `PATH_INDEX`

## Workflow

### Step 1 — Read the config file

Use the Read tool on `Revenue Reviews/specs/github_publishing_config.md` in the user's working folder.

If the file does not exist, contains placeholder values like `<PASTE_FINE_GRAINED_PAT_HERE>`, or has a malformed YAML block:

- Stop the calling task.
- Tell the user the publishing config is missing or invalid.
- Direct them to run the `publishing-config-setup` skill (or invoke it directly if the calling task is interactive).
- Do NOT proceed with any GitHub API calls.

### Step 2 — Parse the YAML config block

Extract the four primary variables from the ```yaml``` fenced block under "## Config block". Compute the derived variables in memory; do not hardcode them.

### Step 3 — Parse the path roots

Extract `PATH_*` from the ```yaml``` fenced block under "## Publishing path conventions". The calling task picks whichever root applies to the artifact it is publishing.

### Step 4 — Build URLs the right way

For every published artifact, build URLs as:

- **Pages URL:** `${GITHUB_PAGES_URL}/${PATH_<ARTIFACT>}<filename>`
- **API URL (read/write):** `${GITHUB_API_BASE}/contents/${PATH_<ARTIFACT>}<filename>?ref=${GITHUB_BRANCH}`

Never concatenate a literal `https://api.github.com/...` or `https://<owner>.github.io/...` string anywhere in the calling task or in any output artifact (footers, Notion, Slack, etc.).

### Step 5 — Use the PAT safely

When making GitHub API calls, pass the PAT in the `Authorization: Bearer ${GITHUB_PAT}` header. Never:

- Print the PAT in any user-visible message.
- Commit the PAT to GitHub.
- Embed the PAT in HTML, Notion blocks, Slack messages, or any other artifact.
- Pass the PAT through a URL query parameter.

### Step 6 — Pass resolved variables to the caller

Return the resolved variables to the calling task as a structured block (or use them directly if the calling task is the same agent turn). The caller is responsible for picking the correct `PATH_*` root for its artifact type.

## Publish helper (recommended pattern)

When publishing a single HTML artifact, the calling task should:

1. GET `${GITHUB_API_BASE}/contents/<path>?ref=${GITHUB_BRANCH}` with `Authorization: Bearer ${GITHUB_PAT}` to look up the existing SHA (404 means new file — omit the SHA on PUT).
2. PUT to the same URL with body:
   ```json
   {
     "message": "Publish <artifact-name> for <date>",
     "content": "<base64-encoded HTML>",
     "branch": "${GITHUB_BRANCH}",
     "sha": "<existing-sha-if-update>"
   }
   ```
3. Wait 30–90 seconds for GitHub Pages to rebuild before asserting the URL is live.
4. Optionally GET the Pages URL to verify a 200 before announcing success.
