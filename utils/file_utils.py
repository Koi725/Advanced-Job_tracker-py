# utils/file_utils.py

import os
import json
from cryptography.fernet import Fernet

KEY_FILE = "data/user_file.key"


# ────────────────────────────────────────────────
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)


def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()


def get_cipher():
    key = load_key()
    return Fernet(key)


# ────────────────────────────────────────────────
def read_encrypted_json(file_path):
    if not os.path.exists(file_path):
        return {}

    cipher = get_cipher()
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
        return json.loads(decrypted_data)
    except Exception:
        return {}


def write_encrypted_json(file_path, data):
    cipher = get_cipher()
    json_str = json.dumps(data, indent=4)
    encrypted_data = cipher.encrypt(json_str.encode("utf-8"))
    with open(file_path, "wb") as f:
        f.write(encrypted_data)


# ────────────────────────────────────────────────
def read_encrypted_text(file_path):
    if not os.path.exists(file_path):
        return ""

    cipher = get_cipher()
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        return cipher.decrypt(encrypted_data).decode("utf-8")
    except Exception:
        return ""


def write_encrypted_text(file_path, text):
    cipher = get_cipher()
    encrypted_data = cipher.encrypt(text.encode("utf-8"))
    with open(file_path, "wb") as f:
        f.write(encrypted_data)
