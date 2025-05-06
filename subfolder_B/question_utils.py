# subfolder_B/question_utils.py
import json
from subfolder_A.kuis_table import load_quiz_data, lookup_quiz

def load_questions_by_category(category):
    quizzes = load_quiz_data()
    return [q for q in quizzes if q['category'] == category]

def evaluate_answer(correct_answer, user_answer):
    return correct_answer.strip().lower() == user_answer.strip().lower()

def calculate_score(correct_count, total_questions):
    return int((correct_count / total_questions) * 100)