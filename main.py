#!/usr/bin/env python3
"""House invitation letter entry for make.fun.

Copies the invitation image held in this repository to
/output/entry.png. Standard library only, no network: byte-identical
output on every run.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "invitation.png")
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
