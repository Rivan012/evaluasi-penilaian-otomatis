import json
import os
from backend.database.connection import get_connection

USERS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "users.json"
)

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
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
