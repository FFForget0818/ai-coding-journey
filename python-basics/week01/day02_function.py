# Week 1 Day 2 - Functions

def add(a, b):
    total = a + b
    return total
print(add(3, 5))
# a / b → parameter 参数
# 3 / 5 → argument 实际传进去的值
# result → 函数返回结果

def add1(a, b):
    print(a + b)
#Python 一个非常重要的规则：所有函数都有返回值；如果你没有显式 return，返回值就是 None。所以这里相当于是 return None 了

def add2(a, b):
    return a + b

x = add1(3, 5)
y = add2(3, 5)

print("x=", x)
print("y=", y)

# print() is for displaying a value; return is for giving a value back to the caller.

# practise 1
def is_even(n):
    if n % 2 == 0:
        return True
    else: return False

# 可以简化为下述内容，因为n % 2 == 0的结果本身就算True或False
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))

# practise 2
def classify_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: return "F"
print(classify_score(92))
print(classify_score(81))
print(classify_score(56))

# practise 3
def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num >max_num:
            max_num = num
    return max_num
print(find_max([3, 8, 2, 6]))

# practise 4
def calculate_average(nums):
    return sum(nums) / len(nums) # 这里其实不是特别严谨因为除数可能会是0（空列表）
print(calculate_average([80, 90, 70]))

# practise 5
def count_keyword(feedbacks, keyword):
    count = 0
    for feedback in feedbacks:
        if keyword in feedback:
            count += 1
    return count
feedbacks = [
    "最近加班很多",
    "食堂不错",
    "项目压力有点大",
    "最近又开始加班",
]
print(count_keyword(feedbacks, "加班"))

employees = [
    {"name": "Alice", "department": "HR", "score": 85},
    {"name": "Bob", "department": "Tech", "score": 92},
    {"name": "Carol", "department": "HR", "score": 78},
    {"name": "David", "department": "Finance", "score": 88},
    {"name": "Eve", "department": "Tech", "score": 95},
]
# TASK A
def count_departments(employees):
    departments = {}
    for employee in employees:
        department = employee["department"]
        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1
    return departments
result = count_departments(employees)
print(result)

# TASK B
def find_highest_score_employee(employees):
    highest_score_employee = employees[0]
    for employee in employees: #可以改为 for employee in employees[1:]: 这样就不用再比较第一个人了
        if employee["score"] > highest_score_employee["score"]:
            highest_score_employee = employee
    return highest_score_employee
highest = find_highest_score_employee(employees)
print(
    f"最高分员工：{highest['name']},"
    f"{highest['score']}分"
)

# TASK C
def calculate_department_averages(employees):
    departments_total_score = {}
    for employee in employees:
        department = employee["department"]
        if department in departments_total_score:
            departments_total_score[department] += employee["score"]
        else:
            departments_total_score[department] = employee["score"]
    departments_count = count_departments(employees)
    departments_average_score = {}
    for department in departments_total_score: # 这里我不确定在字典里遍历，得到的是key还是value还是key-value，我查了一下
        departments_average_score[department] = departments_total_score[department] / departments_count[department]
    return departments_average_score
print(calculate_department_averages(employees))

# for key in my_dict:
# for value in my_dict.values():
# for key, value in my_dict.items():

# PART 6 ASSERT
assert add(3,5) == 8
assert is_even(4) == True
assert classify_score(92) == "A"
assert count_departments(employees) == {
    "HR": 2,
    "Tech": 2,
    "Finance": 1
}
assert find_highest_score_employee(employees)["name"] == "Eve"
assert calculate_department_averages(employees)["HR"] == 81.5

# PART 7
# BUG 1
def calculate_average(nums):
    return(sum(nums) / len(nums))  # 一般写 return sum(nums) / len(nums)
result = calculate_average([80, 90, 70])
print(result * 2)

# BUG 2
def classify_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:  # 这个条件一开始没有想到
        return "F"
print(classify_score(95))

# BUG 3
def count_departments(employees):
    department_count = {}

    for employee in employees:
        department = employee["department"]

        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1
    return department_count

print(count_departments(employees))

# PART 8
def analyze_employees(employees):
    analyze_report = {}
    analyze_report["employee_count"] = 0 # 这里其实直接 analyze_report["employee_count"] = len(employees) 就行了
    for count in count_departments(employees).values():
        analyze_report["employee_count"] += count
    analyze_report["department_count"] = count_departments(employees) # 这里第二次调用 count_departments 这个函数，如果重复调用，可以把第一次的调用结果记为一个变量，后续复用变量而不是重新调用
    analyze_report["highest_score_employee"] = find_highest_score_employee(employees)
    analyze_report["department_average_scores"] = calculate_department_averages(employees)
    return analyze_report
print(analyze_employees(employees))
