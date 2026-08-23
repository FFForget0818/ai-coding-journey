# 放普通函数
# Exercise 2 — 拆 Services

from employee_models import Employee


def calculate_average_score(employees: list[Employee]) -> float:
    if len(employees) == 0:
        raise ValueError("Employees must not be empty!")
    total_score = 0  # 不太确定这里要不要else，好像差不多的？
    for employee in employees:
        total_score += employee.score
    return total_score / len(employees)


def find_highest_score_employee(employees: list[Employee]) -> Employee:
    # 这里其实漏了一种情况，如果最高分有同分，则只会返回第一个人，但是如果要保证返回的是 Employee ，那应该怎么写？
    if len(employees) == 0:
        raise ValueError("Employees must not be empty!")
    highest_score_employee = employees[0]
    for employee in employees[1:]:
        if employee.score > highest_score_employee.score:
            highest_score_employee = employee
    return highest_score_employee


def count_department(employees: list[Employee], department: str) -> int:
    # 这个函数不建议当employees是空list的时候报ValueError，因为空list代表没有人，其实是有意义的，而不是一种错误
    total_count = 0
    for employee in employees:
        if employee.department.name == department:
            total_count += 1
    return total_count  # 我本来是想返回字符串的，说清楚这里是xx部门有xx人，但是这样并不好，因为这个返回值无法再参与后续的计算了。


def find_employee_by_name(employees: list[Employee], name: str) -> Employee | None:  # 这里一开始忘记None了，看见右上角报错才改了
    for employee in employees:
        if employee.name == name:
            return employee
    return None
