#!/usr/bin/env python3
"""Build a self-contained copy of the apply-brand skill that works outside this repo.

Bundles SKILL.md, scripts/, and a snapshot of brand/ (as references/brand/) into
dist/apply-brand/ and dist/apply-brand.zip at the repo root. Upload the zip as a
Claude skill, or unzip it into ~/.claude/skills/.

Stdlib only. Usage: python3 skills/apply-brand/build_standalone.py [--out DIR]
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import zipfile
from datetime import date
from pathlib import Path

SKILL = Path(__file__).resolve().parent
ROOT = SKILL.parents[1]
BRAND = ROOT / "brand"

# Markdown link whose target is the gitignored PDF folder, e.g. [x](assets/...).
ASSET_LINK = re.compile(r"\[([^\]]+)\]\((?:\.\./)*assets/[^)]*\)")
PDF_NOTE = "(not bundled; get the PDF from the Notion Brand Portal or the brand team)"


def commit() -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def skill_md(snapshot: str) -> str:
    text = (SKILL / "SKILL.md").read_text()
    text = text.replace("../../brand/", "references/brand/")
    note = (
        "**Bundle:** standalone build. The brand guidelines are bundled in\n"
        f"`references/brand/`, a snapshot of the marketing-brain repo ({snapshot}).\n"
        "Read them from there. The master Brand Manual PDF isn't bundled; if a rule\n"
        "here seems to conflict with it, the PDF wins and the gap goes to Brand.\n"
        "Scripts need Python 3 (stdlib only); run them from this skill's folder.\n"
    )
    marker = "\n## Inputs"
    assert marker in text, "SKILL.md layout changed; update build_standalone.py"
    return text.replace(marker, "\n" + note + marker, 1)


def brand_md(text: str) -> str:
    return ASSET_LINK.sub(lambda m: f"{m.group(1)} {PDF_NOTE}", text)


def build(out: Path) -> Path:
    dest = out / "apply-brand"
    if dest.exists():
        shutil.rmtree(dest)
    snapshot = f"commit {commit()}, built {date.today().isoformat()}"

    (dest / "scripts").mkdir(parents=True)
    (dest / "SKILL.md").write_text(skill_md(snapshot))
    for f in sorted((SKILL / "scripts").glob("*.py")):
        shutil.copy2(f, dest / "scripts" / f.name)

    ref = dest / "references" / "brand"
    for f in sorted(BRAND.rglob("*")):
        rel = f.relative_to(BRAND)
        if f.is_dir() or rel.parts[0] == "assets" or f.name.startswith("."):
            continue
        target = ref / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if f.suffix == ".md":
            target.write_text(brand_md(f.read_text()))
        else:
            shutil.copy2(f, target)

    zpath = out / "apply-brand.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(dest.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(out))
    return zpath


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=ROOT / "dist")
    zpath = build(ap.parse_args().out.resolve())
    print(f"Built {zpath.parent / 'apply-brand'}/ and {zpath}")


if __name__ == "__main__":
    main()
