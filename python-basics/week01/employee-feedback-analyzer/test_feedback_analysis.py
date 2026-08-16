from feedback_analysis import clean_text, contains_keyword, extract_feedback_texts

assert clean_text(" Hello ") == "hello"
assert contains_keyword("I like Python", "python") is True
assert contains_keyword("I like Python", "java") is False
assert extract_feedback_texts([]) == []

assert extract_feedback_texts([
    {"feedback": "Hello"}
]) == ["Hello"]

assert extract_feedback_texts([
    {"feedback": None}
]) == []

assert extract_feedback_texts([
    {"feedback": ""}
]) == []

assert extract_feedback_texts([
    {"feedback": "   "}
]) == []

assert extract_feedback_texts([
    {"feedback": "Hello"},
    {"feedback": None},
    {"feedback": "   "},
    {"feedback": "World"}
]) == ["Hello", "World"]