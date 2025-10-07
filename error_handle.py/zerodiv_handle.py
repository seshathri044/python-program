a=int(input("Enter the numarator:"))
b=int(input("enter the divisor:"))
try:
    result =a/b
except ZeroDivisionError:
    print("Error cannot divide by zero")
else:
    print("The result:",result)  
finally:
    print("Thank you!!") 