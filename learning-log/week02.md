## Day 1 — OOP Basics

### What I practiced

今天主要练习了：

* `class`
* object / instance
* `__init__`
* `self`
* attribute
* method
* object state
* object reference
* list of objects

完成了一个简单的 `Employee` class，并加入：

```python
is_pass()
update_score()
get_summary()
get_grade()
```

---

### What I learned

#### 1. Class 和 Object

`Employee` 是一个 class，用来定义一类对象的数据和行为。

```python
employee1 = Employee("Alice", "Tech", 90)
```

这里会创建一个具体的 `Employee` object。

---

#### 2. `__init__` 和 `self`

创建 object 时，会自动执行 `__init__` 来初始化它。

```python
self.name = name
```

可以理解为：

> 把传进来的 `name` 保存到当前 object 自己的 `name` attribute 中。

`self` 表示当前正在操作的这个 object。

---

#### 3. Method

class 里面定义的 function 是 method。

普通 method 不会因为创建 object 而自动执行，需要主动调用：

```python
employee1.is_pass()
```

是否需要 `return` 取决于 method 的职责。

```python
def is_pass(self):
    return self.score >= 60
```

需要返回判断结果。

```python
def update_score(self, new_score):
    self.score = new_score
```

主要负责修改 object state，可以不返回结果。

---

#### 4. Object State

object 的 attribute 可以被修改：

```python
employee1.update_score(95)
```

修改后：

```python
employee1.score
```

会变成 `95`。

---

#### 5. Object Reference

```python
employee2 = employee1
```

不会创建新的 Employee object。

而是：

```text
employee1 ─┐
           ├→ 同一个 Employee object
employee2 ─┘
```

所以通过 `employee2` 修改 attribute，也会影响 `employee1` 看到的数据。

如果写：

```python
employee2 = Employee("Alice", "Tech", 90)
```

才会创建一个新的 object。

---

### Key Takeaway

今天最重要的是开始理解：

```text
class
→ 定义一类 object

object
→ 保存自己的 state

self
→ 当前这个 object

method
→ object 可以执行的行为
```

OOP 并不是替代之前学过的 function、list 和 `if`，而是提供了一种新的代码组织方式。

## Day 2 — OOP Design

### What I practiced

今天主要练习了：

* function vs method
* responsibility
* composition
* object reference
* 多个 object 协作

完成了：

```python
Department
Employee
```

以及：

```python
calculate_average_score()
find_highest_score_employee()
count_department()
```

### What I learned

如果行为主要依赖某个 object 自己的数据，适合写成 method：

```python
employee.get_grade()
```

如果处理的是一组 objects，普通 function 往往更合适：

```python
calculate_average_score(employees)
```

一个 object 也可以保存另一个 object：

```python
employee.department
```

这里 `department` 可以直接是一个 `Department object`，这就是 composition。

另外，多个变量或 attribute 可以指向同一个 object，因此修改共享 object 后，所有引用它的地方都会看到变化。

### Key Takeaway

```text
自己的数据和行为 → method
集合操作 → function
object 包含 object → composition
class 要有清晰 responsibility
```

## Day 3 — Type Hints

### What I practiced

今天主要学习了：

* parameter type
* return type
* `-> None`
* `list[Employee]`
* `dict[str, int]`
* 自定义 class 作为 type
* `Employee | None`

例如：

```python
def find_employee_by_name(
    employees: list[Employee],
    name: str
) -> Employee | None:
```

### What I learned

Type Hint 可以直接说明函数的数据流：

```text
输入什么类型
→ 返回什么类型
```

例如：

```python
def is_pass(self) -> bool:
```

```python
def update_score(self, new_score: int) -> None:
```

```python
def find_highest_score_employee(
    employees: list[Employee]
) -> Employee:
```

同时理解了：

> Type Hint 只是描述预期类型，不等于 Python 运行时会自动强制检查。

### Key Takeaway

```text
list[Employee] → Employee objects 的 list
dict[str, int] → key 是 str，value 是 int
Employee | None → 可能返回 Employee，也可能返回 None
-> None → 不返回有效结果
```
## Day 4 — Dataclass & Data Modeling

### What I practiced

今天主要练习了：

* `@dataclass`
* default value
* `__post_init__`
* data model
* validation
* `raise ValueError`
* dataclass + type hints + composition

把原来的 `Department` 和 `Employee` 改成了 dataclass，并保留：

```python
is_pass()
update_score()
get_grade()
get_summary()
deactivate()
```

---

### What I learned

`@dataclass` 可以减少大量重复的 `__init__` 代码：

```python
@dataclass
class Department:
    name: str
    manager: str
```

同时 `print(object)` 时会得到更清晰的内容，方便 debug。

dataclass 仍然是普通 object，之前学过的：

```text
attribute
method
state
reference
composition
```

都继续成立。

---

### Validation

Type Hint 只能说明预期类型：

```python
score: int
```

但：

```python
score = 900
```

虽然类型正确，业务上仍然不合理。

因此可以用：

```python
def __post_init__(self) -> None:
```

在 object 创建后检查数据，例如：

```python
if self.score < 0 or self.score > 100:
    raise ValueError(...)
```

同时也给 `update_score()` 加入 validation，避免通过 method 把 object 修改成非法状态。

---

### Key Takeaway

```text
dataclass
→ 更简洁地定义结构化数据

type hints
→ 描述数据类型

validation
→ 判断数据是否符合业务规则

raise ValueError
→ 主动拒绝非法数据
```

今天开始从“写 class”进一步进入了简单的 data modeling。

