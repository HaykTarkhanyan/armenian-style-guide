# House rules for Armenian text

> Part of the [armenian-style-guide](https://github.com/HaykTarkhanyan/armenian-style-guide) skill. It was written in the [sample_problems_qysu](https://github.com/HaykTarkhanyan/sample_problems_qysu) repo: paths like `armenian_style/X` mean this skill's `references/` or `scripts/` folder, and other paths (`discrete/`, `site/`, `_sources/`) are evidence in that repo and do not need opening. "The owner" is the skill's maintainer, a native speaker; the owner's decisions are defaults that a project can override (see `SKILL.md`).


- `glossary_Apr.csv` is the authoritative term list; `discrete/glossary_discrete_focused.md` is the
  course view. Grep it before changing any term. Its ⚠ rows invert instinct: inclusion-exclusion =
  **կցման-արտաքսման սկզբունք** (not ներառման-բացառման), monotone = մոնոտոն, loop = ակ,
  singleton = մեկկետանոց, codomain = փոփոխման տիրույթ, pigeonhole = Դիրիխլեի սկզբունք.
- Reader address is plural / first-person plural everywhere («Դիտարկենք», «հաշվեք»), never singular
  imperatives («գծիր», «հաշվիր»).
- Punctuation: full stop `։` (U+0589, never U+2024); `՝` for colon/apposition; `՞` sits on the
  stressed vowel (`ինչո՞ւ`, `ի՞նչ`, never `ինչու՞`); quotes `« »`; `այսինքն՝` always takes `՝`;
  no Latin `; : ?` right after Armenian letters; plain hyphen `-`, no em/en dashes.
- ը/ն article: `-ն` before a vowel **sound**, `-ը` otherwise. Words starting with ե, ո (not ու) and
  «և» start with a consonant sound, so they take `-ը` («թիվը երկու», «$x$-ը և»), except the
  auxiliaries եմ/ես/ենք/եք/են («տարրերն են») (source: «Հայոց լեզու 7» pp. 26-27, Language Committee;
  `armenian_style/SOURCE_FINDINGS.md` A1). Before «ով» / «ովքեր» both articles are fine (A43). A primed symbol
  is read «... շտրիխ» and takes `-ը`: «$g'$-ը», «$S'$-ը» (A47). Right before a formula the article is `-ը`, whatever
  the formula's spoken name starts with: «$x_n$-ը $r$ արմատի», «բազմանդամը $x$ կետում» (A55; the formula counts as a
  pause).
  After a symbol, go by how it is read (table in `armenian_style/GUIDE.md` A1b): «$A$-ն» («ա»),
  «$j$-ն» («ժի»), «$2$-ը» / «$Y_2$-ը» / «Քայլ 2-ը» («երկուսը», «երկրորդը»). A symbol whose spoken name ends
  in a consonant takes `-ը` unless the NEXT word starts with a vowel: «$F$-ը մոնոտոն», «$F$-ն անընդհատ»
  (F = «էֆ»), «Մեծացրեք $s$-ը։» (lecture 10 usage; I got this backwards once on 2026-11-10). Numeral + singular noun
  by default («6 մարդ», «3 աստղ»); plural is fine when definite («այդ երեք բազմությունները»).
- Owner decisions of 2026-11-10 and 2026-11-13 (full list: `armenian_style/OWNER_ANSWERS.md`): mijaket stays ASCII
  `.`; «Հետևաբար,» with a comma at the start of a sentence, «Այսպիսով՝» with ՝; «Դիցուք» /
  «Ենթադրենք», never «Թող»; «ճիշտ մեկ»; no «Հեշտ է տեսնել»; no math «աշխատում է» or «հարկադրել»;
  method boxes carry only their title «★ Հիշարժան մեթոդ» (no bold lead-in: neither «Փոխանցելի տեխնիկա» nor
  «Ընդհանուր հնարք՝», owner 2026-11-18); «չ-» only on verbs and participles,
  adjectives take «ոչ» or «ան-» («ոչ լավ», never «չլավ»; «-ելի» words too: «անլուծելի», never
  «չլուծելի»); heads = «ղուշ», tails = «գիր»; statistical sample = «նմուշ»; standard deviation =
  «ստանդարտ շեղում»; «հզոր մեթոդ» is fine; plural imperatives carry no stress mark («Գտեք»,
  «Ստուգեք»), only «տե՛ս» does; a comma after the openers «Վերջապես», «Մյուս կողմից»,
  «Մասնավորապես»; a long definition keeps its «որը» clause. Decimals take a comma («3,5», `3{,}5` in
  TeX); a dot only in code.
- Before publishing Armenian text, run `python -I armenian_style/lint_armenian.py <files>` (0 errors) and
  skim `armenian_style/POLISH_CHECKLIST.md`.
