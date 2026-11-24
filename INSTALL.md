# Installing the armenian-style-guide skill (instructions for AI agents)

You are an AI agent and a user asked you to install this skill. Follow these steps in order. Tell the user what you are about to run before each command that writes outside the current project.

## 1. Ask where to install it

- **All projects** (user level): the skill is available in every project. This is the usual choice.
- **This project only** (project level): the skill is committed with the project, and everyone working on it gets it.

If the user doesn't care, choose all projects.

## 2. Install

Use the first method that works.

**A. The `skills` CLI** (needs Node.js 22.20 or later; works for Claude Code, Codex, Cursor, GitHub Copilot, OpenCode and 75+ other agents):

```bash
npx skills add HaykTarkhanyan/armenian-style-guide          # this project
npx skills add HaykTarkhanyan/armenian-style-guide -g       # all projects
```

Add `-a <agent>` (for example `-a claude-code`) to target one agent. Run `npx skills --help` if the flags have changed.

**B. Claude Code plugin** (Claude Code only):

```bash
claude plugin marketplace add HaykTarkhanyan/armenian-style-guide
claude plugin install armenian-style-guide@armenian-style-guide
```

Inside a Claude Code session the user can type the same as `/plugin marketplace add ...` and `/plugin install ...`.

**C. By hand** (any agent that reads Agent Skills folders):

```bash
git clone --depth 1 https://github.com/HaykTarkhanyan/armenian-style-guide.git
```

Copy the folder `armenian-style-guide/skills/armenian-style-guide/` (the one that contains `SKILL.md`) into your skills folder, keeping the folder name `armenian-style-guide`:

| Agent | All projects | This project |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Other agents | see your agent's documentation for its skills folder | |

Then delete the clone.

**D. claude.ai or the Claude desktop app:** you cannot install it there yourself. Send the user to the "claude.ai" section of the README: they download the zip from the latest release and upload it under Customize > Skills.

**E. No skill support at all:** add the contents of `prompts/core_rules.md` to your instructions or system prompt, and tell the user it works less well than the skill (no glossary, no lint).

## 3. Check it

From the installed skill folder:

```bash
python scripts/lint_armenian.py --selftest      # or python3; expect "selftest: 100/100 passed"
```

Then confirm that the folder contains `SKILL.md`, `references/glossary_Apr.csv` and `scripts/lint_armenian.py`.

## 4. Tell the user

- Where it was installed, and that a new session may be needed before the agent sees the skill.
- That it loads by itself when they ask for Armenian text, and that in Claude Code they can also type `/armenian-style-guide`.
- That their own decisions about wording will be kept in `ARMENIAN_DECISIONS.md` in their project.

## Updating

- `skills` CLI: `npx skills update armenian-style-guide` (add `-g` if it was installed for all projects).
- Claude Code plugin: `claude plugin marketplace update armenian-style-guide`, then `claude plugin update armenian-style-guide@armenian-style-guide`.
- By hand: repeat method C and replace the folder. Never keep project decisions inside the skill folder, because updates replace it.
