# utils/styles.py

from colorama import Style, Fore

# Basic Styles
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
DIM = Style.DIM

# Custom Style Aliases
SUCCESS = Fore.GREEN + BOLD
WARNING = Fore.YELLOW + BOLD
ERROR = Fore.RED + BOLD
INFO = Fore.CYAN + BOLD
NEUTRAL = Fore.WHITE + DIM

# Tag/Label styles
TAG = Fore.MAGENTA + BOLD
LINK = Fore.BLUE + BOLD
HIGHLIGHT = Fore.LIGHTBLUE_EX + BOLD

# Title and Section Headers
TITLE = Fore.LIGHTCYAN_EX + BOLD
SUBTITLE = Fore.CYAN + BOLD
DIVIDER = Fore.WHITE + DIM

# Example usage:
# print(SUCCESS + "✔ Successfully saved!" + RESET)
# print(TITLE + "🔍 Job Analysis Results" + RESET)
