# BMI Calculator

# Global variable declaration for metric conversions
lbs_to_kgs = 0.453592
inch_to_meters = 0.0254

# Conversions to metric and calculate BMI


def calculate_bmi(weight_lb, height_in):
    # Convert from lbs to kg
    weight = weight_lb * lbs_to_kgs

    # Convert from inches to meters
    height = height_in * inch_to_meters

    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

# To determine BMI category


def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "normal weight"
    elif bmi <= 29.9:
        return "overweight"
    else:
        return "obese"

# Main part of the program


def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI is {bmi:.1f}")
    print(f"You are in the {category} category.")


main()
