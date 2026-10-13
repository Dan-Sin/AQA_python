import pytest


@pytest.mark.math
@pytest.mark.parametrize(
    "first_nomber, second_number, expected_result ",
    [
        (1, 2, 3),
        (2, 3, 5),
        (5, 5, 10),
        (10, 1, 11),
    ],
    ids=[
        "small_numbers",
        "simple_sum",
        "same_numbers",
        "ten_plus_one",
    ],
)
def test_sum(first_nomber, second_number, expected_result):
    assert first_nomber + second_number == expected_result
