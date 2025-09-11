import sys
#fun
print("Hello, World!", sep=' ', end='\n', file=sys.stdout, flush=False)
#file - ahova ki lesz írva
#flush - ha True akkor azonnal üríti a kimeneti puffert

int(123.45)
123
int('123')
123
int('   -12_345\n')
-12345
int('FACE', 16)
64206
int('0xface', 0)
64206
int('01110011', base=2)
115

bin(3000) #-> '0b101110111000'

#----------------------------------------------------------------------------------------------------

username = input("Enter username:")
print("Username is: " + username)
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favorite_color = input("Enter your favorite color: ")
hobbies = input("Enter your hobbies separated by commas: ").split(',')


print("Age is:", age)
print("Height is:", height)
print("Favorite color is:", favorite_color)
print("Hobbies are:", hobbies)

while True:
    try:
        a = int(input("Enter a positive number: "))
        if a < 0:
            raise ValueError("Please enter a positive number!")
        else:
            break
    except ValueError as e:
        print(e)

#---------------------------------------------------------------------------------------------------------------------------

# For loop example
print("For loop example:")
for i in range(5):
    print(i)

# For loop with array example
print("For loop with array example:")
array = ['apple', 'banana', 'cherry']
for element in array:
    print(element)

# While loop example
print("While loop example:")
count = 0
while count < 5:
    print(count)
    count += 1

# Nested loop example
print("Nested loop example:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop with else example
print("Loop with else example:")
for i in range(3):
    print(i)
else:
    print("Loop completed")

# Break statement example
print("Break statement example:")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue statement example
print("Continue statement example:")
for i in range(5):
    if i == 3:
        continue
    else:
        print(i)

#------------------------------------------------------------ 
# *args and **kwargs
# *args: A függvény bármennyi argumentumot elfogad, és egy tuple-ként kezeli őket.
# **kwargs: A függvény bármennyi kulcs-érték párt elfogad, és egy dictionary-ként kezeli őket.

def function(*args):
    print(args)
    for arg in args:
        print(arg)

function(1, 2, 3, 4, 5)


def function(**kwargs):
    print(kwargs)
    for kwarg in kwargs: 
        print(f"kwarg = {kwarg}, value = {kwargs[kwarg]}")

function(a=1, b=2, c=3, d=4, e=5)

#---------------------------------------------------------------------------------------------------------------------------
# A függvényeket lehet objektumként kezeleni, tehát lehet rájuk hivatkozni, mint egy változóra.
def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
# Output: HELLO\nHELLO

print('-------------------------------------------------------------')

# A függvényeket be lehet adni más függvényeknek paraméterként.
def whisper(text):
    return text.lower()

def temp(func):
    return func('I am in Spain but without the s')

print(temp(shout))
print(temp(whisper))

print('-------------------------------------------------------------')
# Egy függvény visszatérhet egy másik függvénnyel.
# Ennek akkor van értelme, ha dinamikusan kell függvényeket létrehozni, például adószázalék, vagy mértékegységátváltás esetén
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15) # add_15 egy függvény lesz, amely hozzáad 15-öt a bemeneti paraméterhez.
add_20 = create_adder(20) # add_20 egy függvény lesz, amely hozzáad 20-at a bemeneti paraméterhez.

print(add_15(10))  # Output: 25
print(add_20(10))  # Output: 30


print('-------------------------------------------------------------')
# A dekorátoroknak az a feladata, hogy megváltoztassák egy függvény működését.

# Decorators and Special Methods (__str__, __repr__)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# Ekvivalensen viselkedik a következővel, viszont a dekorátorok használata sokkal olvashatóbbá teszi a kódot.:
@my_decorator
def say_hello(a : int = 0, b : str = ''):
    print(a*b)

say_hello(a=4, b='Hello!')
say_hello(8, "whatever\t")
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

print('-------------------------------------------------------------')

import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed {func.__name__} in {end_time - start_time:.4f} seconds") # .4f kerekít 4 tizedesjegyre
        return result
    return wrapper

@log_execution
def compute(x):
    time.sleep(1)
    return x * x

compute(5)
compute(1082828282)

