#4.Create a Python program that checks if a user-given number is positive, negative, or zero.

# Prompt the user to enter a number and convert the input to a float
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    # If the number is greater than 0, it is positive
    print("The number is positive.")
elif number < 0:
    # If the number is less than 0, it is negative
    print("The number is negative.")
else:
    # If the number is neither greater nor less than 0, it must be zero
    print("The number is zero.")

"""Ans: Enter a number: 8
The number is positive.
Enter a number: -2
The number is negative.
Enter a number: 0
The number is zero."""
