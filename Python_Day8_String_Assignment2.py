"""2. Write a Python program to remove a newline in Python

 String = "\nBest \nDeeptech \nPython \nTraining\n" """

# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines
cleaned_string = string.replace('\n', ' ').strip()

# Print the cleaned string
print(cleaned_string)


#Ans:Best  Deeptech  Python  Training
