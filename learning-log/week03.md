## Day 1 — Practical Python Collections

### What I practiced

今天主要练习了 Python 中处理 collection 的常见写法，包括：

- `enumerate`
- unpacking
- `zip`
- `sorted`
- `max`
- `key`
- `lambda`
- list comprehension
- dict comprehension
- set / set comprehension
- `any`
- `all`

主要围绕 Ticket 数据完成了：

```text
create_ticket_labels
build_priority_updates
find_highest_priority_ticket
sort_tickets_by_priority
get_open_ticket_titles
build_ticket_index
get_all_tags
has_urgent_open_ticket
are_all_tickets_closed
get_top_open_ticket_titles
```

同时继续使用 pytest 测试：

```text
normal case
empty
tie
duplicate
invalid input
原 list 是否被修改
```

### What I learned

#### `enumerate` 和 unpacking

```python
for index, ticket in enumerate(tickets):
```

`enumerate()` 每次会产生类似：

```python
(0, ticket1)
```

而：

```python
index, ticket
```

会把 tuple 里的两个值分别拆给两个变量，这就是 unpacking。

如果希望编号从 1 开始，可以直接写：

```python
enumerate(tickets, start=1)
```

#### `zip` 可以把多个序列按位置配对

例如：

```python
for ticket_id, priority in zip(ticket_ids, priorities):
```

可以把两个 list 中对应位置的元素组合起来。

但 `zip()` 在两个 list 长度不一致时不会报错，而是自动截断到较短的序列，所以如果业务要求两个 list 必须一样长，需要先主动 validation：

```python
if len(ticket_ids) != len(priorities):
    raise ValueError
```

#### `key` 用来定义“按照什么比较”

例如：

```python
max(
    tickets,
    key=lambda ticket: ticket.priority
)
```

表示比较 Ticket 时，不直接比较 object，而是比较每个 Ticket 的 `priority`。

```python
lambda ticket: ticket.priority
```

可以理解成一个临时的小函数，类似：

```python
def get_priority(ticket):
    return ticket.priority
```

多维排序时，`key` 可以返回 tuple：

```python
key=lambda ticket: (
    -ticket.priority,
    ticket.ticket_id
)
```

表示：

```text
priority 降序
ticket_id 升序
```

Python 会先比较 tuple 的第一个值，如果相同，再比较第二个值。

#### `sorted()` 不会修改原 list

```python
sorted(tickets, key=...)
```

会返回一个新的 list，原来的 `tickets` 不会改变。

而：

```python
tickets.sort(...)
```

会直接修改原 list。

所以测试时可以同时检查“返回结果已经排序”和“原 tickets 顺序没有变化”。

#### Comprehension 适合简单的筛选和转换

List comprehension：

```python
[
    ticket.title
    for ticket in tickets
    if ticket.status == "open"
]
```

Dict comprehension：

```python
{
    ticket.ticket_id: ticket
    for ticket in tickets
}
```

Set comprehension：

```python
{
    tag
    for ticket in tickets
    for tag in ticket.tags
}
```

理解 comprehension 时可以记成：

```text
最前面
→ 最终要收集什么

后面
→ 从哪里遍历
→ 是否需要筛选
```

如果业务逻辑比较复杂，包含很多判断、异常或状态修改，普通 `for loop` 往往更清楚，不需要为了代码短而强行使用 comprehension。

#### Dict 的 key 不能重复

例如：

```python
result[101] = ticket1
result[101] = ticket2
```

最终：

```python
result[101]
```

只会得到 `ticket2`，因为相同的 key 再次赋值时，后面的 value 会覆盖前面的 value。

#### Set 适合去重

Set 不保存重复元素。

空 set 必须写：

```python
set()
```

而：

```python
{}
```

表示的是空 dict。

给 set 增加元素使用：

```python
result.add(tag)
```

而不是 list 的 `append()`。

#### `any` 和 `all`

```python
any(...)
```

表示是否至少有一个条件成立。

例如：

```python
any(
    ticket.status == "open"
    and "urgent" in ticket.tags
    for ticket in tickets
)
```

表示是否至少存在一个 open 且带有 urgent tag 的 Ticket。

```python
all(...)
```

表示是否所有元素都满足条件。

需要注意：

```python
any([]) == False
all([]) == True
```

但 Python 的默认逻辑不一定符合业务规则。例如业务规定“没有 ticket 不算所有 ticket 都已经 closed”，那么就需要自己额外处理 empty list。

### Bugs / Notes

今天遇到的几个值得记住的问题：

- 变量赋值后多一个逗号会变成单元素 tuple。
- Dict 的 key 可以直接使用变量，例如 `result[ticket_id] = priority`。
- `zip` 长度不同不会自动报错，需要根据业务规则主动 validation。
- `max(..., key=...)` 在最大值并列时返回最先出现的元素。
- Duplicate dict key 会被后面的 value 覆盖。
- `sorted()` 返回新 list，`.sort()` 会修改原 list。
- `set()` 是空 set，`{}` 是空 dict。

### Summary

今天开始从：

```text
所有 collection 处理都手写 for loop
```

逐渐进入：

```text
根据问题选择合适工具
```

现在可以开始按照问题类型判断：

```text
需要 index
→ enumerate

两个序列按位置对应
→ zip

排序 / 找最大 object
→ sorted / max + key

简单筛选和转换
→ comprehension

去重 / 集合关系
→ set

有没有至少一个满足条件
→ any

是不是全部满足条件
→ all
```

同时继续保持 W2 已经建立的习惯，不能只考虑 normal case，还需要注意：

```text
empty
tie
duplicate
invalid input
side effect
```

W3D1 的重点不是追求“Pythonic”或让代码尽可能短，而是开始学会根据业务问题选择更合适、更清晰的数据处理方式。
