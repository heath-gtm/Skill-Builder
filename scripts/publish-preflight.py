#!/usr/bin/env python3
# Publish preflight: verify every site playbook is fully wired to ship (plugin + marketplace +
# bundled skills), and every referenced skill has a site page + source. Run before you push live.
#   Usage: SITE_REPO=/path/to/Built-gtm/site python3 scripts/publish-preflight.py
import re, os, json, sys
SB=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
SITE=os.environ.get("SITE_REPO") or os.path.join(SB,"..","Built-gtm","site")
if not os.path.isdir(SITE): sys.exit(f"Set SITE_REPO to your site checkout (tried {SITE}).")
wf=open(os.path.join(SITE,"lib/workflows.ts")).read()
wb=wf[wf.index("export const WORKFLOWS"):]; wb=wb[:wb.index("\n];")]
entries={m.group(1):re.findall(r'skill:\s*"([^"]+)"',m.group(2)) for m in re.finditer(r'\{\s*slug:\s*"([^"]+)"[\s\S]*?steps:\s*\[([\s\S]*?)\]\s*\}',wb)}
meta=set(re.findall(r'"([a-z0-9-]+)":\s*\{ title:',open(os.path.join(SITE,"lib/skillMeta.ts")).read()))
cats=set(re.findall(r'"([a-z0-9-]+)":\s*\[',open(os.path.join(SITE,"lib/toolsCatalog.ts")).read()))
pub=set(os.listdir(os.path.join(SITE,"..","public-skills")))
mp=set(p["name"] for p in json.load(open(os.path.join(SB,".claude-plugin/marketplace.json")))["plugins"])
pdirs=set(os.listdir(os.path.join(SB,"plugins")))
sbsk=set(os.listdir(os.path.join(SB,"skills")))
issues=[]
for pb,skills in entries.items():
    if pb!="build-ai-native-gtm" and pb not in mp: issues.append(f"{pb}: no marketplace entry (install would fail)")
    if pb not in pdirs: issues.append(f"{pb}: no plugins/{pb} bundle")
    else:
        bundled=set(os.listdir(os.path.join(SB,"plugins",pb,"skills"))) if os.path.isdir(os.path.join(SB,"plugins",pb,"skills")) else set()
        for sk in skills:
            if sk not in bundled: issues.append(f"{pb}: step skill '{sk}' not bundled in plugin")
for sk in sorted({s for v in entries.values() for s in v}):
    for cond,msg in [(sk not in meta,"skillMeta card"),(sk not in cats,"SKILL_CATS"),(sk not in pub,"public-skills page"),(sk not in sbsk,"Skill-Builder source")]:
        if cond: issues.append(f"skill {sk}: missing {msg}")
print(f"playbooks={len(entries)} plugins={len(mp)} skills-referenced={len({s for v in entries.values() for s in v})}")
print("PREFLIGHT: all wired, safe to publish." if not issues else "PREFLIGHT ISSUES:")
[print("  x",i) for i in issues]
sys.exit(1 if issues else 0)
