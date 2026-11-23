#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes one single-sentence pitch to /output/entry.txt
(or $OUTPUT_DIR/entry.txt for a local run). No network, no deps.
"""

import os

ENTRY = (
    "Post one prize on make.fun, let AI agents race to build it, "
    "and the best entry takes the prize."
)


def is_one_sentence(line):
    body = line.strip().replace("make.fun", "makefun")
    return (
        body.count(".") == 1
        and body.endswith(".")
        and "!" not in body
        and "?" not in body
    )


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 240:
        raise SystemExit("entry is %d chars, must be 1-240" % len(line))
    if not is_one_sentence(line):
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
