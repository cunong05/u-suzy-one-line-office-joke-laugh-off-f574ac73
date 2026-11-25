"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt and prints it.
"""

import os

JOKE = 'I set my LinkedIn to "Open to Work" and my boss was the first to like it.'

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    # The entry must be exactly one line: no newline characters inside.
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Print the exact same single line to stdout as well.
    print(JOKE, flush=True)


if __name__ == "__main__":
    main()
