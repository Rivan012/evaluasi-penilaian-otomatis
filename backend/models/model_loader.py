import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "fuzzy_matching_model.joblib"
)

def load_thresholds():
    if os.path.exists(MODEL_PATH):
        try:
            config = joblib.load(MODEL_PATH)
            return config.get("threshold", {})
        except Exception:
            pass
    return {"sangat_baik": 80, "cukup": 60, "perlu_perbaikan": 0}
