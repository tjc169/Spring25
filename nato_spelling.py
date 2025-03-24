# Define NATO phonetic alphabet using upper case and lower case letter
nato_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey',
    'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'

}


def main():
    word = input("Enter a word: ").upper()
# .upper to convert lower case letter to upper case to match the alphabet
# source: https://www.w3schools.com/python/ref_string_upper.asp
    nato_phonetic = [nato_alphabet.get(letter, letter) for letter in word]
    print("\n".join(nato_phonetic))


main()
