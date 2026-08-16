import csv # 原来这个要放在函数文件里，而不是main文件
import json

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
        return None

def save_analysis_result(result, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=4
        )