from typing import Any
import re
from pathlib import Path

UP = "^"
DOWN = "v"
RIGHT = ">"
LEFT = "<"


def parse_input(file) -> tuple[list[tuple[int, int]], list[int | str], tuple[int, int]]:

    obstacle_pattern = r"#"
    guard_pattern = r"[\^><v]"

    obstacles: list[tuple[int, int]] = []
    guard: list[int | str] = []

    for line_idx, line in enumerate(file):
        matches = re.finditer(obstacle_pattern, line)
        for match in matches:
            obstacles.append((line_idx, match.start()))

        matches = re.finditer(guard_pattern, line)

        for match in matches:
            if not guard:
                guard += [line_idx, match.start(), match.group(0)]
            else:
                raise ValueError("More than one guard!")

    map_dims = (line_idx, len(re.sub(r"\s+", "", line)))

    return obstacles, guard, map_dims


def is_facing_obstacle(guard_face, obstacles):

    return any(
        (
            guard_face[0] == obstacle[0] and guard_face[1] == obstacle[1]
            for obstacle in obstacles
        )
    )


def rotate_right(direction):

    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    if direction == LEFT:
        return UP


def rotate_guard(guard):

    guard[2] = rotate_right(guard[2])

    return guard


def get_guard_face(guard):

    guard_face = [None, None]

    if guard[2] == UP:
        guard_face = [guard[0] - 1, guard[1]]
    if guard[2] == DOWN:
        guard_face = [guard[0] + 1, guard[1]]
    if guard[2] == LEFT:
        guard_face = [guard[0], guard[1] - 1]
    if guard[2] == RIGHT:
        guard_face = [guard[0], guard[1] + 1]

    return guard_face


def move_guard(guard):

    guard_face = get_guard_face(guard)
    guard[0] = guard_face[0]
    guard[1] = guard_face[1]

    return guard


def is_map_edge(guard, map_dims):

    if guard[2] == UP and guard[0] == 0:
        return True
    if guard[2] == DOWN and guard[0] == map_dims[0]:
        return True
    if guard[2] == LEFT and guard[1] == 0:
        return True
    if guard[2] == RIGHT and guard[1] == map_dims[1]:
        return True

    return False


def one_step(guard, obstacles):

    while is_facing_obstacle(get_guard_face(guard), obstacles):
        guard = rotate_guard(guard)

    guard = move_guard(guard)

    return guard


def main_cycle(guard: list, obstacles, map_dims):

    guard_history = []
    guard_history.append(guard.copy())

    while not is_map_edge(guard, map_dims):
        guard = one_step(guard, obstacles)
        guard_history.append(guard.copy())

    return guard_history


if __name__ == "__main__":

    input_path = Path() / "input_day_6.txt"

    with input_path.open() as file:
        obstacles, guard, map_dims = parse_input(file)

    guard_history = main_cycle(guard, obstacles, map_dims)

    print(len(set([(guard[0], guard[1]) for guard in guard_history])))
