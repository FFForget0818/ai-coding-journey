# 把python从脑子里“叫回来”

#  practise 1
nums = [3, 7, 2, 9, 5]

# 输出所有数字
for i in nums:
    print(i)

# 输出大于 5 的数字
for i in nums:
    if i > 5:
        print(i)

# 求和
print(sum(nums))

# 找最大值
maxnum = 0
for i in nums:
    if i > maxnum:
        maxnum = i
print(maxnum)
# 这个地方埋了一个雷，如果都是负数，就找不到最大值了，其实我写的时候迷迷糊糊的意识到了，但是没理
maxnum = nums[0] # 这里没有引入0这个数字，而是直接用了list的第一个数，然后依次做比较找最大数
for num in nums:
    if num > maxnum:
        maxnum = num
print(maxnum)
# 更简单的写法
print(max(nums)) # 既然sum可以用，那max肯定也可以用啊

# 计算平均值
print(sum(nums)/len(nums))

#  practise 2
employees = [
    {"name": "Alice", "department": "HR", "score": 85},
    {"name": "Bob", "department": "Tech", "score": 92},
    {"name": "Carol", "department": "HR", "score": 78},
]

# 输出所有人的姓名
for i in employees:
    print(i["name"]) # 这里怎么访问字典我忘记了，是搜的

# 找出 score > 80 的员工
for i in employees:
    if i["score"] > 80:
        print(i["name"])

# 计算平均分
scores = 0
for i in employees:
    scores += i["score"]
print(scores/len(employees))

# 统计每个 department 有多少人
departments = []
for i in employees:
    departments.append(i["department"])
print("HR 有")
print(departments.count("HR"))
print("人")
print("Tech 有")
print(departments.count("Tech"))
print("人")
# 简单写法
print(f"HR 有 {departments.count('HR')} 人")
print(f"Tech 有 {departments.count('Tech')} 人")
# 如果有新的部门，这个程序是无法感知到的，我写的时候意识到了，但是因为不知道怎么写就放弃了
# 现在chat给了我新的思路
department_count = {}
for employee in employees:
    department = employee["department"]
    if department in department_count:
        department_count[department] = department_count[department]+1   # 简化版本department_count[department] += 1
    else:
        department_count[department] = 1
print(department_count)

# TEST
employees = [
    {"name": "Alice", "department": "HR", "score": 85},
    {"name": "Bob", "department": "Tech", "score": 92},
    {"name": "Carol", "department": "HR", "score": 78},
    {"name": "David", "department": "Finance", "score": 88},
    {"name": "Eve", "department": "Tech", "score": 95},
]

# 第一题：不用 .count()，用一个 dictionary 自动统计每个部门人数。
department_count = {}
for employee in employees:
    if employee["department"] in department_count:
        department_count[employee["department"]] += 1
    else:
        department_count[employee["department"]] = 1
print(department_count)

# 第二题：找出最高分员工
highest_score = employees[0]["score"]
highest_score_name = employees[0]["name"]
for employee in employees:
    if employee["score"] > highest_score:
        highest_score = employee["score"]
        highest_score_name = employee["name"]
print(f"最高分员工：{highest_score_name}，{highest_score}分")
# 更简单的方法：只维护最高分员工这个字典
highest_employee = employees[0]
for employee in employees:
    if employee["score"] > highest_employee["score"]:
        highest_employee = employee
print(f"最高分员工：{highest_employee['name']}， {highest_employee['score']} 分")

# 第三题稍难一点：同时计算每个部门的平均分
department_total_score = {}
for employee in employees:
    if employee["department"] in department_total_score:
        department_total_score[employee["department"]] += employee["score"]
    else:
        department_total_score[employee["department"]] = employee["score"]
department_mean_score = {}
for department in department_total_score:
    department_mean_score[department] = department_total_score[department]/department_count[department]
print(department_mean_score)