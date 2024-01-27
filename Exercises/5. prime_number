import math

def is_prime(number):
    # Check if the number is less than 2, which is not prime
    if number < 2:
        return False
    
    # Check for divisibility up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

# Example Test Cases
print(is_prime(11))  # True, as 11 is a prime number
print(is_prime(4))   # False, as 4 is not a prime number
print(is_prime(2))   # True, as 2 is a prime number
print(is_prime(1))   # False, as 1 is not considered a prime number
