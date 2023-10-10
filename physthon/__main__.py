from __future__ import annotations

import os

from argparse import ArgumentParser
from sysconfig import get_paths

import rich
from lark import Lark

from physthon import __author__, __version__


def gen_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Command interface for Physthon.",
        prog="Physthon",
    )

    parser.add_argument("--author", action="store_true")
    parser.add_argument("--version", action="store_true")

    parser.add_argument(
        "--hook",
        action="store_true",
        help="Hook the codec loader.",
    )

    parser.add_argument("--run", help="Run a file.")
    return parser


def main() -> None:
    parser = gen_parser()
    args = parser.parse_args()

    if args.version is True:
        print(f"Physthon {__version__}")

    elif args.author is True:
        print(__author__)

    elif args.hook is True:
        path = get_paths()["purelib"]

        with open(path + "/physthon_autoload.pth", "a") as fp:
            fp.write("import physthon")

        print(f"Wrote `physthon_autoload.pth` to {path}")

    elif args.run:
        path = os.path.dirname(__file__)

        with open(f"{path}/parser/grammar.lark", "r") as fp:
            parser = Lark(
                fp.read(), start="module", parser="lalr", propagate_positions=True
            )
        
        with open(args.run, "r") as fp:
            rich.inspect(parser.parse(fp.read()))

if __name__ == "__main__":
    main()
