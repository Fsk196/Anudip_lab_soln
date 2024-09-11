#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # Using end='' to avoid double new lines
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Example usage:
read_file_line_by_line("ABC.txt")

"""Ans: Hello, World!
This is a test file.
Python is great!"""
