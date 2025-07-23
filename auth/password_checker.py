# auth/password_checker.py

import re
from utils.styles import print_error


def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        print_error("❌ Password must be at least 8 characters long.")
        return False
    if not re.search(r"[A-Z]", password):
        print_error("❌ Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print_error("❌ Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"\d", password):
        print_error("❌ Password must contain at least one digit.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print_error("❌ Password must contain at least one special character.")
        return False

    return True
