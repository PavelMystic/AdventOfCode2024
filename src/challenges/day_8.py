from __future__ import annotations
from typing import TextIO, Any, Callable
from pathlib import Path
import re
from dataclasses import dataclass
from itertools import combinations
from math import gcd


@dataclass
class Antenna:
    type: str
    x: int
    y: int


@dataclass
class MapLimits:
    x: int
    y: int

    def is_within(self: MapLimits, x: int, y: int) -> bool:

        return x >= 0 and x <= self.x and y >= 0 and y <= self.y


def parse_input(file: TextIO) -> tuple[list[Antenna], MapLimits]:

    pattern = r"[a-zA-Z0-9]"

    antennas: list[Antenna] = []

    for line_idx, line in enumerate(file):
        matches = re.finditer(pattern, line)

        for match in matches:
            antennas.append(Antenna(match.group(0), line_idx, match.start()))

    return antennas, MapLimits(line_idx, len(line.replace("\n", "")) - 1)


def get_antinodes(
    antennas: tuple[Antenna, Antenna], map_limits: MapLimits
) -> list[Antenna]:

    antinodes: list[Antenna] = []

    if antennas[0].type == antennas[1].type:
        difference = [antennas[0].x - antennas[1].x, antennas[0].y - antennas[1].y]

        if map_limits.is_within(
            antennas[0].x + difference[0], antennas[0].y + difference[1]
        ):
            antinodes.append(
                Antenna(
                    antennas[0].type,
                    antennas[0].x + difference[0],
                    antennas[0].y + difference[1],
                )
            )

        if map_limits.is_within(
            antennas[1].x - difference[0], antennas[1].y - difference[1]
        ):
            antinodes.append(
                Antenna(
                    antennas[0].type,
                    antennas[1].x - difference[0],
                    antennas[1].y - difference[1],
                )
            )

    return antinodes


def get_antinodes_resonant_harmonics(
    antennas: tuple[Antenna, Antenna], map_limits: MapLimits
) -> list[Antenna]:

    antinodes: list[Antenna] = []
    if antennas[0].type == antennas[1].type:
        difference = [antennas[0].x - antennas[1].x, antennas[0].y - antennas[1].y]
        common_divisor = gcd(difference[0], difference[1])
        difference[0] /= common_divisor
        difference[1] /= common_divisor

        new_coords = [antennas[1].x, antennas[1].y]

        while map_limits.is_within(new_coords[0], new_coords[1]):
            antinodes.append(Antenna(antennas[0].type, new_coords[0], new_coords[1]))
            new_coords[0] += difference[0]
            new_coords[1] += difference[1]

        new_coords = [antennas[1].x - difference[0], antennas[1].y - difference[1]]

        while map_limits.is_within(new_coords[0], new_coords[1]):
            antinodes.append(Antenna(antennas[0].type, new_coords[0], new_coords[1]))
            new_coords[0] -= difference[0]
            new_coords[1] -= difference[1]

    return antinodes


def get_all_antinodes(
    antennas: list[Antenna], map_limits: MapLimits, antinodes_fcn: Callable
) -> list[Antenna]:

    antinodes: list[Antenna] = []

    for antenna_combination in combinations(antennas, 2):
        combination_antinodes = antinodes_fcn(antenna_combination, map_limits)

        for antinode in combination_antinodes:
            antinodes.append(antinode)

    return antinodes


if __name__ == "__main__":

    INPUT_PATH = Path() / "input_day_8.txt"

    with INPUT_PATH.open(encoding="utf-8", mode="r") as file:
        antennas, map_limits = parse_input(file)

    antinodes = get_all_antinodes(antennas, map_limits, get_antinodes)

    print(len(set([(antinode.x, antinode.y) for antinode in antinodes])))

    # my first result was 280, which is apparently the right answer for "someone else" which I have
    # no idea what means, at this moment

    antinodes = get_all_antinodes(
        antennas, map_limits, get_antinodes_resonant_harmonics
    )

    print(len(set([(antinode.x, antinode.y) for antinode in antinodes])))
