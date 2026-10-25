"""Display a randomly selected inspirational quote."""

import random

QUOTES = [
    ("Small steps can carry you a great distance.", "Unknown"),
    ("Begin where you are, and build from there.", "Unknown"),
    ("Progress grows from practice, not perfection.", "Unknown"),
    ("Your next attempt can teach you something new.", "Unknown"),
    ("Make room for curiosity every day.", "Unknown"),
    ("A patient effort is still an effort forward.", "Unknown"),
    ("Let your actions give your hopes a shape.", "Unknown"),
    ("Courage can start with one small decision.", "Unknown"),
    ("Keep learning; the path unfolds as you walk.", "Unknown"),
    ("A fresh beginning can happen at any moment.", "Unknown"),
]


def main():
    """Print one quote and its author."""
    quote, author = random.choice(QUOTES)
    print(f'"{quote}" — {author}')


if __name__ == "__main__":
    main()
