import unittest
from subfolder_B.question_utils import load_questions_by_category, evaluate_answer, calculate_score

class TestQuestionUtils(unittest.TestCase):

    def test_load_questions_by_category(self):
        questions = load_questions_by_category("Matematika")
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]['category'], "Matematika")

    def test_evaluate_answer_different_cases(self):
        self.assertTrue(evaluate_answer("Jawaban Benar", "Jawaban Benar"))
        self.assertTrue(evaluate_answer("jawaban benar", "jawaban benar"))
        self.assertFalse(evaluate_answer("Jawaban Benar", "jawaban salah"))
        self.assertFalse(evaluate_answer("Jawaban Benar", "Jawaban salah"))

    def test_calculate_score_different_cases(self):
        self.assertEqual(calculate_score(10, 10), 100)
        self.assertEqual(calculate_score(5, 10), 50)
        self.assertEqual(calculate_score(0, 10), 0)

if __name__ == '__main__':
    unittest.main()