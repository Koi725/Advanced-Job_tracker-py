# 🛡️ Job Application Tracker (CLI-Based, Encrypted)

A full-featured command-line job tracking system built in Python. Secure, modular, and role-based — made for developers, freelancers, and recruiters to manage job applications and searches efficiently and safely.

---

## 🚀 Features

### ✅ User Functionalities

- 🔐 **Login/Register System** with Username/Password
- 📝 **Edit Profile** (Username & Skills)
- 📄 **View Saved Jobs** (Encrypted per user)
- 🗑️ **Edit Saved Jobs** (Add/Delete securely)
- 🔍 **Search for Jobs** by Skills from:
  - **RemoteOK**
  - **Arbeitnow**
- 💾 **Save Jobs** to Encrypted JSON (`res.json`) + TXT Log (`{user}_jobs_DATE.txt`)

### 🛠️ Admin Functionalities

- 👁️ **View All Saved Jobs** for All Users
- ❌ **Delete Specific Job** from Any User
- 📜 **Role-Based Access** to User/Admin Dashboards

### 🔒 Security

- ✅ **End-to-End Encryption** using `cryptography.Fernet`
- 🔑 Auto-generated key saved to `data/res_file.key`
- 🔏 User job data stored in encrypted `res.json`

---

## 🗂️ Project Structure

Job Tracker/
├── core/
│ ├── user/
│ │ ├── user_dashboard.py
│ │ ├── edit_profile.py
│ │ ├── view_saved_jobs.py
│ │ ├── edit_saved_jobs.py
│ │ └── job_search_engine.py
│ └── admin/
│ ├── view_jobs.py
│ └── delete_job.py
├── auth/
│ └── auth_utils.py
├── utils/
│ ├── styles.py
│ ├── logger.py
│ └── crypto.py
├── data/
│ ├── users.json
│ ├── res.json 🔒 (Encrypted)
│ └── res_file.key 🔑
├── main.py
└── README.md

---

## ⚙️ How to Run

```bash
# Step 1: Install dependencies
pip install cryptography requests

# Step 2: Run the main file
python3 main.py
```

Technologies Used

    Python 3.10+

    cryptography → For AES-level encryption

    requests → Fetching live job listings

    Role-Based OOP Architecture

    Modular CLI interface

✍️ Author

Made by Kousha, a passionate full-stack & security-focused developer.

✅ Final Notes

    All user data is encrypted — your job search remains private.

    The tool can be extended to support:

        📬 Email notifications

        🌐 More job APIs (e.g., LinkedIn, Indeed)

        🌍 Web dashboard version

    If you liked this tool, feel free to ⭐ the repo and contribute!
