# Exercise 4 — 拆 Tests

import pytest
from employee_models import Department, Employee


# 测试is_pass
def test_is_pass() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    assert employee1.is_pass() is True  # 这里一开始又写成 == 了，bool应该用is


def test_is_not_pass() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 50)

    assert employee1.is_pass() is False  # 这里一开始又写成 == 了，bool应该用is


def test_is_pass_boundary() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 60)

    assert employee1.is_pass() is True


# 测试update_score
def test_update_score() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    employee1.update_score(95)

    assert employee1.score == 95


def test_update_score_max() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    employee1.update_score(100)

    assert employee1.score == 100


def test_update_score_above() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    with pytest.raises(ValueError):
        employee1.update_score(101)


def test_update_score_min() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    employee1.update_score(0)

    assert employee1.score == 0


def test_update_score_below() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    with pytest.raises(ValueError):
        employee1.update_score(-1)


# 测试deactivate
def test_deactivate() -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90)

    employee1.deactivate()

    assert employee1.active is False


def test_deactivate_when_already_inactive() -> None:  #原名test_deactivate_false，这个名字不清晰
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, 90, active=False)

    employee1.deactivate()

    assert employee1.active is False


# 测试get_grade，这个完全不熟啊，写不出来
@pytest.mark.parametrize(
    "score, expected_grade",
    [
        (95, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (55, "F"),
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (59, "F"),  # 本来写的50，其实没什么意义，这里的本意是测一些边界
    ]
)
def test_get_grade(score: int, expected_grade: str) -> None:
    tech = Department("Tech", "David")
    employee1 = Employee("Alice", tech, score)

    assert employee1.get_grade() == expected_grade


# 测试score validation
def test_score_validation_above() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("Alice", tech, 101)


def test_score_validation_below() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("Alice", tech, -1)


# 测试name validation
def test_name_validation_empty() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("", tech, 90)


def test_name_validation_space() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("  ", tech, 90)


# 测试 boundary
# 上面测过-1和101，这里应该测0和100
def test_boundary_above() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("Alice", tech, 100)


def test_boundary_below() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("Alice", tech, 0)
