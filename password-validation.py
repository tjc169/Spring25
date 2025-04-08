def main():
    try:
        # User inputs password
        password = input("\nPlease enter your password: ")

        # Check if the password is between 8 and 20 characters long
        if len(password) < 8:
            print("\nPassword is too short. It must be at least 8 characters.")
        elif len(password) > 20:
            print("\nPassword is too long. It must 20 characters or less.")
        else:
            # Global variables to start
            has_number = False
            has_symbol = False
            has_upper = False
            has_lower = False
            symbol = "!@#$%&*"

            # Check each character in the password
            for char in password:
                if char.isdigit():
                    has_number = True
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
                if char in symbol:
                    has_symbol = True

            # Print responses if password is missing a requirement
            if not has_upper:
                print("\nPassword must have at least one uppercase letter.")
            if not has_lower:
                print("\nPassword must have at least one lowercase letter.")
            if not has_number:
                print("\nPassword must have at least one number.")
            if not has_symbol:
                print("\nPassword must have at least one of these symbols: !@#$%&*.")
            
            else:
                # Ask to re-enter password
                confirm_password = input("\nRe-enter your password to confirm: ")

                # Check if passwords match
                if password == confirm_password:
                    print("\nPasswords are good!")
                else:
                    print("\nPassword does not match.")

    except:
        print(f"An error occurred")

# Call the main function
main()
