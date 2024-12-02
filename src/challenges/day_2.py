from pathlib import Path
import re


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


if __name__ == "__main__":

    input_path = Path().cwd() / "inputs" / "day_2.txt"

    pattern = r"\d+"

    reports: list[list[int]] = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            pattern_match = re.findall(pattern, line)
            reports.append([int(number) for number in pattern_match])

    print(sum(get_reports_safety(reports)))
