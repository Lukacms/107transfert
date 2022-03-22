##
## EPITECH PROJECT, 2022
## 106bombyx
## File description:
## parse_args
##

from argparse import ArgumentError, ArgumentTypeError, ArgumentParser
from typing import NamedTuple
from sys import argv

from sys import exit


class Arguments(NamedTuple):
    arg: list[str]


def valid_arg(arg: str) -> str:

    nb: int
    split_arg: list[str] = arg.split("*")

    for string_nb in split_arg:
        try:
            nb = int(string_nb)
        except ValueError:
            raise ArgumentTypeError(f"Parameter {split_arg} isn't an integer")
    return arg


def parse_args() -> Arguments:
    parser = ArgumentParser()

    if (
        len(argv) % 2 == 0
        and (len(argv) != 2 and (argv[1] != "-h" or argv[1] != "--help"))
        or len(argv) <= 2
    ):
        exit(84)

    parser.add_argument("args", type=valid_arg, help="list of num and den", nargs="*")

    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)

    return Arguments(args.args)
