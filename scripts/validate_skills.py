#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINE_RE = re.compile(r"^(name|description):\s*(.+)$")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    content = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        raise ValueError("missing or invalid YAML frontmatter block")

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line_match = LINE_RE.match(line)
        if not line_match:
            raise ValueError(f"unsupported frontmatter line: {raw_line}")
        key, value = line_match.groups()
        data[key] = value.strip()
    return data


def validate_openai_yaml(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    required_snippets = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
    ]
    for snippet in required_snippets:
        if snippet not in text:
            issues.append(f"missing `{snippet}`")
    return issues


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"[FAIL] Missing skills directory: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print("[FAIL] No skill directories found")
        return 1

    failures = 0

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            print(f"[FAIL] {skill_dir.name}: missing SKILL.md")
            failures += 1
            continue

        try:
            frontmatter = parse_frontmatter(skill_md)
        except ValueError as exc:
            print(f"[FAIL] {skill_dir.name}: {exc}")
            failures += 1
            continue

        expected_keys = {"name", "description"}
        actual_keys = set(frontmatter)
        if actual_keys != expected_keys:
            print(
                f"[FAIL] {skill_dir.name}: frontmatter keys must be exactly "
                f"{sorted(expected_keys)}, found {sorted(actual_keys)}"
            )
            failures += 1

        skill_name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if skill_name != skill_dir.name:
            print(
                f"[FAIL] {skill_dir.name}: frontmatter name `{skill_name}` "
                f"does not match folder name"
            )
            failures += 1

        if not NAME_RE.match(skill_name):
            print(f"[FAIL] {skill_dir.name}: invalid skill name `{skill_name}`")
            failures += 1

        if not description or description.startswith("[TODO"):
            print(f"[FAIL] {skill_dir.name}: missing description")
            failures += 1

        if "[TODO" in skill_md.read_text(encoding="utf-8"):
            print(f"[FAIL] {skill_dir.name}: unresolved TODO marker found")
            failures += 1

        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            yaml_issues = validate_openai_yaml(openai_yaml)
            for issue in yaml_issues:
                print(f"[FAIL] {skill_dir.name}: agents/openai.yaml {issue}")
                failures += 1

    if failures:
        print(f"[FAIL] Validation failed with {failures} issue(s)")
        return 1

    print(f"[OK] Validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
