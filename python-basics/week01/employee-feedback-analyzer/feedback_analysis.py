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

def extract_feedback_texts(feedback_data):
    feedbacks = []
    for row in feedback_data:
        feedback = row["feedback"]
        if feedback is not None and feedback.strip() != "":
            # 我原本写的是 if row["feedback"] is not (None or []): 实在是不懂python这个逻辑的语法
            # 查询之后，我错误的改成了 if row["feedback"] is not None and row["feedback"] != []: 但row["feedback"]应该是字符串，而不是list，所以这里不能用 != []
            # 再次，我害怕使用row["feedback"].strip()，因为我怕row["feedback"]是None。但实则如果是None的话，if row["feedback"] is not None这里会判断为False，就不会再执行row["feedback"].strip()了
            # 总结一下：if xxxxx1 and xxxxx2，如果xxxxx1是False，直接就不执行了；如果xxxxx1是True，才会判断xxxxx2，此时如果xxxxx2是False则不执行，是True则执行
            feedbacks.append(feedback)
    return feedbacks