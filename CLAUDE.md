# armenian-style-guide repo

This repo publishes one Agent Skill, `skills/armenian-style-guide/`, for anyone to install. It is public: no personal data, private paths or credentials in any file.

- The maintainer's own `~/.claude/skills/armenian-style-guide` is a junction into this repo's skill folder, so an edit here is live at once. There is no other copy.
- Before changing the skill, read `CONTRIBUTING.md` (glossary row numbers, lint self-tests, the 1,024 and 200 character description limits).
- New maintainer decisions go in `skills/armenian-style-guide/references/OWNER_ANSWERS.md` with the next free `A` number. Other users record theirs in their own project's `ARMENIAN_DECISIONS.md`, never in the skill.
- Paths inside the skill are relative to the skill folder; never write `~/.claude/...` or `${CLAUDE_SKILL_DIR}` there, because other agents don't resolve them.
- Run the CI checks before committing: `python skills/armenian-style-guide/scripts/lint_armenian.py --selftest`, `python tools/check_skill.py`, `python tools/build_zip.py`.
- See `CONVENTIONS.md` for repo rules and `DECISIONS.md` for why things are built this way.
