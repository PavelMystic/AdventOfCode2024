from pathlib import Path
import re
from itertools import compress


def is_report_safe_w_dampener(report: list[int]) -> bool:
    """The function evaluated the safety of report. Report is safe, if it is
    monotonic and the difference bwtween subsequent numbers is one or more and
    three and less.

    loo - leave one out

    Args:
        report (list[int]): report, sequence of integers

    Returns:
        bool: true means the report is safe
    """

    damped_idxs: list[int] = []
    first_report_diff = [
        next_element - element for element, next_element in zip(report[:-1], report[1:])
    ]
    second_report_diff = [
        next_element - element for element, next_element in zip(report[:-2], report[2:])
    ]
    n_undamped = len(first_report_diff) - 1
    decreasing_test = [element < 0 for element in first_report_diff]
    increasing_test = [element > 0 for element in first_report_diff]

    n_decreasing = sum(decreasing_test)
    n_increasing = sum(increasing_test)

    is_loo_decreasing = False

    if n_decreasing == n_undamped:
        damped_idx = [
            idx for idx, element in enumerate(decreasing_test) if not (element)
        ]

        assert len(damped_idx) == 1

        damped_idx = damped_idx[0]
        damped_idxs.append(damped_idx)

        if damped_idx == 0 or damped_idx == len(decreasing_test):
            is_loo_decreasing = True
        if second_report_diff[damped_idx - 1] < 0:
            is_loo_decreasing = True

    if n_decreasing > n_undamped:
        is_loo_decreasing = True

    is_loo_increasing = False

    if n_increasing == n_undamped:
        damped_idx = [
            idx for idx, element in enumerate(increasing_test) if not (element)
        ]

        assert len(damped_idx) == 1

        damped_idx = damped_idx[0]
        damped_idxs.append(damped_idx)

        if damped_idx == 0 or damped_idx == len(increasing_test) - 1:
            is_loo_increasing = True
        if second_report_diff[damped_idx - 1] > 0:
            is_loo_increasing = True

    if n_increasing > n_undamped:
        is_loo_increasing = True

    is_loo_monotonic = is_loo_decreasing or is_loo_increasing

    if not is_loo_monotonic:
        return False

    within_boundaries_test = [1 <= abs(element) <= 3 for element in first_report_diff]
    n_within_boundaries = sum(within_boundaries_test)

    is_within_boundaries = False

    if n_within_boundaries == n_undamped:
        damped_idx = [
            idx for idx, element in enumerate(within_boundaries_test) if not (element)
        ]

        assert len(damped_idx) == 1

        damped_idx = damped_idx[0]

        # if there already exists a damped idx, it either is in the vicinity of
        # the new one or there are two indices that need to be dumped and the
        # report is unsafe

        if damped_idx == 0 or damped_idx == len(decreasing_test) - 1:
            is_within_boundaries = True
        if 1 <= abs(second_report_diff[damped_idx - 1]) <= 3:
            is_within_boundaries = True

    if n_within_boundaries > n_undamped:
        is_within_boundaries = True

    return is_within_boundaries


def is_report_safe(report: list[int]) -> bool:
    """The function evaluated the safety of report. Report is safe, if it is
    monotonic and the difference bwtween subsequent numbers is one or more and
    three and less.

    Args:
        report (list[int]): report, sequence of integers

    Returns:
        bool: true means the report is safe
    """

    report_diff = [
        next_element - element for element, next_element in zip(report[:-1], report[1:])
    ]
    is_monotonic = all((element < 0 for element in report_diff)) or all(
        (element > 0 for element in report_diff)
    )

    if not is_monotonic:
        return False

    is_within_boundaries = all((1 <= abs(element) <= 3 for element in report_diff))

    if is_within_boundaries:

        return True

    return False


def get_reports_safety_w_dampener(reports: list[list[int]]) -> list[bool]:
    """This function tests list of reports safety. For each sublist (report) the
    function reports it safety in the for of bool value (True means its safe).

    Args:
        reports (list[list[int]]): reports to be tested

    Returns:
        list[bool]: safety report
    """

    safety_list: list[bool] = []

    for report_idx, report in enumerate(reports):
        safety_list.append(is_report_safe_w_dampener(report))

    return safety_list


def get_reports_safety(reports: list[list[int]]) -> list[bool]:
    """This function tests list of reports safety. For each sublist (report) the
    function reports it safety in the for of bool value (True means its safe).

    Args:
        reports (list[list[int]]): reports to be tested

    Returns:
        list[bool]: safety report
    """

    safety_list: list[bool] = []

    for report in reports:
        safety_list.append(is_report_safe(report))

    return safety_list


def get_reports_safety_w_dampener_brute(reports: list[list[int]]) -> list[bool]:

    safety_list: list[bool] = []

    for report in reports:
        is_safe_at_all = False
        for idx in range(len(report)):
            is_safe = is_report_safe(
                [
                    element
                    for element_idx, element in enumerate(report)
                    if element_idx != idx
                ]
            )

            if is_safe:
                is_safe_at_all = True

        safety_list.append(is_safe_at_all)

    return safety_list


if __name__ == "__main__":

    input_path = Path().cwd() / "inputs" / "day_2.txt"

    pattern = r"\d+"

    reports: list[list[int]] = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            pattern_match = re.findall(pattern, line)
            reports.append([int(number) for number in pattern_match])

    safety = get_reports_safety_w_dampener(reports)
    safety_w_dampener = get_reports_safety_w_dampener_brute(reports)

    for idx, (is_safe, is_safe_w_dampener) in enumerate(zip(safety, safety_w_dampener)):
        if is_safe != is_safe_w_dampener:
            # print(idx)
            pass

    print(sum(safety_w_dampener))
