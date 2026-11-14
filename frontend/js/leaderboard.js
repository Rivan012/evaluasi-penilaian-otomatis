document.addEventListener("DOMContentLoaded", async () => {
    const tbody = document.getElementById("leaderboard-body");
    if (!tbody) return;

    const currentUsername = getCurrentUsername();
    const res = await fetch("/leaderboard");
    const players = await res.json();

    if (players.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="4" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">
                    Belum ada peserta terdaftar.
                </td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = players.map((player, index) => {
        const rank = index + 1;
        const rankClass = rank <= 3 ? `rank-${rank}` : "";
        const isMe = player.username === currentUsername;
        const displayName = isMe ? `${player.username} (Kamu)` : player.username;
        const highlightStyle = isMe ? 'style="background: rgba(168, 85, 247, 0.22);"' : "";

        return `
            <tr ${highlightStyle}>
                <td><span class="rank-badge ${rankClass}">${rank}</span></td>
                <td><strong>${displayName}</strong></td>
                <td>Level ${player.level}</td>
                <td style="color: var(--cyan-accent); font-weight: 700;">${player.xp} XP</td>
            </tr>
        `;
    }).join("");
});