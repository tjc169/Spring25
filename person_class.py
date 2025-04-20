# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(person, name, address, age, phone_number):
        person.__name = name  # Private variable for name
        person.__address = address   # Private variable for address
        person.__age = age    # Private variable for age
        person.__phone_number = phone_number # Private variable for phone number

    # Method to get person's info as a formatted string
    def get_info(person):
        return f"{person.__name}, Address: {person.__address}, Age: {person.__age}, Phone Number: {person.__phone_number}"

    # Getter for name
    def get_name(person):
        return person.__name

    # Getter for address
    def get_address(person):
        return person.__address

    # Getter for age
    def get_age(person):
        return person.__age

    # Getter for phone number
    def get_phone_number(person):
        return person.__phone_number

    # Setter for name
    def set_name(person, name):
        person.__name = name

    # Setter for address
    def set_address(person, address):
        person.__address = address

    # Setter for age
    def set_age(person, age):
        person.__age = age

    # Setter for phone number
    def set_phone_number(person, phone_number):
        person.__phone_number = phone_number

person1 = Person("Tom Cooper", "123 Drury Lane", "45", "312-222-6062")
person2 = Person("Jenny Smith", "45 Penny Lane", "37", "773-867-5309")
person3 = Person("John Doe", "35 Johnson Blvd", "28", "123-456-7890")

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())