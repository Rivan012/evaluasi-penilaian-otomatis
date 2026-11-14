document.addEventListener("DOMContentLoaded", async () => {
    const submitBtn = document.getElementById("submit-btn");
    const nextBtn = document.getElementById("next-btn");
    const studentInput = document.getElementById("student-answer");
    const resultSection = document.getElementById("result-section");

    let questions = [];
    let currentIndex = 0;

    try {
        questions = await fetchQuestionsAPI();
        renderQuestion(currentIndex);
    } catch (err) {
        document.getElementById("question-text").textContent = "Gagal memuat soal. Pastikan server uvicorn berjalan.";
    }

    function renderQuestion(index) {
        const q = questions[index];
        if (!q) return;

        document.getElementById("question-badge").textContent = `SOAL #0${index + 1} / 0${questions.length} • ${q.kategori}`;
        document.getElementById("question-text").textContent = q.pertanyaan;
        studentInput.value = "";
        resultSection.classList.add("hidden");

        nextBtn.textContent = (index === questions.length - 1) ? "Ulangi dari Soal #01 ↺" : "Soal Berikutnya →";
    }

    submitBtn.addEventListener("click", async () => {
        const jawaban = studentInput.value.trim();
        if (!jawaban) {
            alert("Isi jawaban terlebih dahulu!");
            return;
        }

        const currentQuestion = questions[currentIndex];
        submitBtn.disabled = true;
        submitBtn.innerHTML = "<span>Memproses Fuzzy Ratio...</span>";

        try {
            const result = await evaluateAnswerAPI(currentQuestion.id, jawaban);
            renderResult(currentQuestion.pertanyaan, jawaban, result);
        } catch (err) {
            alert("Terjadi kesalahan saat menghubungi server evaluasi.");
        }

        submitBtn.disabled = false;
        submitBtn.innerHTML = "<span>Analisis Jawaban</span>";
    });

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % questions.length;
        renderQuestion(currentIndex);
    });

    function renderResult(pertanyaan, jawaban, result) {
        const { score, kategori, kunci_jawaban } = result;

        if (typeof recordEvaluation === "function") {
            recordEvaluation(pertanyaan, jawaban, score, kategori);
        }

        resultSection.classList.remove("hidden");
        document.getElementById("score-value").textContent = `${score}%`;
        document.getElementById("progress-fill").style.width = `${score}%`;
        document.getElementById("ideal-answer-text").textContent = kunci_jawaban;

        const statusBadge = document.getElementById("status-badge");
        const feedbackText = document.getElementById("feedback-text");
        const xpBadge = document.getElementById("xp-badge");

        statusBadge.className = "status-pill";

        if (kategori === "sangat_baik" || score >= 80) {
            statusBadge.textContent = "Sangat Baik";
            statusBadge.classList.add("status-sangat-baik");
            feedbackText.textContent = "Jawabanmu sangat akurat dan sesuai dengan konsep kunci!";
            xpBadge.textContent = "+50 XP";
        } else if (kategori === "cukup" || score >= 60) {
            statusBadge.textContent = "Cukup";
            statusBadge.classList.add("status-cukup");
            feedbackText.textContent = "Jawaban sudah mendekati benar, namun masih ada kata kunci penting yang terlewat.";
            xpBadge.textContent = "+25 XP";
        } else {
            statusBadge.textContent = "Perlu Perbaikan";
            statusBadge.classList.add("status-perlu-perbaikan");
            feedbackText.textContent = "Tingkat kemiripan masih rendah. Bandingkan jawabanmu dengan referensi jawaban ideal di bawah.";
            xpBadge.textContent = "+5 XP";
        }
    }
});