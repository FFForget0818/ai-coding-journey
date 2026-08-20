# Part 1 — 为什么需要 dataclass
# Exercise 1 — 第一个 Dataclass

from dataclasses import dataclass

@dataclass
class Department:
    name: str
    manager: str

tech = Department("Tech", "David")
hr = Department("HR", "Emma")

print(tech.name, tech.manager, hr.name, hr.manager)
print(tech) # 这里的输出和之前直接用class不一样


# Part 2 — dataclass 帮你生成了什么？
# Part 3 — 把 Employee 也改成 dataclass
# Exercise 2 — Employee Dataclass
@dataclass
class Employee:
    name: str
    department: Department
    score: int
    active: bool = True

    def __post_init__(self) -> None:
        if self.score<0 or self.score>100:
            raise ValueError("Score must be between 0 and 100") #第一次学习怎么写报错
        if self.name.strip() == "":
            raise ValueError("Name must not be blank")

    def deactivate(self) -> None:
        self.active = False

    def is_pass(self) -> bool:
        return self.score >= 60

    def update_score(self, new_score: int) -> None:
        if new_score >= 0 and new_score <= 100 :# 可以直接写if 0 <= new_score <= 100:
            self.score = new_score
        else:
            raise ValueError("Score must be between 0 and 100") # 忘记写raise了
    #建议先写报错的情况：
    def update_score(self, new_score: int) -> None:
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score = new_score

    def get_grade(self) -> str:
        if self.score >= 90:
            return "A"
        elif self.score >=80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def get_summary(self) ->str:
        return f"{self.name} works in {self.department.name} managed by {self.department.manager} and has a score of {self.score}."

employee = Employee("Alice", tech, 90)

print(employee)
print(employee.name)
print(employee.department.name)
print(employee.is_pass())
print(employee.get_grade())
print(employee.get_summary())

# Part 4 — Dataclass 仍然是普通 Object
# Part 5 — Default Value
# Exercise 3 — Default Value
employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55, False) # 建议写成employee2 = Employee("Bob", hr, 55, active=False)

print(employee1.active)
print(employee2.active)

employee1.deactivate()
print(employee1.active)

# Part 6 — Data Model 是什么？
# 要为数据找到它最适合的载体，比如员工信息，class就在简洁的同时，比dict信息量更大

# Part 7 — Type Hint 仍然不等于 Validation

# Part 8 — Validation 思维
# 有的时候可能类型正确，但是业务逻辑不对（score=900）

# Part 9 — __post_init__
# 如果你希望：object 初始化完成以后，再执行一些检查。
# Exercise 4 — Score Validation
employee1 = Employee("Alice", tech, 90)
print(employee1)
employee2 = Employee("Bob", hr, 100) # 这里如果写150就会报错ValueError
print(employee2)

# Part 10 — 再加一个 Validation
# Exercise 5 — Name Validation

# Part 11 — 创建成功后仍然能被改坏
# 初始化 validation 只能保证“创建时有效”，不一定保证以后永远有效。
employee = Employee("Alice", tech, 90)
employee.update_score(95)
print(employee.score)
employee.update_score(80)
print(employee.score)

# Part 12 — 综合 Data Model
# Exercise 7 — Employee Management V3
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

def find_employee_by_name(employees: list[Employee], name: str) -> Employee | None:
    for employee in employees:
        if employee.name == name:
            return employee
    return None

tech = Department("Tech", "David")
hr = Department("HR", "Emma")
finance = Department("Finance", "Frank")

employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55)
employee3 = Employee("Charlie", finance, 78)
employee4 = Employee("Diana", tech, 85)
employees = [employee1, employee2, employee3, employee4]

employee1.update_score(95)
print(employee1.score)

employee1.deactivate()
print(employee1.active)
