import unittest
from backend.algorithms.preprocessing import clean_text
from backend.algorithms.prediction import evaluate_answer_text
from backend.database.connection import init_db
from backend.database.crud import get_all_questions, get_question_by_id

class BackendTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    def test_clean_text(self):
        self.assertEqual(clean_text("  Halo DUNIA  "), "halo dunia")

    def test_evaluation(self):
        res = evaluate_answer_text(
            "proses tumbuhan hijau menghasilkan makanan",
            "proses tumbuhan hijau menghasilkan makanan dan energi"
        )
        self.assertGreaterEqual(res["score"], 80)
        self.assertEqual(res["kategori"], "sangat_baik")
        self.assertEqual(res["earned_xp"], 50)

    def test_sqlite_bank_soal(self):
        questions = get_all_questions()
        self.assertGreaterEqual(len(questions), 4)
        q1 = get_question_by_id(1)
        self.assertIsNotNone(q1)
        self.assertIn("kunci_jawaban", q1)

if __name__ == "__main__":
    unittest.main()
