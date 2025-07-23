# utils/color_utils.py


class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def success(msg):
    return f"{Colors.GREEN}[✔] {msg}{Colors.END}"


def error(msg):
    return f"{Colors.FAIL}[✖] {msg}{Colors.END}"


def warning(msg):
    return f"{Colors.WARNING}[!] {msg}{Colors.END}"


def info(msg):
    return f"{Colors.BLUE}[-] {msg}{Colors.END}"


def title(msg):
    return f"{Colors.HEADER}{Colors.BOLD}{msg}{Colors.END}"
