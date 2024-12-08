from pathlib import Path
from day_8 import (
    parse_input,
    get_antinodes,
    get_all_antinodes,
    get_antinodes_resonant_harmonics,
)

INPUT_PATH = Path() / "test_input_day_8.txt"


def test_parse_input() -> None:

    with INPUT_PATH.open(encoding="utf-8", mode="r") as file:
        antennas, map_limits = parse_input(file)

    print(antennas)
    print(map_limits)


def test_get_antinodes() -> None:

    with INPUT_PATH.open(encoding="utf-8", mode="r") as file:
        antennas, map_limits = parse_input(file)

    antinodes = get_antinodes((antennas[0], antennas[1]), map_limits)
    print(antinodes)
    # [0, 11]
    # [3, 2]


def test_get_all_antinodes() -> None:

    with INPUT_PATH.open(encoding="utf-8", mode="r") as file:
        antennas, map_limits = parse_input(file)

    antinodes = get_all_antinodes(antennas, map_limits, get_antinodes)

    print(len(set([(antinode.x, antinode.y) for antinode in antinodes])))


def test_get_all_antinodes_with_resonant_harmonics() -> None:

    with INPUT_PATH.open(encoding="utf-8", mode="r") as file:
        antennas, map_limits = parse_input(file)

    antinodes = get_all_antinodes(
        antennas, map_limits, get_antinodes_resonant_harmonics
    )

    print(len(set([(antinode.x, antinode.y) for antinode in antinodes])))


if __name__ == "__main__":
    # test_parse_input()
    # test_get_antinodes()
    # test_get_all_antinodes()
    test_get_all_antinodes_with_resonant_harmonics()
