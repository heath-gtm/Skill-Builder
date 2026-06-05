#!/usr/bin/env python3
"""Build a Cowork .plugin bundle from in-repo plugin source.

Usage: python3 scripts/build_plugin.py <plugin-name>
Reads plugins/<plugin-name>/{.claude-plugin/plugin.json, README.md, skills.txt},
pulls each listed skill folder from the repo root, validates, and writes:
  dist/<plugin-name>/            (assembled plugin dir)
  dist/<plugin-name>.plugin      (zip bundle, ready to install)
"""
import sys, os, shutil, json, zipfile, re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {'evals', '__pycache__', 'node_modules', '.git'}

def fail(msg):
    print(f"❌ {msg}"); sys.exit(1)

def main():
    if len(sys.argv) != 2:
        fail("usage: build_plugin.py <plugin-name>")
    name = sys.argv[1]
    src = REPO / "plugins" / name
    manifest = src / ".claude-plugin" / "plugin.json"
    skills_txt = src / "skills.txt"
    if not manifest.exists(): fail(f"missing manifest: {manifest}")
    if not skills_txt.exists(): fail(f"missing skills list: {skills_txt}")

    meta = json.loads(manifest.read_text())
    skills = [l.strip() for l in skills_txt.read_text().splitlines()
              if l.strip() and not l.strip().startswith('#')]

    dist = REPO / "dist" / name
    if dist.exists(): shutil.rmtree(dist)
    (dist / ".claude-plugin").mkdir(parents=True)
    shutil.copy2(manifest, dist / ".claude-plugin" / "plugin.json")
    if (src / "README.md").exists():
        shutil.copy2(src / "README.md", dist / "README.md")

    def ignore(d, names):
        return [n for n in names if n in EXCLUDE_DIRS]

    missing = []
    for s in skills:
        vend = src / "skills" / s            # vendored under the plugin definition
        root = REPO / s                       # shared skill at repo root
        sp = vend if (vend / "SKILL.md").exists() else root
        if not (sp / "SKILL.md").exists():
            missing.append(s); continue
        shutil.copytree(sp, dist / "skills" / s, ignore=ignore)
    if missing:
        fail(f"skills missing from repo root: {', '.join(missing)}")

    # --- validation gate ---
    problems = []
    for f in (dist / "skills").rglob("SKILL.md"):
        txt = f.read_text()
        for m in re.finditer(r'.*MEDDIC.*', txt):
            if 'never meddic' not in m.group(0).lower():
                problems.append(f"{f.relative_to(dist)}: {m.group(0).strip()[:80]}")
        if 'or humanizer' in txt:
            problems.append(f"{f.relative_to(dist)}: stale 'or humanizer' reference")
    if problems:
        print("⚠️  validation findings:")
        for p in problems: print("   -", p)
        fail("validation failed — fix sources before packaging")

    # --- zip ---
    bundle = REPO / "dist" / f"{name}.plugin"
    if bundle.exists(): bundle.unlink()
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for p in dist.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(dist))

    n_skills = len(list((dist / "skills").iterdir()))
    print(f"✅ Built {name} v{meta['version']} — {n_skills} skills")
    print(f"   dir:    dist/{name}/")
    print(f"   bundle: dist/{name}.plugin")

if __name__ == "__main__":
    main()
