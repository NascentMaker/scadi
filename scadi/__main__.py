"""Entry point for cliff CLI application"""

import sys

from scadi.main import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
