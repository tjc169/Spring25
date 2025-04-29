class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    # Getters
    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # Setters
    def set_kind(self, kind):
        self.kind = kind

    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name

    # Print pet details
    def print_details(self):
        print(f"\nPet Details: \nKind: {self.kind} \nBreed: {self.breed} \nName: {self.name}")
        print("\n############")


# Creating instances of Pet class
pet1 = Pet("Dog", "Chihuahua", "Roo")
pet2 = Pet("Cat", "Tabby", "Sparks")
pet3 = Pet("Bird", "Parakeet", "Rocco")

# Calling print_details for each Pet
pet1.print_details()
pet2.print_details()
pet3.print_details()

# *** Special Methods Demonstration ***

# Display name of the class
print("\nClass name of Pet:")
print(Pet.__name__)  # Output: Pet

# Using getattr() to access an attribute
print("\nAccessing pet3's name using getattr:")
print(getattr(pet3, 'name'))  # Output: Rocco

# 3. isinstance(): Checking if pet3 is an instance of Pet
print("\nIs pet2 an instance of Pet?")
print(isinstance(pet2, Pet))  # Output: True


