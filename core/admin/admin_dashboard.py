# core/admin/admin_dashboard.py

from utils.styles import print_title, print_info, print_success, print_error


def admin_dashboard(user_data):  # ✅ ورودی اضافه شد
    while True:
        print_title("\n🛠️ Admin Dashboard")
        print_info("1. View All Users")
        print_info("2. View All Jobs")
        print_info("3. Delete a User")
        print_info("4. Delete a Job")
        print_info("5. Export Data")
        print_info("6. Logout")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print_success("[ADMIN] View All Users - Coming soon")
        elif choice == "2":
            print_success("[ADMIN] View All Jobs - Coming soon")
        elif choice == "3":
            print_success("[ADMIN] Delete a User - Coming soon")
        elif choice == "4":
            print_success("[ADMIN] Delete a Job - Coming soon")
        elif choice == "5":
            print_success("[ADMIN] Export Data - Coming soon")
        elif choice == "6":
            print_success("Logged out successfully.")
            break
        else:
            print_error("Invalid option. Try again.")
