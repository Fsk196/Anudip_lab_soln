#5.Write a Python program that determines the largest of three numbers entered by the user.

# Prompt the user to enter three numbers and convert them to floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number among the three
if num1 >= num2 and num1 >= num3:
    # If num1 is greater than or equal to both num2 and num3, num1 is the largest
    largest = num1
elif num2 >= num1 and num2 >= num3:
    # If num2 is greater than or equal to both num1 and num3, num2 is the largest
    largest = num2
else:
    # If neither num1 nor num2 is the largest, then num3 is the largest
    largest = num3

# Print the largest number
print(f"The largest number is {largest}.")

"""Ans: Enter the first number: 16
Enter the second number: 80
Enter the third number: 44
The largest number is 80.0."""
