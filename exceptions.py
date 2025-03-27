# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
    except ValueError:
        print("ERROR! Incorrect value.")
    else:
        print(f"The square of {number} is {squared_number}.")


square_number()
