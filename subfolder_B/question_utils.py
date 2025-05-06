# subfolder_B/question_utils.py
import json
from subfolder_A.kuis_table import load_quiz_data, lookup_quiz

def load_questions_by_category(category):
    if category is None:
        print("Kategori tidak boleh None")
        return []
    quizzes = load_quiz_data()
    if quizzes is None:
        return []
    return [q for q in quizzes if q.get('category') == category]

def evaluate_answer(correct_answer, user_answer):
    if correct_answer is None or user_answer is None:
        print("Jawaban tidak boleh None")
        return False
    return correct_answer.strip().lower() == user_answer.strip().lower()

def calculate_score(correct_count, total_questions):
    if total_questions == 0:
        print("Total pertanyaan tidak boleh nol")
        return 0
    return int((correct_count / total_questions) * 100)

# Komentar hasil uji unit test
# Testcase: TestQuestionUtils.test_load_questions_by_category
# Deskripsi: Memastikan bahwa fungsi load_questions_by_category
#           dapat memuat pertanyaan dari kategori "Matematika"
# Hasil: Berhasil, jumlah pertanyaan yang dimuat adalah 2
#        dan kategori pertama sesuai dengan "Matematika"

# Testcase: TestQuestionUtils.test_evaluate_answer
# Deskripsi: Memastikan bahwa fungsi evaluate_answer dapat
#           mengevaluasi jawaban dengan benar
# Hasil: Berhasil, fungsi mengembalikan True untuk jawaban
#        yang benar dan False untuk jawaban yang salah

# Testcase: TestQuestionUtils.test_calculate_score
# Deskripsi: Memastikan bahwa fungsi calculate_score dapat
#           menghitung skor dengan benar
# Hasil: Berhasil, fungsi menghitung skor dengan tepat

# Unit test kode ini telah diuji oleh Hamid (2211104040)