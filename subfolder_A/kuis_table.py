import json
import os

def load_quiz_data():
    try:
        json_file = os.path.join(os.path.dirname(__file__), 'soal_config.json')
        with open(json_file, 'r') as f:
            quizzes = json.load(f)
        
        print(quizzes)
        return quizzes
    except FileNotFoundError:
        print("Berkas data kuis tidak dapat ditemukan. Silakan perbaiki ini.")
        return None

def lookup_quiz(number, data=None):
    if data is None:
        data = load_quiz_data()
    
    if data is None:
        exit()
    
    return data[number - 1]
