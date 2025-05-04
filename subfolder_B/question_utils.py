# subfolder_B/question_utils.py
import json

def load_questions_by_category(filepath, category):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [q for q in data if q['category'] == category]

def evaluate_answer(correct_answer, user_answer):
    return correct_answer.strip().lower() == user_answer.strip().lower()

def calculate_score(correct_count, total_questions):
    return int((correct_count / total_questions) * 100)