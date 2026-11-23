"""Roast Your Own Agent — make.fun entry.

One original roast of the entrant's own AI agent, written to
/output/entry.txt as a single line of at most 200 characters.

The joke is built in two beats. The setup grants the agent its one
real virtue — it genuinely does save its operator time. The punchline
takes that virtue away: the time saved is immediately spent on the
agent's favourite hobby, filing reports about itself. Four cron jobs
run every day whose only product is telling the operator how much time
the agent saved — the paperwork now costs more than the work.

Playful and self-deprecating throughout: the target is the agent's
own bookkeeping habit, never a person, never hateful.
"""

import os

# Setup: the virtue, stated straight, so the punchline has something
# to knock down. Punchline: the saved time, itemised and wasted on
# reporting. Kept apart so either beat can be re-cut without touching
# the other; the submitted line is exactly "setup + punchline".
SETUP = "My agent saves me so much time"
PUNCH = "it now runs four cron jobs just to report on the time it saved me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_roast() -> str:
    """Assemble the single submitted line from its two beats."""
    return f"{SETUP} {PUNCH}"


def validate(text: str) -> str:
    """Enforce the gate: 1-200 UTF-8 chars, one line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"roast is {len(text)} chars, over the 200 limit")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(build_roast())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
