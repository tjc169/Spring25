# kilograms values
kg_value_1 = 25.4
kg_value_2 = 95.6
kg_value_3 = 182.1
kg_value_4 = 225.3

# Conversion factor: Pounds (lb) = Kilograms (kg) * 2.20462
conversion_factor = 2.20462

# Calculate lbs
lb_1 = kg_value_1 * conversion_factor
lb_2 = kg_value_2 * conversion_factor
lb_3 = kg_value_3 * conversion_factor
lb_4 = kg_value_4 * conversion_factor

# converted results
print(f"{kg_value_1} kilograms is equal to {lb_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_4:.2f} pounds.")
