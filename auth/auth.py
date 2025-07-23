from auth.auth_utils import load_users, save_users, encrypt_password, decrypt_password
from auth.password_checker import is_password_strong


def register_user():
    print("\n📋 Register New User")

    username = input("👤 Enter username: ").strip()
    users = load_users()

    if username in users:
        print("❌ Username already exists.")
        return

    password = input("🔑 Enter password: ").strip()

    if not is_password_strong(password):
        print("❌ Weak password. Try again.")
        return

    encrypted_password = encrypt_password(password)
    skill_tags = input("🛠️ Enter your skills (comma-separated): ").strip()

    users[username] = {
        "password": encrypted_password,
        "skills": [tag.strip() for tag in skill_tags.split(",") if tag.strip()],
    }

    save_users(users)
    print("✅ Registration successful!")


def login_user():
    print("\n🔐 Login")

    username = input("👤 Enter username: ").strip()
    password = input("🔑 Enter password: ").strip()

    users = load_users()

    if username not in users:
        print("❌ User not found.")
        return None

    decrypted_password = decrypt_password(users[username]["password"])
    if decrypted_password != password:
        print("❌ Incorrect password.")
        return None

    print("✅ Login successful!")
    return {"username": username, "skills": users[username]["skills"]}
