# main.py

from auth import register_user, login_user
from dashboard import run_dashboard
from utils.color_utils import print_banner
from dashboard import show_dashboard


def main():
    print_banner()

    while True:
        print("\n🎯 Welcome to Job Tracker!")
        print("1. Log In")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            if login_user():
                run_dashboard()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input. Please try again.")
    if login_user():
        show_dashboard()


if __name__ == "__main__":
    main()
