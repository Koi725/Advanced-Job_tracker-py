# core/admin/delete_job.py

import json
import os
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_warning

RES_FILE = "data/res.json"


def delete_job():
    print_title("\n🗑️ Delete a Job from a User")

    if not os.path.exists(RES_FILE):
        print_error("⚠️ No job data found (res.json missing). Nothing to delete.")
        return

    try:
        with open(RES_FILE, "r", encoding="utf-8") as file:
            job_data = json.load(file)
    except Exception:
        print_error("❌ Failed to load job data.")
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

    # Save updated data
    with open(RES_FILE, "w", encoding="utf-8") as file:
        json.dump(job_data, file, indent=4)

    print_success(
        f"✅ Deleted job: {deleted_job.get('title')} at {deleted_job.get('company')}"
    )
    log_warning(f"Admin deleted a job for user: {username}")
