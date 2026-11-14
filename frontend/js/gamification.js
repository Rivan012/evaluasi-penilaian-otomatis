const CURRENT_USER_KEY = "neurograde_current_user";

function getCurrentUsername() {
    return localStorage.getItem(CURRENT_USER_KEY);
}

(function enforceAuth() {
    const isLoginPage = window.location.pathname.endsWith("login.html");
    const loggedInUser = getCurrentUsername();

    if (!loggedInUser && !isLoginPage) {
        window.location.replace("login.html");
    }
})();

async function registerUser(username, password) {
    const res = await fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (data.success) {
        localStorage.setItem(CURRENT_USER_KEY, data.user.username);
    }
    return data;
}

async function loginUser(username, password) {
    const res = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (data.success) {
        localStorage.setItem(CURRENT_USER_KEY, data.user.username);
    }
    return data;
}

function logoutUser() {
    localStorage.removeItem(CURRENT_USER_KEY);
    window.location.replace("login.html");
}

async function fetchUserData() {
    const current = getCurrentUsername();
    if (!current) return null;

    const res = await fetch(`/user/${encodeURIComponent(current)}`);
    const data = await res.json();
    if (data.error) {
        logoutUser();
        return null;
    }
    return data;
}

document.addEventListener("DOMContentLoaded", () => {
    const currentFile = window.location.pathname.split("/").pop() || "index.html";
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === currentFile) {
            link.classList.add("active");
        }
    });
});