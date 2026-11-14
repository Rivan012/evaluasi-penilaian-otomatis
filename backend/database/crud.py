import json
import os
from backend.database.connection import get_connection
from backend.config import USERS_FILE, ADMIN_USERNAME, ADMIN_PASSWORD

def get_all_questions():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, kategori, pertanyaan FROM questions ORDER BY id ASC")
        return [dict(row) for row in cursor.fetchall()]

def get_question_by_id(question_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, kategori, pertanyaan, kunci_jawaban FROM questions WHERE id = ?", (question_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

def load_users():
    if not os.path.exists(USERS_FILE):
        initial = {
            ADMIN_USERNAME: {
                "username": ADMIN_USERNAME,
                "password": ADMIN_PASSWORD,
                "xp": 500,
                "level": 6,
                "totalAnswered": 10,
                "highScores": 8,
                "history": []
            }
        }
        save_users(initial)
        return initial
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
