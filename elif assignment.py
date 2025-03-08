# Define a function to calculate a student's letter grade

# Get the student's numeric grade
grade = int(input("What is your numberic grade?   "))

# Check if grade is above 100
if grade > 100:
    print("Grade must be 100 or lower.")


# Check if grade is an A (90-100)
elif grade >= 90:
    print("Your letter grade is A.")

# Check if grade is a B (80-89)
elif grade >= 80:
    print("Your letter grade is B.")

# Check if grade is a C (70-79)
elif grade >= 70:
    print("Your letter grade is C.")

# Check if grade is a D (69-60)
elif grade >= 60:
    print("Your letter grade is D.")

# Check if grade is a f (0-59)
elif grade >= 0:
    print("Your letter grade is F.")

# Check if grade is below zero
else:
    print("Grade must be 0 or higher.")
