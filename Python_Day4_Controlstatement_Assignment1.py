"""1.Write a Python program that takes a number as input and prints "Even" if
the number is even and "Odd" if it's odd."""

# Prompt the user to enter a number and convert the input to an integer
number = int(input("Enter a number: "))

# Check if the number is divisible by 2 (i.e., if the remainder when divided by 2 is 0)
if number % 2 == 0:
    # If the number is divisible by 2, it's even, so print "Even"
    print("Even")
else:
    # If the number is not divisible by 2, it's odd, so print "Odd"
    print("Odd")

"""Ans:Enter a number: 32
Even
Enter a number: 7
Odd"""
