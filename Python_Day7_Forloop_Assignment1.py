#1.Python program to check if the given string is a palindrome 

def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    length = len(s)  # Get the length of the string

    # Iterate over the first half of the string
    for i in range(length // 2):
        # Compare characters from the start and end of the string
        if s[i] != s[length - i - 1]:
            return False  # If any characters don't match, it's not a palindrome
    
    return True  # If all characters matched, it's a palindrome

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

"""Ans: Enter a string: Pop
'Pop' is a palindrome.
Enter a string: GAMER
'GAMER' is not a palindrome."""
