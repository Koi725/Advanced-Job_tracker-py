from InquirerPy import inquirer
from auth import get_current_user


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
            print("📁 Listing projects...")
            # TODO: call your function
        elif choice == "add_project":
            print("➕ Creating project...")
            # TODO
        elif choice == "mark_done":
            print("✅ Marking task done...")
            # TODO
        elif choice == "search":
            print("🔍 Searching...")
            # TODO
        elif choice == "settings":
            print("⚙️ Settings panel...")
            # TODO
        elif choice == "logout":
            print("🚪 Logged out.")
            break
        elif choice == "exit":
            print("👋 Exiting app.")
            exit()
