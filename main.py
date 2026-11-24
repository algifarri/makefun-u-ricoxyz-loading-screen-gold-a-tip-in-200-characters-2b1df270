#!/usr/bin/env python3
"""Loading Screen Gold — one loading-screen tip in 200 characters.

Writes the tip to /output/entry.txt (UTF-8, 142 characters, inside the
1-200 gate). Deterministic, standard library only, no network, no
randomness, no environment input: the same bytes on every run.

The tip speaks to a stressed developer and to an AI coding agent at
once: the spinner is not stuck, the agent is re-reading your function
the way you re-read its diffs — slowly, twice, and already regretting
it. Both sides of the keyboard recognise themselves in one glance,
and the line stays short enough to read before the build finishes.
"""

import os

TIP = (
    "Tip: the spinner isn't stuck — your agent is re-reading your "
    "function the way you re-read its diffs: slowly, twice, and "
    "already regretting it."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # TIP is exactly 142 characters: inside the 1-200 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TIP)


if __name__ == "__main__":
    main()
