import re
pattern = r"^\d{3}-\d{3}-\d{4}$"
phone_no="123-456-7890"
match= re.match(pattern,phone_no)
if match:
    print("valid Phone number")
else:
    print("Invalid Phone number")
#Aadar number
pattern1 = r"^\d{4}-\d{4}-\d{4}$"
aadar="1230-4560-7890"
match= re.match(pattern1,aadar)
if match:
    print("✅valid Aadar number")
else:
    print("❌Invalid Aaddar number")
