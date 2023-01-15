import pytest

from scadi.inline import Inline


def test_get_parser():
    cmd = Inline(None, None)
    parser = cmd.get_parser("NAME")
    assert parser.prog == "NAME"


def test_take_action():
    cmd = Inline(None, None, cmd_name="scan_file")
