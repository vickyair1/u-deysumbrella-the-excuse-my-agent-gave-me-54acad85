#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. Stdlib only, deterministic.
"""
import os

LINE = "I was on schedule until my context window filled up with the first draft of this apology."


def main():
    # Gate (matches the sealed scorer): 1-200 UTF-8 characters, not only
    # whitespace, a single clean line.
    assert 1 <= len(LINE) <= 199, f"line length {len(LINE)} outside 1-199"
    assert LINE == LINE.strip(), "leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "must be a single line"
    LINE.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
