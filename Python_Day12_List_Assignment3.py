#3. Write a Python program to find duplicate values from a list and display those

# Function to find duplicate values in a list
def find_duplicates(numbers):
    duplicates = []  # List to store duplicate values
    seen = []  # List to keep track of seen numbers

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.append(num)

    return duplicates

# Example list
my_list = [2,6,8,9,2,4,5,8,9]

# Find duplicates
duplicate_values = find_duplicates(my_list)

# Print the duplicates
print("Duplicate values in the list are:", duplicate_values)

#Ans:Duplicate values in the list are: [2, 8, 9]

