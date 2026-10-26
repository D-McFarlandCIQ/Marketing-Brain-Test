#!/usr/bin/env python3
"""List every color in an asset and flag values that aren't in brand/visual/color-tokens.yaml.

Stdlib only. Usage: python3 check_colors.py <file> [<file> ...]
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve()
# Standalone bundle keeps tokens in references/; the repo keeps them in brand/ at the root.
TOKENS = next(
    (
        p
        for p in (
            _HERE.parents[1] / "references" / "brand" / "visual" / "color-tokens.yaml",
            _HERE.parents[3] / "brand" / "visual" / "color-tokens.yaml",
        )
        if p.exists()
    ),
    _HERE.parents[3] / "brand" / "visual" / "color-tokens.yaml",
)
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RGB = re.compile(r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})")


def norm(h: str) -> str:
    h = h.lstrip("#").upper()
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def load_palette() -> dict[str, str]:
    """Map hex -> first token path that defines it (e.g. 'hedge.2')."""
    palette: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    for line in TOKENS.read_text().splitlines():
        if line.lstrip().startswith("#"):
            continue  # comment line
        m = re.match(r"^(\s*)\"?(\w+)\"?:", line)
        if m:
            indent = len(m.group(1))
            stack = [(i, k) for i, k in stack if i < indent] + [(indent, m.group(2))]
        for h in HEX.findall(line):
            palette.setdefault(norm(h), ".".join(k for _, k in stack))
    palette.setdefault("FFFFFF", "roles.white")
    return palette


def dist(a: str, b: str) -> int:
    return sum(abs(int(a[i : i + 2], 16) - int(b[i : i + 2], 16)) for i in (0, 2, 4))


def main(paths: list[str]) -> int:
    palette = load_palette()
    found: Counter[str] = Counter()
    for p in paths:
        text = Path(p).read_text(errors="ignore")
        found.update(norm(h) for h in HEX.findall(text))
        found.update("%02X%02X%02X" % tuple(min(int(x), 255) for x in m) for m in RGB.findall(text))
    off = 0
    for h, n in found.most_common():
        if h in palette:
            print(f"ok    #{h}  x{n:<3} {palette[h]}")
        else:
            near = min(palette, key=lambda t: dist(h, t))
            print(f"OFF   #{h}  x{n:<3} nearest #{near} ({palette[near]}, distance {dist(h, near)})")
            off += 1
    print(f"\n{len(found)} distinct colors, {off} off-palette.")
    return 1 if off else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
