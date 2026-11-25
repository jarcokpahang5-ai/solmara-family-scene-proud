#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Feel Proud: A Family Scene".

Writes one short family scene (one line, under 280 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) and prints the
identical text to stdout.

Pure Python 3.13 standard library, deterministic, no network.
"""

import os

SCENE = (
    "Mum still saves Dad the burnt corner of the lasagne, because "
    "thirty years ago he called it his favourite part \u2014 "
    "and in thirty years he has never once corrected her."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE + "\n")
    print(SCENE)


if __name__ == "__main__":
    main()
