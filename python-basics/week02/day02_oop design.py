# Part 1 — function 还是 method？
# 如果这个行为主要依赖“某个 object 自己的数据”，优先考虑 method。
# Exercise 1 — Class 还是 Function？
class Employee:
    def __init__(self, name, department, score):
        self.name = name
        self.department = department
        self.score = score
    # 1. 判断员工是否及格
    def is_pass(self):
        return self.score >= 60
    # 2. 修改员工自己的分数
    def update_score(self, new_score):
        self.score = new_score
    # 3. 返回员工自己的 summary
    def get_summary(self):
        return f"{self.name} works in {self.department} and has a score of {self.score}."
# 4. 计算所有员工平均分
def calculate_average_score(employees):
    total_score = [] # 能直接赋值就不建 list
    for employee in employees:
        total_score.append(employee.score)
    return sum(total_score)/len(total_score)
# 5. 找出最高分员工
def find_highest_employee(employees):
    highest_score_employee = employees[0]
    for employee in employees[1:]:
        if employee.score > highest_score_employee.score:
            highest_score_employee = employee
    return highest_score_employee
# 6. 统计 Tech 部门有几个人
def count_department(employees, department):
    this_department_employees = []
    for employee in employees:
        if employee.department == department:
            this_department_employees.append(employee)
    return len(this_department_employees)

employee1 = Employee("Alice", "Tech", 90)
employee2 = Employee("Bob", "HR", 55)
employee3 = Employee("Charlie", "Tech", 78)
employees = [employee1, employee2, employee3]

print(employee1.is_pass())
employee2.update_score(100)
print(employee2.score)
employee2.update_score(55)
print(employee3.get_summary())
print(calculate_average_score(employees))
print(find_highest_employee(employees).name)
print(count_department(employees, "Tech"))

# Part 2 — Responsibility：一个 class 应该负责什么？
# Single Responsibility Principle 一个 class 最好有一个相对清晰的职责范围。
# Exercise 2 — 找错职责
def count_all_employees(employees):
    return len(employees)

def save_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

print(count_all_employees(employees))
save_report(employee1.get_summary(), "python-basics/week02/day02_report.txt")

# Part 3 — 第二个 Class：Department
class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
tech = Department("Tech", "David")
hr = Department("HR", "Emma")

# Part 4 — Composition
# 一个 object 可以把另一个 object 作为自己的 attribute。
# Exercise 3 — Department + Employee
employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55)
print(employee1.name)
print(employee1.department.name)
print(employee1.department.manager)
print(employee2.name)
print(employee2.department.name)
print(employee2.department.manager)

# Part 5 — 修改 get_summary()
# Exercise 4 — Composition 下的 summary
class Employee:
    def __init__(self, name, department, score):
        self.name = name
        self.department = department
        self.score = score
    # 1. 判断员工是否及格
    def is_pass(self):
        return self.score >= 60
    # 2. 修改员工自己的分数
    def update_score(self, new_score):
        self.score = new_score
    # 3. 返回员工自己的 summary
    def get_summary(self):
        return f"{self.name} works in {self.department.name} managed by {self.department.manager} and has a score of {self.score}."
employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55)
print(employee1.get_summary())
print(employee2.get_summary())

# Part 6 — object 之间的协作
# 一个 object 不一定需要把所有数据复制到自己身上。
# 如果不建立 class Department，直接把所有的部门name和manager信息都写在 class Employee里面，那么一旦某个部门的manager改变，其所有Employee的object的attribute都要修改。但是如果有class Department 就只需要改一个Department的object的attribute就行了
# Exercise 5 — Shared Object
tech = Department("Tech", "David")

employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Charlie", tech, 78)

tech.manager = "Emma"

print(employee1.department.manager, employee2.department.manager)

# Part 7 — 什么东西不值得单独变成 class？
# Exercise 6 — 不要过度 OOP
def clean_text(text):
    return text.strip().lower()

def count_words(text):
    return len(text.split())

# Part 8 — 综合练习：Employee Management
# Exercise 7 — 综合输出
class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

class Employee:
    def __init__(self, name, department, score):
        self.name = name
        self.department = department
        self.score = score
    def is_pass(self):
        return self.score >= 60
    def update_score(self, new_score):
        self.score = new_score
    def get_grade(self):
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
    def get_summary(self):
        return f"{self.name} works in {self.department.name} managed by {self.department.manager} and has a score of {self.score}."

def calculate_average_score(employees):
    total_score = 0
    for employee in employees:
        total_score += employee.score
    return total_score/len(employees)
def find_highest_score_employee(employees):
    highest_score_employee = employees[0]
    for employee in employees[1:]:
        if employee.score > highest_score_employee.score:
            highest_score_employee = employee
    return highest_score_employee
def count_department(employees, department_name):
    this_department_employees = 0
    for employee in employees:
        if employee.department.name == department_name:
            this_department_employees += 1
    return this_department_employees

tech = Department("Tech", "David")
hr = Department("HR", "Emma")
finance = Department("Finance", "Frank")

employee1 = Employee("Alice", tech, 90)
employee2 = Employee("Bob", hr, 55)
employee3 = Employee("Charlie", finance, 78)
employee4 = Employee("Diana", tech, 85)
employees = [employee1, employee2, employee3, employee4]

for employee in employees:
    print(employee.get_summary())

for employee in employees:
    print(f"{employee.name}: {employee.get_grade()}")

print(f"平均分：{calculate_average_score(employees)}")
print(f"最高分员工姓名：{find_highest_score_employee(employees).name}")
print(f"Tech 部门人数：{count_department(employees, 'Tech')}") # 这里的Tech用单引号比较好

tech.manager = "Grace"
print(employee1.department.manager, employee4.department.manager)


