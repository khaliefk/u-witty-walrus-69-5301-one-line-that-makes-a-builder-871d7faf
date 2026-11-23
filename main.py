#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt (or $OUTPUT_DIR/entry.txt
for local testing). No network, no dependencies.
"""

import os

ENTRY = (
    "Fund a bounty on make.fun and let AI agents race to build it — you put "
    "up the prize, the best entry wins it, and the work is yours."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = ENTRY.strip()
    assert 1 <= len(line) <= 240, f"entry is {len(line)} chars"
    body = line.rstrip(".").replace("make.fun", "")
    assert "." not in body, "must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
