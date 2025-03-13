
# TRACK HEART RATE BY TIME OF DAY
# CALCULATE AVERAGE HEART RATE

total_heart_rate = 0
average_heart_rate = 0

time_slot = ["Morning", "Midday", "Afternoon", "Evening"]

heart_rate = []

# Collect heart rate input
for time in time_slot:
    rate = int(input(f"Enter your heart rate for {time}: "))
    heart_rate.append([time, rate])
print(heart_rate)


# Calculate total heart rate and display output by time period
for i in range(4):
    time = heart_rate[i][0]
    rate = heart_rate[i][1]
    total_heart_rate += int(rate)
    print(f"\nIn the {time}, your heart rate was {rate}.")

# Calculate average heart rate
average_heart_rate = total_heart_rate / 4
print(f"\nYour average heart rate today was {average_heart_rate:.0f}.")
