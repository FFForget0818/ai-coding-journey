# Exercise 4 — 拆 Tests
import pytest

from employee_models import Department, Employee
from employee_services import calculate_average_score, find_highest_score_employee, count_department, find_employee_by_name


# 测试calculate_average_score
def test_calculate_average_score() -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    assert calculate_average_score(employees) == 77.0


def test_calculate_average_score_empty() -> None:
    employees = []

    with pytest.raises(ValueError):
        calculate_average_score(employees)


# 测试find_highest_score_employee
def test_find_highest_score_employee() -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    assert find_highest_score_employee(employees) is employee1  # 这里用is更好
# 这里其实还想测一下多个人都是最高分，但是不知道怎么写了


def test_find_highest_score_employee_empty() -> None:
    employees = []

    with pytest.raises(ValueError):
        find_highest_score_employee(employees)


# 测试count_department
# 这个我一开始就是普通的写的，然后感觉怎么写都不对，突然觉得应该用@pytest.mark.parametrize，然后就觉得好写了
# 什么时候要用@pytest.mark.parametrize？有没有什么判断标准减少思考量：
# 测试步骤完全一样，只是输入和预期结果不同 → parametrize。
@pytest.mark.parametrize(
    "department, count",
    [
        ("Tech", 2),
        ("HR", 1),
        ("Finance", 1),
        ("Marketing", 0),
    ],
)
def test_count_department(department: str, count: int) -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    assert count_department(employees, department) == count


# 测试find_employee_by_name
def test_find_employee_by_name() -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    assert find_employee_by_name(employees, "Alice") == employee1


def test_find_employee_by_name_none_empty() -> None:
    employees = []

    assert find_employee_by_name(employees, "Alice") is None


# 这里漏了一种情况：列表不为空，但是没有我要找的人
def test_find_employee_by_name_none() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)

    employees = [employee]

    assert find_employee_by_name(employees, "Genji") is None

# 测试empty list
# 这个在前面都测过了
