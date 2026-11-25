#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
Pure Python standard library only; no third-party packages.
"""

import os

LINE = (
    "The office printer only jams on documents marked urgent \u2014 "
    "I've decided that's a union rule it negotiated "
    "while we were all at lunch."
)


def main() -> None:
    # The sealed scorer gates on 1-200 chars of UTF-8 text, not only
    # whitespace, on a single line. Fail loudly here rather than ship
    # an entry the gate would refuse.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
