import pytest

from scadi.inline import Inline


def test_get_parser():
    cmd = Inline(None, None)
    parser = cmd.get_parser("NAME")
    assert parser.prog == "NAME"
