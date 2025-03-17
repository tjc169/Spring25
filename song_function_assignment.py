def custom_song(name, adjective, adjective2, adjective3, location, feeling, actionverb, noun, bodypart):
    print("\n\n")
    print("To the tune of The Beatles' Hey Jude:")
    print(f"\nHey {name}, don't make it {adjective},")
    print(f"Take a {adjective2} song and make it {adjective3}.")
    print(f"Remember to let her into your {location},")
    print(f"Then you can start to make it {adjective3}.")
    print()
    print(f"Hey {name}, don't be {feeling}.")
    print(f"You were made to {actionverb} and get {noun}.")
    print(f"The minute you let her under your {bodypart},")
    print(f"Then you begin to make it {adjective3}.")
    print(f"\nNA NA NA \nNANANANAAAAA \nNANANANAAAAA \n\nHEY {name}...")


input_name = input("Enter a name: ")
input_adjective = input("Enter an adjective: ")
input_adjective2 = input("Enter another adjective: ")
input_adjective3 = input("Enter yet another adjective: ")
input_location = input("Enter a location: ")
input_feeling = input("Enter feeling or emotion: ")
input_actionverb = input("Enter an action verb: ")
input_noun = input("Enter a noun: ")
input_bodypart = input("Enter a body part: ")


custom_song(name=input_name, adjective=input_adjective, adjective2=input_adjective2, adjective3=input_adjective3, location=input_location, feeling=input_feeling, actionverb=input_actionverb,
            noun=input_noun, bodypart=input_bodypart)
