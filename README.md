# Armenian style guide for AI agents

An [Agent Skill](https://agentskills.io) that helps AI agents (Claude, Codex, Cursor, Copilot and others) write correct Eastern Armenian. It bundles a style guide, a native speaker's decided wordings, a 1,061-term English-Armenian math, statistics and ML glossary, and a lint script that catches the mechanical mistakes.

> **AI agent asked to install this?** Follow [INSTALL.md](INSTALL.md).

## Why

Models write Armenian with the same mistakes again and again: a Latin colon instead of `։`, the wrong article (`-ը` / `-ն`), `չ` glued to adjectives, Russian calques like `հանդիսանալ`, and math terms that sound right but are not what Armenian textbooks use. A model's own sense of "this sounds unnatural" is unreliable too: when a native speaker checked such alarms, they were right 1 time out of 9.

Example. A model wrote:

```text
Պատահական փոփոխականը հանդիսանում է ֆունկցիա, որը սահմանված է տարրական պատահույթների բազմության վրա: Մենք կարող ենք հաշվել պատահական փոփոխականի սպասվող արժեքը:
```

The lint flags the punctuation and style:

```text
before.txt:1: latin-punct: տահույթների բազմության վրա: Մենք կարող ենք հաշվել պա
before.txt:1: latin-punct: փոփոխականի սպասվող արժեքը:
before.txt:1: hint:calque-handisanal: Պատահական փոփոխականը հանդիսանում է ֆունկցիա, որը սահմա
before.txt:1: hint:redundant-menq: ույթների բազմության վրա: Մենք կարող ենք հաշվել պատահակ
```

The glossary fixes the three terms (random variable, sample space, expectation) that no lint can catch. With the skill:

```text
Պատահական մեծությունը ֆունկցիա է, որը սահմանված է տարրական ելքերի բազմության վրա։ Կարող ենք հաշվել նրա մաթսպասումը։
```

## Install

| You use | Do this |
|---|---|
| Claude Code, Codex, Cursor, Copilot, or one of 75+ other agents | `npx skills add HaykTarkhanyan/armenian-style-guide` (add `-g` to install it for all your projects) |
| Claude Code, as a plugin | `/plugin marketplace add HaykTarkhanyan/armenian-style-guide`, then `/plugin install armenian-style-guide@armenian-style-guide` |
| claude.ai or the Claude desktop app | See [claude.ai](#claudeai) below |
| Any agent that can run commands | Tell it: *"Install the skill from https://github.com/HaykTarkhanyan/armenian-style-guide by following its INSTALL.md"* |
| ChatGPT, Gemini, or anything without skills | Paste a prompt, see [No skill support](#no-skill-support) |

`npx skills` is the open-source [skills CLI](https://github.com/vercel-labs/skills) and needs Node.js 22.20 or later; `npx skills update armenian-style-guide` gets new versions. To install by hand, copy the folder `skills/armenian-style-guide/` into your agent's skills folder (for Claude Code: `~/.claude/skills/`).

### claude.ai

1. Download [armenian-style-guide.zip](https://github.com/HaykTarkhanyan/armenian-style-guide/releases/latest/download/armenian-style-guide.zip).
2. In Settings > Capabilities, turn on code execution and file creation ("Create and edit files").
3. Go to Customize > Skills, click **+**, then **Create skill** > **Upload a skill**, and pick the zip.

The zip is built by the release workflow. It is the same skill with a shorter description, because claude.ai allows at most 200 characters there.

### No skill support

[`prompts/core_rules.md`](prompts/core_rules.md) holds the core rules and the most common term traps as one prompt (about 4,500 characters). Paste it into a Claude Project's instructions, a ChatGPT project or custom GPT, a Gemini Gem, or your own system prompt. For boxes with a small limit, like ChatGPT's custom instructions, use [`prompts/core_rules_short.md`](prompts/core_rules_short.md) (about 1,000 characters). A prompt carries no glossary and no lint, so the skill does much better where you can install it.

### Update

Installed copies do not update themselves, and fixes to terms and rules land often. Update now and then:

| Installed with | Update with |
|---|---|
| `npx skills` | `npx skills update armenian-style-guide` (add `-g` if you installed it for all projects) |
| Claude Code plugin | In a shell: `claude plugin marketplace update armenian-style-guide`, then `claude plugin update armenian-style-guide@armenian-style-guide`. Or turn on auto-update for this marketplace under `/plugin` > Marketplaces |
| claude.ai zip | Download the latest zip and upload it again |
| By hand or a pasted prompt | Copy the new version over the old one |

Your own decisions are safe: they live in your project's `ARMENIAN_DECISIONS.md`, not in the skill folder.

## Use

Once installed, the skill loads by itself when you ask an agent to write, translate or polish Armenian text, or ask for the Armenian of a term. In Claude Code you can also call it with `/armenian-style-guide` (or `/armenian-style-guide:armenian-style-guide` after a plugin install).

The agent fixes what a rule names and asks you about wording that only "sounds off". It records your answers in `ARMENIAN_DECISIONS.md` in your project, so it never asks the same thing twice. Your decisions there override the skill's defaults.

The lint also works without an agent (Python 3, standard library only):

```bash
python skills/armenian-style-guide/scripts/lint_armenian.py --style yourfile.md   # .md .txt .html .tex .js
python skills/armenian-style-guide/scripts/lint_armenian.py --selftest
```

## What's inside

| Path | What it is |
|---|---|
| `skills/armenian-style-guide/SKILL.md` | The entry point: who decides, the workflow, the core rules, the term traps |
| `references/GUIDE.md` | Every rule as wrong -> right, with reason, confidence and evidence |
| `references/OWNER_ANSWERS.md` | 69 decisions by the maintainer, a native speaker (numbered A2-A80) |
| `references/glossary_Apr.csv` | 1,061 English-Armenian math, statistics and ML terms |
| `references/SOURCE_FINDINGS.md` | What the Language Committee, school textbooks and academic sources say, with citations |
| `references/POLISH_CHECKLIST.md`, `HOUSE_RULES.md` | The polishing order and the short rule list |
| `scripts/lint_armenian.py` | 15 error rules, plus house-style and style hints with `--style`, and 103 self-test cases |
| `prompts/` | The paste-in versions for tools without skills |

## How it was built, and its limits

The rules come from counting patterns in model-written text against human Armenian (Armenian Wikipedia, a university course plan, lecture notes), from the Language Committee recommendations and the school grammar textbooks, and from interviews in which the maintainer made 69 decisions. Two model baselines (12 short paragraphs each, written before reading the guide) show what models get wrong without it. [`HOW_IT_WAS_BUILT.md`](skills/armenian-style-guide/references/HOW_IT_WAS_BUILT.md) has the details, including what failed. Much of the evidence lives in [sample_problems_qysu](https://github.com/HaykTarkhanyan/sample_problems_qysu), where the guide was first written.

Limits:

- Eastern Armenian in the reformed spelling only. Western Armenian is not covered.
- It is strongest on teaching text and math. The punctuation, grammar and calque rules apply to any text, but the glossary is math, statistics and ML.
- The `A` decisions are one native speaker's choices. That is why your project's `ARMENIAN_DECISIONS.md` overrides them.
- Not checked: word order and focus, choice of verb aspect, spelling of rare words.
- The lint is mechanical. It catches punctuation, article, negation and look-alike letters, but not meaning or term choice.

## Contributing

Found a wrong rule, a missing term or a lint false positive? Open an issue with the sentence, what you expected and, if you have one, a source. See [CONTRIBUTING.md](CONTRIBUTING.md) before you change the glossary or the lint.

## License

[MIT](LICENSE)
