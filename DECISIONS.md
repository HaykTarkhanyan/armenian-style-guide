# Decisions

Newest at the top.

## 10. Three house choices are lint hints, not errors

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q10), recorded as owner decision A80.
- **Why:** A review found that `one-dot-leader` (U+2024 mijaket), `imperative-stress` and `article-before-vowel` failed the lint although GUIDE.md itself calls the other forms correct Armenian, and SKILL.md told agents to fix lint errors without asking, so strangers' correct text would be "fixed". They now come out as hints with `--style` and never change the exit code (`HOUSE_CHOICE_RULES` in `lint_armenian.py`); the self-test grew from 100 to 103 cases to check both sides.
- **Alternatives rejected:** keep them as errors with a `--skip RULE` flag (keeps the maintainer's hard check, but every user would need to know the flag); leave as is.
- **What would change this:** the maintainer's own texts start slipping on these three; then a `--strict` flag that turns them back into errors.

## 9. OWNER_ANSWERS.md holds language decisions only

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q11).
- **Why:** Five rows were about the source repo's pages, not language (which solutions may be published, solutions shown by default, A73 page layout, A56 a solution's order, the deferred discrete sweep). Every user's agent reads this file. They were removed; the file says where they went, and the other `A` numbers are unchanged.
- **Alternatives rejected:** keep them (harmless for agents, but noise and private course matters in a public file).
- **What would change this:** nothing expected.

## 8. Keep the reference files' history as is and fix only their headers

- **Date / status:** 2026-11-24, active.
- **Why:** The files cite evidence by path in `sample_problems_qysu` (`discrete/`, `site/`, `_sources/`). Rewriting every citation would lose the trail and risk changing meaning; one header per file now says where the paths point, links that public repo, and defines "the owner" as the maintainer. `_sources/` there is gitignored, so those citations stay unreachable for the public.
- **Alternatives rejected:** rewrite or strip the citations (lossy, a lot of Armenian text to touch); move the evidence files out of the skill (they are what agents read when they doubt a rule).
- **What would change this:** users report the dead paths confuse their agents.

## 7. MIT license for code and content

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q5).
- **Why:** The goal is reuse by the community; one permissive license is the simplest to explain.
- **Alternatives rejected:** MIT for scripts plus CC BY 4.0 for guide and glossary (two licenses to explain); no license (visible but not reusable).
- **What would change this:** the glossary or decisions get copied without credit in a way the maintainer minds.

## 6. No `version` in plugin.json; tags only for the claude.ai zip

- **Date / status:** 2026-11-24, active.
- **Why:** Without `version`, Claude Code plugin users get the latest commit on update, and `npx skills` tracks commits anyway. A version field would make every glossary fix wait for a version bump. `claude plugin validate` warns about the missing version; that warning is accepted.
- **Alternatives rejected:** semver in plugin.json synced to tags (more ceremony for a content skill that changes in small steps).
- **What would change this:** a breaking change that users must opt into.

## 5. The repo is the only copy; the maintainer's global skill is a junction to it

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q3). Replaces the maintainer's earlier private backup copy of the skill.
- **Why:** One place to edit; GitHub is the backup; the maintainer's sessions see an edit at once.
- **Alternatives rejected:** install from GitHub like every user (every fix needs a push and an update before the maintainer gets it); keep a separate personal copy (drifts).
- **What would change this:** the maintainer needs personal rules that must not be public; they then go in the global `CLAUDE.md`, not in a second copy.

## 4. Skill paths are relative to the skill folder, not `${CLAUDE_SKILL_DIR}`

- **Date / status:** 2026-11-24, active.
- **Why:** The Agent Skills spec says to reference files by relative path from the skill root. `${CLAUDE_SKILL_DIR}` is substituted only by Claude Code; elsewhere it stays literal text, and in a shell it expands to empty, so `${CLAUDE_SKILL_DIR}/scripts/x.py` becomes `/scripts/x.py`.
- **Alternatives rejected:** `${CLAUDE_SKILL_DIR}` (Claude Code only); `~/.claude/skills/...` (wrong for project installs, plugins and every other agent).
- **What would change this:** the spec adds a portable variable for the skill folder.

## 3. The maintainer's decisions are defaults; each user's decisions live in their project

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q2).
- **Why:** The 68 `A` decisions are the skill's main value, but they are one native speaker's taste. Users' agents record their answers in `ARMENIAN_DECISIONS.md` at their project root with `U` numbers, which override the defaults and survive skill updates (which replace the skill folder).
- **Alternatives rejected:** keep "Hayk decides" wording (other users' agents would think they must ask Hayk); keep only source-backed rules (loses the calque list, terms and most decisions).
- **What would change this:** many users override the same `A` decision; then the default should change.

## 2. Ship one skill folder through four paths: `npx skills`, a Claude Code marketplace, a claude.ai zip, and paste-in prompts

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q4), plus CI.
- **Why:** The same `skills/armenian-style-guide/` folder serves all of them. `npx skills add` covers Claude Code, Codex, Cursor, Copilot and 75+ agents (vercel-labs/skills README, checked 2026-11-24). The repo root doubles as a Claude Code marketplace with `"source": "./"` (docs checked 2026-11-24). claude.ai needs a zip with a description of at most 200 characters (support article 12512198), so `tools/build_zip.py` swaps in `SHORT_DESCRIPTION` instead of shortening the description that every other agent uses to decide when to load the skill. `prompts/` serves ChatGPT, Gemini and tools without skills.
- **Alternatives rejected:** a 200-character description for everyone (worse triggering, where Agent Skills allows 1,024); separate packages per agent (duplicated content); an npm or pip package (no agent reads those as skills).
- **What would change this:** claude.ai raises its limit (drop the swap), or a path proves unused.

## 1. Name: `armenian-style-guide` for the repo, skill, plugin and marketplace

- **Date / status:** 2026-11-24, active. Chosen by Hayk (Q1). The repo was created as `armenian-lang-agents` and renamed; the skill was `armenian-writing` in the maintainer's global skills.
- **Why:** The most self-explanatory name for people who don't speak Armenian and for agents.
- **Alternatives rejected:** `hayeren` (short, but unreadable to non-Armenian speakers); `armenian-writing` with repo `armenian-agent-skills` (keeps the old name); keeping `armenian-lang-agents`.
- **What would change this:** more Armenian skills join the repo; then a collection name for the repo, keeping this skill's name.
