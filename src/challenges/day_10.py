from typing import TextIO, Any
import re
from collections import namedtuple
from pathlib import Path

coordMap = list[list[int]]

Position = namedtuple("Position", ["row", "col"])


def parse_input(file: TextIO) -> coordMap:

    pattern = r"[0-9]"
    height_map: coordMap = []

    for line in file:

        matches = re.finditer(pattern, line)

        height_vec: list[int] = []

        for match in matches:
            height_vec.append(int(match.group()))

        height_map.append(height_vec)

    return height_map


def get_viable_neighbours(position: Position, height_map: coordMap) -> list[Position]:

    n_row = len(height_map)
    n_col = len(height_map[0])
    current_height = height_map[position.row][position.col]
    viable_neighbours: list[Position] = []

    next_steps = [
        Position(position.row - 1, position.col),
        Position(position.row + 1, position.col),
        Position(position.row, position.col - 1),
        Position(position.row, position.col + 1),
    ]

    for step in next_steps:
        if 0 <= step.row < n_row and 0 <= step.col < n_col:
            if height_map[step.row][step.col] == current_height + 1:
                viable_neighbours.append(step)

    return viable_neighbours


def explore_trail(positions: list[Position], height_map: coordMap) -> int:

    done = False

    n_ends = 0

    while not done:

        new_positions: list[Position] = []

        for position in positions:

            [
                new_positions.append(pos)
                for pos in get_viable_neighbours(position, height_map)
            ]

        positions = list(set(new_positions))

        n_ends += sum(
            height_map[position.row][position.col] == 9 for position in positions
        )

        done = not positions

    return n_ends


def explore_trail_rating(positions: list[Position], height_map: coordMap) -> int:

    done = False

    rating = 0

    n_distinct = [1 for _ in positions]

    while not done:

        new_positions: list[Position] = []
        new_distinct: list[int] = []

        for position_idx, position in enumerate(positions):

            neighbours = get_viable_neighbours(position, height_map)

            [new_positions.append(pos) for pos in neighbours]

            [new_distinct.append(n_distinct[position_idx]) for _ in neighbours]

        positions = list(set(new_positions))
        n_distinct = [0 for _ in positions]

        for position_idx, position in enumerate(positions):
            for new_idx, new_position in enumerate(new_positions):
                if (
                    position.row == new_position.row
                    and position.col == new_position.col
                ):
                    n_distinct[position_idx] += new_distinct[new_idx]

        rating += sum(
            (
                n_distinct[position_idx]
                for position_idx, position in enumerate(positions)
                if height_map[position.row][position.col] == 9
            )
        )

        done = not positions

    return rating


def explore_trails(height_map: coordMap) -> list[int]:

    trail_ends: list[int] = []

    for row_idx, row in enumerate(height_map):
        for col_idx, _ in enumerate(row):
            if height_map[row_idx][col_idx] == 0:
                trail_ends.append(
                    explore_trail([Position(row_idx, col_idx)], height_map)
                )

    return trail_ends


def explore_trails_rating(height_map: coordMap) -> list[int]:

    trail_ratings: list[int] = []

    for row_idx, row in enumerate(height_map):
        for col_idx, height in enumerate(row):
            if height == 0:
                trail_ratings.append(
                    explore_trail_rating([Position(row_idx, col_idx)], height_map)
                )

    return trail_ratings


if __name__ == "__main__":

    INPUT_PATH = Path() / "input_day_10.txt"

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        height_map = parse_input(file)

    print(sum(explore_trails(height_map)))

    print(sum(explore_trails_rating(height_map)))
