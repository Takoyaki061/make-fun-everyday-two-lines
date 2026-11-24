#!/usr/bin/env python3
"""Everyday Things, Two Lines — microwave entry.

Writes the chosen two-line explanation to /output/entry.txt.
Line 1 explains a microwave to a 10-year-old with one vivid analogy;
line 2 says honestly what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A microwave is a box that makes the tiny drops of water inside your food "
    "dance so fast that the dancing itself turns into heat, cooking your dinner "
    "without any flame.\n"
    "The dancing water explains why food gets hot with no fire and no hot oven "
    "walls, but it leaves out that only water dances, so dry bread barely warms "
    "and the edges can end up hotter than the middle.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
