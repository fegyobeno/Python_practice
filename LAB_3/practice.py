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

a = 0b1010
print(a)  # Output: 10
print(~a)
print(a & 0b1100)  # Output: 8 # Bitwise AND
print(a | 0b1100)  # Output: 14
print(a ^ 0b1100)  # Output: 6  # Bitwise XOR
print(a << 2)      # Output: 40 # Bitwise left shift
print(a >> 2)      # Output: 2  # Bitwise right shift

#----------------------------------------------------------------------------------------------------

def test_function(a = 3, b=2, c=3):
    print(a, b, c)

test_function(1)          # a=1, b=2, c=3
test_function(1, 10)     # a=1, b=10, c
test_function(1, 10, 20) # a=1, b=10, c=20
test_function(a=1, b=30) # a=1, b=2,

'''
def test(a = 2, b): --> Error because non-default argument follows default argument
    print(a, b)
'''

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

# list
l = []
for i in range(100):
    l.append(create_adder(i))

print(l[10](5))  # Output: 15
print(l[50](5))  # Output: 55


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