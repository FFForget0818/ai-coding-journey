# Part 5 — 第一个 pytest
from employee_management import Department, Employee, calculate_average_score, find_highest_score_employee
import pytest

def test_employee_is_pass() -> None:# 这个函数就是为了检测is_pass函数的
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)
    assert employee.is_pass() is True # 在最开头import了Employee，所以这里可以直接调用is_pass

# Exercise 1 — 最基础的 method tests
def test_employee_is_not_pass() -> None: # 这个函数得换一个名字，否则就把第一个覆盖了
    tech = Department("Tech", "David") # 这里必须重新新建一个
    employee = Employee("Bob", tech, 55)
    assert employee.is_pass() is False # bool的测试建议直接写为is

# Part 6 — Test 的基本结构: arrange（准备测试数据） act（执行要测试的行为） assert（检查结果）
# Exercise 2 — Test Employee Methods
def test_update_score() -> None: # pytest 里的普通 test_xxx() 函数，现阶段基本都写 -> None。
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)
    employee.update_score(95)
    assert employee.score == 95

def test_deactivate() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)
    employee.deactivate()
    assert employee.active is False

def test_get_grade_A() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)
    assert employee.get_grade() == "A"

def test_get_grade_B() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 80)
    assert employee.get_grade() == "B"

def test_get_grade_C() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 70)
    assert employee.get_grade() == "C"

def test_get_grade_D() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 60)
    assert employee.get_grade() == "D"

def test_get_grade_F() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 50)
    assert employee.get_grade() == "F"

# Part 7 — 测试普通 Function
# Exercise 3 — 集合 Function Tests
def test_calculate_average_score() -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    assert calculate_average_score(employees) == 77 # 这里其实算完后会是77.0这个浮点数，但是因为python里77.0=77所以也算通过了

def test_find_highest_score_employee() -> None:
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    result = find_highest_score_employee(employees)
    assert result.name == "Alice"
    assert result.score == 90

# Part 8 — Test Exception
# Exercise 4 — Exception Tests
def test_invalid_score() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError): # 其实不确定这里能不能把两个测试合在一起写，但是好像没问题；不过最好还是分开写啦
        Employee("Alice", tech, 150)

    with pytest.raises(ValueError):
        Employee("Alice", tech, -1)

def test_invalid_name() -> None:
    tech = Department("Tech", "David")

    with pytest.raises(ValueError):
        Employee("", tech, 50)

    with pytest.raises(ValueError):
        Employee("   ", tech ,50)

def test_invalid_update_score() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 90)

    with pytest.raises(ValueError):
        employee.update_score(999)

# Part 9 — 为什么异常也要测试？

# Part 10 — Boundary Case
# Exercise 5 — Boundary Tests
def test_score_min_boundary() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 0)
    assert employee.score == 0

def test_score_max_boundary() -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, 100)
    assert employee.score == 100

def test_score_below_min_boundary() -> None: # 用below和above更合适
    tech = Department("Tech", "David")
    with pytest.raises(ValueError):
        Employee("Alice", tech, -1)

def test_score_above_max_boundary() -> None:
    tech = Department("Tech", "David")
    with pytest.raises(ValueError):
        Employee("Alice", tech, 101)

# Part 11 — Parametrize
# Exercise 6 — Parametrize Grade
@pytest.mark.parametrize( # 这个写法好难记啊
    "score, expected_grade", # 这里是一起不是分开的
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
        (59, "F"),# 每行都算一次passed
    ], # 这还有逗号
)
def test_get_grade(score: int, expected_grade: str) -> None:
    tech = Department("Tech", "David")
    employee = Employee("Alice", tech, score)
    assert employee.get_grade() == expected_grade

# Part 12 — 测试失败是什么样？
# 测试失败
# → 要么生产代码有 bug
# → 要么 test expectation 写错了

# Part 13 — 空 List Edge Case
# Exercise 7 — Empty List
def test_calculate_average_score_empty_list() -> None: # 我去测试函数必须以test开头吗！！
    employees = []
    with pytest.raises(ValueError):
        calculate_average_score(employees)

def test_find_highest_score_employee_empty_list() -> None:
    employees = []
    with pytest.raises(ValueError):
        find_highest_score_employee(employees)

# Part 14 — 今天的完整测试文件
# Part 15 — 运行所有 tests
# Exercise 8 — Final Test Suite
# python -m pytest python-basics/week02/test_employee_management.py -v one by one的看测试结果

