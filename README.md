# AI Coding Journey｜AI 编程转型学习记录

This repository documents my journey of transitioning into AI application development.

这个仓库用于记录我向 **AI 应用开发 / Agent / Applied AI** 方向转型的学习过程。

我的目标不是单纯“学会一些 AI 框架”，而是逐步建立完整的软件工程和 AI Engineering 能力，最终能够独立完成：

```text
理解业务问题
→ 设计解决方案
→ 编写代码
→ Debug
→ 测试
→ Evaluation
→ 部署
→ 解释技术取舍
```

The goal is not simply to learn more AI libraries, but to gradually develop the ability to independently:

```text
Understand the problem
→ Design the solution
→ Write the code
→ Debug
→ Test
→ Evaluate
→ Deploy
→ Explain technical trade-offs
```

---

## Learning Roadmap｜学习路线

当前计划是一条约 7 个月的学习路线：

```text
Python Fundamentals
Python 基础
        ↓
Software Engineering
软件工程基础
        ↓
FastAPI / SQL / Backend
后端开发
        ↓
ML / LLM Fundamentals
机器学习与 LLM 基础
        ↓
RAG
        ↓
Agent & AI Engineering
Agent 与 AI 工程
        ↓
Production AI Project
完整 AI 项目
        ↓
Interview & Job Search
面试与求职
```

当前技术主线是 **AI Application Engineering**，同时保留以下方向作为未来可能的职业出口：

* AI Application Engineer｜AI 应用工程师
* LLM Application Engineer｜LLM 应用工程师
* Agent Application Engineer｜Agent 应用工程师
* Applied AI Engineer｜应用型 AI 工程师
* AI Solutions Engineer｜AI 解决方案工程师
* AI / Agent Product｜AI / Agent 产品
* FDE-like roles｜FDE 类岗位

---

## Current Progress｜当前进度

### Week 1 — Python Fundamentals｜Python 基础

已完成：

* Python 基础语法回顾
* `list` / `dict`
* `for`
* `if / else`
* Functions
* Parameters / Arguments
* `return`
* 函数组合与复用
* 基础 `assert`
* String processing
* Text cleaning
* Keyword search
* 文件读写
* 相对路径 / cwd
* CSV 处理
* JSON 输出
* `try / except`
* `FileNotFoundError`
* Modules / Imports
* 基础数据清洗
* Edge cases
* 基础测试
* Refactoring

Completed topics include:

* Python syntax recall
* Lists and dictionaries
* Loops and conditionals
* Functions and return values
* Function composition
* Basic assertions
* String and text processing
* File I/O
* CSV and JSON
* Exception handling
* Modules and imports
* Basic data cleaning
* Edge-case handling
* Basic testing
* Refactoring

---

## Week 1 Mini Project｜第一周小项目

### Employee Feedback Analyzer｜员工反馈分析器

这是 Week 1 完成的第一个小型 Python 项目。

The first mini project built during Week 1.

程序从 CSV 文件读取员工反馈，对文本进行清洗和分析，并将结果保存为 JSON。

The program reads employee feedback from a CSV file, cleans and analyzes the text, and saves the analysis results as JSON.

### Data Pipeline｜数据流程

```text
feedbacks.csv
      ↓
load_feedback_data()
      ↓
list of dict
      ↓
extract_feedback_texts()
      ↓
list of strings
      ↓
analyze_feedbacks()
      ↓
analysis result
      ↓
analysis_result.json
```

当前支持：

* 从 CSV 读取反馈
* 过滤 `None`、空字符串和纯空格反馈
* 文本标准化
* 关键词搜索
* 关键词统计
* 简单负面反馈识别
* 文件不存在时的异常处理
* JSON 结果保存
* 基础 edge-case 测试

Current features:

* Read feedback from CSV
* Filter invalid or empty feedback
* Normalize text
* Search keywords
* Count keyword-related feedback
* Detect simple negative feedback
* Handle missing files
* Save analysis results to JSON
* Run basic edge-case tests

---

## Repository Structure｜仓库结构

```text
ai-coding-journey/
│
├── README.md
│
├── learning-log/
│   └── week01.md
│
└── python-basics/
    └── week01/
        ├── day01_recall.py
        ├── day02_functions.py
        ├── day03_text_processing.py
        ├── day04_file_io.py
        │
        └── employee-feedback-analyzer/
            ├── main.py
            ├── feedback_analysis.py
            ├── file_utils.py
            ├── test_feedback_analysis.py
            │
            ├── data/
            │   └── feedbacks.csv
            │
            └── output/
                └── analysis_result.json
```

项目结构会随着后续学习和项目复杂度继续调整。

The repository structure will continue to evolve as the projects become larger and more complex.

---

## How I Learn｜学习方式

目前采用的学习方式是：

```text
学习一个小概念
↓
自己写代码
↓
遇到 Bug
↓
Debug
↓
Refactor
↓
Test
↓
做成可以运行的东西
```

My current learning loop is:

```text
Learn a small concept
↓
Write code
↓
Encounter bugs
↓
Debug
↓
Refactor
↓
Test
↓
Build something runnable
```

我更关注：

* 我现在能独立做什么
* 能不能解释自己写的代码
* 遇到 Bug 后能否定位原因
* 能否把大问题拆成小函数
* 能否复用已有代码
* 能否处理 edge cases
* 能否逐渐把代码组织成项目

而不是单纯以“看了多少小时课程”作为进度。

I measure progress mainly by:

* What I can build independently
* Whether I understand and can explain my code
* Whether I can debug problems
* Whether I can decompose larger problems
* Whether I can reuse existing code
* Whether I can handle edge cases
* Whether I can organize code into maintainable projects

rather than by the number of tutorials completed.

---

## Learning Logs｜学习日志

学习日志保存在：

```text
learning-log/
```

主要记录：

* 每天练习了什么
* 遇到的 Bug
* 哪些概念最开始理解错了
* 后来如何修正理解
* Refactoring 过程
* Edge cases
* 学习感受和阶段性总结

The learning logs mainly record:

* What I practiced
* Bugs I encountered
* Concepts I misunderstood
* How my understanding changed
* Refactoring decisions
* Edge cases
* Learning reflections

---

## Next Steps｜下一阶段

接下来会逐步学习：

```text
Python deeper fundamentals
Python 进阶基础
↓
Data Structures & Algorithms Basics
数据结构与算法基础
↓
HTTP / REST API
↓
FastAPI
↓
SQL / PostgreSQL
↓
Testing
↓
Docker
↓
LLM APIs
↓
Structured Output / Tool Calling
↓
RAG
↓
Evaluation
↓
Agents
↓
Production-oriented AI Systems
生产级 AI 应用
```

后续项目会逐渐从：

```text
Python 小程序
```

升级到：

```text
Backend
+
Database
+
LLM
+
RAG
+
Agent
+
Evaluation
+
Deployment
```

最终目标是建立一套完整的 AI Application Engineering 能力，而不仅仅是能够调用一个模型 API。

The long-term goal is to develop end-to-end AI application engineering capability, rather than simply learning how to call an LLM API.
