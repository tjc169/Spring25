def main():
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
        "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"
    ]
    modify_list(top_artists)

def modify_list(artists):
    #Try/except block
    try:
        print("Current top artists list:")
        #Number the current artist to make it easier to the select the index
        for i, artist in enumerate(artists):
            print(f"{i}: {artist}")
        
        index = int(input("Enter the index of the artist you want to replace (0-9): "))
        
        # Check if index is in the allowed range
        if index < 0 or index > 9:
            raise ValueError("Index out of range. Must be between 0 and 9.")
        
        new_artist = input("Enter the new artist's name: ")
        artists[index] = new_artist
        
        #Print new list
        print("\nUpdated top artists list:")
        for artist in artists:
            print(artist)
    
    except ValueError as e:
        print(f"An input error occurred: {e}")

main()
