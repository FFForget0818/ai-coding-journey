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

## Day 3 — String & Text Processing

### What I practiced

今天主要练习了 Python 的字符串处理，以及怎么把前两天学的 `list`、`for`、`if` 和函数组合起来处理一组文本。

今天用到的字符串操作包括：

* `.strip()`
* `.lower()`
* `.split()`
* `.replace()`
* `in`

完成的函数：

* `clean_text()`
* `contains_keyword()`
* `count_words()`
* `search_feedbacks()`
* `count_feedbacks_with_keyword()`
* `find_negative_feedbacks()`
* `analyze_feedbacks()`

### What I learned

#### 1. 文本搜索前可以先统一格式

一开始直接判断：

```python
"communication" in text
```

时，如果原文里是 `"Communication"`，结果会是 `False`。

后来通过 `clean_text()` 先统一处理：

```python
def clean_text(text):
    return text.strip().lower()
```

这样搜索时就不用考虑大小写差异。

我的理解：

clean_text 可以“标准化”文本，让后续操作文本的时候，不会出现大小写不一致的问题

---

#### 2. 函数可以一层一层复用

今天比较明显感受到，前面写好的函数可以直接成为后面函数的零件。

例如：

```text
clean_text()
    ↓
contains_keyword()
    ↓
search_feedbacks()
    ↓
count_feedbacks_with_keyword()
```

以前我可能会在每个函数里面重新写一次 `.lower()` 或循环，但现在开始意识到：

复用函数相当于造轮子，已经造好的小轮子后续直接调用就行，不用重复造轮子
---

#### 3. `break` 在双层循环里的作用

在 `find_negative_feedbacks()` 里，我需要检查每条 feedback 是否包含任意一个负面关键词。

这里用了双层循环。

如果一条 feedback 同时包含多个负面关键词，不加 `break` 就可能被加入结果多次。

我的理解：

> `break` 会结束 当前循环，但不会结束 外层的循环。

---

#### 4. 相同的计算没有必要做两遍

最开始在 `analyze_feedbacks()` 里，我调用了两次：

```python
find_negative_feedbacks(feedbacks, negative_keywords)
```

后来改成：

```python
negative_feedbacks = find_negative_feedbacks(feedbacks, negative_keywords)
```

再分别使用：

```python
len(negative_feedbacks)
negative_feedbacks
```

我的理解：

如果重复调用函数，会增加计算量，最好是只调用一次

---

#### 5. 函数最好不要偷偷依赖外部变量

最开始：

```python
def analyze_feedbacks(feedbacks):
```

函数内部直接使用了外面的 `negative_keywords`。

后来改成：

```python
def analyze_feedbacks(feedbacks, negative_keywords):
```

我的理解：

把需要的数据通过 parameter 传进来，可以提示我们需要哪些数据；如果不传 parameter ，后续少了这个变量都不知道怎么回事

### Bugs / Things I noticed

今天遇到或发现的问题：

1. `contains_keyword("I like teamwork", "team")` 会返回 `True`

   * 原因：目前使用的是子字符串匹配，team 本身就是 teamwork 的一部分，所以会返回 True；如果业务要求匹配完整单词，就需要进一步处理。
   * 我认为当前业务下更合理的结果：False
   * 暂时还没有解决，因为：还没学怎么分词

2. `contains_keyword("Communication.", "communication")` 返回 `True`

   * 我觉得这个结果：OK
   * 原因：当前使用子字符串匹配，句号在关键词后面，不影响 communication 作为子字符串存在。

3. `count_words("")` 返回 `0`

   * 我原来以为：我就是觉得是0啊
   * 实际发现：/

4. `search_feedbacks([], "team")` 返回 `[]`

   * 我觉得这个结果：没问题

### What felt easy

今天觉得比较顺的部分：

* 都还可以

### What was difficult

今天比较需要思考的部分：

* 多注意，同一个函数不要调用另一个函数2次
* 注意函数的 parameter ，不要误用全局变量

### My current understanding

今天最大的感觉不是学会了几个字符串方法，而是开始能把不同东西组合起来：

```text
字符串
+
list
+
for / if
+
function
+
dict
```

最后组成一个简单的 Feedback Analyzer。

我现在对“一个大任务拆成多个小函数”的理解是：

> 先从小轮子开始造，慢慢变复杂

### Next

下一步准备学习：

* 文件读写
* CSV
* JSON
* `try / except`

目标是把现在写死在 Python 代码里的 `feedbacks`，变成从真实文件读取的数据。

