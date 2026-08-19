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
