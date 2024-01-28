def calculate_factorial(number):
    # Handling negative input
    if number < 0:
        return "Factorial is not defined for negative numbers"

    # Factorial of 0 is 1
    if number == 0:
        return 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial

# Test cases
print(calculate_factorial(5))  # Should return 120
print(calculate_factorial(0))  # Should return 1
print(calculate_factorial(3))  # Should return 6
print(calculate_factorial(-1)) # Should handle negative input
