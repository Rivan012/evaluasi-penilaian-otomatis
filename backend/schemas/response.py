from pydantic import BaseModel

class EvaluationResponse(BaseModel):
    score: int
    kategori: str
    earned_xp: int
    kunci_jawaban: str
    feedback: str