## Day 5 — pytest & Testing Basics

### What I practiced

今天主要练习了：

* `pytest`
* `assert`
* `pytest.raises`
* boundary case
* invalid case
* edge case
* `@pytest.mark.parametrize`
* 测试文件和生产代码分离

测试覆盖了：

```text
Employee methods
calculate_average_score()
find_highest_score_employee()
非法 score / name
空 list
边界值
```

---

### What I learned

pytest 会自动寻找：

```text
test_xxx.py
test_xxx()
```

测试基本结构是：

```text
Arrange
→ 准备数据

Act
→ 执行行为

Assert
→ 检查结果
```

正常结果用：

```python
assert result == expected
```

异常行为用：

```python
with pytest.raises(ValueError):
    ...
```

`@pytest.mark.parametrize` 可以用一套测试逻辑跑多组数据，减少重复代码。

---

### Testing Mindset

今天开始区分：

```text
Normal Case
→ 正常输入

Boundary Case
→ 0 / 100 这种边界

Invalid Case
→ -1 / 101 / 空 name

Edge Case
→ 空 list
```

测试失败不一定代表生产代码错，也可能是 test expectation 写错。

---

### Environment

今天还创建并切换到了项目自己的：

```text
.venv
```

并在虚拟环境中安装了 `pytest`。

同时在 `.gitignore` 中忽略：

```text
.venv/
```

避免把本地虚拟环境提交到 GitHub。

---

### Key Takeaway

```text
写完代码
→ 不是只手动跑一次

而是
→ 用 tests 持续验证重要行为
```

pytest 让测试从零散的 `assert` 变成了可以自动发现、批量执行和重复运行的测试体系。

## Day 6 — Refactor & Project Structure

### What I practiced

今天主要把已有代码按照职责拆分成多个 module，并用 pytest 验证 refactor 前后程序行为一致。

项目结构大致拆分为：

```text
models
services
main
tests
```

主要练习：

* Separation of Concerns
* Module responsibility
* Import / dependency
* Project structure
* Refactor
* pytest regression check

---

### What I learned

#### 1. 不同 module 应该负责不同事情

大致可以理解为：

```text
models
→ 定义数据和 object 本身的行为

services
→ 处理多个 object 之间的业务逻辑

main
→ 创建 object、组织程序执行流程

tests
→ 验证程序行为
```

这样比把所有代码放在一个文件里更容易维护。

#### 2. Dependency 有方向

例如：

```text
main → services → models
  └────────────→ models
```

表示：

```text
main imports services
services imports models
```

底层的 `models` 不应该反过来依赖 `services` 或 `main`，否则容易出现 circular import。

#### 3. Refactor 不应该改变程序行为

Refactor 的目标是：

```text
改变代码结构
而不是改变功能
```

因此正确流程应该是：

```text
pytest 全通过
→ refactor
→ 再运行 pytest
→ 仍然全部通过
```

测试可以帮助确认重构有没有意外破坏原来的逻辑。

---

### Summary

今天开始从“代码能运行”进一步关注：

```text
代码应该放在哪里
module 之间应该怎样依赖
如何安全地重构代码
```

这是从小脚本向真正 application structure 过渡的一步。

# Day 7 — Mini Project: Support Ticket Manager

### What I practiced

今天独立完成了 Week 2 Mini Project：

```text
Support Ticket Manager
```

主要设计了：

```text
SupportAgent
Ticket
```

并实现：

```text
validation
method
service functions
pytest
main.py
```

主要功能包括：

* assign ticket
* close ticket
* update priority
* find ticket
* count open tickets
* find highest priority ticket
* get tickets by agent
* calculate average priority

---

### What I learned

#### 1. 开始自己判断代码应该怎么设计

这次没有完全按照现成 architecture 写，而是开始自己判断：

```text
哪些数据应该放进 class
哪些行为应该写成 method
哪些逻辑应该放进 service
函数应该返回什么
异常情况应该怎么处理
```

相比 Week 1，对 requirement 的独立设计能力提高了一步。

#### 2. `break` 和 `continue` 的区别

```text
break
→ 结束整个 loop

continue
→ 跳过当前这一轮，继续下一轮
```

曾经在 `get_tickets_by_agent()` 中错误使用 `break`：

```python
if ticket.assignee is None:
    break
```

这样遇到一个 unassigned ticket 后，后面的 ticket 都不会再检查。

应该使用：

```python
continue
```

#### 3. `is` 和 `==` 不完全一样

```text
==
→ 比较 value / 内容

is
→ 判断是不是同一个 object
```

如果函数应该从原列表中返回原来的 Ticket object，可以测试：

```python
assert result is ticket2
```

这样比只检查 value 是否相同更准确。

#### 4. Test 本身也可能有 bug

这次测试 `ticket_id` 非法值时，曾经误把测试参数传给了 `priority`。

说明：

```text
production code 可能有 bug
tests 本身也可能有 bug
```

写测试时也要确认：

> 我实际测试的东西，真的是我想测试的吗？

---

### Testing

这次测试覆盖了：

```text
normal case
invalid case
boundary case
empty list
None
tie
unassigned ticket
```

也继续使用了：

```python
@pytest.mark.parametrize
```

来处理测试步骤相同、只有 input / expected 不同的情况。

---

### Summary

Week 2 结束后，我已经从：

```text
学习 Python syntax
```

逐渐进入：

```text
data modeling
+
object design
+
business logic
+
project structure
+
testing
+
debugging
```

下一阶段需要继续减少 architecture 提示，开始更多地根据 requirement 自己设计 application。
