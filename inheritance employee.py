
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    #Getter and Setter
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

# ProductionWorker class is super class of Employee
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate


def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")

    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Hourly Pay Rate: "))
    shift = int(input("Enter Shift Number (1 for Day, 2 for Night): ")) 

    
    # Create the ProductionWorker object
    worker = ProductionWorker(name, number, shift, pay_rate)

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())

    # Show Day or Night shift
    if worker.get_shift_number() == 1:
        print("Shift: Day")
    elif worker.get_shift_number() == 2:
        print("Shift: Night")
    else:
        print("Shift: Unknown")

    print("Pay Rate: ${:.2f}".format(worker.get_hourly_pay_rate()), "per hour")


main()
