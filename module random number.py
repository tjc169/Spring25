# Import random module
import random

# Define the function


def main():
    actual_number = random.randint(1, 100)

# Set guess to "None" to stop the loop if guess is between 1 and 100
    guess = None
    while not guess == actual_number:
        try:
            guess = int(input("Pick a number between 1 and 100: "))

        # Error if guess is not an integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            guess = None

        if guess is not None:
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            else:
                difference = abs(guess - actual_number)

                if difference > 25:
                    print("Cold")
                elif difference > 15:
                    print("Cool")
                elif difference > 5:
                    print("Hot")
                elif difference > 0:
                    print("Very Hot")
                else:
                    print(
                        f"\nCongratulations! You guessed the correct number. It was {actual_number}.")


main()
