---
name: armenian-style-guide
description: Style guide for Eastern Armenian text written by AI agents - punctuation (։ ՝ « » and stress marks), the -ը / -ն article, negation, calques from Russian and English, a native speaker's decided wordings, a 1,061-term English-Armenian math, statistics and ML glossary, and a lint script. Use BEFORE writing, translating, editing, polishing or reviewing any Armenian text meant for readers, even a few words - website copy, UI labels, docs, slides, lecture notes, math solutions, posts, emails, captions, or an English-to-Armenian translation. Also use when asked for the Armenian of a math, statistics or ML term, or to 'check the Armenian', 'fix the Armenian', 'polish this Armenian' or 'հայերենը ստուգիր'. Not for chatting with the user in Armenian, quoting text verbatim, or NLP work on Armenian (tokenizers, stemming, OCR).
---

# Armenian style guide

Model-written Armenian fails in predictable ways. This skill holds what a native speaker (the maintainer, called "the owner" in the reference files) and the sources have already decided, so nobody has to ask again. It covers Eastern Armenian as written in Armenia today. It is strongest on teaching text and math, statistics and ML terms, but the punctuation, grammar and calque rules apply to any text.

All paths below are relative to this skill's folder (the folder that contains this `SKILL.md`). Use `python3` instead of `python` where that is the command name.

```bash
python scripts/lint_armenian.py --style FILE...   # under 1 s per file; exit 1 if any error
python scripts/lint_armenian.py --selftest        # 100 cases
rg -i "term" references/glossary_Apr.csv          # look up a term
```

Search Armenian text with `rg` or a dedicated search tool. On Windows, Git Bash's `grep -i` crashes on an Armenian pattern and looks like "no matches".

## Who decides

When two sources disagree, the higher one wins:

1. What the user says in the current conversation.
2. The user's project files: `ARMENIAN_DECISIONS.md` (see "Record the user's answers" below), then `CONVENTIONS.md`, `CLAUDE.md` or `AGENTS.md`.
3. `references/OWNER_ANSWERS.md`: the maintainer's decisions, A2 to A77. They are defaults, not law.
4. `references/HOUSE_RULES.md`: the standing rules.
5. `references/glossary_Apr.csv`, for terms.
6. `references/GUIDE.md`, for everything else.
7. Your own sense of what sounds natural. See "Do not trust your ear".

## Workflow

1. **Decide what you may change.** Leave proverbs, jokes, lyrics, quotations, titles of works, names of people and organizations, and lines in the author's own voice as written (`Լուրջ եմ ասում, շատ լավն ա`). Their colloquial forms are the point. If something there looks wrong, ask.
2. **Look up every technical term** in the glossary and in `references/OWNER_ANSWERS.md`, even ones you feel sure about. From memory, a model matched only 48 of 60 randomly drawn glossary terms. If a term is missing, say so and list it as a question.
3. **Write or edit** using the core rules below. For long or math-heavy text, read the matching section of `references/GUIDE.md`.
4. **Run the lint.** Fix every error and consider every hint. For a short string, put it in a temporary `.txt` file. The lint reads `.tex`, `.html`, `.md`, `.js` and `.txt`. For other formats, extract the Armenian strings first.
5. **Read the text once** following `references/POLISH_CHECKLIST.md`: terms, negation, calques, rhythm.
6. **Run the lint again.** Fixes introduce new article and punctuation slips, and this happened in every past polishing round.
7. **Report two lists:** fixes backed by a rule, and wording you are unsure about. Do not bury the second list.

## Do not trust your ear

When the maintainer checked a model's judgements on 2026-11-13, its alarms of the "this sounds Russian or unnatural" kind were right **1 time out of 9**. Points with something checkable behind them (a typo, a swapped row, a stated rule) were right **8 times out of 10**. The model's ear leans towards textbook Armenian and suspects patterns native speakers use freely.

- **Fix without asking:** lint errors, glossary mismatches, and anything a rule in `references/GUIDE.md` or `references/OWNER_ANSWERS.md` names explicitly, except `GUIDE.md` rules marked `needs native check`, which are questions for the user.
- **Ask before rewriting:** anything that merely sounds off or like a calque. Show the current wording and your suggestion, and leave the text as it is until the user answers.
- **When drafting new text,** prefer plain wording and flag the phrases you are unsure of.
- **A question the user skipped is not a yes.** Ask again rather than recording it as decided.

### Record the user's answers

Record every answer as one row in `ARMENIAN_DECISIONS.md` at the root of the user's project, so the same question never comes back. Create the file if it is missing:

