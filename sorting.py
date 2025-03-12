# Create empty list for names
names_list = []


# Prompt user to enter 5 names
for i in range(5):
    name = input("Enter a friend's name: ")
    names_list.append(name)

# Sort Names
swapped = True
while swapped:
    swapped = False
    for i in range(len(names_list) - 1):
        if names_list[i] > names_list[i + 1]:
            names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]

# Print sorted list
print("Sorted list: ", names_list)

# Reverse sorted list
names_list.reverse()
print("\nReversed list:", names_list)  # Reversed
