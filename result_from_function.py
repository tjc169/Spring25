def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Ask user for input for principal, rate, time
principal = float(input("Enter the principal for the loan: "))
rate = float(input("Enter your interest rate: "))
time = float(input("Enter the duration of the loan in years: "))

# Using the function
interest = calculate_interest(principal, rate, time)

# Print results
print(
    f"\nThe simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
