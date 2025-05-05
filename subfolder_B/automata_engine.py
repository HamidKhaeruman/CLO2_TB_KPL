# subfolder_B/automata_engine.py
from subfolder_B.question_utils import load_questions_by_category, evaluate_answer, calculate_score
from subfolder_A.kuis_table import load_quiz_data, lookup_quiz

def start_quiz():
    print("=== Selamat datang di EduQuiz ===")
    name = input("Masukkan nama Anda: ")

    print("\nPilih kategori:")
    print("1. Matematika")
    print("2. Bahasa Indonesia")
    print("3. Bahasa Inggris")
    print("4. Manajemen Bisnis")
    print("5. Cryptography")

    category_input = input("Pilihan (1-5): ")

    category = "" # Inisialisasi category dengan nilai default
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
        print("Pilihan tidak valid. Default ke 'Matematika'")
        category = "Matematika"

    chosen_set = load_questions_by_category(category)

    correct_count = 0
    for index, quiz in enumerate(chosen_set):
        print(f"\nSoal {index}: {quiz['question']}")
        answer = input("Jawaban Anda: ")
        if evaluate_answer(quiz['answer'], answer):
            print("✅ Benar!")
            correct_count += 1
        else:
            print(f"❌ Salah. Jawaban yang benar: {quiz['answer']}")

    score = calculate_score(correct_count, len(chosen_set))
    print(f"\n{name}, skor akhir Anda: {score}/100")
    print("=== Terima kasih telah bermain! ===")