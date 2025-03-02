"""
    input
    """
name = input("Please enter your name: ")
print(f"Hello, {name}. Let's figure out your annual budget and how much you spend on each category. NOTE: WHEN YOU ENTER EACH NUMBER, AVOID USING PUNCTUATION.")
net_income = int(input("Please enter your annual net income: "))
print(
    f"Great. Now let's figure out the percentage that {net_income} you are spending on each category.")

# - INDIVIDUAL CATEGORIES TO INPUT
housing = int(input("How much do you spend annually on rent or mortgage? "))
utilities = int(input("How much do you spend on utilities? "))
groceries = int(input("How much do you spend annually on groceries?  "))
transportation = int(
    input("Great. How much do you spend on transportation?  "))
health_care = int(input("How much do you spend on health care costs?  "))
personal_care = int(
    input("Just a few more to go. How much do you spend on personal care?  "))
clothing = int(
    input("What about clothing? How much do you spend annually on that?  "))
debt = int(input("Finally, how much debt do you have to pay this year?  "))

# - CALCULATE EXTRA MONEY IN BUDGET
leftover = int(net_income - housing - utilities - groceries -
               transportation - health_care - personal_care - clothing - debt)


# - HERE ARE RESULTS
# - CALCULATE # - (category / net_income * 100.2f) to convert to percentages

print(
    "Awesome! Here is the percent of your annual {net income} that you are spending on each category:")
print(f"Housing: {housing / net_income * 100:.2f}%")
print(f"Utilities: {utilities / net_income * 100:.2f}%")
print(f"Groceries: {groceries / net_income * 100:.2f}%")
print(f"Transportation: {transportation / net_income * 100:.2f}%")
print(f"Health Care: {health_care / net_income * 100:.2f}%")
print(f"Personal Care: {personal_care / net_income * 100:.2f}%")
print(f"Clothing: {clothing / net_income * 100:.2f}%")
print(f"Debt: {debt / net_income * 100:.2f}%")

# - Extra budget leftover

print(f"Extra money: ${leftover}")
