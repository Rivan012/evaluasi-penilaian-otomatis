from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from thefuzz import fuzz
from datetime import datetime
import joblib
import json
import os

app = FastAPI(title="Intelligent Tutoring System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "fuzzy_matching_model.joblib"
USERS_FILE = "users.json"

if os.path.exists(MODEL_PATH):
    model_config = joblib.load(MODEL_PATH)
else:
    model_config = {
        "threshold": {"sangat_baik": 80, "cukup": 60, "perlu_perbaikan": 0}
    }

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

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

class AuthRequest(BaseModel):
    username: str
    password: str

class EvaluationRequest(BaseModel):
    username: str
    question_id: int
    jawaban_siswa: str

# --- ENDPOINT AUTH & PROFIL ---
@app.post("/register")
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

@app.post("/login")
def login(data: AuthRequest):
    username = data.username.strip()
    users = load_users()

    if username not in users:
        return {"success": False, "message": "Akun tidak ditemukan. Silakan daftar dulu."}
    if users[username]["password"] != data.password:
        return {"success": False, "message": "Password salah!"}

    return {"success": True, "user": users[username]}

@app.get("/user/{username}")
def get_user(username: str):
    users = load_users()
    if username not in users:
        return {"error": "User tidak ditemukan"}
    return users[username]

@app.get("/leaderboard")
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

# --- ENDPOINT SOAL & EVALUASI ---
@app.get("/questions")
def get_questions():
    return [
        {"id": q["id"], "kategori": q["kategori"], "pertanyaan": q["pertanyaan"]}
        for q in BANK_SOAL
    ]

@app.post("/evaluate")
def evaluate_answer(data: EvaluationRequest):
    soal = next((q for q in BANK_SOAL if q["id"] == data.question_id), None)
    if not soal:
        return {"error": "Soal tidak ditemukan"}

    score = fuzz.ratio(
        data.jawaban_siswa.lower().strip(),
        soal["kunci_jawaban"].lower().strip()
    )

    thresholds = model_config.get("threshold", {})
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

    users = load_users()
    if data.username in users:
        user = users[data.username]
        user["xp"] += earned_xp
        user["level"] = (user["xp"] // 100) + 1
        user["totalAnswered"] += 1
        if kategori == "sangat_baik":
            user["highScores"] += 1

        user["history"].insert(0, {
            "tanggal": datetime.now().strftime("%H:%M"),
            "soal": soal["pertanyaan"][:45] + "...",
            "skor": score,
            "kategori": kategori,
            "xp": earned_xp
        })
        user["history"] = user["history"][:10]
        save_users(users)

    return {
        "score": score,
        "kategori": kategori,
        "earned_xp": earned_xp,
        "kunci_jawaban": soal["kunci_jawaban"]
    }

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")