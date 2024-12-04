from typing import Any
from pathlib import Path

ENCODING_DICT = {"X": 1, "M": 2, "A": 3, "S": 4}


def encode_letters(letters: list[list[str]]) -> list[list[str]]:

    encoded_letters: list[list[int]] = []

    for row in letters:
        encoded_row: list[int] = []
        for letter in row:
            encoded_row.append(ENCODING_DICT[letter])

        encoded_letters.append(encoded_row)

    return encoded_letters


def find_rows(encoded_letters: list[list[int]]) -> Any:

    words: list[list[tuple[int, int]]] = []
    last_code = 0
    words.append([])

    for row_idx, row in enumerate(encoded_letters):
        for letter_idx, letter in enumerate(row):
            if letter == last_code + 1:
                words[-1].append((row_idx, letter_idx))
                last_code = letter
                if letter == 4:
                    words.append([])
                    last_code = 0
            else:
                words[-1] = []
                last_code = 0
                if letter == 1:
                    words[-1].append((row_idx, letter_idx))
                    last_code = letter

        last_code = 0

    for word in words:
        if len(word) < 4:
            words.remove(word)
    return words


def row_diff(encoded_letters: list[list[int]]) -> list[list[int]]:

    diff: list[list[int]] = []

    for row in encoded_letters:
        diff.append([row[idx] - row[idx - 1] for idx in range(1, len(row))])

    return diff


def col_diff(codes: list[list[int]]) -> list[list[int]]:

    n_row = len(codes)
    n_col = len(codes[0])

    diff: list[list[int]] = []

    for col_idx in range(n_col):
        col_diff: list[int] = []
        for row_idx in range(1, n_row):
            col_diff.append(codes[row_idx][col_idx] - codes[row_idx - 1][col_idx])
        diff.append(col_diff)

    return diff


def positive_diagonal_diff(codes: list[list[int]]) -> list[list[int]]:

    n_row = len(codes)
    n_col = len(codes[0])
    diff: list[list[int]] = []

    for col_idx in range(n_col):
        diagonal_diff: list[int] = []
        for add_idx in range(1, n_col - col_idx):
            diagonal_diff.append(
                codes[add_idx][col_idx + add_idx]
                - codes[add_idx - 1][col_idx + add_idx - 1]
            )
        diff.append(diagonal_diff)

    for row_idx in range(1, n_row):
        diagonal_diff: list[int] = []
        for add_idx in range(1, n_col - row_idx):
            diagonal_diff.append(
                codes[row_idx + add_idx][add_idx]
                - codes[row_idx + add_idx - 1][add_idx - 1]
            )
        diff.append(diagonal_diff)

    return diff


def negative_diagonal_diff(codes: list[list[int]]) -> list[list[int]]:

    n_row = len(codes)
    n_col = len(codes[0])
    diff: list[list[int]] = []

    for col_idx in range(0, n_col):
        diagonal_diff: list[int] = []
        for add_idx in range(1, n_col - col_idx):
            diagonal_diff.append(
                codes[n_row - add_idx][col_idx + add_idx - 1]
                - codes[n_row - add_idx - 1][col_idx + add_idx]
            )
        diff.append(diagonal_diff)

    for row_idx in range(n_row - 2, 0, -1):
        diagonal_diff: list[int] = []
        for add_idx in range(1, n_col - (n_row - row_idx) + 1):
            diagonal_diff.append(
                codes[row_idx - add_idx][add_idx]
                - codes[row_idx - add_idx + 1][add_idx - 1]
            )
        diff.append(diagonal_diff)

    return diff


def count_triplets(series: list[list[int]]) -> int:

    negative_subsequent_count: int = 0
    positive_subsequent_count: int = 0
    n_triplets: int = 0

    for serie in series:
        for element in serie:
            if element == -1:
                negative_subsequent_count += 1
            else:
                negative_subsequent_count = 0

            if element == 1:
                positive_subsequent_count += 1
            else:
                positive_subsequent_count = 0

            if positive_subsequent_count == 3:
                n_triplets += 1
                positive_subsequent_count = 0

            if negative_subsequent_count == 3:
                n_triplets += 1
                negative_subsequent_count = 0
        positive_subsequent_count = 0
        negative_subsequent_count = 0

    return n_triplets


def find_rows_reversed(encoded_letters: list[list[int]]) -> Any:

    words: list[list[int]] = []
    last_code = 5
    words.append([])

    for row_idx, row in enumerate(encoded_letters):
        for letter_idx, letter in enumerate(row):
            if letter == last_code - 1:
                words[-1].append(letter_idx)
                last_code = letter
                if letter == 1:
                    words.append([])
                    last_code = 0
            else:
                words[-1] = []
                last_code = 0

    for word in words:
        if len(word) < 4:
            words.remove(word)
    return words


if __name__ == "__main__":

    input_path = Path() / "inputs" / "day_4.txt"

    letters: list[list[str]] = []

    with input_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            letters.append([char for char in line if not char.isspace()])

    codes = encode_letters(letters)
    differences = row_diff(codes)
    differences += col_diff(codes)
    differences += positive_diagonal_diff(codes)
    differences += negative_diagonal_diff(codes)

    print(count_triplets(differences))
