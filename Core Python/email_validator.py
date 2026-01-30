"""
Task: Write a function that checks if an email is valid based on these rules:

Must contain exactly one '@' symbol
Must contain at least one '.' after the '@'
Must be at least 5 characters long
Cannot start or end with '@' or '.'
"""
# Example: "user@example.com" -> Valid
# Example: "invalid.email" -> Invalid (no @)

def email_validator(email):
    if len(email) < 5:
        return False
    elif email.count('@') != 1:
        return False
    
    elif email[0] == '@' or email[0] == '.':
        return False
    elif email[-1] == '@' or email[-1] == '.':
        return False
    
    else:
        index = email.index('@')
        substring = email[index+1:]

        if '.' in substring:
            return True
        else:
            return False
            
email = input("enter an email: ")
result = email_validator(email)
print(result)