from challenges.day_2 import is_report_safe

input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def test_is_report_safe() -> None:

    report_idx = 0
    safety_exp = True
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act

    report_idx = 1
    safety_exp = False
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act

    report_idx = 2
    safety_exp = False
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act

    report_idx = 3
    safety_exp = False
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act

    report_idx = 4
    safety_exp = False
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act

    report_idx = 5
    safety_exp = True
    safety_act = is_report_safe(input[report_idx])

    assert safety_exp == safety_act


if __name__ == "__main__":

    test_is_report_safe()
