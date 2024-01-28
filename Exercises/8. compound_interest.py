def compound_interest_calculator(P, r, n, t):
    # Check for edge cases where inputs are not valid
    if P <= 0 or r <= 0 or n <= 0 or t <= 0:
        return "Invalid input. All inputs must be positive numbers."

    # Calculate the compound interest using the formula
    A = P * (1 + r/n)**(n*t)
    
    return A

# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years
print(compound_interest_calculator(-2000,0.05,5,8)) # Expected: Invalid input. All inputs must be positive numbers.
