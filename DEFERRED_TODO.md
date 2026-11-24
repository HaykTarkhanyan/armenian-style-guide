# Deferred

- **Test the claude.ai upload once by hand.** The zip follows the documented format (folder at the root, description of 174 ASCII characters), but nobody has uploaded it yet.
- **Armenian README.** Declined for v1 (Q6, English only). Worth adding if the community asks; it would go through the skill and its lint.
- **Glossary as a dataset** (Hugging Face or similar), so people can use the terms outside agents.
- **Submit to directories:** the Claude Code plugin directory (needs a 512 px PNG icon, `claude plugin validate . --profile directory`) and community skill lists.
- **Western Armenian.** Not covered at all; would need its own rules and a native speaker.
- **Make the evidence reachable.** The reference files cite `_sources/` in `sample_problems_qysu`, which is gitignored there.
- **Lint as a standalone tool** (pre-commit hook or a pip package) for people who don't use agents.
