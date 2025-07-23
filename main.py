# main.py

from auth import register_user, login_user
from utils.styles import print_title, print_info, print_success, print_error
from core.admin.admin_dashboard import admin_dashboard
from core.user.user_dashboard import user_dashboard


def main_menu():
    print_title("\n📌 Welcome to Job Tracker CLI")
    print_info("1. Register")
    print_info("2. Login")
    print_info("3. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        user_data = login_user()
        if user_data:
            role = user_data.get("role", "user")
            if role == "admin":
                admin_dashboard(user_data)
            else:
                user_dashboard(user_data)
    elif choice == "3":
        print_success("Bye 👋")
        exit()
    else:
        print_error("Invalid option. Try again.")


if __name__ == "__main__":
    while True:
        main_menu()
