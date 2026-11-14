const API_BASE_URL = "";

async function fetchQuestionsAPI() {
    const response = await fetch(`${API_BASE_URL}/questions`);
    if (!response.ok) throw new Error("Gagal memuat soal dari server");
    return await response.json();
}

async function evaluateAnswerAPI(questionId, studentAnswer) {
    const response = await fetch(`${API_BASE_URL}/evaluate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: getCurrentUsername(),
            question_id: questionId,
            jawaban_siswa: studentAnswer
        })
    });

    if (!response.ok) throw new Error("Gagal terhubung ke server evaluasi");
    return await response.json();
}