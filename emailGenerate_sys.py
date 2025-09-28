import sys

if len(sys.argv) == 2:
    print("Usage :Python email_generate.py 'Full name and last name' ")
    sys.exit()




full_name = sys.argv[1]  # if do not want to the sys.argv[argument] manually use//  full_name = " ".join(sys.argv[1:]) 
Last_name = sys.argv[2]

#Format the name
email = full_name.lower().replace(" ",".") + Last_name + "@comapany.com"

#output
print("\n---Your Profile ---")
print("Full Name:",full_name + Last_name)
print("Generated Email:",email)
