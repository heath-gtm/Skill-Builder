# Built GTM Skills

Operator-built Claude skills, bundled by the problem they solve. Free. Each one is genericized so you can customize it for your own stack in minutes. Browse them at https://builtgtm.ai/skills

## Install one skill (no clone needed)
```
mkdir -p ~/.claude/skills/<name> && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/<name>/SKILL.md -o ~/.claude/skills/<name>/SKILL.md
```
Then restart Claude Code.

## Install everything
```
git clone https://github.com/heath-gtm/Skill-Builder.git
cp -r Skill-Builder/skills/* ~/.claude/skills/
```

## What is inside
Each skill has a "Customize this for yourself" block. Set your CRM, your fields, your thresholds. See `plugins.json` for the bundles. Built by an operator. Customize them, break them, make them better.
