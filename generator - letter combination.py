# Prompt user for five letters
def get_five_letters():
    letters = []
    
    # try-except for user input
    while len(letters) < 5:
        try:
            user_input = input("Enter a letter: ")
            if not user_input.isalpha():
                raise ValueError("Input must be alphabetic.")
            if len(user_input) != 1:
                raise ValueError("Please enter only one letter.")
            if user_input in letters: #Note- used ChatGPT to help raise ValueError for redundant letters
                raise ValueError("You already entered that letter. Please enter a different one.")
            letters.append(user_input)
        except ValueError as e:
            print("Error:", e)
    return letters

# Implement the generator function
def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second

# Call the generator function and print each combination
def main():
    print("Please enter five letters.")
    char_list = get_five_letters()

    print("\nHere are the possible two-letter combinations:")
    for combo in two_letter_combinations(char_list):
        print(combo)

# Run program
main()
