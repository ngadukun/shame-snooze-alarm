"""One-Sentence Absurd Invention Pitch - make.fun entry.

A single sentence, at most 220 characters, pitching a ridiculous
invention that fixes a tiny everyday annoyance: the alarm clock
that weaponises embarrassment against the snooze button.
Deterministic, stdlib only, no network. Running it writes the
pitch to output/entry.txt and prints it.
"""

from pathlib import Path

LINE = (
    "Introducing ShameSnooze: the alarm clock that, after your third "
    "snooze, texts your boss a live photo of you drooling — so the "
    "only way to stop it is to actually get up."
)

MAX_CHARS = 220


def validate() -> None:
    """The gate in one place: exactly one sentence, at the cap or under."""
    assert 0 < len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    assert "\n" not in LINE, "one line only"
    assert LINE.count(".") == 1 and LINE.endswith("."), "one sentence only"


def main() -> None:
    validate()
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
