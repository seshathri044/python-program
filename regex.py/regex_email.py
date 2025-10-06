import re

def check_gmail(email):
    # Regex pattern to match Gmail addresses
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    
    # Match the pattern with the provided email
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
emails = ["example@gmail.com", "test@yahoo.com", "user123@gmail.com", "not_a_gmail@outlook.com"]

for email in emails:
    print(f"{email}: {check_gmail(email)}")
