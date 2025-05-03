def main():
    try:
        # Open the file and process each line
        with open('sales_totals.txt', 'r') as file:

        # Set count and total sales to 0
            total = 0.00
            count = 0

            print("Sales Totals:")
            print("-------------")

            for line in file:
                line = line.strip()
                if line:  
                    try:
                        # Converts line to a float
                        amount = float(line)
                        total += amount
                        count += 1
                        # Format and print the individual sale amount
                        print(f"${amount:,.2f}")
                    except ValueError:
                        print(f"Warning: Invalid number found: {line}")

            if count > 0:
                average = total / count
                # Format and display total, count, and average
                print("\nSummary:")
                print(f"Total Sales: ${total:,}")
                print(f"Number of Entries: {count}")
                print(f"Average Sale: ${average:,.2f}")
            else:
                print("No valid sales data found.")

    except IOError:
        print("An IOError has occurred.")

# Call the main function
main()
