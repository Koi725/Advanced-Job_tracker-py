from utils.file_utils import read_project_data, write_project_data
from auth import get_current_user
from datetime import datetime


def view_all_projects():
    data = read_project_data()
    user = get_current_user()
    projects = [p for p in data["projects"] if p["created_by"] == user]

    if not projects:
        print("📭 You have no projects yet.")
        return

    print("\n📁 Your Projects:\n")
    for proj in projects:
        print(
            f"🆔 {proj['id']} | 📌 {proj['title']} | 📊 {proj['status']} | 🕒 {proj['created_at']}"
        )


def add_project():
    title = input("Enter project title: ").strip()
    description = input("Enter project description: ").strip()
    category = input("Enter category: ").strip()
    created_by = get_current_user()
    created_at = datetime.now().isoformat()

    data = read_project_data()
    existing = data["projects"]

    new_id = max([p["id"] for p in existing], default=0) + 1

    new_project = {
        "id": new_id,
        "title": title,
        "description": description,
        "category": category,
        "status": "In Progress",
        "created_by": created_by,
        "created_at": created_at,
    }

    data["projects"].append(new_project)
    write_project_data(data)

    print(f"✅ Project '{title}' added successfully!")


def mark_task_done():
    try:
        project_id = int(input("Enter project ID to mark as done: ").strip())
    except ValueError:
        print("❌ Invalid ID.")
        return

    data = read_project_data()
    user = get_current_user()

    for proj in data["projects"]:
        if proj["id"] == project_id and proj["created_by"] == user:
            proj["status"] = "Completed"
            write_project_data(data)
            print(f"✅ Project '{proj['title']}' marked as completed!")
            return

    print("❌ Project not found or access denied.")


def search_projects():
    query = input("Enter project title or ID to search: ").strip().lower()
    data = read_project_data()
    user = get_current_user()
    projects = [p for p in data["projects"] if p["created_by"] == user]

    results = [
        p for p in projects if query in p["title"].lower() or query == str(p["id"])
    ]

    if results:
        print("\n🔍 Search Results:\n")
        for proj in results:
            print(
                f"🆔 {proj['id']} | 📌 {proj['title']} | 📊 {proj['status']} | 🕒 {proj['created_at']}"
            )
    else:
        print("❌ No matching project found.")


def delete_project():
    try:
        project_id = int(input("Enter project ID to delete: ").strip())
    except ValueError:
        print("❌ Invalid ID.")
        return

    data = read_project_data()
    user = get_current_user()

    for proj in data["projects"]:
        if proj["id"] == project_id and proj["created_by"] == user:
            data["projects"].remove(proj)
            write_project_data(data)
            print(f"🗑️ Project '{proj['title']}' deleted.")
            return

    print("❌ Project not found or access denied.")
