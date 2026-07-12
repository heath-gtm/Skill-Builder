#!/usr/bin/env bash
# Re-sync the core skill files from Skill-Builder (the source of truth) into the
# Built GTM starter kit repo, then push. The kit ships self-contained skill copies,
# so run this whenever a loop or context skill body changes.
#   Usage: GITHUB_PAT=<token-with-Built-GTM-access> ./scripts/sync-starter-kit.sh
set -euo pipefail

KIT_SKILLS="solve-the-problem stack-the-tech cut-the-drag keep-the-judgment define-your-icp positioning-brief brand-voice-guide build-signal-library github-for-gtm context-pack knowledge-base workspace-organizer decision-log"

: "${GITHUB_PAT:?Set GITHUB_PAT to a token with push access to Built-GTM/builtgtm-starter-kit}"
SB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone --quiet --depth 1 "https://x-access-token:${GITHUB_PAT}@github.com/Built-GTM/builtgtm-starter-kit.git" "$TMP/kit"

missing=""
for sk in $KIT_SKILLS; do
  src="$SB_ROOT/skills/$sk/SKILL.md"
  if [ ! -f "$src" ]; then missing="$missing $sk"; continue; fi
  mkdir -p "$TMP/kit/skills/$sk" "$TMP/kit/.claude/skills/$sk"
  cp "$src" "$TMP/kit/skills/$sk/SKILL.md"
  cp "$src" "$TMP/kit/.claude/skills/$sk/SKILL.md"
done
[ -n "$missing" ] && { echo "ERROR: missing source skills:$missing"; exit 1; }

cd "$TMP/kit"
if git diff --quiet; then
  echo "Starter kit skills already in sync. Nothing to push."
  exit 0
fi
git config user.email "heath@builtgtm.ai"
git config user.name "Heath Barnett"
git add -A
git commit --quiet -m "Sync core skills from Skill-Builder"
git push --quiet origin main
echo "Starter kit skills re-synced and pushed:"
git --no-pager show --stat --oneline HEAD | head -20
