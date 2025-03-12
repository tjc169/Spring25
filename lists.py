# List for days of the week
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

# Empty List for steps
steps = []

total_steps = 0

# Loop for user input
for day in days:
    step_count = int(input(f"How many steps did you take on {day}? "))
    steps.append(step_count)
    total_steps += step_count


# Calculate average steps
average_steps = total_steps / len(steps)

# Results
print(f"\nTotal steps: {total_steps}")
print(f"Average steps: {average_steps:.2f}")
