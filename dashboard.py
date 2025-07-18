from settings import change_password, delete_account
from InquirerPy import inquirer
from auth import get_current_user
from job_track.project_utils import (
    view_all_projects,
    add_project,
    mark_task_done,
    search_projects,
)


def show_dashboard():
    user = get_current_user()
    print(f"\n👋 Welcome, {user}! Choose an option:\n")

    while True:
        choice = inquirer.select(
            message="📋 Main Menu:",
            choices=[
                {"name": "📁 View All Projects", "value": "view_projects"},
                {"name": "➕ Add New Project", "value": "add_project"},
                {"name": "✅ Mark Task as Done", "value": "mark_done"},
                {"name": "🔍 Search Projects", "value": "search"},
                {"name": "⚙️ Settings", "value": "settings"},
                {"name": "🚪 Logout", "value": "logout"},
                {"name": "❌ Exit App", "value": "exit"},
            ],
            default="view_projects",
        ).execute()

        if choice == "view_projects":
            view_all_projects()
        elif choice == "add_project":
            add_project()
        elif choice == "mark_done":
            mark_task_done()
        elif choice == "search":
            search_projects()
        elif choice == "settings":
            settings_choice = inquirer.select(
                message="⚙️ Settings:",
                choices=[
                    {"name": "🔐 Change Password", "value": "change_pass"},
                    {"name": "🗑️ Delete Account", "value": "delete_acc"},
                    {"name": "🔙 Back to Menu", "value": "back"},
                ],
            ).execute()

            if settings_choice == "change_pass":
                change_password()
            elif settings_choice == "delete_acc":
                delete_account()
        elif choice == "logout":
            print("🚪 Logged out.\n")
            break
        elif choice == "exit":
            print("👋 Exiting app.\n")
            exit()
