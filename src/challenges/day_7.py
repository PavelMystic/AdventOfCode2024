from typing import Any, TextIO, Callable
import re
from dataclasses import dataclass
from operator import add, mul
from itertools import product, pairwise
from pathlib import Path


def concat(x: int, y: int) -> int:
    return int(str(x) + str(y))


@dataclass
class Equation:
    result: int
    arguments: list[int]


def read_input(file: TextIO) -> list[Equation]:

    equations = []

    for line in file:

        pattern = r"(\d+):\s*((?:\d+\s*)*)"
        match = re.match(pattern, line)

        first_integer = int(match.group(1))  # The integer before the colon
        integers_after_colon = [
            int(num) for num in match.group(2).split()
        ]  # Integers after the colon

        equations.append(Equation(first_integer, integers_after_colon))

    return equations


def eval_equation(equation: Equation, operator_list: list[Callable]) -> bool:

    n_argument = len(equation.arguments)
    n_operator = n_argument - 1

    operations_list = list(product(operator_list, repeat=n_operator))

    for operations in operations_list:
        result = equation.arguments[0]
        for operation_idx, operation in enumerate(operations):
            result = operation(result, equation.arguments[operation_idx + 1])
        if result == equation.result:
            return True

    return False


if __name__ == "__main__":

    INPUT_PATH = Path() / "input_day_7.txt"

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        equations = read_input(file)

    result = 0
    for equation in equations:
        if eval_equation(equation, [add, mul]):
            result += equation.result

    print(f"Part one result: {result}")

    result = 0
    for equation in equations:
        if eval_equation(equation, [add, mul, concat]):
            result += equation.result

    print(f"Part two result: {result}")
