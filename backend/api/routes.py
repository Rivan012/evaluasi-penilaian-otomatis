from fastapi import APIRouter
from backend.schemas.request import AuthRequest, EvaluationRequest
from backend.database.crud import load_users, save_users, BANK_SOAL
from backend.algorithms.prediction import evaluate_answer_text
from backend.services.gamification_service import update_user_progress
from backend.services.its_service import get_feedback

router = APIRouter()

@router.post("/register")
def register(data: AuthRequest):
    username = data.username.strip()
    if not username or not data.password:
        return {"success": False, "message": "Username dan password wajib diisi!"}

    users = load_users()
    if username in users:
        return {"success": False, "message": "Username sudah terdaftar, gunakan yang lain."}

    users[username] = {
        "username": username,
        "password": data.password,
        "xp": 0,
        "level": 1,
        "totalAnswered": 0,
        "highScores": 0,
        "history": []
    }
    save_users(users)
    return {"success": True, "user": users[username]}

@router.post("/login")
def login(data: AuthRequest):
    username = data.username.strip()
    users = load_users()

    if username not in users:
        return {"success": False, "message": "Akun tidak ditemukan. Silakan daftar dulu."}
    if users[username]["password"] != data.password:
        return {"success": False, "message": "Password salah!"}

    return {"success": True, "user": users[username]}

@router.get("/user/{username}")
def get_user(username: str):
    users = load_users()
    if username not in users:
        return {"error": "User tidak ditemukan"}
    return users[username]

@router.get("/leaderboard")
def get_leaderboard():
    users = load_users()
    board = [
        {
            "username": u["username"],
            "level": u["level"],
            "xp": u["xp"]
        }
        for u in users.values()
    ]
    board.sort(key=lambda x: x["xp"], reverse=True)
    return board

@router.get("/questions")
def get_questions():
    return [
        {"id": q["id"], "kategori": q["kategori"], "pertanyaan": q["pertanyaan"]}
        for q in BANK_SOAL
    ]

@router.post("/evaluate")
def evaluate_answer(data: EvaluationRequest):
    soal = next((q for q in BANK_SOAL if q["id"] == data.question_id), None)
    if not soal:
        return {"error": "Soal tidak ditemukan"}

    result = evaluate_answer_text(data.jawaban_siswa, soal["kunci_jawaban"])
    feedback = get_feedback(result["kategori"])
    update_user_progress(
        username=data.username,
        score=result["score"],
        kategori=result["kategori"],
        earned_xp=result["earned_xp"],
        question_text=soal["pertanyaan"]
    )

    return {
        "score": result["score"],
        "kategori": result["kategori"],
        "earned_xp": result["earned_xp"],
        "kunci_jawaban": soal["kunci_jawaban"],
        "feedback": feedback
    }
