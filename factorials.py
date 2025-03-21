# Calculating Factorials

# Define the function
def factorial(n):
    if n <= 1:  # If user inputs 0 or 1
        return 1
    else:   # For all other inputs
        return n * factorial(n-1)

# Prompt user and run code


def main():
    n = int(input("Enter a non-negative integer: "))
    factorial_answer = factorial(n)
    print(f"The total of {n} factorial is {factorial_answer}")


main()
