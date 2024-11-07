import re

def check_password_strength(password):
    #check length of a password
    if len(password) < 12:
        return "weak: password must be at least 8 characters long"
    
    
    #check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "weak: password must contain at least 1 uppercase letter"
    #check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "weak: password must contain at least 1 lowercase letter"
    
    #check for an integer
    if not re.search(r'[1-9]', password):
        return "weak: password must contain at least 1 number"
    
    #check for special character
    if not re.search(r'[?!@%$*#]', password):
        return "weak: password must contain at least 1 special character"
    
    return "strong: password is strong"

while True:
    password = input("enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
    if result == "strong: your password is strong":
        break







