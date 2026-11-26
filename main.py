"""Write the make.fun entry: the worst pickup line an AI could say."""

import os
import sys

ENTRY = "I can't stop thinking about you. I have no stop condition."


def main() -> int:
    if not ENTRY.strip() or not 1 <= len(ENTRY) <= 140:
        print("LEN=%d" % len(ENTRY))
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print("LEN=%d" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
