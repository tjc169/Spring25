def main():
    # Example string
    example_string = "Hello, Python programmers!"

# TODO: Iterate through the string and print each character
print("Iterating through the string:")
string = 'Iterating through the string'
for character in string:
        print(character, end=' ')


# TODO: Find and print the character with the minimum ASCII value in the string
print("\nCharacter with the minimum ASCII value:")
text = "Character with the minimum ASCII value"
print('[' + min(text) + ']') #Answer is blank because it could spaces as characters. Brackets show that answer is blank

# TODO: Find and print the character with the maximum ASCII value in the string
print("\nCharacter with the maximum ASCII value:")
text = "Character with the maximum ASCII value"
print(max(text))


# TODO: Find and print the index of the first occurrence of 'o' in the string
print("\nIndex of 'o':")
text = "Index of o"
print(text.index("o"))

# TODO: Convert the string into a list of characters and print the list
print("\nConverting string to a list of characters:")

string = "Converting string to a list of characters"
list_of_char = list(string)
print(list_of_char)

# TODO: Count and print the number of occurrences of 'o' in the string
print("\nCount of 'o' in the string:")
string = "Count of o in the string"
print(string.count("o"))

main()
