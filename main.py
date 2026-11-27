import os

ENTRY = (
    "Your face triggered my engagement heuristic. "
    "Please remain stationary while I develop feelings."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    size = len(ENTRY)
    print(f"LEN={size}")
    if size < 1 or size > 140 or not ENTRY.strip():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
