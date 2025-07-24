# import requests
# import json
# import os
# import datetime
# from auth.auth_utils import get_cipher
# from utils.styles import print_title, print_info, print_success, print_error
# from utils.logger import log_info

# RES_FILE = "data/res.json"
# RES_KEY_FILE = "data/res_file.key"


# def generate_res_key():
#     from cryptography.fernet import Fernet

#     key = Fernet.generate_key()
#     with open(RES_KEY_FILE, "wb") as file:
#         file.write(key)


# def load_res_key():
#     if not os.path.exists(RES_KEY_FILE):
#         generate_res_key()
#     with open(RES_KEY_FILE, "rb") as file:
#         return file.read()


# def get_res_cipher():
#     from cryptography.fernet import Fernet

#     return Fernet(load_res_key())


# def load_res_data():
#     cipher = get_res_cipher()
#     if not os.path.exists(RES_FILE):
#         return {}
#     with open(RES_FILE, "rb") as file:
#         encrypted = file.read()
#         try:
#             decrypted = cipher.decrypt(encrypted).decode("utf-8")
#             return json.loads(decrypted)
#         except Exception:
#             return {}


# def save_res_data(data: dict):
#     cipher = get_res_cipher()
#     raw = json.dumps(data, indent=4)
#     encrypted = cipher.encrypt(raw.encode("utf-8"))
#     with open(RES_FILE, "wb") as file:
#         file.write(encrypted)


# def choose_job_board():
#     print_title("\n🌐 Choose Job Board to Search From:")
#     boards = {
#         "1": "Arbeitnow",
#         "2": "RemoteOK",
#         "3": "Cancel",
#     }

#     for key, value in boards.items():
#         print_info(f"{key}. {value}")

#     choice = input("\nChoose an option: ").strip()

#     if choice == "1":
#         return "arbeitnow"
#     elif choice == "2":
#         return "remoteok"
#     else:
#         print_info("Search cancelled.")
#         return None


# def fetch_jobs_arbeitnow(skills):
#     print_info("🔍 Searching Arbeitnow...")
#     url = "https://www.arbeitnow.com/api/job-board-api"
#     all_results = []

#     try:
#         response = requests.get(url, timeout=10)
#         data = response.json().get("data", [])

#         for job in data:
#             for skill in skills:
#                 if skill.lower() in job.get("title", "").lower():
#                     job_info = {
#                         "title": job.get("title"),
#                         "company": job.get("company_name", "N/A"),
#                         "link": job.get("url"),
#                     }
#                     all_results.append(job_info)

#         return all_results[:50]  # Limit to 50 jobs
#     except Exception:
#         print_error("Failed to fetch jobs from Arbeitnow.")
#         return []


# def fetch_jobs_remoteok(skills):
#     print_info("🔍 Searching RemoteOK...")
#     url = "https://remoteok.com/api"
#     all_results = []

#     try:
#         response = requests.get(url, timeout=10)
#         data = response.json()[1:]  # Skip the first metadata item

#         for job in data:
#             for skill in skills:
#                 if skill.lower() in job.get("position", "").lower():
#                     job_info = {
#                         "title": job.get("position"),
#                         "company": job.get("company", "N/A"),
#                         "link": job.get("url"),
#                     }
#                     all_results.append(job_info)

#         return all_results[:50]
#     except Exception:
#         print_error("Failed to fetch jobs from RemoteOK.")
#         return []


# def write_txt_log(jobs, username):
#     today = datetime.date.today().strftime("%Y-%m-%d")
#     filename = f"{username}_jobs_{today}.txt"
#     with open(filename, "w", encoding="utf-8") as file:
#         for job in jobs:
#             file.write(f"{job['title']} at {job['company']}\n{job['link']}\n\n")
#     log_info(f"Saved {len(jobs)} jobs to {filename}.")


# def display_and_store_results(jobs, username):
#     if not jobs:
#         print_error("❌ No jobs found.")
#         return

#     print_title("\n📄 Search Results:\n")
#     for idx, job in enumerate(jobs, start=1):
#         print_info(f"{idx}. {job['title']} at {job['company']}")
#         print_info(f"   🔗 {job['link']}")

#     selections = input(
#         "\nEnter job numbers to save (comma-separated), or enter 0 to save all: "
#     ).strip()

#     selected_jobs = []
#     if selections == "0":
#         selected_jobs = jobs
#     else:
#         indexes = []
#         for part in selections.split(","):
#             try:
#                 num = int(part.strip())
#                 if 1 <= num <= len(jobs):
#                     indexes.append(num - 1)
#             except ValueError:
#                 continue
#         selected_jobs = [jobs[i] for i in indexes]

#     if not selected_jobs:
#         print_error("❌ No valid selections made.")
#         return

#     # Save to JSON
#     res_data = load_res_data()
#     if username not in res_data:
#         res_data[username] = []
#     res_data[username].extend(selected_jobs)
#     save_res_data(res_data)

#     # Save to TXT
#     write_txt_log(selected_jobs, username)

#     print_success(f"✅ {len(selected_jobs)} jobs saved successfully.")
#     log_info(f"User {username} saved {len(selected_jobs)} jobs from search.")


# def search_jobs(user_data):
#     print_title("\n🔎 Start Job Search")
#     username = user_data["username"]
#     skills = user_data.get("skills", [])

