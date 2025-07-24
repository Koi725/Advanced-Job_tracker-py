# core/admin/delete_user.py

from auth.auth_utils import load_users, save_users
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_warning


def delete_user():
    print_title("\n🗑️ Delete a User")

    users = load_users()
    if not users:
        print_error("No users to delete.")
        return

    print_info("Current Users:")
    for idx, username in enumerate(users, start=1):
        print_info(f"{idx}. {username}")

    username_to_delete = input("\n👤 Enter username to delete: ").strip()

    if username_to_delete not in users:
        print_error("❌ User not found.")
        log_warning(f"Attempted to delete non-existent user: {username_to_delete}")
        return

    if users[username_to_delete].get("role") == "admin":
        print_error("⛔ Cannot delete an admin user!")
        return

    confirm = (
        input(f"⚠️ Are you sure you want to delete '{username_to_delete}'? (yes/no): ")
        .strip()
        .lower()
    )
    if confirm != "yes":
        print_info("Deletion cancelled.")
        return

    del users[username_to_delete]
    save_users(users)

    print_success(f"✅ User '{username_to_delete}' deleted successfully.")
    log_warning(f"Admin deleted user: {username_to_delete}")
