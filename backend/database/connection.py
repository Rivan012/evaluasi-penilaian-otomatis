import sqlite3
from backend.config import DATABASE_PATH

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    # ponytail: sqlite DDL embedded directly; upgrade to Alembic if schema migrations across environments are needed.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(questions)")
    cols = [row["name"] for row in cursor.fetchall()]
    if cols and "kategori" not in cols:
        cursor.execute("DROP TABLE questions")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kategori TEXT NOT NULL,
        pertanyaan TEXT NOT NULL,
        kunci_jawaban TEXT NOT NULL
    );
    """)
    cursor.execute("SELECT COUNT(*) as count FROM questions")
    if cursor.fetchone()["count"] == 0:
        seed_questions = [
            (
                "SISTEM INFORMASI",
                "Jelaskan fungsi utama dari algoritma Fuzzy Matching dalam evaluasi jawaban teks otomatis!",
                "Mengukur tingkat kemiripan teks antara jawaban siswa dan kunci jawaban berdasarkan jarak karakter"
            ),
            (
                "ALGORITMA & NLP",
                "Apa yang dimaksud dengan Levenshtein Distance dalam pencocokan string?",
                "Jumlah minimum operasi pengeditan karakter seperti penyisipan penghapusan atau penggantian untuk mengubah satu kata menjadi kata lain"
            ),
            (
                "INTELLIGENT TUTORING SYSTEM",
                "Mengapa Intelligent Tutoring System membutuhkan umpan balik otomatis setelah penilaian jawaban?",
                "Membantu siswa mengetahui letak kekurangan jawaban dan memperbaiki pemahaman secara mandiri"
            ),
            (
                "PEMROSESAN TEKS",
                "Apa tujuan tahap preprocessing seperti lowercase pada penilaian jawaban singkat?",
                "Menyeragamkan huruf kapital menjadi huruf kecil agar perbandingan teks lebih konsisten dan akurat"
            )
        ]
        cursor.executemany(
            "INSERT INTO questions (kategori, pertanyaan, kunci_jawaban) VALUES (?, ?, ?)",
            seed_questions
        )
        conn.commit()
    conn.close()
