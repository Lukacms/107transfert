##
## EPITECH PROJECT, 2022
## 107transfer [WSL: Manjaro]
## File description:
## drawing
##


def drawing(results: dict[float, float]) -> int:
    i: float = 0

    for j in range(0, len(results)):
        print(f"{i:.3f} -> {results[i]:.5f}")
        i += 0.001
    return 0
