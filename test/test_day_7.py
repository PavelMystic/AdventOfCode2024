from pathlib import Path
from typing import Final
from operator import add, mul
from day_7 import read_input, eval_equation, concat

INPUT_PATH: Final = Path() / "test_input_day_7.txt"


def test_read_input() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        equations = read_input(file)

    # print(equations)


def test_eval_equation() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        equations = read_input(file)

    operator_list = [add, mul]

    act_result = eval_equation(equations[0], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[1], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[2], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[3], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[4], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[5], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[6], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[7], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[8], operator_list)
    exp_result = True

    assert act_result == exp_result


def test_eval_equation_concat() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        equations = read_input(file)

    operator_list = [add, mul, concat]

    act_result = eval_equation(equations[0], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[1], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[2], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[3], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[4], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[5], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[6], operator_list)
    exp_result = True

    assert act_result == exp_result

    act_result = eval_equation(equations[7], operator_list)
    exp_result = False

    assert act_result == exp_result

    act_result = eval_equation(equations[8], operator_list)
    exp_result = True

    assert act_result == exp_result


if __name__ == "__main__":

    test_read_input()
    test_eval_equation()
    test_eval_equation_concat()
