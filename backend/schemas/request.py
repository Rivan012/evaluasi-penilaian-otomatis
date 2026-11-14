from pydantic import BaseModel

class AuthRequest(BaseModel):
    username: str
    password: str

class EvaluationRequest(BaseModel):
    username: str
    question_id: int
    jawaban_siswa: str
