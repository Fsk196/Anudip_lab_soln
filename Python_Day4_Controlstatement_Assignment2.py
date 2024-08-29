"""2.Create a Python program that checks whether a person is eligible to vote
(18 years or older) based on their age."""

# Prompt the user to enter their age and convert the input to an integer
age = int(input("Enter your age: "))

# Check if the person is 18 years old or older
if age >= 18:
    # If the age is 18 or more, print that the person is eligible to vote
    print("You are eligible to vote.")
else:
    # If the age is less than 18, print that the person is not eligible to vote
    print("Sorry, you are not eligible to vote yet.")

"""Ans: Enter your age: 25
You are eligible to vote.
Enter your age: 15
Sorry, you are not eligible to vote yet."""

