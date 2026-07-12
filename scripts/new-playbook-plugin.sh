#!/usr/bin/env bash
# Scaffold a Built GTM playbook plugin + marketplace entry so `/plugin install <slug>@built-gtm` resolves.
# Run this whenever you add a playbook to the site's lib/workflows.ts.
#   Usage: ./scripts/new-playbook-plugin.sh <slug> "<category>" "<description>" "skill-a skill-b skill-c"
set -euo pipefail
SLUG="${1:?slug}"; CATEGORY="${2:?category}"; DESC="${3:?one-line description}"; SKILLS="${4:?space-separated step skills}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
mkdir -p "plugins/$SLUG/.claude-plugin"
for sk in $SKILLS; do
  [ -f "skills/$sk/SKILL.md" ] || { echo "ERROR: skill '$sk' not in skills/. Add it first."; exit 1; }
  mkdir -p "plugins/$SLUG/skills/$sk"; cp "skills/$sk/SKILL.md" "plugins/$SLUG/skills/$sk/SKILL.md"
done
cat > "plugins/$SLUG/.claude-plugin/plugin.json" <<JSON
{
  "name": "$SLUG",
  "version": "1.0.0",
  "description": "$DESC",
  "author": { "name": "Heath Barnett", "url": "https://builtgtm.ai" },
  "homepage": "https://builtgtm.ai/playbooks/$SLUG",
  "keywords": ["built-gtm", "playbook", "gtm"]
}
JSON
python3 - "$SLUG" "$CATEGORY" "$ROOT" <<'PY'
import json,sys,os
slug,cat,root=sys.argv[1],sys.argv[2],sys.argv[3]
p=os.path.join(root,".claude-plugin","marketplace.json"); d=json.load(open(p))
pl=d.setdefault("plugins",[])
if not any(x.get("name")==slug for x in pl):
    pl.append({"name":slug,"source":f"./plugins/{slug}","category":cat,"homepage":f"https://builtgtm.ai/playbooks/{slug}"})
    json.dump(d,open(p,"w"),indent=2); print("  + marketplace entry added:",slug)
else: print("  = marketplace entry already present:",slug)
PY
echo "Scaffolded plugins/$SLUG ($(echo $SKILLS | wc -w) skills). Commit + push Skill-Builder to publish the install."
