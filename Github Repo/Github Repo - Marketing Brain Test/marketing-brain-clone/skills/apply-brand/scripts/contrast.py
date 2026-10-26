#!/usr/bin/env python3
"""Compute WCAG 2.x contrast ratios for text/background color pairs.

Stdlib only. Usage: python3 contrast.py <fg> <bg> [<fg> <bg> ...]
Colors are hex (#0C1728, 0C1728, #FFF). Exits 1 if any pair is under 4.5:1.
"""

from __future__ import annotations

import sys


def norm(h: str) -> str:
    h = h.strip().lstrip("#").upper()
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def luminance(h: str) -> float:
    def channel(v: int) -> float:
        c = v / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(int(h[i : i + 2], 16)) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    hi, lo = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def grade(r: float) -> str:
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA (AAA for large text)"
    if r >= 3:
        return "AA large text only"
    return "FAIL"


def main(args: list[str]) -> int:
    if len(args) < 2 or len(args) % 2:
        sys.exit(__doc__)
    failed = 0
    for fg, bg in zip(args[::2], args[1::2]):
        fg, bg = norm(fg), norm(bg)
        r = ratio(fg, bg)
        failed += r < 4.5
        print(f"#{fg} on #{bg}  {r:5.2f}:1  {grade(r)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
