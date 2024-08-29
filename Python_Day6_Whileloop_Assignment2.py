#2. Write a python program finding the factorial of a given number using a while loop

def find_factorial(number):
    # Initialize variables
    factorial = 1
    current = number
    
    # Use a while loop to calculate the factorial
    while current > 0:
        factorial *= current
        current -= 1
    
    return factorial

# Example usage
number = int(input("Enter a number to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = find_factorial(number)
    print(f"The factorial of {number} is: {result}")

"""Ans: Enter a number to find its factorial: 8
The factorial of 8 is: 40320"""
