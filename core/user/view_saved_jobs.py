# core/user/view_saved_jobs.py

from utils.styles import print_title, print_info, print_error
from utils.logger import log_info
from core.user.job_search_engine import load_res_data


def view_saved_jobs(user_data):
    print_title("\n📁 Your Saved Jobs")
    username = user_data["username"]
    res_data = load_res_data()

    jobs = res_data.get(username, [])
    if not jobs:
        print_error("❌ You have no saved jobs.")
        return

    for idx, job in enumerate(jobs, start=1):
        print_info(f"{idx}. {job['title']} at {job['company']}")
        print_info(f"   🔗 {job['link']}")

    log_info(f"User {username} viewed {len(jobs)} saved jobs.")
