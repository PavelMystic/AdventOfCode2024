from pathlib import Path
import re
from typing import Any, Optional


def main() -> None:

    pass


def parse_operations(line: str) -> list[dict[str, str | int]]:

    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.finditer(pattern, line)

    results: list[dict[str, str | int]] = [
        {
            "type": "mul",
            "start_idx": match.start(),
            "x": int(match.group(1)),
            "y": int(match.group(2)),
        }
        for match in matches
    ]

    return results


def parse_executions(line: str) -> list[dict[str, bool | int]]:

    pattern = r"do\(\)"

    matches = re.finditer(pattern, line)

    do_results = [{"type": True, "start_idx": match.start()} for match in matches]

    pattern = r"don't\(\)"

    matches = re.finditer(pattern, line)

    dont_results = [{"type": False, "start_idx": match.start()} for match in matches]

    return do_results + dont_results


def create_execution_ranges(
    executions: list[dict[str, bool | int]]
) -> list[list[Optional[int]]]:

    sorted_executions = sorted(executions, key=lambda x: x["start_idx"])

    execute = True
    execution_ranges: list[list[Optional[int]]] = [[0, None]]

    for execution in sorted_executions:
        if execute:
            if not execution["type"]:
                execution_ranges[-1][1] = execution["start_idx"]
                execute = False
        if not execute:
            if execution["type"]:
                execution_ranges.append([execution["start_idx"], None])
                execute = True

    if not execution_ranges[-1][1]:
        execution_ranges[-1][1] = 10000000

    return execution_ranges


def eval_operations(
    operations: list[dict[str, str | int]], execution_ranges: list[list[Optional[int]]]
) -> int:

    result: int = 0

    for operation in operations:

        if any(
            (
                execution_range[0] <= operation["start_idx"] <= execution_range[1]
                for execution_range in execution_ranges
            )
        ):

            if operation["type"] == "mul":

                result += operation["x"] * operation["y"]

    return result


def eval_all(operations, executions) -> int:

    oper_exec = operations + executions
    sorted_oper_exec = sorted(oper_exec, key=lambda x: x["start_idx"])

    result = 0

    enable = True

    for element in sorted_oper_exec:

        if isinstance(element["type"], bool):
            enable = element["type"]
        if isinstance(element["type"], str) and enable:
            if element["type"] == "mul":
                result += element["x"] * element["y"]

    return result


if __name__ == "__main__":

    input_path = Path() / "input.txt"

    lines: list[str] = []

    with input_path.open() as file:
        for line in file:
            lines.append(line)

    total: int = 0
    n_do = 0
    n_dont = 0

    for line in lines:
        operations = parse_operations(line)
        executions = parse_executions(line)
        # execution_ranges = create_execution_ranges(executions)
        # total += eval_operations(operations, execution_ranges)
        total += eval_all(operations, executions)

    print(total)

    total1 = total2 = 0
    enabled = True
    data = open(input_path).read()

    for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        if do or dont:
            enabled = bool(do)
        else:
            x = int(a) * int(b)
            total1 += x
            total2 += x * enabled

    print(total1, total2)
