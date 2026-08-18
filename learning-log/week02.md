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
