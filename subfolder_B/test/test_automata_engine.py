import unittest
from unittest.mock import patch
from io import StringIO
from subfolder_B.automata_engine import start_quiz

class TestAutomataEngine(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'Nama Tester',  # nama pengguna
        '1',            # pilih kategori Matematika
        '2',            # jawaban 1
        '4'             # jawaban 2
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_quiz_matematika(self, stdout, mock_input):
        # Dummy soal
        questions = [
            {"category": "Matematika", "question": "1+1?", "answer": "2"},
            {"category": "Matematika", "question": "2+2?", "answer": "4"}
        ]

        # Patch agar tidak ambil soal dari file
        with patch('subfolder_B.automata_engine.load_questions_by_category', return_value=questions):
            start_quiz()
            output = stdout.getvalue()
            
            # Uji bahwa skor akhir 100/100 muncul
            self.assertIn("skor akhir Anda: 100/100", output)
            
            # Uji bahwa 2 jawaban benar muncul
            self.assertEqual(output.count("✅ Benar!"), 2)

if __name__ == '__main__':
    unittest.main()
