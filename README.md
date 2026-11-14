# Sistem Evaluasi dan Penilaian Otomatis Jawaban Short-Answer

Aplikasi web berbasis FastAPI untuk penilaian otomatis jawaban esai pendek (*short-answer*) siswa dalam Bahasa Indonesia menggunakan algoritma **Fuzzy Matching** (`thefuzz` / Levenshtein Distance Ratio). Dilengkapi sistem umpan balik formatif (*Intelligent Tutoring System* / ITS), sistem gamifikasi (XP, level, history skor), dan papan peringkat (*leaderboard*).

---

## Fitur Utama

- **Automatic Evaluation Engine**: Mengukur kemiripan leksikal teks jawaban siswa terhadap kunci jawaban rujukan secara toleran salah ketik (*typo-tolerant*) menggunakan rasio Levenshtein (`thefuzz`).
- **Klasifikasi Predikat & Ambang Batas (Threshold)**:
  - `sangat_baik`: Skor $\ge 80$ (+50 XP)
  - `cukup`: $60 \le \text{Skor} < 80$ (+25 XP)
  - `perlu_perbaikan`: Skor $< 60$ (+5 XP)
- **Gamifikasi & Tracking Siswa**: Akumulasi XP, kenaikan level berkala ($Level = \lfloor XP / 100 \rfloor + 1$), riwayat pengerjaan soal, dan pencatatan high scores.
- **Papan Peringkat (Leaderboard)**: Menampilkan ranking seluruh siswa terdaftar berdasarkan perolehan XP.
- **Frontend Interaktif & Responsif**: Antarmuka berbasis web modern (HTML, CSS, JS) dengan navigasi portal login/register, dashboard evaluasi soal, profil, dan leaderboard.

---

## Struktur Direktori

```text
evaluasi-penilaian-otomatis/
├── backend/
│   ├── algorithms/        # Logika fuzzy matching & pra-pemrosesan teks
│   ├── api/               # Endpoint REST API (health, routes)
│   ├── database/          # Penyimpanan data (users.json & bank soal CRUD)
│   ├── models/            # Model loader (fuzzy_matching_model.joblib)
│   ├── schemas/           # Pydantic request & response schemas
│   ├── services/          # Layanan ITS feedback & gamifikasi
│   └── main.py            # Konfigurasi FastAPI & static files
├── frontend/
│   ├── index.html         # Portal utama & navigasi
│   ├── login.html         # Halaman autentikasi login & registrasi
│   ├── dashboard.html     # Pengerjaan kuis & kartu hasil evaluasi instan
│   ├── profile.html       # Tampilan level, XP, & riwayat pengerjaan
│   ├── leaderboard.html   # Papan peringkat siswa realtime
│   ├── css/
│   │   ├── style.css      # Styling global antarmuka
│   │   ├── dashboard.css  # Styling khusus komponen dashboard & kuis
│   │   └── responsive.css # Penyesuaian layout perangkat mobile/tablet
│   └── js/
│       ├── api.js         # Endpoint helper & request client
│       ├── app.js         # Logika autentikasi & interaksi UI utama
│       ├── dashboard.js   # State management pengerjaan kuis
│       ├── gamification.js# Kalkulasi XP, level, & badge
│       └── leaderboard.js # Fetch & render tabel peringkat
├── tests/                 # Unit test backend
├── main.py                # Server entrypoint (Uvicorn runner)
├── users.json             # Penyimpanan data pengguna & histori skor
├── requirements.txt       # Dependensi pustaka Python
└── README.md              # Dokumentasi proyek
```

---

## Persyaratan Sistem

- Python 3.10+
- Browser modern (Chrome, Edge, Firefox)

---

## Instalasi & Menjalankan Proyek

1. **Clone atau buka direktori proyek**:
   ```bash
   cd D:/evaluasi-penilaian-otomatis
   ```

2. **Buat dan aktifkan virtual environment**:
   ```bash
   python -m venv .venv
   # Windows (CMD / PowerShell):
   .venv\Scripts\activate
   # Git Bash:
   source .venv/Scripts/activate
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi Environment**:
   ```bash
   cp .env.example .env
   ```

5. **Jalankan server aplikasi**:
   ```bash
   python main.py
   ```
   Aplikasi berjalan di `http://127.0.0.1:8000`.

6. **Akses Aplikasi**:
   - Web App: `http://127.0.0.1:8000/index.html` (atau `http://127.0.0.1:8000/login.html`)
   - Dokumentasi Interaktif API (Swagger UI): `http://127.0.0.1:8000/docs`

---

## Ringkasan Endpoint API

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `POST` | `/register` | Registrasi akun pengguna baru |
| `POST` | `/login` | Autentikasi dan login pengguna |
| `GET` | `/user/{username}` | Mengambil data profil, XP, level, dan histori pengguna |
| `GET` | `/questions` | Mengambil daftar soal kuis short-answer |
| `POST` | `/evaluate` | Evaluasi jawaban teks siswa, hitung skor, predikat, dan reward XP |
| `GET` | `/leaderboard` | Mengambil data peringkat seluruh siswa berdasarkan akumulasi XP |

---

## Lisensi

Proyek ini dikembangkan untuk keperluan akademik tugas evaluasi pembelajaran otomatis.
