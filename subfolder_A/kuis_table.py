import json
import os

def load_quiz_data():
    try:
        json_file = os.path.join(os.path.dirname(__file__), 'soal_config.json')
        with open(json_file, 'r') as f:
            quizzes = json.load(f)
        if not isinstance(quizzes, list):
            raise ValueError("Data kuis harus berupa list")
        return quizzes
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error memuat data kuis: {e}")
        return None

def lookup_quiz(number, data=None):
    if data is None:
        data = load_quiz_data()
    if data is None:
        print("Data kuis tidak tersedia")
        return None
    if number < 1 or number > len(data):
        print("Nomor kuis tidak valid")
        return None
    return data[number - 1]
