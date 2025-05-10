import calendar
from datetime import datetime

def main():
    
    
    # Get current year
    current_year = datetime.now().year

    # Prompt user to enter birth month
    user_input = input("Enter the number for your birth month (1-12): ")

    try:
        # Convert input to an integer
        birth_month = int(user_input)

        # Check if the month is in the valid range
        if 1 <= birth_month <= 12:
            # If valid, generate and display the calendar
            cal = calendar.month(current_year, birth_month)
            print(f"\nHere is the calendar for your birth month in {current_year}:\n")
            print(cal)
        else:
            # If the number is out of range
            print("Error: Month must be between 1 and 12.")
            main()

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")

# Call the main function
main()
