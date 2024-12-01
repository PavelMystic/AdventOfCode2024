from pathlib import Path
import re


def get_total_distance(left_list: list[int], right_list: list[int]) -> int:
    """The function has the two list at the input. It sorts the lists in
    ascending order and then calculated the differences between corresponding
    elements. The output of the function is the sum of the differences.

    Args:
        left_list (list[int]): left list
        right_list (list[int]): right list

    Returns:
        int: sum of all differences
    """

    assert len(left_list) == len(right_list)

    return sum(
        abs(left_element - right_element)
        for left_element, right_element in zip(sorted(left_list), sorted(right_list))
    )


def get_similarity_score_multiplier(element: int, occurence_list: list[int]) -> int:
    """Similarity score equals to the number of times the element appears in the
    occcurence_list.

    Args:
        int (_type_): single element from the left list
        occurence_list (list[int]): the right list in which the element should
        be present.

    Returns:
        int: similarity score multiplier
    """

    return sum((element == list_element for list_element in occurence_list))


def get_total_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    """The total similarity score is the sum of the element values multiplied by
    their respective similarity score multiplier. The elements are taken from
    the left list, the right list serves for the multiplier calculation.

    Args:
        left_list (list[int]): left list
        right_list (list[int]): right list

    Returns:
        int: total similarity score
    """

    return sum(
        (
            get_similarity_score_multiplier(left_element, right_list) * left_element
            for left_element in left_list
        )
    )


if __name__ == "__main__":

    input_path = Path().cwd() / "inputs" / "day_1.txt"

    # regular expression to match and capture two integers separated by whitespace
    pattern = r"(\d+)\s+(\d+)"

    left_list = []
    right_list = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            pattern_match = re.match(pattern, line)

            if pattern_match:
                left_list.append(int(pattern_match[1]))
                right_list.append(int(pattern_match[2]))

    print(get_total_distance(left_list, right_list))

    print(get_total_similarity_score(left_list, right_list))
