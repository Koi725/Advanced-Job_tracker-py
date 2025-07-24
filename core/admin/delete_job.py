# core/admin/delete_job.py

import os
import json
from utils.crypto import get_res_cipher
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_warning

RES_FILE = "data/res.json"


def delete_job():
    print_title("\n🗑️ Delete a Job from a User")

    if not os.path.exists(RES_FILE):
        print_error("⚠️ No job data found (res.json missing). Nothing to delete.")
        return

    try:
        with open(RES_FILE, "rb") as file:
            encrypted = file.read()
            cipher = get_res_cipher()
            decrypted = cipher.decrypt(encrypted).decode("utf-8")
            job_data = json.loads(decrypted)
    except Exception:
        print_error("❌ Failed to load or decrypt job data.")
        return

    if not job_data:
        print_error("No saved jobs found.")
        return

    username = input("👤 Enter the username: ").strip()
    if username not in job_data or not job_data[username]:
        print_error("❌ No jobs found for this user.")
        return

    print_info(f"\nSaved Jobs for {username}:")
    for idx, job in enumerate(job_data[username], start=1):
        title = job.get("title", "Unknown")
        company = job.get("company", "Unknown")
        print_info(f"{idx}. {title} at {company}")

    try:
        choice = int(input("\nEnter job number to delete: ").strip())
        if choice < 1 or choice > len(job_data[username]):
            raise ValueError
    except ValueError:
        print_error("❌ Invalid selection.")
        return

    deleted_job = job_data[username].pop(choice - 1)

    try:
        # Re-encrypt and save updated data
        new_raw = json.dumps(job_data, indent=4)
        new_encrypted = cipher.encrypt(new_raw.encode("utf-8"))
        with open(RES_FILE, "wb") as file:
            file.write(new_encrypted)

        print_success(
            f"✅ Deleted job: {deleted_job.get('title')} at {deleted_job.get('company')}"
        )
        log_warning(f"Admin deleted a job for user: {username}")
    except Exception:
        print_error("❌ Failed to save updated job data.")
