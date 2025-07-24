# core/user/edit_saved_jobs.py

from utils.styles import print_title, print_info, print_error, print_success
from utils.logger import log_info
from core.user.job_search_engine import load_res_data, save_res_data


def edit_saved_jobs(user_data):
    print_title("\n🛠️ Edit Your Saved Jobs")
    username = user_data["username"]
    res_data = load_res_data()
    jobs = res_data.get(username, [])

    if not jobs:
        print_error("❌ No saved jobs to edit.")
        return

    for idx, job in enumerate(jobs, start=1):
        print_info(f"{idx}. {job['title']} at {job['company']}")

    print_info("\n1. Delete a Job")
    print_info("2. Cancel")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        to_delete = input("Enter job number to delete: ").strip()
        try:
            index = int(to_delete) - 1
            if 0 <= index < len(jobs):
                deleted_job = jobs.pop(index)
                res_data[username] = jobs
                save_res_data(res_data)
                print_success(
                    f"✅ Deleted: {deleted_job['title']} at {deleted_job['company']}"
                )
                log_info(f"User {username} deleted a saved job.")
            else:
                print_error("❌ Invalid job number.")
        except ValueError:
            print_error("❌ Invalid input.")
    else:
        print_info("Cancelled.")
