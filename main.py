"""Make the Judge Smile — one small good thing from this morning.

The line is fixed: a bus driver waits, an elderly neighbour boards with
her shopping, and the whole bus applauds. The program only has to land
it inside the sealed gate (UTF-8, 1-200 chars, not only whitespace), so
it checks its own output before writing.
"""

ENTRY_LINE = (
    "This morning the bus driver held the doors while Mrs. Chen from 4B "
    "shuffled across with two bags of oranges — and when she finally sat "
    "down, the whole bus applauded."
)

MAX_ENTRY_CHARS = 200


def checked_entry() -> str:
    """Return the entry line after asserting it fits the gate."""
    assert ENTRY_LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY_LINE) <= MAX_ENTRY_CHARS, "entry must be 1-200 chars"
    ENTRY_LINE.encode("utf-8")  # raises if the line is not UTF-8 encodable
    return ENTRY_LINE


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(checked_entry())


if __name__ == "__main__":
    main()
