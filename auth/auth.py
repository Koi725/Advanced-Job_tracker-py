# auth/auth.py

from auth.auth_utils import load_users, save_users, encrypt_password, decrypt_password
from auth.password_checker import is_password_strong
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_info, log_error, log_warning


def register_user():
    print_title("\n📋 Register New User")
    username = input("👤 Enter username: ").strip()
    users = load_users()

    if username in users:
        print_error("❌ Username already exists.")
        log_warning(f"Registration attempt with existing username: {username}")
        return

    password = input("🔑 Enter password: ").strip()

    if not is_password_strong(password):
        print_error("❌ Weak password. Try again.")
        log_warning(f"Weak password attempt for username: {username}")
        return

    encrypted_password = encrypt_password(password)
    skill_tags = input("🛠️ Enter your skills (comma-separated): ").strip()

    users[username] = {
        "password": encrypted_password,
        "skills": [tag.strip() for tag in skill_tags.split(",") if tag.strip()],
        "role": "user",
    }

    save_users(users)
    print_success("✅ Registration successful!")
    log_info(f"User registered: {username}")


def login_user():
    print_title("\n🔐 Login")
    username = input("👤 Enter username: ").strip()
    password = input("🔑 Enter password: ").strip()

    users = load_users()

    if username not in users:
        print_error("❌ User not found.")
        log_error(f"Login failed: user '{username}' not found.")
        return None

    decrypted_password = decrypt_password(users[username]["password"])
    if decrypted_password != password:
        print_error("❌ Incorrect password.")
        log_error(f"Login failed: incorrect password for user '{username}'")
        return None

    print_success("✅ Login successful!")
    log_info(f"User logged in: {username}")

    return {
        "username": username,
        "skills": users[username]["skills"],
        "role": users[username].get("role", "user"),
    }