```markdown
# Armenian decisions

Decisions for this project. They override the armenian-style-guide skill's defaults.

| ID | Decision | What it means in practice |
|----|----------|---------------------------|
| U1 | ... | ... |
```

Number the rows `U1`, `U2`, ... so they never clash with the maintainer's `A` numbers. Do not write answers into this skill's own files: they are replaced when the skill is updated. If an answer would help every user, suggest the user opens an issue or pull request on the skill's repository (see the end of this file).

## Core rules

**Punctuation**

- Full stop `։` (U+0589). `՝` for a colon or apposition. Quotes `« »`. Plain hyphen, no em or en dashes.
- No Latin `:` `;` `?` after Armenian. The mijaket is ASCII `.`, never `․` (U+2024).
- `՞ ՛ ՜` sit on the stressed vowel: `ինչո՞ւ`, `Ինչպե՞ս`, `Քննարկե՞լ եք`, `Խո՞սքը`. Never on a positive auxiliary or on the article `ը`.
- Openers: `Այսինքն՝`, `Օրինակ՝`, `Այսպիսով՝`, but `Հետևաբար,`, `Վերջապես,`, `Մյուս կողմից,`, `Մասնավորապես,`.
- Decimals `3,5` (`3{,}5` in TeX, a dot only in code). Dates `15 մայիսի 2018 թ.` or `15.05.2019`. Capital ու is written `Ու` at the start of a word and `ՈՒ` in all caps (`Ուջան`, `ՏՈՒՆ`).

**Grammar**

- **Article:** a word ending in a vowel always takes `-ն` (`առուն երկար է`). A word ending in a consonant takes `-ն` right before a vowel sound (`թիվն է`, `բազմությունն ունի`), otherwise `-ը`. Words starting with ե, ո (not ու) and `և` start with a consonant sound, so they take `-ը` (`թիվը երկու`), except the auxiliaries եմ, ես, ենք, եք, են (`տարրերն են`). Before a pause or a formula, a consonant-final word takes `-ը`. After a symbol, go by its spoken name (`$A$-ն`, `$x$-ը`; table in `references/GUIDE.md`, A1b). Before `ով` / `ովքեր`, and before words with an unwritten initial ը (`ստանալ`, `սկսել`, `սպասել`, `զգալ`), both articles are correct.
- **Negation:** `չ-` only on verbs and participles (`չունի`, `չհատվող`). Adjectives take `ոչ` or an antonym (`ոչ լավ`, `վատ`, `անլուծելի`), never `չլավ` or `չլուծելի`. A negated predicate negates the copula: `դատարկ չէ`, `սյուրյեկտիվ չէ`, never `ոչ սյուրյեկտիվ է`. Negative words need a negative verb (`ոչ մի տարր չի պատկանում`).
- **Numerals** take a singular noun by default (`երեք տարր`, `257 երգի`, `Երկու բազմություն հավասար են`). Plural is fine when definite (`այդ երեք բազմությունները`).
- **Reader address is plural:** `գտեք`, `հաշվեք`, `Դիտարկենք`, never `գտիր`. Plural imperatives take no stress mark. `տե՛ս` always does.
- **After a noun,** use `որ / որը`, even for people. `ով` goes after `նա`, `բոլորը`, `ամեն ոք`.
- `որպեսզի` is only for purpose. Otherwise use `որ` (`Անհրաժեշտ է, որ ...`).
- For "let" in math, use `Դիցուք` (definitions, proofs) or `Ենթադրենք` (assumptions), never `Թող`.

**Style**

- Drop pronouns the verb already carries (`ստանում ենք`, not `մենք ստանում ենք`).
- Prefer the active voice with a named actor over `... կողմից`.
- Vary `Ուստի` and sentence-opening `Սա` / `Այն`. Turn short `որը` clauses into participles, but a long definition keeps its `որը` (A45).
- Avoid: `հանդիսանալ` as "to be", `Կարևոր է նշել`, `Հեշտ է տեսնել`, `արդյունքում`, `X-ի մոտ` for Russian "у", `հարկադրել`, `պարտադրել`, `ձախողվել`, `կրում է` for information, `թողեք, որ`, `X-ը երաշխիք է`, `երաշխիք չի տալիս`, and `աշխատում է` for math "works" (programs may `աշխատել`). Do not let `իրականացնել` replace a plain verb.
- No Title Case headings. Prefer `գործընթաց` to `պրոցես` and `արդյունավետ` to `էֆեկտիվ`, but glossary terms stay as they are.

**Already approved, so do not "fix" these:** `հզոր մեթոդ`, `Իր հերթին, ...`, `X-ը, դա ... է`, `դեր չի խաղում`, `Ահա ...`, `տեղի ունի`, `ճիշտ մեկ`, `իրենից ներկայացնում է`, `հանդես է գալիս որպես` (prefer a shorter form where it fits), and scare quotes.

