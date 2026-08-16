from file_utils import load_feedback_data, save_analysis_result
from feedback_analysis import extract_feedback_texts, analyze_feedbacks

def main():
    file_path = "python-basics/week01/employee-feedback-analyzer/data/feedbacks.csv"
    negative_keywords = [
        "poor",
        "high",
        "unclear",
        "overtime",
    ]

    feedback_data = load_feedback_data(file_path)
    print(feedback_data)

    if feedback_data is not None:
        feedback_texts=extract_feedback_texts(feedback_data)
        print(feedback_texts)

        result = analyze_feedbacks(feedback_texts, negative_keywords)
        print(result)

        save_analysis_result(result, "python-basics/week01/employee-feedback-analyzer/output/analysis_result.json")

if __name__ == "__main__":
    main()