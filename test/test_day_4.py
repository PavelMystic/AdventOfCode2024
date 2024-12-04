from challenges.day_4 import (
    encode_letters,
    find_rows,
    row_diff,
    col_diff,
    positive_diagonal_diff,
    negative_diagonal_diff,
    count_triplets,
)

input = [
    ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
    ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
    ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
    ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
    ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
    ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
    ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
    ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
    ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
    ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
]


def test_encoded_letters():

    output = encode_letters(input)
    print(output)


def test_find_rows():

    output = find_rows(encode_letters(input))
    print(output)


def test_row_diff():

    output = row_diff(encode_letters(input))
    print(output)


def test_positive_diagonal_diff():

    output = positive_diagonal_diff(encode_letters(input))


def test_negative_diagonal_diff():

    output = negative_diagonal_diff(encode_letters(input))


def test_col_diff():

    output = col_diff(encode_letters(input))
    print(output)


def test_first_part():

    codes = encode_letters(input)
    differences = row_diff(codes)
    differences += col_diff(codes)
    differences += positive_diagonal_diff(codes)
    differences += negative_diagonal_diff(codes)

    output = count_triplets(differences)

    assert output == 18


if __name__ == "__main__":

    # test_encoded_letters()
    # test_find_rows()
    # test_row_diff()
    # test_col_diff()
    # test_positive_diagonal_diff()
    # test_negative_diagonal_diff()
    test_first_part()
