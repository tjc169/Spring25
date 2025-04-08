def main():
    title_list = []
    count = 0

    # Use WHILE loop to collect book titles
    while count < 10:
        title = input(f"Enter the title of book #{count + 1}: ")
        title_list.append(title.title())  # Capitalizes title and changes it in list
        count += 1

    # Sort list alphabetically
    sorted_list = sorted(title_list)

    # Display sorted list
    print("\nHere is your book list sorted alphabetically:")
    for book in sorted_list:
        print(book)

main()
