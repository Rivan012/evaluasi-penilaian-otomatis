def get_feedback(kategori: str) -> str:
    feedbacks = {
        "sangat_baik": "Pemahaman konsep sangat baik dan presisi.",
        "cukup": "Jawaban cukup mendekati, cermati detail kata kunci.",
        "perlu_perbaikan": "Jawaban belum sesuai, silakan tinjau kembali materi."
    }
    return feedbacks.get(kategori, "")
