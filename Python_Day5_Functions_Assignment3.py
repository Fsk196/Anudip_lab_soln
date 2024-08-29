#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate 5 random numbers between a range, for example 1 to 100
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the list of random numbers
print(f"Random numbers: {random_numbers}")

# Find the maximum and minimum numbers using max() and min()
max_number = max(random_numbers)
min_number = min(random_numbers)

print(f"Maximum number: {max_number}")
print(f"Minimum number: {min_number}")

"""Ans: Random numbers: [72, 68, 22, 30, 57]
Maximum number: 72
Minimum number: 22"""
