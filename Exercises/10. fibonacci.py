def fibonacci_sequence(max_value):
    # Handling edge cases for 0 and negative inputs
    if max_value < 0:
        return "Fibonacci sequence is not defined for non-positive values"
    
    if max_value == 0:
        return [0]

    # Initializing the first two values of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Using a while loop to generate the Fibonacci sequence up to max_value
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > max_value:
            break
        fib_sequence.append(next_value)

    return fib_sequence

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
