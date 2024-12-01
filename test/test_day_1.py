from challenges.day_1 import (
    get_total_distance,
    get_similarity_score_multiplier,
    get_total_similarity_score,
)

left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]


def test_get_total_distance():

    dist_exp = 11
    dist_act = get_total_distance(left_list, right_list)

    assert dist_exp == dist_act


def test_get_similarity_score_multiplier():

    similarity_exp = 3
    similarity_act = get_similarity_score_multiplier(left_list[0], right_list)

    assert similarity_exp == similarity_act

    similarity_exp = 0
    similarity_act = get_similarity_score_multiplier(left_list[2], right_list)


def test_get_total_similarity_score():

    similarity_exp = 31
    similarity_act = get_total_similarity_score(left_list, right_list)

    assert similarity_exp == similarity_act
