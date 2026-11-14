from datetime import datetime
from backend.database.crud import load_users, save_users

def update_user_progress(username: str, score: int, kategori: str, earned_xp: int, question_text: str):
    users = load_users()
    if username not in users:
        return None

    user = users[username]
    user["xp"] += earned_xp
    user["level"] = (user["xp"] // 100) + 1
    user["totalAnswered"] += 1
    if kategori == "sangat_baik":
        user["highScores"] += 1

    user["history"].insert(0, {
        "tanggal": datetime.now().strftime("%H:%M"),
        "soal": question_text[:45] + "...",
        "skor": score,
        "kategori": kategori,
        "xp": earned_xp
    })
    user["history"] = user["history"][:10]
    save_users(users)
    return user
