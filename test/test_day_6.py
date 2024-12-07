from pathlib import Path
from typing import Final
from day_6 import (
    parse_input,
    main_cycle,
    move_guard,
    rotate_guard,
    get_guard_face,
    one_step,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    rotate_right,
)
from itertools import permutations

INPUT_PATH: Final = Path() / "test_input_day_6.txt"
NEW_OBSTACLE_INPUT_PATH: Final = Path() / "test_input_day_6_new_obstacle.txt"


def test_parse_input() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        obstacles, guard, map_dims = parse_input(file)

    print(obstacles, guard)


def test_main_cycle() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        obstacles, guard, map_dims = parse_input(file)

    guard_history = main_cycle(guard, obstacles, map_dims)

    assert len(set([(guard[0], guard[1]) for guard in guard_history])) == 41


def test_move_guard() -> None:

    guard = [1, 2, "^"]
    new_guard = move_guard(guard.copy())
    exp_guard = [0, 2, "^"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [1, 2, ">"]
    new_guard = move_guard(guard.copy())
    exp_guard = [1, 3, ">"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [1, 2, "v"]
    new_guard = move_guard(guard.copy())
    exp_guard = [2, 2, "v"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [1, 2, "<"]
    new_guard = move_guard(guard.copy())
    exp_guard = [1, 1, "<"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )


def test_rotate_guard() -> None:

    guard = [1, 2, "^"]
    new_guard = rotate_guard(guard.copy())
    exp_guard = [1, 2, ">"]

    assert new_guard[2] == exp_guard[2]

    guard = [1, 2, ">"]
    new_guard = rotate_guard(guard.copy())
    exp_guard = [1, 2, "v"]

    assert new_guard[2] == exp_guard[2]

    guard = [1, 2, "v"]
    new_guard = rotate_guard(guard.copy())
    exp_guard = [1, 2, "<"]

    assert new_guard[2] == exp_guard[2]

    guard = [1, 2, "<"]
    new_guard = rotate_guard(guard.copy())
    exp_guard = [1, 2, "^"]

    assert new_guard[2] == exp_guard[2]


def test_get_guard_face() -> None:

    guard = [2, 3, "^"]
    new_face = get_guard_face(guard.copy())
    exp_face = [1, 3]

    assert new_face[0] == exp_face[0] and new_face[1] == exp_face[1]

    guard = [2, 3, "v"]
    new_face = get_guard_face(guard.copy())
    exp_face = [3, 3]

    assert new_face[0] == exp_face[0] and new_face[1] == exp_face[1]

    guard = [2, 3, ">"]
    new_face = get_guard_face(guard.copy())
    exp_face = [2, 4]

    assert new_face[0] == exp_face[0] and new_face[1] == exp_face[1]

    guard = [2, 3, "<"]
    new_face = get_guard_face(guard.copy())
    exp_face = [2, 2]

    assert new_face[0] == exp_face[0] and new_face[1] == exp_face[1]


def test_one_step() -> None:

    # ---------------
    guard = [2, 3, ">"]
    obstacles = [(1, 1)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [2, 4, ">"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [2, 3, ">"]
    obstacles = [(2, 4)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [3, 3, "v"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    # -------------------
    guard = [2, 3, "v"]
    obstacles = [(1, 1)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [3, 3, "v"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [2, 3, "v"]
    obstacles = [(3, 3)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [2, 2, "<"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    # -------------------
    guard = [2, 3, "<"]
    obstacles = [(1, 1)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [2, 2, "<"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [2, 3, "<"]
    obstacles = [(2, 2)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [1, 3, "^"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    # -------------------
    guard = [2, 3, "^"]
    obstacles = [(1, 1)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [1, 3, "^"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )

    guard = [2, 3, "^"]
    obstacles = [(1, 3)]
    new_guard = one_step(guard.copy(), obstacles)
    exp_guard = [2, 4, ">"]

    assert (
        new_guard[0] == exp_guard[0]
        and new_guard[1] == exp_guard[1]
        and new_guard[2] == exp_guard[2]
    )


def test_loop_detection() -> None:

    with INPUT_PATH.open(mode="r", encoding="utf-8") as file:
        obstacles, guard, map_dims = parse_input(file)

    print(obstacles)

    potential_loops = []

    for first_idx, first_obstacle in enumerate(obstacles):
        for second_idx, second_obstacle in enumerate(obstacles[first_idx + 1 :]):
            for third_obstacle in obstacles[first_idx + second_idx + 1 + 1 :]:
                # print(f"{first_obstacle}, {second_obstacle}, {third_obstacle}")

                perms = permutations([first_obstacle, second_obstacle, third_obstacle])

                for perm in perms:

                    # test, prepokladam, ze prvni prekazka vede nahoru
                    #
                    # ......#......
                    # ...........#.
                    # .....#^......
                    # ..........#..
                    if (
                        perm[0][1] + 1 == perm[1][1]  # o sloupec dale musi byt prekazka
                        and perm[1][0] < perm[0][0]  # ktera je smerem nahoru
                        and perm[1][0] + 1 == perm[2][0]  # dalsi musi byt o radek nize
                        and perm[2][0] > perm[1][0]  # ktera je smerem doprava
                    ):
                        print("FIRST UP")
                        print(f"{perm[0]}, {perm[1]}, {perm[2]}")
                        base_direction = UP
                        new_loop = (
                            perm,
                            [
                                base_direction,
                                rotate_right(base_direction),
                                rotate_right(rotate_right(base_direction)),
                            ],
                        )
                        potential_loops.append(new_loop)

                    # test, predpokladam, ze prvni prekazka vede doprava
                    #
                    # ......#......
                    # ......>....#.
                    # .....#.......
                    # ..........#..
                    if (
                        perm[0][0] + 1 == perm[1][0]  # o radek nize musi byt prekazka
                        and perm[1][1] > perm[0][1]  # ktera je smerem doprava
                        and perm[1][1] - 1
                        == perm[2][1]  # pro dalsi musi byt o sloupec zpet
                        and perm[2][0] > perm[1][0]  # ktera je smerem dolu
                    ):
                        print("FIRST RIGHT")
                        print(f"{perm[0]}, {perm[1]}, {perm[2]}")
                        base_direction = RIGHT
                        new_loop = (
                            perm,
                            [
                                base_direction,
                                rotate_right(base_direction),
                                rotate_right(rotate_right(base_direction)),
                            ],
                        )
                        potential_loops.append(new_loop)

                    # test, predpokladam, ze prvni prekazka vede doleva
                    #
                    # ......#......
                    # ...........#.
                    # .....#....<..
                    # ..........#..
                    if (
                        perm[0][0] - 1 == perm[1][0]  # o radek vyse musi byt prekazka
                        and perm[1][1] < perm[0][1]  # ktera je smerem doleva
                        and perm[1][1] + 1
                        == perm[2][1]  # pro dalsi musi byt o sloupec dale
                        and perm[2][0] < perm[1][0]  # ktera je smerem nahoru
                    ):
                        print("FIRST LEFT")
                        print(f"{perm[0]}, {perm[1]}, {perm[2]}")
                        base_direction = LEFT
                        new_loop = (
                            perm,
                            [
                                base_direction,
                                rotate_right(base_direction),
                                rotate_right(rotate_right(base_direction)),
                            ],
                        )
                        potential_loops.append(new_loop)

                    # test, predpokladam, ze prvni prekazka vede dolu
                    #
                    # ......#......
                    # ..........v#.
                    # .....#.......
                    # ..........#..
                    if (
                        perm[0][1] - 1 == perm[1][1]  # o sloupec zpet musi byt prekazka
                        and perm[1][0] > perm[0][0]  # ktera je smerem dolu
                        and perm[1][1] - 1
                        == perm[2][1]  # pro dalsi musi byt o radek vyse
                        and perm[2][1] < perm[1][1]  # ktera je smerem doleva
                    ):
                        print("FIRST DOWN")
                        print(f"{perm[0]}, {perm[1]}, {perm[2]}")
                        base_direction = DOWN
                        new_loop = (
                            perm,
                            [
                                base_direction,
                                rotate_right(base_direction),
                                rotate_right(rotate_right(base_direction)),
                            ],
                        )
                        potential_loops.append(new_loop)

    # TODO navrh nove prekazky
    for potential_loop in potential_loops:
        if potential_loop[1][0] == UP:
            new_obstacle = [potential_loop[0][0][0] - 1, potential_loop[0][-1][1] - 1]
        if potential_loop[1][0] == RIGHT:
            new_obstacle = [potential_loop[0][0][1] - 1, potential_loop[0][-1][1] + 1]
        if potential_loop[1][0] == LEFT:
            new_obstacle = [potential_loop[0][0][1] + 1, potential_loop[0][-1][1] + 1]
        if potential_loop[1][0] == DOWN:
            new_obstacle = [potential_loop[0][0][1] - 1, potential_loop[0][-1][1] + 1]

    # TODO detekce jestli k ceste ve ctverci nebrani jina prekazka


if __name__ == "__main__":
    # test_parse_input()
    # test_main_cycle()

    # test_move_guard()
    # test_get_guard_face()
    # test_one_step()

    test_loop_detection()
