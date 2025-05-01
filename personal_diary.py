def main():

    # Writing user input to a file
    date = input("Enter today's date: ")
    time = input("Enter the current time: ")
    entry = input("Please write your diary entry: ")


    # Open or create the file in append mode
    with open('diary.txt', 'a') as file:  # 'a' mode appends content to the file
        # Add newline for better formatting
        file.write(date + ', ' + time + ': ' + entry + '\n ########### \n')


main()

def read_diary():
    try:
        # Open the file in read mode
        file = open('diary.txt', 'r')
        content = file.read()
        print("\nDiary Contents:\n")
        print(content)
        file.close() #ALWAYS close the file
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
# Run this function to see what's in diary.txt
read_diary()