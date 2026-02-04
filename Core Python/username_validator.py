"""
Rules:

 -> Length: 5–15
 -> Only letters, digits, underscore
 -> Cannot start with digit
"""
def username_validator(username):
    if len(username) < 5 or len(username) > 15:
        return False
    
    if not username[0].isalpha():
        return False
    
    for ch in username:
        if not(ch.isalnum() or ch == '_'):
            return False
    
    return True

username = input("Enter a username: ")
result  = username_validator(username)
print(result)