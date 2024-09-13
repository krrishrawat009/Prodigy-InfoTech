
def check_password_complexity(password: str) -> str:
    # Criteria
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = set("!@#$%^&*()-_+=")

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character (!@#$%^&*()-_+=)."

    return "Password is complex enough."

# Example usage
password = input("Enter a password to check its complexity: ")
result = check_password_complexity(password)
print(result)
