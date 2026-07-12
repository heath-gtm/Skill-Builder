# Skill-Builder scripts

## sync-starter-kit.sh
Re-syncs the 12 core skill files (the GTM Loop + context skills) from this repo into the
public Built GTM starter kit (`Built-GTM/builtgtm-starter-kit`) and pushes.

The starter kit ships self-contained skill copies so it runs on clone. Those copies can
drift from the source here. Whenever you rewrite a loop or context skill body, run:

```
GITHUB_PAT=<token-with-Built-GTM-access> ./scripts/sync-starter-kit.sh
```

It clones the kit, copies the current SKILL.md files, and pushes only if something changed.
Idempotent: safe to run anytime; a no-op when already in sync.
