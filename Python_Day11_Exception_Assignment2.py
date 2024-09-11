#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer():
    user_input = input("Please enter an integer: ")
    try:
        # Attempt to convert the input to an integer
        user_input = int(user_input)
        print(f"You entered the integer: {user_input}")
    except ValueError:
        # Raise a ValueError if the input is not a valid integer
        raise ValueError("Invalid input! You must enter a valid integer.")

# Example usage
try:
    get_integer()
except ValueError as e:
    print(e)

"""Ans: Please enter an integer: 24
You entered the integer: 24
Please enter an integer: fai
Invalid input! You must enter a valid integer."""
