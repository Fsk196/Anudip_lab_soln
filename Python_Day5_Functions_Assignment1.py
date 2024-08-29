#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

def div(a, b):
    # Check if the second number is not zero to avoid division by zero error
    if b != 0:
        result = a / b
        print(f"The division of {a} by {b} is: {result}")
    else:
        print("Division by zero is not allowed.")

# Call the function with two numbers
div(16, 4)  # Example: 16 divided by 4

#Ans: The division of 16 by 4 is: 4.0
