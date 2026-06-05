---
name: publishing-config-setup
description: >
  First-run setup for the Mixmax publishing config — collects the GitHub PAT,
  owner, repo, and branch from the user, validates the PAT against the GitHub
  API, and writes the canonical config file at
  `Revenue Reviews/specs/github_publishing_config.md`. Use whenever the user
  says "set up Mixmax publishing", "configure GitHub publishing", "install
  publishing config", "set up the GitHub PAT for revenue reports", "I just
  installed the Mixmax publishing plugin", or any time another Mixmax plugin
  reports that `Revenue Reviews/specs/github_publishing_config.md` is missing,
  contains placeholder values, or has an invalid PAT. Also use when the user
  needs to rotate their PAT or migrate the publishing repo.
---

# Mixmax Publishing Config — Setup

This skill provisions the single-source-of-truth GitHub publishing config that every Mixmax revenue-reporting plugin depends on. Run it once at install time, and again any time the PAT rotates or the repo moves.

## Outputs

- `Revenue Reviews/specs/github_publishing_config.md` in the user's working folder — the canonical config every other plugin reads.

## When to trigger

Trigger any of the following:

- The user explicitly asks to set up, configure, install, or rotate the Mixmax GitHub publishing config / PAT.
- Another Mixmax plugin (leader-update-slides, sales-leader-weekly, cs-leader-weekly, weekly-gtm-report, monthly-gtm-report, quarterly-gtm-report) reports that the config file is missing, empty, or contains placeholder values like `<PASTE_FINE_GRAINED_PAT_HERE>`.
- A publishing step returns 401/403 from the GitHub API and the user wants to fix the credential.

## Workflow

### Step 1 — Confirm the working folder

Confirm the user has a Cowork working folder selected (the folder where `Revenue Reviews/` lives or will live). If they don't, ask them to select one first using the Cowork directory picker.

### Step 2 — Check whether config already exists

Read `Revenue Reviews/specs/github_publishing_config.md` from the user's working folder.

- If the file exists and contains a real-looking PAT (no `<PASTE_...>` placeholders, `GITHUB_PAT` starts with `github_pat_` or `ghp_`), tell the user the config already exists, show them the current `GITHUB_OWNER`/`GITHUB_REPO`/`GITHUB_BRANCH` (NEVER print the PAT), and ask whether they want to (a) keep it, (b) rotate the PAT only, or (c) replace the whole config.
- If the file is missing, contains placeholders, or is malformed, proceed to Step 3.

### Step 3 — Collect inputs from the user

Use AskUserQuestion (or plain chat questions if AskUserQuestion is unavailable) to gather:

1. **GITHUB_OWNER** — GitHub username or org that owns the publishing repo (e.g., `heath-gtm`).
2. **GITHUB_REPO** — repo name (e.g., `mixmax-revenue-reports`).
3. **GITHUB_BRANCH** — default `main`; ask only if user wants to override.
4. **GITHUB_PAT** — the fine-grained Personal Access Token. Ask the user to paste it directly into the chat. Treat it as sensitive: do NOT echo it back in any subsequent message, do NOT log it to a report, do NOT include it in any committed artifact.

If the user does not yet have a PAT, walk them through generating one:

> Go to https://github.com/settings/personal-access-tokens/new and create a **fine-grained** token:
> - **Resource owner:** the account that owns the publishing repo
> - **Repository access:** Only select repositories → pick the publishing repo
> - **Permissions:** Contents = Read and write, Pages = Read-only
> - Set an expiration that matches your security policy and paste the resulting `github_pat_…` string back here.

### Step 4 — Validate the PAT against the GitHub API

Before writing the file, validate the credentials by hitting the GitHub API. Use the Bash tool:

```bash
curl -sS -o /tmp/gh_check.json -w "%{http_code}" \
  -H "Authorization: Bearer <PAT>" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<OWNER>/<REPO>"
```

- **200** → valid; proceed to Step 5.
- **401** → bad credentials; the PAT is wrong or expired. Ask for a new one.
- **403** → either the PAT lacks repo access, the account is suspended, or rate-limited. Show the response body to the user (it usually contains a clear message) and ask how to proceed.
- **404** → repo does not exist or PAT cannot see it. Confirm the owner/repo spelling and the PAT's repository access scope.

Never write the config file if validation fails. Never print the PAT in error messages.

### Step 5 — Write the canonical config file

Copy the template at `${CLAUDE_PLUGIN_ROOT}/references/github_publishing_config.template.md` to `Revenue Reviews/specs/github_publishing_config.md` in the user's working folder. Substitute the four collected values into the YAML config block. Leave the rest of the template (paths, derived values, rotation playbook, validation checklist) untouched.

If `Revenue Reviews/specs/` does not yet exist in the working folder, create it.

### Step 6 — Confirm

Tell the user:

- Where the config was written (e.g., `Revenue Reviews/specs/github_publishing_config.md`).
- Which OWNER/REPO/BRANCH was set (do NOT print the PAT).
- That the config is now ready for use by `mixmax-leader-update-slides`, `mixmax-sales-leader-weekly`, `mixmax-cs-leader-weekly`, and the other Mixmax revenue-reporting plugins.
- The rotation procedure: "If your PAT ever rotates or you move the repo, just run this skill again."

## Security rules

- Never commit the PAT into the plugin bundle, into a published HTML artifact, into Notion, into Slack, or into any GitHub commit.
- Never echo the PAT back to the user after they paste it.
- If the user pastes a PAT into the chat, do not repeat it in subsequent assistant messages.
- The config file lives in `Revenue Reviews/specs/`, which is the user's local working folder — it is NOT pushed to GitHub by any of the publishing workflows.
