#!/usr/bin/env python3
"""Entry point for make.fun bounty news-image-20261125.

Copies the pre-rendered summary image (entry.png, drawn by draw.py)
to the output directory as entry.png. Deterministic: byte-identical
on every run. Standard library only, no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    sys.exit(main())
