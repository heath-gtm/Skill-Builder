# Installing a Skill

This guide covers how to install a skill from this repo into Claude Cowork (the desktop tool for AI-powered work). It assumes you have Cowork installed — if not, get it at [claude.com/download](https://claude.com/download).

---

## Option 1 — Install from a `.skill` file (recommended)

The fastest path. Use this for any skill where I've published a release.

1. Go to the [Releases page](https://github.com/heath-gtm/Skill-Builder/releases) of this repo.
2. Find the release for the skill you want (e.g., `strike-zone-math-v2.0`).
3. Download the `.skill` file from the release's assets.
4. Open Cowork.
5. Drag the `.skill` file into the Cowork chat window.
6. Cowork will prompt you to install — click **Save Skill**.
7. Test it by typing one of the skill's kickoff phrases (listed in the [main README](./README.md) catalog).

The skill is now installed and will auto-trigger whenever you say something that matches its description.

---

## Option 2 — Build a `.skill` file from source

Use this if you want to make changes to a skill before installing, or if there's no release yet.

**Requirements:** Python 3.10+, git.

```bash
# Clone the repo
git clone https://github.com/heath-gtm/Skill-Builder.git
cd Skill-Builder

# Build the .skill file from the skill folder
python scripts/package_skill.py strike-zone-math/

# This produces strike-zone-math.skill in the current directory.
# Drag it into Cowork as in Option 1, step 5.
```

If you want to put the `.skill` somewhere specific:

```bash
python scripts/package_skill.py strike-zone-math/ ~/Downloads/
```

---

## Option 3 — Install into Claude Code (CLI)

If you use Claude Code (the CLI tool) rather than Cowork, skills install differently:

```bash
# Copy the skill folder to your Claude Code skills directory
cp -r strike-zone-math ~/.claude/skills/

# Restart Claude Code. The skill will appear in the skill list.
```

---

## Verifying installation

Once installed, you can confirm a skill is active by asking Claude:

> Which skills do you have available?

Claude should list the installed skill by name. You can also try a kickoff phrase from the catalog — if the skill is properly installed, you'll see a `<command-message>The "skill-name" skill is loading</command-message>` indicator before Claude responds.

---

## Troubleshooting

**The skill installed but doesn't trigger when I use kickoff phrases.**
- Restart Cowork — sometimes installed skills need a session restart to appear.
- Verify the skill's trigger description matches your phrasing. Open `<skill-folder>/SKILL.md` and read the `description:` field in the YAML frontmatter — that's what controls when the skill fires.
- Try a more direct phrase. If the catalog says _"score our PQAs"_, try exactly that before paraphrasing.

**The `.skill` file fails to install.**
- Check the file is a valid zip — `unzip -l <file>.skill` should show `SKILL.md` at the root of a single folder.
- Rebuild from source using `package_skill.py` to make sure the bundle is clean.

**The skill triggers but produces bad output.**
- Open the skill folder and read `SKILL.md` — you may need to recalibrate weights, field names, or trigger phrases for your environment.
- Many skills here reference Mixmax-specific Salesforce fields. If you're using this in another org, expect to update the SOQL templates.

**I want to uninstall a skill.**
- Open Cowork, go to Settings → Skills, click the skill, click Remove.
- Or via CLI: delete the skill folder from `~/.claude/skills/`.

---

## Questions

Open an issue on this repo or DM Heath in Slack.
