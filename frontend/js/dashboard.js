document.addEventListener("DOMContentLoaded", async () => {
    const data = await fetchUserData();
    if (!data) return;

    const elTotal = document.getElementById("stat-total");
    const elAvg = document.getElementById("stat-avg");
    const elXP = document.getElementById("stat-xp");
    const elLevel = document.getElementById("stat-level");

    if (elTotal) elTotal.textContent = data.totalAnswered;
    if (elXP) elXP.textContent = `${data.xp} XP`;
    if (elLevel) elLevel.textContent = `Level ${data.level}`;

    if (elAvg) {
        if (data.history.length === 0) {
            elAvg.textContent = "0%";
        } else {
            const sum = data.history.reduce((acc, item) => acc + item.skor, 0);
            elAvg.textContent = `${Math.round(sum / data.history.length)}%`;
        }
    }

    const xpProgress = data.xp % 100;
    const xpFill = document.getElementById("level-progress-fill");
    const xpText = document.getElementById("level-progress-text");
    if (xpFill) xpFill.style.width = `${xpProgress}%`;
    if (xpText) xpText.textContent = `${xpProgress} / 100 XP menuju Level ${data.level + 1}`;

    const historyBody = document.getElementById("history-body");
    if (historyBody) {
        if (data.history.length === 0) {
            historyBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:#94a3b8;">Belum ada riwayat evaluasi.</td></tr>`;
        } else {
            historyBody.innerHTML = data.history.map(item => `
                <tr>
                    <td>${item.tanggal}</td>
                    <td>${item.soal}</td>
                    <td><strong>${item.skor}%</strong></td>
                    <td>+${item.xp} XP</td>
                </tr>
            `).join("");
        }
    }

    if (data.totalAnswered >= 1) document.getElementById("badge-first")?.classList.add("unlocked");
    if (data.highScores >= 3) document.getElementById("badge-master")?.classList.add("unlocked");
    if (data.level >= 2) document.getElementById("badge-levelup")?.classList.add("unlocked");
});