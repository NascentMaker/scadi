"""pytest tests for Inline class"""

from scadi.inline import Inline


def test_get_parser():
    """Test Cliff command"""
    cmd = Inline(None, None)
    parser = cmd.get_parser("NAME")
    assert parser.prog == "NAME"
