# subfolder_B/automata_engine.py
from subfolder_B.question_utils import load_questions_by_category, evaluate_answer, calculate_score

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
    
if category_input == "1":
    category = "Matematika"
elif category_input == "2":
    category = "Bahasa Indonesia"
elif category_input == "3":
    category = "Bahasa Inggris"
elif category_input == "4":
    category = "Manajemen Bisnis"
elif category_input == "5":
    category = "Cryptography"
else:
    print("Pilihan tidak valid. Default ke 'Matematika'")
    category = "Matematika"


    questions = load_questions_by_category("subfolder_A/soal_config.json", category)

    correct_count = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nSoal {idx}: {q['question']}")
        answer = input("Jawaban Anda: ")
        if evaluate_answer(q['answer'], answer):
            print("✅ Benar!")
            correct_count += 1
        else:
            print(f"❌ Salah. Jawaban yang benar: {q['answer']}")

    score = calculate_score(correct_count, len(questions))
    print(f"\n{name}, skor akhir Anda: {score}/100")
    print("=== Terima kasih telah bermain! ===")
