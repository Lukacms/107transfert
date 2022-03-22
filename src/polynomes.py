##
## EPITECH PROJECT, 2022
## 107transfer [WSL: Manjaro]
## File description:
## polynomial_mulitplication
##

from re import split
from typing import NamedTuple
from src.parse_args import Arguments


class Result(NamedTuple):
    r1: dict[float, float]
    r2: dict[float, float]


def get_polynomes(args: list[str]) -> tuple[list[dict[int, str]], list[dict[int, str]]]:
    numerator: list[str] = args[1::2]
    denominator: list[str] = args[2::2]
    list_dico_num: list[dict[int, str]] = []
    list_dico_deno: list[dict[int, str]] = []
    tmp_dico: dict[int, str] = {}
    tmp: list[str]

    for i in numerator:
        tmp_dico = {}
        tmp = i.split("*")
        for j in range(0, len(tmp)):
            tmp_dico[j] = tmp[j]
        list_dico_num.append(tmp_dico)
    for i in denominator:
        tmp_dico = {}
        tmp = i.split("*")
        for j in range(0, len(tmp)):
            tmp_dico[j] = tmp[j]
        list_dico_deno.append(tmp_dico)
    return (list_dico_num, list_dico_deno)
