def main():
    print("Welcome to your super-duper, handy-dandy calculator.")
    
    try:
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter your 2nd number: "))
        operation = input("Do you want to add, subtract, multiply or divide the numbers? ")


        if operation == "add":
            answer = number_1 + number_2
        elif operation == "subtract":
            answer = number_1 - number_2
        elif operation == "multiply":
            answer = number_1 * number_2
        elif operation == "divide":
            answer = number_1 / number_2
        else:
            print("Unknown operation. Please choose add, subtract, multiply, or divide.")
            return

        print(f"The answer is: {answer}")

    except ZeroDivisionError:
        print("Oops! Can't divide by zero. Try a different number.")
    except ValueError:
        print("That's not a number! Please enter a valid number.")

main()
