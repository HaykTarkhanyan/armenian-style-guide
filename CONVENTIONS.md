# Conventions

- **Not client facing.** The maintainer's own public repo: commit and push without asking. Never force-push or rewrite pushed history.
- **One name everywhere:** `armenian-style-guide` is the repo, the skill folder, the frontmatter `name`, the plugin and the marketplace. Changing it means changing all five (and `tools/check_skill.py` checks they agree).
- **Docs are in English**, plain and short. Armenian appears only as rules, examples and terms, and passes the skill's own lint except for deliberate "not this" examples.
- **Paths in the skill are relative to the skill folder.** Commands in the skill say `python`; the skill tells agents to use `python3` where that is the command name.
- **Releases** are tags `vMAJOR.MINOR.PATCH`; the release workflow attaches the claude.ai zip. A new maintainer decision or glossary fix is a patch, a new rule or lint check a minor version.
- **Scripts** in `tools/` use `logging` (console plus `logs/<script>.log`, gitignored) and the standard library, except PyYAML in `check_skill.py`. The skill's own scripts stay standard-library only, so users need nothing installed.
- **Dependencies are pinned** with `==` (PyYAML 6.0.3 in CI).