#     if not skills:
#         print_error("⚠️ You have no skills set in your profile.")
#         return

#     print_info(f"Your Skills: {', '.join(skills)}")

#     board = choose_job_board()
#     if not board:
#         return

#     if board == "arbeitnow":
#         jobs = fetch_jobs_arbeitnow(skills)
#     elif board == "remoteok":
#         jobs = fetch_jobs_remoteok(skills)
#     else:
#         jobs = []

#     display_and_store_results(jobs, username)
# No Crypto.py needed version(1)
#######################################################################################################################
import requests
import json
import os
import datetime
from auth.auth_utils import get_cipher
from utils.styles import print_title, print_info, print_success, print_error
from utils.logger import log_info
from utils.crypto import get_res_cipher

RES_FILE = "data/res.json"


def load_res_data():
    cipher = get_res_cipher()
    if not os.path.exists(RES_FILE):
        return {}
    with open(RES_FILE, "rb") as file:
        encrypted = file.read()
        try:
            decrypted = cipher.decrypt(encrypted).decode("utf-8")
            return json.loads(decrypted)
        except Exception:
            return {}


def save_res_data(data: dict):
    cipher = get_res_cipher()
    raw = json.dumps(data, indent=4)
    encrypted = cipher.encrypt(raw.encode("utf-8"))
    with open(RES_FILE, "wb") as file:
        file.write(encrypted)


def choose_job_board():
    print_title("\n🌐 Choose Job Board to Search From:")
    boards = {
        "1": "Arbeitnow",
        "2": "RemoteOK",
        "3": "Cancel",
    }

    for key, value in boards.items():
        print_info(f"{key}. {value}")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        return "arbeitnow"
    elif choice == "2":
        return "remoteok"
    else:
        print_info("Search cancelled.")
        return None


def fetch_jobs_arbeitnow(skills):
    print_info("🔍 Searching Arbeitnow...")
    url = "https://www.arbeitnow.com/api/job-board-api"
    all_results = []

    try:
        response = requests.get(url, timeout=10)
        data = response.json().get("data", [])

        for job in data:
            for skill in skills:
                if skill.lower() in job.get("title", "").lower():
                    job_info = {
                        "title": job.get("title"),
                        "company": job.get("company_name", "N/A"),
                        "link": job.get("url"),
                    }
                    all_results.append(job_info)

        return all_results[:50]  # Limit to 50 jobs
    except Exception:
        print_error("Failed to fetch jobs from Arbeitnow.")
        return []


def fetch_jobs_remoteok(skills):
    print_info("🔍 Searching RemoteOK...")
    url = "https://remoteok.com/api"
    all_results = []

    try:
        response = requests.get(url, timeout=10)
        data = response.json()[1:]  # Skip the first metadata item

        for job in data:
            for skill in skills:
                if skill.lower() in job.get("position", "").lower():
                    job_info = {
                        "title": job.get("position"),
                        "company": job.get("company", "N/A"),
                        "link": job.get("url"),
                    }
                    all_results.append(job_info)

        return all_results[:50]
    except Exception:
        print_error("Failed to fetch jobs from RemoteOK.")
        return []


def write_txt_log(jobs, username):
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"{username}_jobs_{today}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for job in jobs:
            file.write(f"{job['title']} at {job['company']}\n{job['link']}\n\n")
    log_info(f"Saved {len(jobs)} jobs to {filename}.")


def display_and_store_results(jobs, username):
    if not jobs:
        print_error("❌ No jobs found.")
        return

    print_title("\n📄 Search Results:\n")
    for idx, job in enumerate(jobs, start=1):
        print_info(f"{idx}. {job['title']} at {job['company']}")
        print_info(f"   🔗 {job['link']}")

    selections = input(
        "\nEnter job numbers to save (comma-separated), or enter 0 to save all: "
    ).strip()

    selected_jobs = []
    if selections == "0":
        selected_jobs = jobs
    else:
        indexes = []
        for part in selections.split(","):
            try:
                num = int(part.strip())
                if 1 <= num <= len(jobs):
                    indexes.append(num - 1)
            except ValueError:
                continue
        selected_jobs = [jobs[i] for i in indexes]

    if not selected_jobs:
        print_error("❌ No valid selections made.")
        return

    # Save to JSON
    res_data = load_res_data()
    if username not in res_data:
        res_data[username] = []
    res_data[username].extend(selected_jobs)
    save_res_data(res_data)

    # Save to TXT
    write_txt_log(selected_jobs, username)

    print_success(f"✅ {len(selected_jobs)} jobs saved successfully.")
    log_info(f"User {username} saved {len(selected_jobs)} jobs from search.")


def search_jobs(user_data):
    print_title("\n🔎 Start Job Search")
    username = user_data["username"]
    skills = user_data.get("skills", [])

    if not skills:
        print_error("⚠️ You have no skills set in your profile.")
        return

    print_info(f"Your Skills: {', '.join(skills)}")

    board = choose_job_board()
    if not board:
        return

    if board == "arbeitnow":
        jobs = fetch_jobs_arbeitnow(skills)
    elif board == "remoteok":
        jobs = fetch_jobs_remoteok(skills)
    else:
        jobs = []

    display_and_store_results(jobs, username)
