# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <jayesh@ambhora.com>
# --------------------------------------------------------------------------------------------------

import argparse
import os
import sys
import mori


class DirInfo:
    def __init__(self, binpath):
        self._binary_path = binpath
        self._binary_dir = os.path.dirname(self._binary_path)
        self._root_dir = os.path.dirname(self._binary_dir)
        self._share_dir = os.path.join(self._root_dir, "share")

    def binary_path(self):
        return self._binary_path

    def binary_dir(self):
        return self._binary_dir

    def root_dir(self):
        return self._root_dir

    def share_dir(self):
        return self._share_dir


def make_wide(formatter, w=140, h=100):
    """Return a wider HelpFormatter, if possible."""
    try:
        # https://stackoverflow.com/a/5464440
        # beware: "Only the name of this class is considered a public API."
        kwargs = {"width": w, "max_help_position": h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        warnings.warn("argparse help formatter failed, falling back.")
        return formatter


def define_serve_parser(subparser):
    subparser.add_argument("input_dir", help="input directory", default=os.getcwd())
    subparser.add_argument("--no-build", help="do not build the website", action="store_true")
    subparser.add_argument("--port", help="port to serve on", default=1313)
    subparser.add_argument("--tmp", help="temporary directory")


def top_level_parser():
    parser = argparse.ArgumentParser(
        description="a typesetting program",
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
    )

    subparser = parser.add_subparsers(dest="subcommand", required=True)
    serve_parser = subparser.add_parser("serve", help="serve the website")
    define_serve_parser(serve_parser)

    return parser


def main():
    dirinfo = DirInfo(os.path.realpath(sys.argv[0]))

    try:
        raw_args = sys.argv[1:]
        parser = top_level_parser()
        cli_args = parser.parse_args(raw_args)

        match cli_args.subcommand:
            case "serve":
                mori.server.serve_cli(dirinfo, cli_args)

    except ValueError as e:
        print("Error: ", e)
        print(parser.print_help())
        exit(os.EX_USAGE)
    #except Exception as e:
    #    print("Bug encountered: ", e)
    #    exit(os.EX_SOFTWARE)

    exit(os.EX_OK)
