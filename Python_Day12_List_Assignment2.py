# 2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

# Function to find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]  # Start with the first element
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Function to find the smallest number in a list
def find_smallest(numbers):
    smallest = numbers[0]  # Start with the first element
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Example list
my_list = [5,24,78,-3,10,-90]

# Find the largest and smallest numbers
largest_number = find_largest(my_list)
smallest_number = find_smallest(my_list)

# Print the results
print("The largest number in the list is:", largest_number)
print("The smallest number in the list is:", smallest_number)

"""Ans:The largest number in the list is: 78
The smallest number in the list is: -90"""