**Approved for math teaching text (A72), so ask before removing them elsewhere:** `հենց` as emphasis, `պարզապես` as "nothing more than", `իրականում` for a contrast. "Exactly when" stays `այն և միայն այն դեպքում, երբ`.

## Terms models get wrong

| English | Armenian | Not |
|---|---|---|
| heads / tails | ղուշ / գիր | գերբ |
| event | պատահույթ | իրադարձություն |
| random variable | պատահական մեծություն | պատահական փոփոխական |
| expectation | մաթսպասում, մաթեմատիկական սպասում | սպասվող արժեք |
| statistical sample | նմուշ | ընտրանք (combinatorics only) |
| standard deviation | ստանդարտ շեղում | միջին քառակուսային շեղում |
| equation / equality | հավասարում / հավասարություն | swapped |
| injective | ինյեկտիվ | ներարկում |
| inclusion-exclusion | կցման-արտաքսման սկզբունք | ներառման-բացառման |
| pigeonhole principle | Դիրիխլեի սկզբունք | |
| loop (graph) | ակ | օղակ |
| monotone | մոնոտոն | միապաղաղ |
| singleton | մեկկետանոց | մեկտարրանոց |
| codomain | փոփոխման տիրույթ | |
| upper bound | վերին եզր | վերին գնահատական |
| pivot | գլխավոր տարր | առանցքային տարր |
| to fix a value | ֆիքսել | ամրագրել |

In teaching text, give the English term in brackets at the first bold mention of an important term (A57).

## Rendering Armenian

- **LaTeX:** use XeLaTeX or LuaLaTeX with `fontspec` and an Armenian font (`\setmainfont{Sylfaen}` on Windows, or the free `Noto Serif Armenian` anywhere), plus `\tolerance=2000` and `\emergencystretch=3.5em`, because Armenian has no hyphenation patterns there. pdflatex stops at the first Armenian letter or `«`.
- **KaTeX:** keep Armenian and `« »` out of formulas and say it in the prose.
- **Python:** pass `encoding="utf-8"` to `open()`, and call `sys.stdout.reconfigure(encoding="utf-8")` before printing Armenian on Windows.
- **JS widgets:** text built at runtime escapes an HTML-only check, so lint the strings in the scripts too.

## References

The reference files were written inside the repository where the guide was built ([sample_problems_qysu](https://github.com/HaykTarkhanyan/sample_problems_qysu), YSU math problem sets). Read `armenian_style/...` in them as this skill's `references/` or `scripts/` folder, `discrete/glossary_discrete_focused.md` as `references/glossary_discrete_focused.md`, and `CONVENTIONS.md` as `references/HOUSE_RULES.md`. Other paths they cite (`discrete/`, `site/`, `_sources/`) are evidence in that repository, and you do not need to open them.

| File | Read it when |
|---|---|
| `references/OWNER_ANSWERS.md` | You touch any wording, term or punctuation choice that might already be decided |
| `references/HOUSE_RULES.md` | You want the short list of standing rules in one place |
| `references/GUIDE.md` | You need a rule's detail, examples or evidence. List its rules with `rg "^###" references/GUIDE.md` |
| `references/POLISH_CHECKLIST.md` | You polish a text, at step 5 |
| `references/glossary_Apr.csv` | Any math, statistics or ML term. Columns are English, Armenian, empty |
| `references/glossary_discrete_focused.md` | Discrete math, organized by topic. ⚠ rows go against instinct |
| `references/SOURCE_FINDINGS.md` | You need the Language Committee or textbook source for a rule |
| `references/QUESTIONS_FOR_NATIVE_SPEAKER.md` | You want the options and reasoning behind an `A<n>` decision |
| `references/GLOSSARY_REPORT.md` | You doubt a glossary row |
| `references/HOW_IT_WAS_BUILT.md` | You want to know how the evidence was gathered and what was never checked |
| `references/learnings/` | You want the evidence behind "do not trust your ear", the glossary traps or the lint's limits |
| `scripts/check_glossary.py` | You changed the glossary. Findings are review candidates, not failures |

## Improving this skill

The skill lives at https://github.com/HaykTarkhanyan/armenian-style-guide. A wrong rule, a missing term or a decision that should become a default goes there as an issue or pull request; `CONTRIBUTING.md` in the repository says how to change the glossary, the decisions and the lint safely. A new word exception in the lint needs a self-test case with `՞ ՛ ՜` inside the word (`ո՞վ`, `և՛`), because these marks split words for the regexes. Run `--selftest` afterwards.
