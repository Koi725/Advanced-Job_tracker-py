# core/user/edit_profile.py

from auth.auth_utils import load_users, save_users, encrypt_password
from auth.password_checker import is_password_strong
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_info, log_warning


def edit_profile(user_data):
    print_title("\n✏️ Edit Your Profile")
    username = user_data["username"]
    users = load_users()

    if username not in users:
        print_error("❌ User not found.")
        return

    print_info("1. Change Password")
    print_info("2. Update Skills")
    print_info("3. Cancel")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        new_password = input("🔑 Enter new password: ").strip()
        if not is_password_strong(new_password):
            print_error("❌ Password too weak. Try again.")
            log_warning(f"Weak password change attempt by {username}")
            return

        users[username]["password"] = encrypt_password(new_password)
        print_success("✅ Password updated.")
        log_info(f"User {username} updated their password.")

    elif choice == "2":
        new_skills = input("🛠️ Enter new skills (comma-separated): ").strip()
        skills_list = [s.strip() for s in new_skills.split(",") if s.strip()]
        users[username]["skills"] = skills_list
        print_success("✅ Skills updated.")
        log_info(f"User {username} updated their skills.")

    elif choice == "3":
        print_info("Cancelled.")
        return

    else:
        print_error("❌ Invalid option.")
        return

    save_users(users)
    user_data.update(users[username])
