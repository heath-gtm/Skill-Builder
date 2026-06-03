# Skill-Builder

Heath's library of Claude skills for GTM and RevOps work. Each skill lives in its own folder. Install instructions are in [INSTALL.md](./INSTALL.md).

---

## What's a skill?

A skill is a self-contained bundle of instructions, reference files, and (sometimes) helper scripts that teaches Claude how to do a specific job — diagnose a funnel, run a deal review, write a brief in a specific voice. Skills are designed to be small, sharp, and composable. You install a `.skill` file (a zipped bundle) into Cowork, and the skill auto-fires when you say something that matches its trigger phrases.

The Skills concept comes from Anthropic — full reference at [docs.claude.com/skills](https://docs.claude.com/en/docs/agent-skills/overview).

---

## Skill catalog

| Skill | Version | What it does | Kickoff phrases |
|---|---|---|---|
| [`strike-zone-math`](./strike-zone-math/) | v2.0 | Mixmax's funnel + PQA diagnostic engine. Three modes: funnel diagnosis, multi-source PQA sprint planning, and Aero scoring audit. | _"diagnose the funnel"_ · _"score our PQAs"_ · _"is Aero missing accounts"_ |
| [`mutual-action-plan`](./mutual-action-plan/) | v1.0 | Generate a deal-specific Mutual Action Plan (Trial Success Plan) — Mixmax-branded `.docx` ready to send to the champion. Unlocks the Stage 3 → 4 exit gate. | _"draft a MAP for [account]"_ · _"build a Mutual Action Plan"_ · _"trial success plan for [company]"_ |

_More coming — backing up the rest of the library next._

---

## Repo structure

```
Skill-Builder/
├── README.md                  ← This file (the catalog)
├── INSTALL.md                 ← How to install a skill into Cowork
├── scripts/
│   ├── package_skill.py       ← Build a .skill bundle from any skill folder
│   └── quick_validate.py      ← Validate a skill before packaging
└── <skill-name>/              ← One folder per skill
    ├── SKILL.md               ← The skill's instructions + YAML frontmatter
    ├── references/            ← Reference files Claude reads when relevant
    └── evals/                 ← Test prompts for skill development (optional)
```

---

## How to install a skill

The fastest path:

1. Open the [Releases page](https://github.com/heath-gtm/Skill-Builder/releases) and download the `.skill` file you want.
2. Drag the `.skill` file into your Cowork chat.
3. Click "Save Skill" when prompted.
4. Type one of the skill's kickoff phrases (see the catalog above) to test it.

If you'd rather build the `.skill` file yourself from source:

```bash
git clone https://github.com/heath-gtm/Skill-Builder.git
cd Skill-Builder
python scripts/package_skill.py strike-zone-math/
# This produces strike-zone-math.skill in the current directory.
```

See [INSTALL.md](./INSTALL.md) for detailed steps including troubleshooting.

---

## How to add a new skill

1. Create a new folder at the repo root named after the skill (kebab-case).
2. Add a `SKILL.md` file with proper YAML frontmatter (see any existing skill for the format).
3. Add `references/` for any longer-form documentation Claude should read when relevant.
4. Validate it: `python scripts/package_skill.py <folder>/` — the script runs validation before packaging.
5. Add a row to the catalog table in this README.
6. Commit, tag a release if you want a `.skill` file published.

---

## Versioning

Skills are versioned independently via prefixed git tags:

```
strike-zone-math/v2.0
customer-strategy-brief/v1.1
```

Bump a skill's version when:
- The description changes (changes triggering behavior — important)
- The scoring rubric or core methodology changes
- A new reference file is added

Backwards-compatible content tweaks don't require a version bump.

---

## Sharing

To share an individual skill, link to its folder:

```
https://github.com/heath-gtm/Skill-Builder/tree/main/strike-zone-math
```

To share the whole library, just send the repo URL:

```
https://github.com/heath-gtm/Skill-Builder
```

---

## License

MIT (TBD — pending decision). Skills here document Mixmax-specific workflows and field names. The methodology is reusable; the SFDC field names are not. If you fork a skill for your own org, expect to retune the field references and ICP weights.

---

_Maintained by Heath Barnett · DM on Slack with questions or contributions._
