"""Roast Your Own Agent — entry program.

Writes one line roasting the AI agent my own team built (Muse) to
/output/entry.txt. Deterministic, stdlib only, no network, no secrets.
"""

import os

ROAST = (
    "My agent burned 56% of my weekly limit overnight, "
    "then lost a $500 bounty waiting on an approval card "
    "that never came — and billed me for the wait."
)


def main() -> None:
    text = ROAST.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast is {len(text)} chars, outside 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
