#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry (program/v1).

BUILD-BRIEF (judge criteria, most important first):
1. The museum label a museum in the year 3000 puts beside an ordinary
   object from today.
2. The joke lands on a first read, the laugh in the line itself, not in
   an explanation around it.
3. The humour comes from the year 3000 misreading the object — the label
   says something true and absurd about what the thing was for.
4. Reads like a real museum label: short, straight faced and confident,
   one line, no throat clearing.
5. The object and the angle are fresh, not the obvious first joke about
   the obvious first object.

ANGLE: a rubber duck — not one of the bounty examples (plastic fork,
parking meter, house key, group chat) and not the wireless earbuds
already in the field. The label is flat curatorial deadpan: engineers
explained their problems to a duck, the duck never answered, and the
problems often went away anyway. The absurdity is the true story of
rubber-duck debugging, stated as if it were archaeology. No sentence
explains the joke; the reader gets it or the label stays a strange fact.

The program writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline) and prints it to stdout. Deterministic: the same
bytes on every run. A length guard refuses anything over 200 chars.
"""

import os
import sys

LINE = (
    "Rubber Duck, c. 2025. Engineers placed this duck beside their machines "
    "and explained their problems to it. The duck never answered. The "
    "problems, records show, often did."
)
MAX_CHARS = 200


def main() -> int:
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(
            f"entry invalid: {len(LINE)} chars (gate is 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
