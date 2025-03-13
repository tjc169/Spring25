# OPERATIONS ON LIST ASSIGNMENT

# Initialize seat list with numbers 1 to 20
seats = list(range(1, 21))
print("The following seats are available: ", seats)

while seats != "done":

    # User inputs seat number:
    seat_number = int(
        input("Please select your seat or press 0 to end your search: "))

# Ends loop:
    if seat_number == 0:
        print("\nThank you for using our booking system!")
        break

# If number not in list:
    if seat_number not in seats:
        print(f"\nSeat", seat_number,
              "invalid or already booked seat. Please choose another.")

# If seat still available
    if seat_number in seats:
        seats.remove(seat_number)
        print(f"\nSeat {seat_number} successfully booked!")
        print("The following seats are still available: ", seats)

# When list is empty:
    if len(seats) == 0:
        print("\nEvent sold out!")
        seats = "done"
