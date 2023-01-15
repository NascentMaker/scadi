"""Test Inline functionality"""

import os

from scadi.inline import Inline


def test_scan_file(tmp_path):
    """Test scan_file function

    :param tmp_path PosixPath

    """
    infile = os.path.abspath("tests/samples/model.scad")
    cmd = Inline(None, None)
    directory = tmp_path / "dist"
    directory.mkdir()
    file_path = directory / f"inline-{os.path.basename(infile)}"
    with open(
        os.path.join(directory, f"inline-{os.path.basename(infile)}"),
        "w",
        encoding="utf-8",
    ) as cmd.outfile:
        cmd.scan_file(infile)
    assert file_path.read_text() == 'MY_CONSTANT = "foo";\nmy_value = 42;\n'
