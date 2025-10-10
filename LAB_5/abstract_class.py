# an abstract class / interface
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @staticmethod
    def static_method(self, param):
        print(self.make)
        print(param)

    @abstractmethod
    def return_speed(self):
        pass

    def __del__(self):
        print("Destructor called") #--> hasznos ha file-t akarunk meghívni, networking etc

    def __eq__(self, value):
        return (self.make == value.make and 
                self.model == value.model and 
                self.year == value.year)
    def __lt__(self, value):
        return self.year < value.year
    def __le__(self, value):
        return self.year <= value.year
    def __gt__(self, value):
        return self.year > value.year
    def __ge__(self, value):
        return self.year >= value.year
    def __ne__(self, value):
        return not self.__eq__(value)
    def __hash__(self):
        return hash((self.make, self.model, self.year))
    def __instancecheck__(self, instance):
        return isinstance(instance, Vehicle)
    def __str__(self):
        return super().__str__() + f" {self.make} {self.model} {self.year}"
    
#a = Vehicle("Toyota", "Corolla", 2020) #TypeError: Can't instantiate abstract class Vehicle with abstract method return_speed
class Auto(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def return_speed(self):
        return 100
    
a = Auto("Toyota", "Corolla", 2020, 4)
print(str(a))
print(a == a)
print(a.__hash__())
print(a >= Auto("Toyota", "Corolla", 2019, 4))
print(isinstance(a, Vehicle))
Vehicle.static_method(a, "Hello")
print(a.make)