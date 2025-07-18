import json
import os

USER_FILE = "data/users.json"
current_user = None


def init_user_file():
    """Create users.json with a default admin if it doesn't exist."""
    if not os.path.exists(USER_FILE):
        os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
        with open(USER_FILE, "w") as f:
            json.dump(
                {"users": [{"username": "admin", "password": "12345"}]}, f, indent=4
            )


def read_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)


def write_users(data):
    with open(USER_FILE, "w") as f:
        json.dump(data, f, indent=4)


def set_current_user(username):
    global current_user
    current_user = username


def get_current_user():
    return current_user


def login_user():
    username = input("👤 Username: ").strip()
    password = input("🔑 Password: ").strip()

    users = read_users()["users"]
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"✅ Welcome back, {username}!")
            set_current_user(username)
            return True

    print("❌ Invalid credentials.")
    return False


def register_user():
    username = input("👤 Choose a username: ").strip()
    password = input("🔑 Choose a password: ").strip()

    data = read_users()
    if any(u["username"] == username for u in data["users"]):
        print("⚠️ Username already exists. Try a different one.")
        return False

    new_user = {"username": username, "password": password}
    data["users"].append(new_user)
    write_users(data)
    print(f"✅ User '{username}' registered successfully.")
    return True


# Initialize on import
init_user_file()
