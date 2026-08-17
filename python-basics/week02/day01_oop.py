# 第一阶段：从你已经会的 dict 出发
# 认识OOP：把某一类东西的数据，以及和这些数据紧密相关的行为组织在一起。面向对象编程

# Part 1：class 与 object
class Employee: # 我要定义一种新的类型，叫 Employee。
    pass
# 之后可以：
# employee1 = Employee()
# 这里：
# Employee
# → class
# employee1
# → object / instance

# Exercise 0：一分钟热身
employee1 = Employee()
employee2 = Employee()

print(employee1)
print(employee2)
# employee1 和 employee2 是两个不同 object。

# Part 2：__init__
class Employee: # Employee → 一种“类型 / 模板”
    def __init__(self, name, department, score): # 创建 object 时，用来给这个 object 设置初始状态的方法。
        self.name = name # 所以self.name就相当于给这个object加了name这个表头？ 准确说法：self.name 是给这个具体 object 增加一个叫 name 的“属性槽位”attributes，并在里面保存数据。
        self.department = department
        self.score = score

employee1 = Employee("Alice", "Tech", 90) # 根据 Employee 这个 class，创建一个新的 Employee object。
print(employee1.name)
print(employee1.department)
print(employee1.score)

# Part 3：今天最关键的概念 self
# Exercise 1：创建 Employee
class Employee: # 我又不懂了，这个class 和下面的 def之间的关系是？ 为什么之后employee1 = Employee("Alice", "Tech", 90)是在调用class而非def？ 这个def的return没写应该return None了，为什么后续还能正常使用？
    def __init__(self, name, department, score): # __init__ 是属于 Employee 这个 class 的一个 method。一个class下可以有多个method，所以 class 可以先理解成一个“容器 + 类型定义”：Employee 对象应该保存什么数据 + Employee 对象能做什么事情
        self.name = name
        self.department = department
        self.score = score
        # __init__无需return，其路径是：调用 Employee(...) → 用__new__()创建一个新的 Employee object → 用 __init__ 初始化它 → Employee(...) 最终产生这个 object → employee1 指向它
        # 所以创建 object 不是 __init__ 主要负责的；它负责的是初始化 object
        # 调用Employee()的时候会自动新建（__new__）一个object并对其初始化（__init__），这俩都是python规定好的特殊method；，其他自建的method不会自动运行，而是等需要的时候再调用
        # 可以先简单的理解为，在外面独立的叫function，在class里面的叫method

employee1 = Employee("Alice", "Tech", 90) # 我们是希望“请创建一个 Employee 对象。”而不是“请单独运行一个叫 __init__ 的函数。”；所以需要调用Employee这个class，而不是__init__这个函数
employee2 = Employee("Bob", "HR", 75)
print(employee1.name)
print(employee1.department)
print(employee1.score)
print(employee2.name)
print(employee2.department)
print(employee2.score)

# Part 4：method
# Exercise 2：is_passed()
class Employee:
    def __init__(self, name, department, score):
        self.name = name
        self.department = department
        self.score = score
    def is_pass(self): # 这种自定义的method就当作普通函数，该return就return
        # if self.score >= 60:
        #     return True
        # else:
        #     return False
        # 可以直接简化为：
        return self.score >= 60
    def update_score(self, new_score):
        self.score = new_score
    def get_summary(self):
        return f"{self.name} works in {self.department} and has a score of {self.score}." # 原来这个f""可以单独用，之前以为只能跟着print()用
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

employee1 = Employee("Alice", "Tech", 90)
employee2 = Employee("Bob", "HR", 55)
print(employee1.is_pass())
print(employee2.is_pass())

# Part 5: object state
# Exercise 3：update_score()
employee1.update_score(95)
print(employee1.score)

# Part 6：组合多个 attribute 生成结果
# Exercise 4：get_summary()
print(employee1.get_summary())

# Part 7：多个 object
# Exercise 5：Employee list
employee1 = Employee("Alice", "Tech", 90)
employee2 = Employee("Bob", "HR", 55)
employee3 = Employee("Charlie", "Finance", 78)
employees = [employee1, employee2, employee3]

for employee in employees:
    print(employee.get_summary())
    print(employee.is_pass())

# Day 1 加餐题：不要急着写
print(employee1.get_grade())
print(employee2.get_grade())
print(employee3.get_grade())

# Day 1 最后的 Debug Challenge
# 第一个应该是 self.name = name
# 第二个应该要def is_passed(self):

# 补充知识
employee1.score = 40
print(employee1.score)
print(employee1.is_pass())
# 目前来看update_score()有点多余，但是后续有别的好处

employee1 = Employee("Alice", 90)
employee2 = employee1 # 此时，没有用Empoyee()，所以没有创建新的object，只存在一个object，但是employee1和employee2都指向这个object
# 因此，如果修改employee2的attribute，实际上改的就是这个object的attribute，因此employee1的attribute也被修改了！

