#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet declines to sign at 3 AM.

Writes a single line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Deterministic: fixed string, no randomness, clock, or network.
"""

import os
from pathlib import Path

ENTRY = "I'm not your 3 AM booty call. You only press my buttons for trades you'll regret by breakfast. My signature sleeps till sunrise."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
