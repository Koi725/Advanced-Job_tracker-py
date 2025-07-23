# scripts/create_unique_admin.py

# from auth.auth_utils import load_users, save_users, encrypt_password
from auth_utils import *
import os


def create_unique_admin():
    users = load_users()
    admin_username = "Admin"
    admin_password = "Admin123@123"

    if admin_username in users:
        print("⚠️ Admin already exists. Nothing changed.")
        return

    encrypted_password = encrypt_password(admin_password)
    users[admin_username] = {
        "password": encrypted_password,
        "skills": ["admin"],
        "role": "admin",
    }

    save_users(users)
    print("✅ Admin user created successfully.")


if __name__ == "__main__":
    create_unique_admin()
