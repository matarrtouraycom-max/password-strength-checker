COMMON_PASSWORDS = [
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "letmein",
    "welcome"
]


def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak", ["Avoid using common passwords."]

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters. 12 or more is better.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>/?"
    if any(char in special_characters for char in password):
        score += 1
    else:
        suggestions.append("Add special characters like !, @, #, or $.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 30)

    password = input("Enter a password to check: ")

    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nGreat job. This password meets strong password guidelines.")

    print("\nSecurity Tip:")
    print("Use unique passwords for every account and consider using a password manager.")


if __name__ == "__main__":
    main()
