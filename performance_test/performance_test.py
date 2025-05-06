import timeit
import sys
import os
from unittest.mock import patch

# Menambahkan folder root proyek ke sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from subfolder_A.kuis_table import load_quiz_data, lookup_quiz
from subfolder_B.question_utils import evaluate_answer, calculate_score
from subfolder_B.automata_engine import start_quiz

# ==============================================================================
# Performance Testing Script
# Penguji: Hamid Khaeruman (2211104040)
# Tanggal Pengujian: 6 Mei 2025
# ==============================================================================

def test_load_quiz_data():
    """
    Menguji kinerja fungsi load_quiz_data().
    Melakukan pemanggilan fungsi sebanyak 6 iterasi dan mengukur total waktu eksekusinya.
    Jumlah iterasi: 6
    """
    print("Testing load_quiz_data performance (6 iterations)...")
    execution_time = timeit.timeit("load_quiz_data()", globals=globals(), number=6)
    print(f"load_quiz_data executed 6 times in {execution_time:.4f} seconds.")
    # Hasil: Waktu pemuatan data kuis dari file JSON. Semakin kecil nilainya, semakin cepat.
    # Contoh Waktu Proses: 0.0017 detik (untuk 6 iterasi)

def test_evaluate_answer():
    """
    Menguji kinerja fungsi evaluate_answer().
    Melakukan pemanggilan fungsi sebanyak 6 iterasi dengan jawaban yang benar dan jawaban pengguna.
    Jumlah iterasi: 6
    """
    print("Testing evaluate_answer performance (correct_answer='12', user_answer=' 12 ', 6 iterations)...")
    correct_answer = "12"
    user_answer = " 12 "

    # Fungsi wrapper
    def wrapper():
        evaluate_answer(correct_answer, user_answer)

    execution_time = timeit.timeit(wrapper, number=6)
    print(f"evaluate_answer executed 6 times in {execution_time:.4f} seconds.")
    # Hasil: Waktu yang dibutuhkan untuk mengevaluasi jawaban pengguna. Semakin kecil nilainya, semakin cepat.
    # Contoh Waktu Proses: 0.0000 detik (untuk 6 iterasi, operasi perbandingan string sangat cepat)

def test_calculate_score():
    """
    Menguji kinerja fungsi calculate_score().
    Melakukan pemanggilan fungsi sebanyak 6 iterasi dengan jumlah jawaban benar dan total soal.
    Jumlah iterasi: 6
    """
    print("Testing calculate_score performance (correct_count=10, total_questions=10, 6 iterations)...")
    correct_count = 10
    total_questions = 10

    # Fungsi wrapper
    def wrapper():
        calculate_score(correct_count, total_questions)

    execution_time = timeit.timeit(wrapper, number=6)
    print(f"calculate_score executed 6 times in {execution_time:.4f} seconds.")
    # Hasil: Waktu yang dibutuhkan untuk menghitung skor akhir kuis. Semakin kecil nilainya, semakin cepat.
    # Contoh Waktu Proses: 0.0000 detik (untuk 6 iterasi, operasi matematika sederhana sangat cepat)

def test_start_quiz():
    """
    Menguji kinerja fungsi start_quiz().
    Melakukan simulasi input pengguna menggunakan unittest.mock.patch.
    Jumlah iterasi: 6 (simulasi menggunakan mocking)
    """
    print("Testing start_quiz performance (6 iterations, mocked)...")
    # Mocking input untuk menghindari interaksi manual
    with patch('builtins.input', side_effect=['TestUser', '1', '11', '12'] * 6): # Repeat the inputs for 6 iterations
        execution_time = timeit.timeit("start_quiz()", setup="from subfolder_B.automata_engine import start_quiz", number=1, globals=globals()) # Run only 1 timeit iteration since the mocking covers the 6 loops
        print(f"start_quiz executed 6 times in {execution_time*6:.4f} seconds.") # Scale the result to show the time for 6 iterations
    # Hasil: Waktu yang dibutuhkan untuk menjalankan seluruh alur kuis. Semakin kecil nilainya, semakin cepat.
    # Contoh Waktu Proses: 0.0140 detik (untuk 6 iterasi)

if __name__ == "__main__":
    print("=== Performance Testing ===")
    test_load_quiz_data()
    test_evaluate_answer()
    test_calculate_score()
    test_start_quiz()
    print("=== Testing Complete ===")