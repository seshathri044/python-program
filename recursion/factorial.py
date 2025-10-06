n = int(input("Enter the Number:"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)  # Call the function and store the result
print("The factorial:", result)
