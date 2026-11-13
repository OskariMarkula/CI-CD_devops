import pytest

from app import add, classify_temperature, points_to_grade


def test_add() -> None:
    assert add(2, 3) == 5


def test_add_negative() -> None:
    assert add(-2, 3) == 1


def test_temperature_boundaries() -> None:
    assert classify_temperature(-1) == "freezing"
    assert classify_temperature(0) == "cool"
    assert classify_temperature(19.9) == "cool"
    assert classify_temperature(20) == "warm"


def test_grade_boundaries() -> None:
    assert points_to_grade(0) == "hylätty"
    assert points_to_grade(4) == "hylätty"
    assert points_to_grade(5) == "hyväksytty"
    assert points_to_grade(7) == "hyväksytty"
    assert points_to_grade(8) == "hyvä"
    assert points_to_grade(10) == "erinomainen"


@pytest.mark.parametrize("points", [-1, 11])
def test_grade_out_of_range(points: int) -> None:
    with pytest.raises(ValueError):
        points_to_grade(points)
