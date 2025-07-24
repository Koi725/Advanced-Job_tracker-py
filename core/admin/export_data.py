# core/admin/export_data.py

import json
import os
from datetime import datetime
from auth.auth_utils import load_users
from utils.styles import print_title, print_info, print_success, print_error

EXPORT_DIR = "exports"


def export_user_data():
    print_title("\n📦 Exporting User Data...")

    users = load_users()
    if not users:
        print_error("No user data to export.")
        return

    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    filename = f"users_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    print_success(f"✅ User data exported to {filepath}")
