from pathlib import Path
from typing import Final
from day_10 import (
    parse_input,
    get_viable_neighbours,
    explore_trail,
    Position,
    explore_trails,
    explore_trail_rating,
    explore_trails_rating,
)

INPUT_PATH: Final = Path() / "test_input_day_10.txt"


def test_parse_input() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    for row in height_map:
        print(row)


def test_get_viable_neighbours() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    neighbours = get_viable_neighbours(Position(0, 1), height_map)

    print(neighbours)


def test_explore_trail() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    n_ends = explore_trail([Position(0, 2)], height_map)

    print(n_ends)


def test_explore_trail_rating() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    rating = explore_trail_rating([Position(0, 2)], height_map)

    print(rating)


def test_explore_trails() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    n_ends_list = explore_trails(height_map)
    print(n_ends_list)
    print(sum(n_ends_list))


def test_explore_trails_rating() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    rating_list = explore_trails_rating(height_map)
    print(rating_list)
    print(sum(rating_list))


if __name__ == "__main__":

    # test_parse_input()
    # test_get_viable_neighbours()
    # test_explore_trail()
    # test_explore_trails()
    # test_explore_trail_rating()
    test_explore_trails_rating()
