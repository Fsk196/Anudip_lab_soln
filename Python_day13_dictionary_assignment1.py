"""1. Write a Python program and calculate the mean of the below dictionary.

 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

Output: 6.2"""

# Given dictionary
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Calculate the sum of all values
total_sum = sum(test_dict.values())

# Calculate the number of items in the dictionary
num_items = len(test_dict)

# Calculate the mean
mean_value = total_sum / num_items

# Print the result
print("The mean is:", mean_value)

#Ans:The mean is: 6.2
