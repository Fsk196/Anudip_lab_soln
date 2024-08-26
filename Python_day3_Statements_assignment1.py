#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Taking input from the user
number = int(input("Enter a number: "))

# Using a ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number {number} is {result}.")

"""Ans: Enter a number: 24
The number 24 is Even.
Enter a number: 75
The number 75 is Odd."""
