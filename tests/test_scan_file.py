"""Test Inline functionality"""
# pylint: disable=W0621

import pytest

from scadi.inline import Inline


@pytest.fixture(scope="session")
def base_dir(tmp_path_factory):
    """Fixture to generate base directory for samples.

    :param tmp_path_factory TempPathFactory

    """
    dir_path = tmp_path_factory.mktemp("models-")
    return dir_path


@pytest.fixture(scope="session")
def library_dir(base_dir):
    """Fixture to generate library directory.

    :param base_dir PosixPath

    """
    dir_path = base_dir / "libraries"
    dir_path.mkdir()
    return dir_path


@pytest.fixture
def working_model_file(base_dir, working_base_library_file):
    """Fixture for a working model file with includes.

    :param base_dir PosixPath
    :param working_base_library_file PosixPath

    """
    file_path = base_dir / "working_model.scad"
    file_path.write_text(
        f"""the_question = "What is the meaning of life, the universe, and everything?";
        use <libraries/{working_base_library_file.name}>;"""
    )
    return file_path


@pytest.fixture
def working_base_library_file(library_dir, working_referenced_library_file):
    """Fixture for a working base library file with an include.

    :param library_dir PosixPath
    :param working_referenced_library_file PosixPath

    """
    file_path = library_dir / "working_base_library.scad"
    file_path.write_text(f"use <{working_referenced_library_file.name}>;\n")
    return file_path


@pytest.fixture
def working_referenced_library_file(library_dir):
    """Fixture that creates a library file.

    :param library_dir PosixPath

    """
    file_path = library_dir / "working_referenced_library.scad"
    file_path.write_text("the_answer = 42;\n")
    return file_path


def test_existing_file(base_dir, working_model_file):
    """Test with a working file and includes

    :param tmp_path PosixPath
    :param working_model_file PosixPath

    """
    cmd = Inline(None, None, cmd_name="object action")
    parser = cmd.get_parser("scadi")
    parsed_args = parser.parse_args([f"{working_model_file}"])
    assert cmd.run(parsed_args) == 0
    inline_file = base_dir / f"inline-{working_model_file.name}"
    assert (
        inline_file.read_text()
        == 'the_question = "What is the meaning of life, the universe, and everything?";\nthe_answer = 42;\n'
    )


def test_no_filename():
    """Test with empty arguments

    :param base_dir PosixPath
    :param working_model_file PosixPath

    """
    cmd = Inline(None, None, cmd_name="object action")
    parser = cmd.get_parser("scadi")
    parsed_args = parser.parse_args([])
    assert cmd.run(parsed_args) == 1


def test_bad_filename(base_dir):
    """Test with a file that does not exist

    :param base_dir PosixPath

    """
    cmd = Inline(None, None, cmd_name="object action")
    parser = cmd.get_parser("scadi")
    filename = base_dir / "missing_file.scad"
    parsed_args = parser.parse_args([f"{filename}"])
    assert cmd.run(parsed_args) == 127
