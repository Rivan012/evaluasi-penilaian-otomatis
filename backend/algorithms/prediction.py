from thefuzz import fuzz
from backend.algorithms.preprocessing import clean_text
from backend.models.model_loader import load_thresholds

def evaluate_answer_text(student_answer: str, reference_answer: str):
    score = fuzz.ratio(clean_text(student_answer), clean_text(reference_answer))
    thresholds = load_thresholds()
    batas_baik = thresholds.get("sangat_baik", 80)
    batas_cukup = thresholds.get("cukup", 60)

    if score >= batas_baik:
        kategori = "sangat_baik"
        earned_xp = 50
    elif score >= batas_cukup:
        kategori = "cukup"
        earned_xp = 25
    else:
        kategori = "perlu_perbaikan"
        earned_xp = 5

    return {
        "score": score,
        "kategori": kategori,
        "earned_xp": earned_xp
    }
