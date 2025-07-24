# utils/crypto.py
import os
from cryptography.fernet import Fernet

RES_KEY_FILE = "data/res_file.key"


def generate_res_key():
    key = Fernet.generate_key()
    with open(RES_KEY_FILE, "wb") as file:
        file.write(key)


def load_res_key():
    if not os.path.exists(RES_KEY_FILE):
        generate_res_key()
    with open(RES_KEY_FILE, "rb") as file:
        return file.read()


def get_res_cipher():
    return Fernet(load_res_key())
