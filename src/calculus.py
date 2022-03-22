##
## EPITECH PROJECT, 2022
## 107transfer [WSL: Manjaro]
## File description:
## calculus
##


from math import pow


def init_dico(dico: dict[int, str]) -> dict[float, float]:
    new_dico: dict[float, float] = {}

    for i in range(0, len(dico)):
        new_dico[i] = float(dico[i])
    return new_dico


def polynomial_mulitplication(
    num: list[dict[int, str]], deno: list[dict[int, str]]
) -> tuple[dict[float, float], dict[float, float]]:
    numerator: dict[float, float] = init_dico(num[0])
    denominator: dict[float, float] = init_dico(deno[0])

    for i in range(len(num) - 1):
        for j in range(len(num[i])):
            for x in range(len(num[i + 1])):
                try:
                    numerator[x + j] = float(numerator[x + j]) + (
                        float(num[i].get(j, 0)) * float(num[i + 1].get(x, 0))
                    )
                except:
                    numerator[x + j] = float(num[i].get(j, 0)) * float(
                        num[i + 1].get(x, 0)
                    )
    for i in range(len(deno) - 1):
        for j in range(len(deno[i])):
            for x in range(len(deno[i + 1])):
                try:
                    denominator[x + j] = float(denominator[x + j]) + (
                        float(deno[i].get(j, 0)) * float(deno[i + 1].get(x, 0))
                    )
                except:
                    denominator[x + j] = float(deno[i].get(j, 0)) * float(
                        deno[i + 1].get(x, 0)
                    )
    return numerator, denominator


def calculs(num: dict[float, float], deno: dict[float, float]) -> dict[float, float]:
    numerator: float = 0
    denominator: float = 0
    results: dict[float, float] = {}
    i: float = 0

    while i <= 1.001:
        numerator, denominator = 0, 0
        for j in range(0, len(num)):
            numerator = numerator + float(num[j]) * pow(i, j)
        for j in range(0, len(deno)):
            denominator = denominator + float(deno[j]) * pow(i, j)
        try:
            results[i] = numerator / denominator
        except ZeroDivisionError:
            exit(84)
        results[i] = round(results[i], 5)
        i += 0.001
    return results
