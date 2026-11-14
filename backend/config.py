import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

APP_NAME = os.getenv("APP_NAME", "Intelligent Tutoring System API")
APP_ENV = os.getenv("APP_ENV", "development")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
SECRET_KEY = os.getenv("SECRET_KEY", "default-dev-secret-key-change-in-production")

DATABASE_PATH = os.getenv("DATABASE_PATH", "database.sqlite")
if not os.path.isabs(DATABASE_PATH):
    DATABASE_PATH = os.path.join(BASE_DIR, DATABASE_PATH)

USERS_FILE = os.getenv("USERS_FILE", "users.json")
if not os.path.isabs(USERS_FILE):
    USERS_FILE = os.path.join(BASE_DIR, USERS_FILE)

MODEL_PATH = os.getenv("MODEL_PATH", "fuzzy_matching_model.joblib")
if not os.path.isabs(MODEL_PATH):
    MODEL_PATH = os.path.join(BASE_DIR, MODEL_PATH)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin#2026!Secure")
