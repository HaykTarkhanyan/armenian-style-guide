# Contributing

Thanks for helping agents write better Armenian. The most useful contributions are concrete: a sentence a model got wrong, the right version, and why.

## Reporting a problem

Open an issue with:

- the Armenian text, what the skill or lint did, and what you expected;
- a source if you have one (Language Committee page, textbook, dictionary), or say that it is your judgement as a native speaker;
- for a lint false positive, the exact line and the rule name the lint printed.

## Changing the skill

Everything the agent reads is in `skills/armenian-style-guide/`. Before you open a pull request:

- **Glossary** (`references/glossary_Apr.csv`): keep existing row numbers stable, because the guide cites rows by number. Add new terms at the end or in alphabetical position only if no row number cited elsewhere moves. Run `python skills/armenian-style-guide/scripts/check_glossary.py` and look at its findings (they are review candidates, not failures).
- **Lint** (`scripts/lint_armenian.py`): every new rule or word exception needs a self-test case. A word exception needs a case with `՞ ՛ ՜` inside the word (`ո՞վ`, `և՛`), because these marks split words for the regexes. Run `--selftest`, and run the lint on some real Armenian text to check for new false positives.
- **Rules** (`references/GUIDE.md`): give each rule wrong -> right, the reason, a confidence level and the evidence. A rule that rests only on how something sounds is marked `needs native check`.
- **Maintainer decisions** (`references/OWNER_ANSWERS.md`): only the maintainer adds rows here, with the next free `A` number. If you disagree with one, open an issue; projects can override any decision in their own `ARMENIAN_DECISIONS.md` meanwhile.
- **SKILL.md**: keep the frontmatter `description` under 1,024 characters and the file short; details belong in `references/`. If you change the description, check that `SHORT_DESCRIPTION` in `tools/build_zip.py` still matches.

Then run the same checks as CI:

```bash
python skills/armenian-style-guide/scripts/lint_armenian.py --selftest
python tools/check_skill.py        # needs: pip install pyyaml==6.0.3
python tools/build_zip.py
```

## Releases

The maintainer pushes a tag (`v1.2.0`); the release workflow builds `armenian-style-guide.zip` and attaches it to a GitHub release. Plugin and `npx skills` users get the latest commit on `main` whenever they update, so a release is only needed for the claude.ai zip.
