import unittest
from unittest.mock import patch
from io import StringIO
from subfolder_B.automata_engine import start_quiz
import json

class TestAutomataEngine(unittest.TestCase):

    @patch('builtins.input', side_effect=['Nama Tester', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_quiz_matematika(self, stdout, mock_input):
        # Load questions manually to avoid file access during test
        questions = [
            {"category": "Matematika", "question": "1+1?", "answer": "2"},
            {"category": "Matematika", "question": "2+2?", "answer": "4"}
        ]
        
        # Patch load_questions_by_category to return our test questions
        with patch('subfolder_B.automata_engine.load_questions_by_category', return_value=questions):
            start_quiz()
            output = stdout.getvalue()
            self.assertIn("Nama Tester, skor akhir Anda", output)

if __name__ == '__main__':
    unittest.main()