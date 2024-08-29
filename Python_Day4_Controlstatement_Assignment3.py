#3.Write a Python program that determines if a given year is a leap year or not.

# Prompt the user to enter a year and convert the input to an integer
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If the year is divisible by 4 but not by 100, or divisible by 400, it's a leap year
    print(f"{year} is a leap year.")
else:
    # If the year does not meet the leap year criteria, it's not a leap year
    print(f"{year} is not a leap year.")

"""Ans: Enter a year: 2024
2024 is a leap year.
Enter a year: 2021
2021 is not a leap year."""
