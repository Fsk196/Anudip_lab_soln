#2. Python program to check if a given number is an Armstrong number

def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    num_digits = len(num_str)  # Number of digits in the number
    
    # Initialize a variable to store the sum of the powered digits
    sum_of_powers = 0
    
    # Iterate over each digit in the string representation of the number
    for digit in num_str:
        # Convert the digit back to an integer
        digit = int(digit)
        # Raise the digit to the power of the number of digits and add to sum_of_powers
        sum_of_powers += digit ** num_digits
    
    # Check if the calculated sum_of_powers is equal to the original number
    return sum_of_powers == number

# Test the function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

"""Ans: Enter a number: 407
407 is an Armstrong number.
Enter a number: 408
408 is not an Armstrong number."""
