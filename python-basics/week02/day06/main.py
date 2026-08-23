# Exercise 3 — 整理 main.py
# 如果两个 module 互相 import，通常要警惕职责是不是拆乱了。

from employee_models import Department, Employee
from employee_services import calculate_average_score, find_highest_score_employee, count_department, find_employee_by_name


def main() -> None:

    # 跑models
    tech = Department("Tech", "David")
    hr = Department("HR", "Emma")
    finance = Department("Finance", "Frank")

    employee1 = Employee("Alice", tech, 90)
    print(employee1.is_pass())

    employee1.update_score(95)
    print(employee1.score)

    employee1.deactivate()
    print(employee1.active)

    print(employee1.get_grade())

    print(employee1.get_summary())

    # 跑services
    employee2 = Employee("Bob", hr, 55)
    employee3 = Employee("Charlie", finance, 78)
    employee4 = Employee("Diana", tech, 85)
    employees = [employee1, employee2, employee3, employee4]

    average_score = calculate_average_score(employees)
    print(average_score)

    highest_score_employee = find_highest_score_employee(employees)
    print(f"{highest_score_employee.name} has the highest score of {highest_score_employee.score}")

    print(f"Department Tech has {count_department(employees, 'Tech')} employees.")

    wanna_find_1 = find_employee_by_name(employees, "Alice")
    print(wanna_find_1)

    wanna_find_2 = find_employee_by_name(employees, "Genji")
    print(wanna_find_2)


if __name__ == "__main__":
    main()
