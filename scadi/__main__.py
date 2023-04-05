"""
 Copyright 2021 Torgny Bjers <torgny@bjers.org>.
 SPDX-License-Identifier: MIT

Entry point for cliff CLI application"""

import sys

from scadi.main import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