## Day 4 — File / CSV / JSON / Exception

### What I practiced

今天主要练习了 Python 如何和外部文件交互，把 Day 3 写死在代码里的 feedback 数据改成了从 CSV 文件读取。

今天接触的内容包括：

* `with open(...)`
* 文件读取和写入
* 相对路径 / 绝对路径
* Current Working Directory（cwd）
* `csv.DictReader`
* JSON
* `json.dump()`
* `try / except`
* `FileNotFoundError`
* 把 Day 3 和 Day 4 串成完整 pipeline

今天最终完成的数据流程：

```text
feedbacks.csv
↓
load_feedback_data()
↓
list of dict
↓
extract_feedback_texts()
↓
list of str
↓
analyze_feedbacks()
↓
dict
↓
save_analysis_result()
↓
analysis_result.json
```

### What I learned

#### 1. 相对路径是相对于 cwd，不是相对于 `.py` 文件

今天一开始遇到了文件找不到的问题。

我原来对路径的理解：

> 就是当前".py“文件的位置

后来理解：

> 相对路径默认是从 Current Working Directory（cwd）开始找，而不是从当前 `.py` 文件的位置开始找。

可以通过：

```python
import os

print(os.getcwd())
```

查看当前 cwd。

目前项目统一把：

```text
ai-coding-journey/
```

作为工作目录。

因此读取 Day 4 的文件可以写：

```python
"python-basics/week01/data/sample.txt"
```

我的理解：

> 要清楚cwd的概念，并且检查一下目前的cwd在哪里呀，这样才知道相对路径怎么写

---

#### 2. `with open()` 负责打开文件并自动关闭

例如：

```python
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
```

目前接触了：

```text
"r" → read
"w" → write / overwrite
```

我的理解：

   > [为什么使用 `with open()`？] 会打开文件，并且在代码块执行结束后自动关闭文件，不需要自己手动 close()。

我还发现，如果 `"w"` 打开的文件已经存在：

> [填发生了什么] 会覆盖掉原本的

---

#### 3. `csv.DictReader` 不是已经读取完成的数据

今天一开始我以为：

```python
reader = csv.DictReader(file)
```

之后 `reader` 已经是 CSV 里的全部数据。

后来发现：

```python
print(reader)
```

打印的是一个 `DictReader object`，并不是所有行的数据。

需要：

```python
for row in reader:
    print(row)
```

才能逐行得到类似：

```python
{
    "id": "1",
    "department": "Tech",
    "feedback": "..."
}
```

我的理解：

> `reader` 更像一个可以读取CSV的机器，但是得用 for row in reader 去一行行读取。

---

#### 4. 为什么 `for row in reader` 要放在 `with open()` 里面

因为 `DictReader` 还需要依赖已经打开的文件继续读取数据。

如果退出：

```python
with open(...)
```

文件就会被关闭。

所以需要在文件还打开时：

```text
file
↓
DictReader
↓
逐行读取
↓
append 到普通 list
```

最终得到：

```python
data = [
    {...},
    {...}
]
```

之后文件即使关闭，`data` 仍然可以正常使用。

我的理解：

> with open就是打开一本书，一旦退出这个，就把书合上了

---

#### 5. CSV 数据进入 Python 后可以继续使用 list 和 dict

CSV：

```csv
id,department,feedback
1,Tech,Hello
2,HR,World
```

通过 `csv.DictReader()` 后，可以得到：

```python
[
    {"id": "1", "department": "Tech", "feedback": "Hello"},
    {"id": "2", "department": "HR", "feedback": "World"}
]
```

也就是：

```text
CSV
→ list of dict
```

所以 Day 1 学的：

```text
list
dict
for
row["feedback"]
```

开始真正用于外部数据。

---

#### 6. 外部数据需要转换成已有函数需要的格式

Day 3 的：

```python
analyze_feedbacks()
```

需要的是：

```python
[
    "Hello",
    "World"
]
```

但是 CSV 读取出来的是：

```python
[
    {"id": "1", "department": "Tech", "feedback": "Hello"},
    ...
]
```

所以增加了：

```python
extract_feedback_texts()
```

把：

```text
list of dict
→
list of str
```

我的理解：

> [为什么不直接修改所有 Day 3 函数，而是先做一次数据转换？]多麻烦啊，改那么多函数。。。 不如直接复用函数，只改今天的数据格式

---

#### 7. JSON 可以用来保存 Python 的分析结果

