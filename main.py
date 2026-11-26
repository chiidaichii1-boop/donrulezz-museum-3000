#!/usr/bin/env python3
"""Museum of the Year 3000 -- one museum label, one line.

The label is a fixed, hand-written line: no randomness, no input,
no network, no third-party code, so every run writes identical bytes.
"""

import os

LABEL = (
    "QR code, c. 2024, printed on a restaurant table. "
    "Humans pointed their telephones at the furniture "
    "and waited for it to bring them food."
)


def main():
    # The gate allows 1 to 200 characters; keep the label well inside it.
    assert 1 <= len(LABEL) <= 200, "label out of gate range"
    assert "\n" not in LABEL, "label must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
