# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

def main():
   
    print("\n\n")
    try:
        today = datetime.today()
        # Prompt user to input birthday
        birth_year = int(input("What year were you born?  "))
        month = int(input("What the number for the month were you born (i.e.: May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
       
        # Display user's birthday
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        # Calculate the time difference between now and the birthday

        delta = today - birthday
        print(f'\nYou are {delta.days} days old')

        # Calculate years
        delta_years = delta.days // 365.25

        # Calculate months
        delta_months = delta.days // 30.41

        # Calculate weeks
        delta_weeks = delta.days // 7

        # Calculate hours
        delta_hours = delta.days * 24

        # Calculate minutes
        delta_minutes = delta.days * 1440

        # Print results
        print(f'You are {delta_years} years old')
        print(f'You are {delta_months} months old')
        print(f'You are {delta_weeks} weeks old')
        print(f'You are {delta_hours} hours old')
        print(f'You are {delta_minutes} minutes old')

      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
 
main()