今天使用：

```python
json.dump()
```

把 Python 数据写入 JSON 文件。

例如：

```python
result = {
    "name": "berber",
    "score": 100
}
```

保存以后可以变成：

```json
{
    "name": "berber",
    "score": 100
}
```

目前理解：

```text
json.dump()
Python object → JSON 文件

json.load()
JSON 文件 → Python object
```

其中：

```python
indent=4
```

作用：

> [自己填]增加人类的可读性

```python
ensure_ascii=False
```

作用：

> [自己填]让中文直接以中文保存，而不是转换成 \uXXXX 形式的 Unicode 转义字符。

---

#### 8. `try / except` 是处理运行时可能出现的问题

例如：

```python
try:
    ...
except FileNotFoundError:
    ...
```

我的理解：

> `try` 中正常运行时：运行try里面的内容

> 如果发生 `FileNotFoundError`：运行except FileNotFoundError:里面的内容

今天理解到，`try / except` 并不是让错误消失，而是：

> [用自己的话填] 如果 try 中发生了我们指定要处理的 FileNotFoundError，程序会转去执行对应的 except，处理完成后继续执行后面的代码，而不是直接因为这个异常退出。

---

#### 9. 函数的返回值类型需要注意

`load_feedback_data()` 正常情况下返回：

```text
list
```

如果读取失败直接返回：

```python
"File not found."
```

就会出现：

```text
成功 → list
失败 → str
```

这可能给后面的代码造成问题。

因此目前使用：

```python
None
```

表示读取失败。

我的理解：

> [为什么 `None` 比 `"File not found."` 更适合作为这里的失败结果？] None 更直接，并且后续可直接用 if xxx is not None

---

### Bugs / Things I noticed

#### 1. 文件路径错误

遇到：

```text
FileNotFoundError
```

原因：

> 不知道cwd的概念

解决：

> 设置一个cwd

---

#### 2. CSV 文件不存在

当 `feedbacks.csv` 不存在时：

```text
load_feedback_data()
→ ?
```

如果后面的 pipeline 仍然直接执行：

```python
extract_feedback_texts(feedback_data)
```

会发生：

> 就报错啊

所以需要考虑：

```python
if feedback_data is not None:
    ...
```

我的理解：

> feedback_data is not None 表示这次读取成功；如果读取失败，load_feedback_data() 返回 None，后面的数据处理就不应该继续。

---

#### 3. CSV 只有 header

例如：

```csv
id,department,feedback
```

最终：

```python
analysis_result
```

结果：

> 全是0或者[]

我认为这个结果：

> 很合理啊

---

#### 4. CSV 中 feedback 是空值

例如：

```csv
9,Tech,
```

读取以后：

```python
row["feedback"]
```

可能是：

```python
None
```

之后：

```python
clean_text(None)
```

会报错，因为：

> feedback 是 None，传给 clean_text() 后相当于执行 None.strip()，但 None 没有 .strip() 方法（去掉两边空格），因此报错。

今天让我意识到：

> 不能默认外部数据一定是干净的。

---

#### 5. JSON 文件已经存在

使用：

```python
with open(file_path, "w", ...)
```

重新保存时：

> [旧文件会发生什么]会被覆盖

---

### What felt easy

今天比较顺的部分：

* 整体都还比较顺把

### What was difficult

今天比较需要理解的部分：

* 相对路径和 cwd
* `DictReader` 为什么还需要 `for`
* 为什么 `for row in reader` 必须在 `with open()` 里面

### My current understanding

Day 3 以前，我处理的数据基本都是直接写在 Python 文件里的。

Day 4 开始，程序的数据流变成：

```text
外部文件
↓
读取
↓
转换成 Python 数据
↓
调用函数分析
↓
产生结果
↓
保存回外部文件
```

我目前对这个过程的理解：

> 这个更符合生产流程

今天也开始意识到，真实程序不能默认外部数据永远是正确的，例如：

```text
文件不存在
CSV 是空的
字段值是 None
```

所以程序除了处理“正常情况”，还需要考虑异常和脏数据。

### Next

下一步进入 Week 1 最后一天：

* Modules
* 把现在过长的 Python 文件拆开
* `import` 自己写的函数
* 处理简单脏数据
* 完成 Employee Feedback Analyzer
* Refactor
* 基础测试
* Week 1 Review

目标是把目前：

```text
所有代码都塞在 day04_file_io.py
```

改造成一个结构更清楚、能够独立运行的小项目。
