import re

def check_password(password):
    # Regex pattern for password validation
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;'\"<>,.?/\\|-]).{6,}$"
    
    # Match the pattern with the provided password
    if re.match(pattern, password):
        return True
    else:
        return False

# Test cases
passwords = ["Password123!", "password", "12345678", "Password", "P@ssw0r", "Strong@Pass123"]

for password in passwords:
    print(f"'{password}': {check_password(password)}")
