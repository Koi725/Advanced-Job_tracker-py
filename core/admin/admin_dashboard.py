# core/admin/admin_dashboard.py

from utils.styles import print_title, print_info, print_success, print_error
from core.admin.view_users import view_all_users
from core.admin.view_jobs import view_all_jobs
from core.admin.delete_user import delete_user
from core.admin.delete_job import delete_job
from core.admin.export_data import export_user_data


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
            view_all_users()
        elif choice == "2":
            view_all_jobs()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            export_user_data()
        elif choice == "6":
            print_success("Logged out successfully.")
            break
        else:
            print_error("Invalid option. Try again.")
