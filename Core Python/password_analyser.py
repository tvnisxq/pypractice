from getpass import getpass
def check_password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_upper = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
    
    if has_upper and has_digit:
        return "Strong"
    else:
        return "Weak"
    
user_password = getpass("Enter a password: ") # Getpass is used to hide passwords
result = check_password_strength(user_password)

print("Password is", result)