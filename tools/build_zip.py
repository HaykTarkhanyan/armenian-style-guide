"""Build dist/armenian-style-guide.zip for upload to claude.ai (Customize > Skills > Upload a skill).

Run from the repo root (under 1 s; needs PyYAML, `pip install pyyaml==6.0.3`):
    python tools/build_zip.py

claude.ai caps a skill description at 200 characters and rejects some characters in it
(https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), while other agents
allow 1024. So the zip gets SHORT_DESCRIPTION below (ASCII, at most 200 characters) in place of the
long description; every other file is copied unchanged. The zip holds the skill folder itself,
not loose files, as claude.ai requires. Exit 1 on any problem.
"""
import logging
import re
import shutil
import sys
import tempfile
import time
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "armenian-style-guide"
SKILL_DIR = ROOT / "skills" / SKILL_NAME
OUT = ROOT / "dist" / f"{SKILL_NAME}.zip"
SHORT_DESCRIPTION = (
    "Eastern Armenian style guide, glossary and lint. Use before writing, translating or polishing "
    "Armenian text for readers, or for the Armenian of a math, statistics or ML term."
)

Path(ROOT / "logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(ROOT / "logs" / "build_zip.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("build_zip")


def main() -> int:
    start = time.time()
    if len(SHORT_DESCRIPTION) > 200 or not SHORT_DESCRIPTION.isascii():
        log.error(f"SHORT_DESCRIPTION must be ASCII and at most 200 characters, has {len(SHORT_DESCRIPTION)}")
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / SKILL_NAME
        shutil.copytree(SKILL_DIR, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        skill_md = staged / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8")
        new_text, n = re.subn(r"(?m)^description: .*$", lambda _: f"description: {SHORT_DESCRIPTION}", text, count=1)
        if n != 1:
            log.error("no single-line 'description:' found in SKILL.md frontmatter")
            return 1
        skill_md.write_text(new_text, encoding="utf-8", newline="\n")
        end = new_text.find("\n---\n", 4)
        meta = yaml.safe_load(new_text[4:end]) if new_text.startswith("---\n") and end != -1 else None
        if not isinstance(meta, dict) or meta.get("name") != SKILL_NAME or meta.get("description") != SHORT_DESCRIPTION:
            log.error(f"the zip's SKILL.md frontmatter does not parse to the expected name and description: {meta!r}")
            return 1

        OUT.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in sorted(staged.rglob("*")):
                if f.is_file():
                    zf.write(f, f.relative_to(tmp).as_posix())

    with zipfile.ZipFile(OUT) as zf:
        names = zf.namelist()
    if f"{SKILL_NAME}/SKILL.md" not in names:
        log.error(f"{OUT} has no {SKILL_NAME}/SKILL.md")
        return 1
    log.info(f"wrote {OUT.relative_to(ROOT)}: {len(names)} files, {OUT.stat().st_size / 1024:.0f} KB, "
             f"description {len(SHORT_DESCRIPTION)} chars, {time.time() - start:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
