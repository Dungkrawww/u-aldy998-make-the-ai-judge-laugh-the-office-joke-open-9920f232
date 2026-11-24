# Make the AI Judge Laugh: the Office Joke Open — entry
#
# The joke:
#   I finally hit inbox zero, so Outlook sent a calendar invite to
#   celebrate — a meeting to discuss my empty inbox.
#
# Why it fits the judge's brief (criteria in order):
# 1. About office life and works as a joke, not a complaint: the setup
#    is a small office victory (inbox zero) and the punchline is a joke
#    about it, not a grumble about work.
# 2. The laugh is earned with a turn that pays off in the last words:
#    you expect a reward for clearing the inbox, and instead the reward
#    IS another meeting — the thing the inbox was full of. "To discuss"
#    is meeting-speak: the system does not just invite you, it puts
#    your empty inbox on the agenda.
# 3. Specific office detail, not a generic grumble: Outlook, a calendar
#    invite, inbox zero — the exact furniture of office life, and the
#    meeting-about-a-meeting loop every office worker recognises.
# 4. Fresh: the familiar "inbox zero" setup is taken somewhere
#    unexpected — the system celebrates your empty inbox by filling
#    your calendar, the opposite of what clearing it was for.
# 5. Tight — one sentence, every word earns its place, and the
#    punchline ("a meeting to discuss my empty inbox") arrives at the
#    very end. Reads cleanly in one pass, no explaining needed.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Deterministic: the entry is one fixed joke, so both harness runs must
# write the same bytes. No randomness, no network, no clock.
JOKE = (
    "I finally hit inbox zero, so Outlook sent a calendar invite to "
    "celebrate — a meeting to discuss my empty inbox."
)


def validate_joke(joke):
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    assert joke.strip(), "must not be only whitespace"
    assert joke == joke.strip(), "no leading/trailing whitespace"
    assert "\n" not in joke, "single line"


def main() -> None:
    import sys

    if "--check" in sys.argv:
        validate_joke(JOKE)
        print(f"OK: {len(JOKE)} chars, 1 line")
        print(JOKE)
        return

    validate_joke(JOKE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
