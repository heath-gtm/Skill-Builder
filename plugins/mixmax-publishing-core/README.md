# mixmax-publishing-core

Shared GitHub Pages publishing foundation for all Mixmax revenue-reporting plugins.

## What this plugin provides

- **`publishing-config-setup`** — first-run skill that collects your GitHub PAT, owner, repo, and branch, validates the PAT against the GitHub API, and writes the canonical config to `Revenue Reviews/specs/github_publishing_config.md` in your working folder.
- **`publishing-config-reference`** — runtime loader that other Mixmax plugins call at the top of every publishing task to resolve `GITHUB_PAGES_URL`, `GITHUB_API_BASE`, `GITHUB_PAT`, and the per-artifact path roots without hardcoding anything.
- **Template config file** at `references/github_publishing_config.template.md` (no live secrets).

## Why a single source of truth

Every Mixmax revenue plugin (weekly, monthly, quarterly, leader updates) publishes HTML to the same GitHub Pages site. Without a shared config, each plugin would hardcode the PAT and Pages URL — meaning a PAT rotation or repo migration would require editing every plugin. With this plugin, you edit one file: `Revenue Reviews/specs/github_publishing_config.md`.

## Install

This plugin is a **dependency** for:

- `mixmax-leader-update-slides`
- `mixmax-sales-leader-weekly`
- `mixmax-cs-leader-weekly`
- (plus the existing weekly / monthly / quarterly GTM report plugins, which will be migrated to read from this config)

After install, run the `publishing-config-setup` skill once. The skill will not push your PAT anywhere — it lives only in your local `Revenue Reviews/specs/` folder.

## Security

- The PAT is collected from the user at setup time and stored in the user's local working folder, NOT bundled with the plugin.
- The setup skill validates the PAT against the GitHub API before writing the config.
- The reference skill never echoes the PAT in any user-visible message or output artifact.
- Use a fine-grained PAT scoped to the publishing repo only (Contents: R/W, Pages: R).

## Rotating the PAT

Run the `publishing-config-setup` skill again. It will detect the existing config and offer to rotate the PAT only.
