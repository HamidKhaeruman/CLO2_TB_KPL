import unittest
from subfolder_B.question_utils import load_questions_by_category, evaluate_answer, calculate_score

class TestQuestionUtils(unittest.TestCase):

    def test_load_questions_by_category(self):
        questions = load_questions_by_category("subfolder_A/soal_config.json", "Matematika")
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]['category'], "Matematika")

    def test_evaluate_answer(self):
        self.assertTrue(evaluate_answer("Jawaban Benar", "jawaban benar"))
        self.assertFalse(evaluate_answer("Jawaban Benar", "jawaban salah"))

    def test_calculate_score(self):
        score = calculate_score(5, 10)
        self.assertEqual(score, 50)

if __name__ == '__main__':
    unittest.main()