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
