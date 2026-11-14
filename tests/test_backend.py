import unittest
from backend.algorithms.preprocessing import clean_text
from backend.algorithms.prediction import evaluate_answer_text
from backend.database.crud import load_users, BANK_SOAL

class BackendTest(unittest.TestCase):
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

    def test_bank_soal(self):
        self.assertGreaterEqual(len(BANK_SOAL), 1)

if __name__ == "__main__":
    unittest.main()
