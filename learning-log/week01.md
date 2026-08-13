# Week 01 Learning Log

## Day 1 — Python Recall

### What I practiced

今天我练习了：

- list 和 dict 的用法
- 回忆了一下基本的 python 语法 

我完成的练习包括：

1. 对数字列表进行遍历、筛选、求和、求最大值、求平均值
2. 从员工字典列表中读取姓名和分数
3. 统计每个部门人数
4. 找出最高分员工
5. 计算各部门平均分


### What I remembered

哪些内容虽然之前忘了，但今天很快“叫回来”了？

- dict 的一些基本操作，比如如何访问字典中的某个 key 的 value ，我当时不记得了，查了才知道是 dict["Key"] 这样
- 读研的时候 matlab 写得多，之前学 python 的时候，总是混淆两种语言的 () 和 [] 的用法
- 不记得 list 可以直接用 max 找最大值（但是下意识知道 sum 是可以用的）


### What I forgot / had to look up

今天哪些语法或操作我需要查资料？

1.如上所述 dict 的一些基本操作


### Mistakes / Bugs

#### 1. 最大值初始化

我一开始写的是：

```python
max_num = 0
```
没有考虑到如果这组数都是负数的情况。其实写的过程中隐隐觉得不对，但没有细想。正确的应该是把该 list 的第一个值作为初始值。

#### 2. Dictionary access

我一开始忘记如何从字典中取出 name。
```python
employee["name"]
```

#### 3.在统计有多少部门的时候，我直接写死了部门的字段，而没有考虑如果有新的部门怎么办
我一开始写的是：
```python
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
```
如果有新的部门，这个程序是无法感知到的，我写的时候意识到了，但是因为不知道怎么写就放弃了\
在提示下写了新的：
```python
department_count = {}
for employee in employees:
    department = employee["department"]
    if department in department_count:
        department_count[department] = department_count[department]+1   # 简化版本department_count[department] += 1
    else:
        department_count[department] = 1
print(department_count)
```
### Key Concepts
#### 1. List 和 Dict 的区别
我目前的理解：\
list 适合：同颗粒度的东西，所有同类别的东西防砸一起，尤其是数组\
dict 适合：以某个主题聚集，比如可以是个人信息（包含姓名、性别、年龄等 Key，每个 Key 还有自己的 Value）

#### 2. 为什么 dictionary 可以用来计数？
例如：
```python
department_count = {}

if department in department_count:
    department_count[department] += 1
else:
    department_count[department] = 1
```
我自己的理解：因为 dict 是非常结构化的，我们可以把”一级“的 dict 理解为原始数据，那自然可以想到，可以对原始数据进行统计形成”二级“dict。\
此时 dict 不再是”样本“的颗粒度，而是”变量“/”字段“的颗粒度。并且这个过程还很简单:)

#### 3. Dictionary 遍历
如果：
```python
scores = {
    "HR": 163,
    "Tech": 187
}
```
那么：
```python
for x in scores:
```
得到的是：Key，是"HR"和"Tech"

如果想得到 value：
```python
for value in scores.values():
```
如果想同时得到 key 和 value：
```python
for key, value in scores.items():
```

### Hardest Exercise

今天我觉得最难的是：start up最难！之前一直没有下定决心，一直逃避。但是工作了一小段时间后发现，真的很草台，凭什么猪b都能做，我不能做？& 在这个过程中确实是有乐趣+朋友们都一直觉得其实我会做技术向的工作，那还说啥了，开转！

为什么难：如上

我是怎么解决的：先开干吧，就算中途放弃了也是试过了。另近期大火的舆情主角也给了我很大的勇气，学3年非CS本科能做到，那我觉得我也能做到。

### Day 1 Reflection

今天我最大的感受：哈哈其实是day2（day3）补写的，day1的感受就是开心啊，很久没碰居然还能上手欸

我觉得自己目前 Python 基础的状态是：10分！

## Day 2 - Functions

### What I practiced

今天我练习了：
- def
- parameter / argument
- return
- function calls
- 一个函数调用另一个函数
- 返回 list / dict / bool / number
- assert
- 基础 debugging

今天写过的函数：
- add()
- is_even()
- classify_score()
- find_max()
- calculate_average()
- count_keyword()
- count_departments()
- find_highest_score_employee()
- calculate_department_averages()
- analyze_employees()

### What I forgot

今天哪些语法需要查？\
我不确定在字典里遍历，得到的是key还是value还是key-value，所以我查了一下
```python
for key in my_dict:
for value in my_dict.values():
for key, value in my_dict.items():
```

### Mistakes

今天遇到了哪些 bug？

#### 1.没有思考除数为 0 的情况
```python
def calculate_average(nums):
    return sum(nums) / len(nums) # 这里其实不是特别严谨因为除数可能会是0（空列表）
print(calculate_average([80, 90, 70]))
```
这里没有思考如果除数是0怎么办，chat指出了我的问题但是没有告诉我应该怎么做。
现在想的话，我可能会写if哦，if 是空的 list 怎样；其余就还是这样写

#### 2.复杂化问题
要求 employee_count ，我没有直接用 len(employees) 而是饶了一大个弯子…… 我忘记了

#### 3.重复调用
在同一个函数里两次调用 count_departments 这个函数，如果重复调用，可以把第一次的调用结果记为一个变量，后续复用变量而不是重新调用

### Key concepts

1. return 和 print 的区别是什么？\
我都会惊讶于有人分不清这俩， return 是反给计算机的返回值， print 只是打印一下结果啦

2. parameter 和 argument 分别是什么？\
paramenter 是抽象的参数，argument 才是真正计算的参数

3. 为什么把代码拆成函数？\
可以复用

4. 为什么尽量不要让函数依赖外面的变量？\
成屎山之后谁还知道外面啥样

5. What happens if there is no return?\
return None 呗

### Hardest exercise

今天哪道题最难？为什么？
感觉都还好，没有印象深刻的题目。但是对 assert 还是没有太多体感。

### Day 2 Reflection

今天相比 Day 1，我觉得最大的变化是：上班好累 T T

现在让我自己写：
```python
def some_function(...):
    ...
    return ...
```
我的感觉是：easy啊，读研的时候那样的屎山都写下来了。。。并且这两天写的时候，居然没有之前学 python 的时候“运行到这里的时候，看不见变量A的值是什么”的焦虑感！（用 matlab 的时候真的总是打断点，让我看看你现在的值是什么！）

目前我对函数的掌握程度（1–10分）：

10 / 10

原因：确实很简单