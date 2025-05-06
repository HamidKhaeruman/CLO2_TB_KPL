# ================================================================
# Unit Test Verification:
# Pengujian fungsi start_quiz() telah berhasil dijalankan menggunakan unittest.
# Hasil: OK (1 test ran, no failures or errors)
# Tester: Hamid Khaeruman (2211104040)
# Tanggal Pengujian: 6 Mei 2025
# ================================================================

# subfolder_B/automata_engine.py
from subfolder_B.question_utils import load_questions_by_category, evaluate_answer, calculate_score
from subfolder_A.kuis_table import load_quiz_data, lookup_quiz

# Unit Test Result:
# Fungsi start_quiz() telah berhasil diuji menggunakan unittest
# dengan hasil OK (tanpa error, fault, atau failure).
# Test mencakup skenario kuis kategori Matematika dengan dua soal.
# Output yang diuji termasuk verifikasi skor akhir 100/100 dan respons jawaban benar sebanyak dua kali.

# Fungsi utama untuk memulai kuis
def start_quiz():
    """
    Memulai kuis dengan meminta nama pengguna dan memilih kategori.
    Kemudian, menampilkan pertanyaan dan menghitung skor akhir.
    """
    print("=== Selamat datang di EduQuiz ===")
    name = input("Masukkan nama Anda: ")

    # Menampilkan pilihan kategori kuis
    print("\nPilih kategori:")
    print("1. Matematika")
    print("2. Bahasa Indonesia")
    print("3. Bahasa Inggris")
    print("4. Manajemen Bisnis")
    print("5. Cryptography")

    # Meminta input pilihan kategori
    category_input = input("Pilihan (1-5): ")

    # Menentukan kategori berdasarkan input pengguna
    # Menggunakan teknik konstruksi Automata State (finite state machine) untuk menentukan kategori
    category = ""  # Inisialisasi category dengan nilai default
    if category_input == "1":
        category = "Matematika"
    elif category_input == "2":
        category = "Bahasa Indonesia"
    elif category_input == "3":
        category = "Bahasa Inggris"
    elif category_input == "4":
        category = "Manajemen Bisnis"
    elif category_input == "5":
        category = "Kriptografi"
    else:
        # Menggunakan teknik konstruksi Defensive Programming untuk menangani input tidak valid
        print("Pilihan tidak valid. Default ke 'Matematika'")
        category = "Matematika"

    # Menggunakan teknik konstruksi Defensive Programming untuk menangani kasus tidak ada pertanyaan
    chosen_set = load_questions_by_category(category)
    if not chosen_set:
        print("Tidak ada pertanyaan untuk kategori ini")
        return

    # Inisialisasi counter jawaban benar
    correct_count = 0
    # Menampilkan pertanyaan dan memeriksa jawaban pengguna
    for index, quiz in enumerate(chosen_set):
        print(f"\nSoal {index}: {quiz['question']}")
        answer = input("Jawaban Anda: ")
        
        # Menggunakan teknik konstruksi Defensive Programming untuk memeriksa jawaban pengguna
        if evaluate_answer(quiz['answer'], answer):
            print("✅ Benar!")
            correct_count += 1
        else:
            print(f"❌ Salah. Jawaban yang benar: {quiz['answer']}")

    # Menghitung skor akhir
    score = calculate_score(correct_count, len(chosen_set))
    print(f"\n{name}, skor akhir Anda: {score}/100")
    print("=== Terima kasih telah bermain! ===")