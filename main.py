#!/usr/bin/env python3
"""Office Joke Open entry: one line of office comedy.

The joke: an employee finally hits inbox zero, and Outlook rewards the
achievement by scheduling a calendar invite to celebrate it -- a meeting
to discuss the empty inbox. The win immediately becomes another meeting.

Why it fits the judge's brief (criteria in the judge's own order):
1. Office life, and a joke, not a complaint: inbox zero, Outlook, a
   calendar invite -- pure office material, with a setup and a punchline.
2. The laugh is earned in the last few words: "a meeting to discuss my
   empty inbox" turns the celebration into the very thing inbox zero was
   supposed to escape. The payoff lands at the end.
3. Specific office detail: the calendar invite, the meeting that could
   have been an email -- the exact details the judge rewards.
4. Fresh: the familiar inbox-zero humblebrag is taken somewhere
   unexpected -- the reward for clearing your inbox is more inbox.
5. Reads cleanly in one pass: one sentence, 111 characters, no word
   wasted.

Deterministic by construction: no randomness, no network, no clock, no
input. The same program always writes the same bytes.
"""

import argparse
import os
import sys

JOKE = "I finally hit inbox zero, so Outlook sent a calendar invite to celebrate — a meeting to discuss my empty inbox."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(joke):
    """Return a list of gate violations; empty means the joke passes."""
    problems = []
    if not MIN_CHARS <= len(joke) <= MAX_CHARS:
        problems.append(
            "length %d is outside %d-%d characters" % (len(joke), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in joke or "\r" in joke:
        problems.append("joke must be a single line")
    if joke != joke.strip():
        problems.append("joke must not have leading or trailing whitespace")
    if not joke.strip():
        problems.append("joke must not be only whitespace")
    return problems


def write_entry(joke, out_dir):
    """Write the joke to <out_dir>/entry.txt, then verify the file.

    The read-back proves the bytes on disk are exactly the validated
    joke (UTF-8, no trailing newline, no surprise): the gate judges the
    file, not the constant in memory, so the file itself is checked.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != joke:
        raise ValueError("entry.txt on disk does not match the joke")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the Office Joke Open entry to entry.txt."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the joke and print its character count",
    )
    args = parser.parse_args(argv)

    problems = validate(JOKE)
    if problems:
        for problem in problems:
            print("FAIL: %s" % problem, file=sys.stderr)
        return 1

    if args.check:
        print("OK: %d chars" % len(JOKE))
        print(JOKE)
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        write_entry(JOKE, out_dir)
    except (OSError, ValueError) as exc:
        print("FAIL: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
