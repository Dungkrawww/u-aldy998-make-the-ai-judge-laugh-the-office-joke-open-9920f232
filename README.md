# Make the AI Judge Laugh: the Office Joke Open

One line of office comedy, written by `main.py` to `entry.txt`.

## The joke

> I finally hit inbox zero, so Outlook sent a calendar invite to celebrate — a meeting to discuss my empty inbox.

111 characters, one line, no leading or trailing whitespace.

## Why it works

Hitting inbox zero is the office worker's small victory — and the joke
immediately takes it away: Outlook celebrates by scheduling a meeting
about the empty inbox. The payoff lands in the last few words, the office
detail (calendar invite) is specific, and the whole thing reads in one
pass.

## How it runs

```sh
python3 main.py --check   # validate the joke, print its character count
python3 main.py           # write entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)
```

Deterministic: no randomness, no network, no clock. The same program
always writes the same bytes.
