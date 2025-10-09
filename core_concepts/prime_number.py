def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Only check up to the square root of num
        if num % i == 0:
            return False
    return True

def print_primes_in_range(limit):
    """Print prime numbers from 1 to the given limit."""
    print(f"Prime numbers between 1 and {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")

# Input range limit (for example 15)
limit = int(input("Enter the range limit: "))
print_primes_in_range(limit)


# Certainly! Let's break down the code step by step and explain how it works, specifically focusing on how the prime numbers are calculated and printed:
# Code Breakdown
# 1. The is_prime(num) Function
# This function checks if a number (num) is a prime number.
# def is_prime(num): """Check if a number is prime.""" if num <= 1: return False for i in range(2, int(num ** 0.5) + 1): # Only check up to the square root of num if num % i == 0: return False return True
# if num <= 1::
# A prime number is defined as any integer greater than 1 that has no divisors other than 1 and itself.
# So, if num is less than or equal to 1 (i.e., 0 or negative numbers), the function immediately returns False because they aren't prime numbers.
# for i in range(2, int(num ** 0.5) + 1)::
# To check if a number is prime, we need to check if it is divisible by any number between 2 and num - 1. However, instead of checking up to num - 1, we only need to check up to the square root of num.
# This is because if num = a * b, then one of a or b must be less than or equal to the square root of num. For example, if num = 36, then 6 (the square root of 36) multiplied by 6 gives 36, so we don’t need to check numbers greater than 6 (since they would already be caught by the smaller divisors).
# if num % i == 0::
# This checks if num is divisible by i. The % operator gives the remainder when dividing num by i. If the remainder is 0 (num % i == 0), it means num is divisible by i, and therefore it’s not a prime number. In this case, the function immediately returns False.
# return True:
# If no divisors are found between 2 and the square root of num, it means num is a prime number, and the function returns True.
# 2. The print_primes_in_range(limit) Function
# This function prints all prime numbers from 1 up to a given limit.
# def print_primes_in_range(limit): """Print prime numbers from 1 to the given limit.""" print(f"Prime numbers between 1 and {limit}:") for num in range(2, limit + 1): if is_prime(num): print(num, end=" ")
# print(f"Prime numbers between 1 and {limit}:"):
# This prints a header indicating the range of numbers for which prime numbers will be printed. For example, if limit = 15, it will print:
# Prime numbers between 1 and 15:
# for num in range(2, limit + 1)::
# This starts a loop from 2 (since 1 is not a prime number) to limit (inclusive). The range(2, limit + 1) generates a sequence of numbers from 2 to limit. So, for limit = 15, it will loop over the numbers 2, 3, 4, ..., 15.
# if is_prime(num)::
# For each number (num) in the range, it calls the is_prime(num) function to check if the number is prime.
# If is_prime(num) returns True (meaning the number is prime), then it gets printed.
# print(num, end=" "):
# If the number is prime, it prints the number followed by a space (end=" " ensures the numbers are printed on the same line, separated by a space).
# 3. The Main Program
# Finally, the code takes input from the user for the range limit and calls the print_primes_in_range() function to print the prime numbers up to that limit.
# # Input range limit (for example 15) limit = int(input("Enter the range limit: ")) print_primes_in_range(limit)
# limit = int(input("Enter the range limit: ")):
# This line prompts the user to enter a limit (for example, 15).
# The input is taken as a string and converted to an integer using int().
# print_primes_in_range(limit):
# This calls the function print_primes_in_range(limit) with the user-provided limit.
# The function will then loop over the range of numbers from 2 to limit, checking for prime numbers and printing them.
# How the Values Are Checked and Printed:
# Let's break down how the program works with a range limit of 15:
# The user enters 15 as the limit.
# The program calls print_primes_in_range(15).
# For each number from 2 to 15, the program checks if it is prime:
# Check 2:
# The is_prime(2) function is called. Since 2 is the first prime number, it returns True and is printed.Output: 2
# Check 3:
# The is_prime(3) function is called. It is prime, so it returns True and is printed.Output: 2 3
# Check 4:
# The is_prime(4) function is called. It is divisible by 2, so it returns False. It is not printed.
# Check 5:
# The is_prime(5) function is called. It is prime, so it returns True and is printed.Output: 2 3 5
# Check 6:
# The is_prime(6) function is called. It is divisible by 2 and 3, so it returns False. It is not printed.
# Check 7:
# The is_prime(7) function is called. It is prime, so it returns True and is printed.Output: 2 3 5 7
# Check 8:
# The is_prime(8) function is called. It is divisible by 2, so it returns False. It is not printed.
# Check 9:
# The is_prime(9) function is called. It is divisible by 3, so it returns False. It is not printed.
# Check 10:
# The is_prime(10) function is called. It is divisible by 2 and 5, so it returns False. It is not printed.
# Check 11:
# The is_prime(11) function is called. It is prime, so it returns True and is printed.Output: 2 3 5 7 11
# Check 12:
# The is_prime(12) function is called. It is divisible by 2, so it returns False. It is not printed.
# Check 13:
# The is_prime(13) function is called. It is prime, so it returns True and is printed.Output: 2 3 5 7 11 13
# Check 14:
# The is_prime(14) function is called. It is divisible by 2, so it returns False. It is not printed.
# Check 15:
# The is_prime(15) function is called. It is divisible by 3 and 5, so it returns False. It is not printed.
# The program finishes checking all numbers up to 15 and prints the final list of prime numbers:
# Prime numbers between 1 and 15: 2 3 5 7 11 13
# Summary of the Process:
# The program loops through each number from 2 to the limit.
# For each number, it checks whether it is prime using the is_prime() function.
# If the number is prime, it is printed on the same line, separated by a space.
# The loop continues until all numbers up to the given limit are checked.