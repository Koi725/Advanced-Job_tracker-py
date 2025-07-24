# core/admin/view_users.py

from auth.auth_utils import load_users
from utils.styles import print_title, print_info, print_success, print_error


def view_all_users():
    print_title("\n📋 All Registered Users:\n")

    users = load_users()

    if not users:
        print_error("No users found.")
        return

    for username, info in users.items():
        print_success(f"👤 Username: {username}")
        print_info(f"🔐 Role: {info.get('role', 'user')}")
        skills = info.get("skills", [])
        if skills:
            print_info("🛠️ Skills: " + ", ".join(skills))
        else:
            print_error("No skills registered.")
        print("-" * 40)
