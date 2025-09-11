from abc import ABC, abstractmethod

"""
# abc is the abstract base class module
# ABC is the base class for defining abstract classes

A metaosztály egy olyan osztály, amely más osztályokat hoz létre vagy módosít. 
A Pythonban a type a beépített metaosztály, amelyet az osztályok létrehozására használnak.

Az absztrakt osztály, egy olyan osztály amivel nem lehet objektumot létrehozni, csak leszármazott osztályokat.

"""

# Polymorphism, Abstract Classes, and Interfaces
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
#miért eszik meg minden metdust aminek van speak metódusa?
#mert az Animal osztály absztrakt osztály, és a Dog és Cat osztályok implementálják a speak metódust

def animal_sound(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

print('-------------------------------------------------------------')

# Multiple Inheritance and MRO (Method Resolution Order)
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

d = D()
d.method()  # Output: B method
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# method resolution order
# int.mro() 
# bool.mro()

print('-------------------------------------------------------------')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(str(p))  # Output: Person(name=Alice, age=30)
print(repr(p))  # Output: Person('Alice', 30)

print('-------------------------------------------------------------')

# Design Patterns - Singleton
# Csak egy példányt hoz létre az osztályból ami globálisan elérhető
# _instance változóval tároljuk az osztály példányát, az első inicializálás előtt ez None
# A __new__ metódus egy új példányt hoz létre az osztályból 
# <<-->> __init__ metódus inicializálja a példányt (beállítja az attribútumokat egy frissen létrehozott osztály példányra)
# Egy osztály hívásánál __new__ metódus hívódik meg először, majd az __init__ metódus

# cls az osztály referenciája, azaz az osztály maga
# *args és **kwargs a paraméterek és kulcsszavak amiket átadunk az osztálynak, bárhány paramétert átadhatunk az osztálynak

# if not cls._instance: ellenőrzi, hogy az osztály példány már létezik-e, ha nem akkor létrehozza

# Az _instance egyenő lesz a Singleton.super().__new__(cls, *args, **kwargs) értékével, azaz a Singleton osztály példányával
# A singleton.Supper() az az object. Singleton.mro()

# return visszatér a példánnyal

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True

print('-------------------------------------------------------------')

class Configuration(Singleton):
    def __init__(self, settings):
        if not hasattr(self, 'initialized'):  # Ensure __init__ runs only once
            self.initialized = True
        else:
            print("Already initialized")

    def __str__(self):
        return type(self.settings)

    def get_settings(self):
        return self.settings

config1 = Configuration()
config2 = Configuration()

config1.settings = {"OS": "windows", "version": "11.7.06.9"}

print(config1.settings)
print(config2.settings)


print(config1 is config2)  # Output: True