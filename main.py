#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — the yogurt, logged and judged.

The joke: the fridge is a meticulous record-keeper — it logged the
yogurt's expiry, held it at exactly 4 degrees the whole time, and
watched the owner open the door six times a day and choose nothing.
"Per my last notification" is the corporate passive-aggressive opener,
and the sting is the comparison: the appliance finishes what it
starts, the human does not. Small, domestic, specific — a note the
fridge would actually keep on its door screen. The em dash sets up the
turn; the last clause is the whole grudge in eight words.
"""

import os
from pathlib import Path

LINE = "Per my last notification, the yogurt expired on Tuesday. I kept it at 4\u00b0C anyway \u2014 unlike you, I finish what I start."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
