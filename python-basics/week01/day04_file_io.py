# Day 04 — File + CSV + JSON + Exception + Project Start

# Part 1：最基础的文件读写｜20～25 分钟
with open("python-basics/week01/data/sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

import os

print(os.getcwd())

# Exercise 1：read_text_file()
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

content = read_text_file("python-basics/week01/data/sample.txt")
print(content)

# 实际项目里尽量不要硬编码绝对路径，例如：
# C:\Users\FFForget\...
#
# 因为换一台电脑、换一个用户目录，这个路径就失效了。
#
# 更常用的是相对路径。相对路径默认是相对于 Current Working Directory（cwd，当前工作目录），不是相对于当前 .py 文件。
# 可以用：
# import os
# print(os.getcwd())
#
# 查看当前 cwd。
#
# 我们现在统一约定：
# cwd = ai-coding-journey/
#
# 也就是仓库根目录。
#
# 这样读取 Day 4 文件时统一写：
#
# "python-basics/week01/data/sample.txt"
# PyCharm 左侧打开的项目已经是 ai-coding-journey，不需要重开。需要设置的是 Run Configuration 里的 Working directory。
#
# 设置方式：
#
# Run
# → Edit Configurations
# → Add new run configuration
# → Python
#
# 然后填写：
#
# Name:
# day04_file_io
#
#
# Script path:
# ai-coding-journey/python-basics/week01/day04_file_io.py
#
#
# Working directory:
# C:\Users\FFForget\Desktop\BERBER转行\ai-coding-journey
#
# 最后 Apply → OK。
#
# 一句话记忆：
#
# 绝对路径从磁盘根位置出发；相对路径从 cwd 出发；我们目前统一把仓库根目录 ai-coding-journey 设为 cwd。

# Exercise 2：write_text_file()
def write_text_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file: # 如果该文件已经存在，则会覆盖
        file.write(content)
    return # 这里其实不需要写return
write_text_file(
    "python-basics/week01/data/output.txt",
    "Hello from Python!"
)

# Part 2：CSV —— 今天最重要的部分｜35～40 分钟
import csv
with open(
    "python-basics/week01/data/feedbacks.csv",
    "r",
    encoding="utf-8",
    newline= "" # 这是啥意思？ 答：使用 Python 的 csv 模块读写 CSV 时，通常固定加上 newline=""，让 csv 模块自己正确处理换行。
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
print(reader) # reader 不是“已经把 CSV 全部读进来了的数据”，而是一个“负责逐行读取 CSV 的读取器”。相当于你打印的是“读取器这个机器”，而不是机器读取出来的结果。

# Exercise 3：load_feedback_data()
def load_feedback_data(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader: # 没太懂为什么这里要缩进成这样，reader都读出csv的内容了，为什么还要在with open的里面去做for循环？ 答：每循环一次，reader 才从 CSV 文件中读取下一行，并转换成一个 dict
            data.append(row)
    return data
print(load_feedback_data("python-basics/week01/data/feedbacks.csv"))

# Exercise 4：把 CSV 转成 Day 3 能处理的数据
def extract_feedback_texts(feedback_data):
    feedbacks = []
    for row in feedback_data:
        feedbacks.append(row["feedback"])
    return feedbacks
feedback_data = [
    {"id": "1", "department": "Tech", "feedback": "Hello"},
    {"id": "2", "department": "HR", "feedback": "World"}
]
print(extract_feedback_texts(feedback_data))

# Part 3：JSON —— 保存分析结果｜20～25 分钟
import json
result = {
    "name": "berber", #这里我还以为是=呢，原来是:
    "score": 100
}
with open(
    "python-basics/week01/data/test.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        result, # dump是把python数据变为json数据；反之是load
        file,
        ensure_ascii = False, # 它主要影响中文等非 ASCII 字符。如果没有这行会存为{"name": "\u8d1d\u8d1d"}，加了之后会变为{"name": "贝贝"}
        indent = 4 # 每深入一层结构，用 4 个空格缩进，让 JSON 更适合人阅读。
    )

# Exercise 5：save_analysis_result()
def save_analysis_result(result, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=4
        )
save_analysis_result(
    result,
    "python-basics/week01/data/analysis_result.json"
)

# Part 4：Exception —— 程序出错时怎么办｜25 分钟
try:
    with open("abc.csv", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError: # 这样写的话，即使报错了后面的程序也能继续跑；如果不这样写到这里就错误退出了
    print("File not found.")

# Exercise 6：给 load_feedback_data() 加异常处理
def load_feedback_data(file_path):
    data = []
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return "File not found." # 一个函数不同情况下返回的数据类型，最好尽可能稳定、明确。 上面try返回的是list of dict，但是这里返回的确实字符串。
print(load_feedback_data("python-basics/week01/data/feedbacks.csv"))

# 上述内容更简易写为：
def load_feedback_data(file_path):
    data = []
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None # 明确这次没有成功得到数据。
# 之后调用者就可以写：
feedback_data = load_feedback_data(
    "python-basics/week01/data/feedbacks.csv"
)
if feedback_data is not None:
    print(feedback_data)

print(load_feedback_data(
    "python-basics/week01/data/feedbacks.csv"
))

print(load_feedback_data(
    "python-basics/week01/data/not_exist.csv"
))

print("程序运行到这里了")

# Part 5：把 Day 3 和 Day 4 接起来｜40 分钟
# 复制day3的代码
def clean_text(text):
    return text.strip().lower()
def contains_keyword(text, keyword):
    text = clean_text(text)
    keyword = clean_text(keyword)
    return keyword in text
def search_feedbacks(feedbacks, keyword):
    result = []
    for feedback in feedbacks:
        if contains_keyword(feedback, keyword):
            result.append(feedback)
    return result
def count_feedbacks_with_keyword(feedbacks, keyword):
    return len(search_feedbacks(feedbacks, keyword))
def find_negative_feedbacks(feedbacks, negative_keywords):
    negative_feedbacks = []
    for feedback in feedbacks:
        for negative_keyword in negative_keywords:
            if contains_keyword(feedback, negative_keyword):
                negative_feedbacks.append(feedback)
                break
    return negative_feedbacks
def analyze_feedbacks(feedbacks, negative_keywords):
    result = {}
    result["total_feedbacks"] = len(feedbacks)
    result["communication_count"] = count_feedbacks_with_keyword(feedbacks, "communication")
    result["team_count"] = count_feedbacks_with_keyword(feedbacks, "team")
    negative_feedbacks = find_negative_feedbacks(feedbacks, negative_keywords)
    result["negative_feedback_count"] = len(negative_feedbacks)
    result["negative_feedbacks"] = negative_feedbacks
    return result
negative_keywords = [
    "poor",
    "high",
    "unclear",
    "overtime",
]

# Exercise 7：完整 Pipeline
feedback_data = load_feedback_data("python-basics/week01/data/feedbacks.csv") # 直接复制路径是\，但是正确的写法是/
print(feedback_data) # 这里有可能是None（如果文件不存在），所以一下内容最好写成if模式，这里我直接修改了
if feedback_data is not None:
    feedbacks = extract_feedback_texts(feedback_data)
    print(feedbacks)
    analysis_result = analyze_feedbacks(feedbacks, negative_keywords)
    print(analysis_result)
    save_analysis_result(analysis_result, "python-basics/week01/data/analysis_result.json")

# Part 6
# Case 1 把：feedbacks.csv临时改名。 程序跑不了了，找不到这个文件。
# Case 2 CSV 只有 header：id,department,feedback 没有任何数据。最终的analysis_result就都是0或者[]
# Case 3 加一条：9,Tech,也就是 feedback 是空的。程序会不会崩？ 结果是会崩，因为feedbacks这个list的的其他行都是字符串，而最后新加的这行是None，而None在面对clean_text函数的时候是不能被strip的
        # 外部数据进入程序时，不能永远假设它是干净的。
# Case 4 JSON 文件原来已经存在。再次运行：save_analysis_result(...) 发生什么？新内容会覆盖原本的文件