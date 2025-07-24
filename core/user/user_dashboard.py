# core/user_dashboard.py

from utils.styles import print_title, print_info, print_success, print_error
from core.user.edit_profile import edit_profile


def user_dashboard(user_data):
    username = user_data.get("username", "Unknown")

    while True:
        print_title(f"\n👤 Welcome, {username} (User Dashboard)")
        print_info("1. View Profile")
        print_info("2. Edit Profile")
        print_info("3. View Saved Jobs")
        print_info("4. Edit Saved Jobs (Add/Delete)")
        print_info("5. Start Job Search")
        print_info("6. Logout")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_profile(user_data)
        elif choice == "2":
            edit_profile(user_data)
        elif choice == "3":
            view_jobs(user_data)
        elif choice == "4":
            edit_jobs(user_data)
        elif choice == "5":
            start_job_search(user_data)
        elif choice == "6":
            print_success("Logging out...")
            break
        else:
            print_error("Invalid option. Try again.")


# Placeholder functions (to be implemented in Phase 4+)
def view_profile(user_data):
    print_success(f"👤 Username: {user_data['username']}")
    skills = user_data.get("skills", [])
    if skills:
        print_success("🛠️ Skills:")
        for skill in skills:
            print(f"   - {skill}")
    else:
        print_error("No skills found.")


def view_jobs(user_data):
    print_info("📄 [VIEW JOBS] Function to be implemented.")


def edit_jobs(user_data):
    print_info("🛠️ [EDIT JOBS] Function to be implemented.")


def start_job_search(user_data):
    print_info("🔍 [START SEARCH] Function to be implemented.")
