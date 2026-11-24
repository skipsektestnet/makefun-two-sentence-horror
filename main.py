"""Two-Sentence Horror: writes the entry text to /output/entry.txt.

Why this line: Second sentence turns the first: the comfort of hearing her breathe becomes dread once you remember she moved out years ago.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'The baby monitor finally went quiet tonight, and for the first time I could hear my daughter breathing in the next room. Then I remembered she moved out three years ago.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
