#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"Result: {result}"

# Example usage
num1 = 20
num2 = 0

print(divide(num1, num2))

#Ans: Error: Cannot divide by zero.
