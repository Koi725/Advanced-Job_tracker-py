from auth import get_current_user, read_users, write_users


def change_password():
    user = get_current_user()
    data = read_users()
    for u in data["users"]:
        if u["username"] == user:
            new_pass = input("🔐 Enter new password: ").strip()
            u["password"] = new_pass
            write_users(data)
            print("✅ Password changed successfully.")
            return


def delete_account():
    user = get_current_user()
    data = read_users()
    data["users"] = [u for u in data["users"] if u["username"] != user]
    write_users(data)
    print("🗑️ Your account has been deleted.")
