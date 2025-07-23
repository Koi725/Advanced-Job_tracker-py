# main.py

from auth import register_user, login_user


def main_menu():
    print("\n📌 Welcome to Job Tracker CLI")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Bye 👋")
        exit()
    else:
        print("Invalid option. Try again.")


if __name__ == "__main__":
    while True:
        main_menu()
