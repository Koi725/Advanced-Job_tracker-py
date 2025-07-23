# auth/auth_utils.py

import json
from cryptography.fernet import Fernet
import os

# مسیر فایل کاربران و کلید رمزنگاری
USER_FILE = "data/users.json"
KEY_FILE = "data/user_file.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def get_cipher():
    return Fernet(load_key())


def load_users():
    cipher = get_cipher()

    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted = cipher.decrypt(encrypted_data).decode("utf-8")
            return json.loads(decrypted)
        except Exception:
            return {}


def save_users(users: dict):
    cipher = get_cipher()
    raw_data = json.dumps(users, indent=4)
    encrypted_data = cipher.encrypt(raw_data.encode("utf-8"))

    with open(USER_FILE, "wb") as file:
        file.write(encrypted_data)


def encrypt_password(password: str) -> str:
    cipher = get_cipher()
    return cipher.encrypt(password.encode("utf-8")).decode("utf-8")


def decrypt_password(encrypted: str) -> str:
    cipher = get_cipher()
    return cipher.decrypt(encrypted.encode("utf-8")).decode("utf-8")
