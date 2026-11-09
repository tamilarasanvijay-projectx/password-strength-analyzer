"""
Password Strength Analyzer
A beginner-friendly, local password strength checker.
The password is analyzed in memory and is never saved or transmitted.
"""

import getpass
import re
import sys


def analyze_password(password: str) -> tuple[int, str, list[str]]:
    """Return (score, strength, suggestions) for the supplied password."""
    score = 0
    suggestions = []

    checks = [
        (len(password) >= 8, "Use at least 8 characters."),
        (len(password) >= 12, "Use 12 or more characters for better protection."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter (A-Z)."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter (a-z)."),
        (bool(re.search(r"[0-9]", password)), "Add a number (0-9)."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Add a special character (for example: @, #, or !)."),
    ]

    for passed, suggestion in checks:
        if passed:
            score += 1
        else:
            suggestions.append(suggestion)

    if len(password) >= 16 and score == 6:
        strength = "VERY STRONG"
    elif len(password) >= 12 and score >= 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    # A common or easily guessed password can still be unsafe even if it
    # passes character checks. This simple project does not check breached
    # password databases or estimate real-world cracking time.
    return score, strength, suggestions


def read_password() -> str:
    """Read a password without echoing it when the terminal supports getpass."""
    if sys.stdin.isatty():
        try:
            return getpass.getpass("Enter a password to analyze: ")
        except (EOFError, OSError):
            pass
    return input("Enter a password to analyze: ")


def main() -> None:
    print("=" * 46)
    print("          PASSWORD STRENGTH ANALYZER")
    print("=" * 46)
    print("Your password is analyzed locally and is not stored.")

    password = read_password()
    score, strength, suggestions = analyze_password(password)

    print("\n------------- ANALYSIS RESULT -------------")
    print(f"Password length : {len(password)} characters")
    print(f"Security score  : {score}/6")
    print(f"Strength        : {strength}")

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print(f"  - {item}")
    else:
        print("\nYour password meets all of this project's checks.")

    print("\nNote: This is an educational rule-based checker, not a guarantee")
    print("that a password is secure or resistant to every attack.")


if __name__ == "__main__":
    main()
