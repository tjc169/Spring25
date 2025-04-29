

# Define custom exception
class NotNumericError(Exception):
    def __init__(self, message="Input must be a numeric value."):
        self.message = message
        super().__init__(self.message)

def get_numeric_input():
    try:
        user_input = input("Enter a number: ")
        if not user_input.isnumeric():
            raise NotNumericError()
    except NotNumericError as e:
        print(f"Error: {e.message}")
        get_numeric_input()  # call again if input is not numeric
    else:
        print(f"Thank you! You entered the number: {user_input}")
    finally:
        print("Execution of input check completed.\n") 
def main():
    get_numeric_input()


# Run main function
main()
