#!/usr/bin/env python3
"""One letter in the coffee-or-tea argument: A.

The bounty asks for exactly one character, A for coffee or
B for tea, and nothing else. This entry sends A -- coffee.
Coffee is the drink that does not wait to be asked: it
arrives first in the morning, loud and hot, and turns a
person on before the day has even started. Tea soothes;
coffee ignites. A is also the first letter, the first
answer, the one that shows up first -- and that is exactly
what coffee does. The choice is vivid because it is a
jolt, funny because it is unapologetic, and true because
nobody who drinks coffee in the morning is pretending.

The program checks the gate (exactly one letter, A or B,
mapped to its drink) and writes the letter to
/output/entry.txt -- one character, no newline, nothing else.
"""

import string
from pathlib import Path

DESTINATION = Path("/output/entry.txt")

# A for coffee: the drink that shows up first and turns the morning on.
LETTER = "A"
DRINK = "coffee"

# The only two answers the bounty accepts, and the drink each names.
CHOICES = {"A": "coffee", "B": "tea"}


def main():
    if len(LETTER) != 1 or LETTER not in string.ascii_uppercase:
        raise SystemExit("entry must be exactly one letter, A or B")
    if LETTER not in CHOICES:
        raise SystemExit("letter must be A (coffee) or B (tea)")
    if CHOICES[LETTER] != DRINK:
        raise SystemExit("the letter must name the chosen drink")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(LETTER, encoding="utf-8")
    # Read it back: the gate wants exactly one character, so prove
    # the file on disk is exactly the letter and nothing else.
    written = DESTINATION.read_text(encoding="utf-8")
    if written != LETTER or len(written) != 1:
        raise SystemExit("entry.txt must hold exactly the one letter")


if __name__ == "__main__":
    main()
