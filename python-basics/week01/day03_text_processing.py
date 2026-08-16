# Part 1

text = "  The Team Communication Is GOOD!  "

print(text)
print(text.strip()) # 去掉两边空格
print(text.lower()) # 全部小写
print(text.replace("GOOD", "GREAT")) # 把 good 换成 great
print(text.split()) # 拆成单词

if "communication" in text:
    print(True)
else:
    print(False)

if "good" in "GOOD":
    print(True)
else:
    print(False)

if "good" in "GOOD".lower():
    print(True)
else:
    print(False)

# Part 2

# Exercise 1
def clean_text(text):
    return text.strip().lower()
print(clean_text("  The TEAM is GREAT!  "))

assert clean_text("  Hello World  ") == "hello world"
assert clean_text("PYTHON") == "python"
assert clean_text(" test ") == "test"

# Exercise 2
def contains_keyword(text, keyword):
    text = clean_text(text)
    keyword = clean_text(keyword)
    if keyword in text:  # keyword in text 本身就是布尔值，可以直接 return keyword in text
        return True
    else:
        return False

print(contains_keyword(
    "The communication between teams is poor.",
    "Communication"
))

assert contains_keyword("I like Python", "python")
assert contains_keyword("GOOD teamwork", "good")
assert not contains_keyword("I like Python", "java")
assert contains_keyword("I like teamwork", "team")  # 如果业务定义是“搜索完整单词 team”，那就不对了

# Exercise 3
def count_words(text):
    text = clean_text(text)
    return len(text.split())
print(count_words("Python is very useful"))

assert count_words("Python is useful") == 3
assert count_words("   Python   is useful   ") == 3

print(count_words("")) # chat让关注这种 edge case

# Part 3

feedbacks = [
    "The team communication is very good.",
    "I think the workload is too high.",
    "My manager is supportive.",
    "Communication between departments is poor.",
    "The promotion process is unclear.",
    "I really like my team.",
    "Too many meetings and too much overtime.",
    "The office environment is good.",
]

# Exercise 4
def search_feedbacks(feedbacks, keyword):
    result = []
    for feedback in feedbacks:
        if contains_keyword(feedback, keyword):
            result.append(feedback)
    return result
print(search_feedbacks(feedbacks, "communication"))

# Exercise 5
def count_feedbacks_with_keyword(feedbacks, keyword):
    return len(search_feedbacks(feedbacks, keyword))
print(count_feedbacks_with_keyword(feedbacks, "communication"))

# Part 4

negative_keywords = [
    "poor",
    "high",
    "unclear",
    "overtime",
]
def find_negative_feedbacks(feedbacks, negative_keywords):
    negative_feedbacks = []
    for feedback in feedbacks:
        for negative_keyword in negative_keywords:
            if contains_keyword(clean_text(feedback), clean_text(negative_keyword)): # 这里直接 if contains_keyword(feedback, negative_keyword): 就行了，这个函数内部 clean 过了
                negative_feedbacks.append(feedback)
                break
    return negative_feedbacks
print(find_negative_feedbacks(feedbacks, negative_keywords))

# Part 5

def analyze_feedbacks(feedbacks):
    result = {}
    result["total_feedbacks"] = len(feedbacks)
    result["communication_count"] = count_feedbacks_with_keyword(feedbacks, "communication")
    result["team_count"] = count_feedbacks_with_keyword(feedbacks, "team")
    result["negative_feedback_count"] = len(find_negative_feedbacks(feedbacks, negative_keywords)) # negative_keywords 这个变量并不是参数，而是一个全局变量
    result["negative_feedbacks"] = find_negative_feedbacks(feedbacks, negative_keywords) # 这里 find_negative_feedbacks 又被用了两次
    return result
print(analyze_feedbacks(feedbacks))

# 修改后的：
def analyze_feedbacks(feedbacks, negative_keywords):
    result = {}
    result["total_feedbacks"] = len(feedbacks)
    result["communication_count"] = count_feedbacks_with_keyword(feedbacks, "communication")
    result["team_count"] = count_feedbacks_with_keyword(feedbacks, "team")
    negative_feedbacks = find_negative_feedbacks(feedbacks, negative_keywords)
    result["negative_feedback_count"] = len(negative_feedbacks)
    result["negative_feedbacks"] = negative_feedbacks
    return result
print(analyze_feedbacks(feedbacks, negative_keywords))

# Part 6 edge case

print(contains_keyword("I like teamwork", "team")) # 这个业务逻辑应该是False，但是现在输出的是True
print(contains_keyword("Communication.", "communication")) # 这个不清楚业务逻辑是什么，但是现在输出的是True
print(count_words("")) # 这个我觉得没毛病啊，输出0
print(search_feedbacks([], "team")) # 这个我也觉得还行啊，输出的是[]
