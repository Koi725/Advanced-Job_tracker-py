# core/admin/view_jobs.py

import os
import json
from utils.crypto import get_res_cipher
from utils.styles import print_title, print_info, print_success, print_error

RES_FILE = "data/res.json"


def view_all_jobs():
    print_title("\n📄 All Saved Jobs from All Users:\n")

    if not os.path.exists(RES_FILE):
        print_error("❌ No job data file found.")
        return

    try:
        with open(RES_FILE, "rb") as file:
            encrypted = file.read()
            cipher = get_res_cipher()
            decrypted = cipher.decrypt(encrypted).decode("utf-8")
            job_data = json.loads(decrypted)
    except Exception as e:
        print_error("❌ Failed to read or decrypt job data.")
        return

    if not job_data:
        print_error("❌ No jobs found.")
        return

    for username, jobs in job_data.items():
        print_success(f"\n👤 User: {username}")
        if not jobs:
            print_error("   ❌ No jobs saved.")
            continue
        for idx, job in enumerate(jobs, start=1):
            print_info(
                f"   {idx}. 🧑‍💻 {job.get('title', 'No Title')} at {job.get('company', 'Unknown')}"
            )
            print_info(f"       🔗 {job.get('link', '-')}")
