"""2. Write a Python program to remove duplicate characters of a given string.

 Input = “String and String Function” Output: String and Function """

def remove_duplicate_words(input_string):
    words = input_string.split()
    seen = set()
    result = []
    
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return ' '.join(result)

# Example usage
input_string = "String and String Function"
output_string = remove_duplicate_words(input_string)

print(f"Output: {output_string}")

#Ans: Output: String and Function

