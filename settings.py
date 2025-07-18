def search_project():
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


def mark_project_done():
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
