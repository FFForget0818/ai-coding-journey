# Part 1 — 最基础的 Type Hint
# Exercise 1 — 给旧函数增加 Type Hints
def is_even(number: int) -> bool: # 冒号的位置是在最后面，一开始都搞错了
    return number % 2 == 0


def clean_text(text: str) -> str:
    return text.strip().lower()


def count_words(text: str) -> int:
    return len(text.split())


def calculate_average(numbers: list[int]) -> float: # 这里一开始搞错了写的int，然后最好说清楚list里面是啥
    return sum(numbers) / len(numbers)

# Part 2 — -> None
# Exercise 2 — 给 Employee 加 Type Hints

# Part 3 — 自定义 Class 也可以是 Type
# Exercise 3 — Department + Employee
class Department:
    def __init__(self, name: str, manager: str) -> None:
        self.name = name
        self.manager = manager

class Employee:
    def __init__(self, name: str, department: Department, score: int) -> None:
        self.name = name
        self.department = department
        self.score = score
    def is_pass(self) -> bool:
        return self.score >= 60
    def update_score(self, new_score: int) -> None:
        self.score = new_score
    def get_grade(self) -> str:
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"
    def get_summary(self) -> str:
        return f"{self.name} works in {self.department.name} managed by {self.department.manager} and has a score of {self.score}"

# Part 4 — Container Types
# Exercise 4 — 给集合函数加 Type Hints
def calculate_average_score(employees: list[Employee]) -> float:
    total_score = 0
    for employee in employees:
        total_score += employee.score
    return total_score / len(employees)

def find_highest_score_employee(employees: list[Employee]) -> Employee:
    highest_score_employee = employees[0]
    for employee in employees[1:]:
        if employee.score > highest_score_employee.score:
            highest_score_employee = employee
    return highest_score_employee

def count_department(employees: list[Employee], department_name: str) -> int:
    count = 0
    for employee in employees:
        if employee.department.name == department_name:
            count += 1
    return count

# Part 5 — None 和 T | None
# 同一个函数，可能有多种返回类型，比如返回结果可能是 Employee，也可能是 None。
# Exercise 5 — find_employee_by_name()
tech = Department("Tech", "David")
hr = Department("HR", "Emma")
finance = Department("Finance", "Frank")

employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55)
employee3 = Employee("Charlie", finance, 78)
employee4 = Employee("Diana", tech, 85)
employees = [employee1, employee2, employee3, employee4]

def find_employee_by_name(employees: list[Employee], name: str) -> Employee | None:
    for employee in employees:
        if employee.name == name:
            return employee
    return None
result1 = find_employee_by_name(employees, "Alice")
result2 = find_employee_by_name(employees, "Nobody")
print(result1.name)
print(result2)

# Part 6 — Type Hint 不等于运行时强制检查
# Type Hint 主要是“说明预期类型”，不是 Python 默认的运行时强制类型检查。
# Exercise 6 — 故意违反 Type Hint
def multiply(number: int, times: int) -> int:
    return number * times
print(multiply(5, 3))
print(multiply("hello", 3))

# Part 7 — Variable Annotation
# 除了 function，也可以给变量标类型
# Exercise 7 — 综合 Refactor
print(calculate_average_score(employees))

highest_employee = find_highest_score_employee(employees)
print(highest_employee.name)

print(count_department(employees, "Tech"))

alice = find_employee_by_name(employees, "Alice")
nobody = find_employee_by_name(employees, "Nobody")

print(alice.name)
print(nobody)

def repeat_text(text: str, times: int) -> str:
    return text * times
result = repeat_text("hello", 3) # 这里一开始是str的3，我没看出来为啥报错