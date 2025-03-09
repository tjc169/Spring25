# LOGICAL OPERATIONS

a = int(input("Enter your first integer:  "))
b = int(input("Enter your second integer: "))

# AND OPERATOR
# BOTH NUMBERS LESS THAN 100
if a < 100 and b < 100:
    print("Both numbers less than 100: True")
else:
    print("Both numbers less than 100: False")

# Both numbers even:

if a % 2 == 0 and b % 2 == 0:
    print("Both numbers are even: True")
else:
    print("Both numbers are even: False")


# OR operator
# Multiples of 5

if a % 5 == 0 or b % 5 == 0:
    print("Either number a multiple of 5? True")
else:
    print("Either number a multiple of 5? False")

# a not equal to b
if a == b:
    print("Intergers are the same number? True")
else:
    print("Integers are the same number? False")


# NOT operator
# B not greater than A
if not b > a:
    print(b, "is not greater than", a)
else:
    print(b, "is greater than", a)

# A not less than 0
if not a < 0:
    print(a, "is not less than 0")
else:
    print(a, "is less than 0")
