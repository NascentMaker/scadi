"""Cliff command module for the Inline command"""

import io
import logging
import os
import re

from cliff.command import Command


class Inline(Command):
    """Inline all files in use/include statements."""

    log = logging.getLogger(__name__)
    outfile: io.TextIOWrapper
    filenames = []
    statement_regex = re.compile("(use|include) <[^>]+>")

    def get_parser(self, prog_name) -> object:
        """Set up and return the parser.

        :param prog_name: name of program

        """
        parser = super().get_parser(prog_name)
        parser.add_argument("filename", nargs="?")
        return parser

    def scan_file(self, filename) -> None:
        """Scan a file for include and use statements.

        :param filename: string name of file

        """
        basename = os.path.basename(filename)
        if basename not in self.filenames:
            self.log.debug(basename)
            self.filenames.append(basename)
            with open(filename, mode="r", encoding="utf-8") as infile:
                self.log.debug("opening %s...", filename)
                directory = os.path.dirname(filename)
                for line in infile.readlines():
                    if self.statement_regex.match(line.lstrip().rstrip()):
                        incl_file = os.path.join(
                            directory, line[line.index("<") + 1 : line.index(">")]
                        )
                        if os.path.isfile(incl_file):
                            file_path = os.path.abspath(incl_file)
                            self.scan_file(file_path)
                    else:
                        self.outfile.write(line.rstrip() + "\n")

    def take_action(self, parsed_args) -> None:
        """Perform action on file

        :param parsed_args: structure of parsed arguments
        :returns: None

        """
        self.log.debug("parsed_args: %s", parsed_args)
        try:
            infile = os.path.abspath(parsed_args.filename)
            if not os.path.exists(infile):
                self.log.error("No such file or directory.")
                return
            directory = os.path.dirname(infile)
            with open(
                os.path.join(directory, f"inline-{os.path.basename(infile)}"),
                "w",
                encoding="utf-8",
            ) as self.outfile:
                self.scan_file(infile)
        except (FileNotFoundError, TypeError) as ex:
            if isinstance(ex, FileNotFoundError):
                self.log.error("No such file or directory.")
            else:
                self.log.error("Please enter a filename.")
