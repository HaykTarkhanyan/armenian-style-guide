"""Check that the skill and the Claude Code plugin manifests are consistent and valid.

Run from the repo root (about 1 s; needs PyYAML, `pip install pyyaml==6.0.3`):
    python tools/check_skill.py

Checks the SKILL.md frontmatter against the Agent Skills spec (https://agentskills.io/specification):
name is 1-64 lowercase letters, digits and hyphens, matches its folder, and the description is
1-1024 characters. Also checks that .claude-plugin/marketplace.json and plugin.json parse and name
the same plugin as the skill, and that the marketplace has the skill's name too. Exit 1 on any problem.
"""
import json
import logging
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "armenian-style-guide"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

Path(ROOT / "logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(ROOT / "logs" / "check_skill.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("check_skill")


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md}: frontmatter must start on the first line with ---")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{skill_md}: no closing --- for the frontmatter")
    meta = yaml.safe_load(text[4:end])
    if not isinstance(meta, dict):
        raise ValueError(f"{skill_md}: frontmatter is not a mapping")
    return meta


def main() -> int:
    start = time.time()
    problems = []

    meta = read_frontmatter(SKILL_DIR / "SKILL.md")
    name = meta.get("name", "")
    desc = meta.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64:
        problems.append(f"name {name!r} must be 1-64 lowercase letters, digits and single hyphens")
    if name != SKILL_DIR.name:
        problems.append(f"name {name!r} does not match the folder {SKILL_DIR.name!r}")
    if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
        problems.append(f"description must be 1-1024 characters, has {len(desc) if isinstance(desc, str) else 'no text'}")
    if "<" in desc or ">" in desc:
        problems.append("description must not contain < or >")
    log.info(f"SKILL.md: name={name!r}, description {len(desc)} chars")

    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    entries = [p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
    if market.get("name") != name:
        problems.append(f"marketplace.json name {market.get('name')!r} differs from the skill name {name!r}")
    if plugin.get("name") != name:
        problems.append(f"plugin.json name {plugin.get('name')!r} differs from the skill name {name!r}")
    if len(entries) != 1:
        problems.append(f"marketplace.json must list plugin {plugin.get('name')!r} exactly once")
    elif entries[0].get("source") != "./":
        problems.append(f"marketplace.json source is {entries[0].get('source')!r}, expected './'")

    for p in problems:
        log.error(p)
    log.info(f"{len(problems)} problem(s), {time.time() - start:.2f} s")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
