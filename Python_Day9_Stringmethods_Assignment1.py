"""1. Write a Python program to Count all letters, digits, and special symbols from the given string

 Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3 """

def count_chars_digits_symbols(input_string):
    chars = digits = symbols = 0

    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return chars, digits, symbols

# Example usage
input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(input_string)

print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

"""Ans: Chars = 8
Digits = 3
Symbols = 4 """
