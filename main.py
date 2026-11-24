"""Dog-ate-my-homework excuse printer.

Reads the one-line excuse from entry.txt next to this file and
prints it unchanged, so the submitted text is exactly what the
judge reads.
"""

import os


ENTRY_FILENAME = "entry.txt"
MAX_CHARS = 200


def load_excuse():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, ENTRY_FILENAME), encoding="utf-8") as handle:
        text = handle.read().strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        raise ValueError("entry must be one line of 1-200 characters")
    return text


def main():
    print(load_excuse())


if __name__ == "__main__":
    main()
