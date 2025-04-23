# Class definition
class Pet:
    # Class variable
    vet_name = "Fox Valley Animal Hospital"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and setter
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Method to print pet and owner info
    def display_pet_info(self):
        print(f"\nOwner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Vet Office: {Pet.vet_name}")
        print("\n***********************\n") # to separate info


# Property existence check with mangled name
def check_property(self, property_name):
    mangled_name = f"_{self.__class__.__name__}__{property_name}"
    exists = hasattr(self, mangled_name)
    print(f"Does '{property_name}' exist in {self.__class__.__name__}? {exists}")
    return exists


# Main function 
def main():
    # Creating Pet objects
    pet1 = Pet("Tom", "Cooper", "000756", "Roo")
    pet2 = Pet("Jane", "Smith", "000452", "Lava", "Cat")
    pet3 = Pet("Sierra", "Thompson", "000670", "Snowflake", "Guinea Pig")

    # Use setter methods to update pet3's name and type
    pet3.set_pet_name("Sparkles")
    pet3.set_pet_type("Fish")

    # Display pet info
    print("\n--- Pet Info ---")
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    # Check properties
    print("\n--- Property Checks ---")
    check_property(pet1, "pet_name")
    check_property(pet2, "owner_last_name")
    check_property(pet3, "age") 

# Calling the main function
main()
