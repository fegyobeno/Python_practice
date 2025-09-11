# lambdas list generators
# Description: Lambda functions, map, filter
#exp = lambda arg1 : experession

printing_lambda = lambda x: print(x)

printing_lambda("Hello, World!")  # Output: Hello, World!

#Több bemeneti paraméter
multiple_arguments_lambda = lambda x,y :print(f"{x} {y}")

multiple_arguments_lambda("Hello", "World!")  # Output: Hello World!

# Egy soros if-else
#(if true) if (condition) else (if false)
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(4))  # Output: Even

# Map
# map() egy beépített függvény, amely egy másik függvényt alkalmaz egy adott iterálható objektum minden elemére
# map(function, iterable)
map_example = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # map objektummal tér vissza

print(map_example)  # Output: [1, 4, 9, 16, 25]

# Filter
# filter() egy beépített függvény, amely egy másik függvényt alkalmaz egy adott iterálható objektum minden elemére, és csak azokat tartalmazza, amelyekre az igaz
# filter(function, iterable)

filter_example = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])) # filter objektummal tér vissza

print(filter_example)  # Output: [2, 4]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print([x for x in range(10)])

print([x for x in range(10) if x % 2 == 0])

# Classes

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    @staticmethod
    def print_balance(account):
        print(account.get_balance())
    
#--------------------------------------------------------------
class A:
    def say_hello(self):
        print("Hello from A")

class B():
    def say_hello(self):
        print("Hello from B")

class C(B, A):
    pass

a = A()
b = B()
c = C()
a.say_hello()
b.say_hello()
c.say_hello()

print(C.mro())
print(C.__bases__)
#--------------------------------------------------------------
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def return_speed(self):
        pass

    def __del__(self):
        print("Destructor called") #--> hasznos ha file-t akarunk meghívni

class Auto(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def return_speed(self):
        return 100
#--------------------------------------------------------------

from vehicle import Vehicle
from vehicle import Auto

# Import the Vehicle class from vehicle.py

# Create an instance of the Vehicle class
my_vehicle = Vehicle(make="Toyota", model="Corolla", year=2020)

# Display the vehicle information
print(my_vehicle.return_speed())

# Create an instance of the Auto class
my_auto = Auto(make="Ford", model="Focus", year=2019, doors=4)
print(my_auto.return_speed())