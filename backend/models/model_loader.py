import os
import joblib
from backend.config import MODEL_PATH

def load_thresholds():
    if os.path.exists(MODEL_PATH):
        try:
            config = joblib.load(MODEL_PATH)
            return config.get("threshold", {})
        except Exception:
            pass
    return {"sangat_baik": 80, "cukup": 60, "perlu_perbaikan": 0}
