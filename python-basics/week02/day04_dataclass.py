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

    def deactivate(self) -> None:
        self.active = False

    def is_pass(self) -> bool:
        return self.score >= 60

    def update_score(self, new_score: int) -> None:
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
employee2 = Employee("Bob", hr, 55, False)

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