import json
import os

USERS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "users.json"
)

BANK_SOAL = [
    {
        "id": 1,
        "kategori": "SISTEM INFORMASI",
        "pertanyaan": "Jelaskan fungsi utama dari algoritma Fuzzy Matching dalam evaluasi jawaban teks otomatis!",
        "kunci_jawaban": "Mengukur tingkat kemiripan teks antara jawaban siswa dan kunci jawaban berdasarkan jarak karakter"
    },
    {
        "id": 2,
        "kategori": "ALGORITMA & NLP",
        "pertanyaan": "Apa yang dimaksud dengan Levenshtein Distance dalam pencocokan string?",
        "kunci_jawaban": "Jumlah minimum operasi pengeditan karakter seperti penyisipan penghapusan atau penggantian untuk mengubah satu kata menjadi kata lain"
    },
    {
        "id": 3,
        "kategori": "INTELLIGENT TUTORING SYSTEM",
        "pertanyaan": "Mengapa Intelligent Tutoring System membutuhkan umpan balik otomatis setelah penilaian jawaban?",
        "kunci_jawaban": "Membantu siswa mengetahui letak kekurangan jawaban dan memperbaiki pemahaman secara mandiri"
    },
    {
        "id": 4,
        "kategori": "PEMROSESAN TEKS",
        "pertanyaan": "Apa tujuan tahap preprocessing seperti lowercase pada penilaian jawaban singkat?",
        "kunci_jawaban": "Menyeragamkan huruf kapital menjadi huruf kecil agar perbandingan teks lebih konsisten dan akurat"
    }
]

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
