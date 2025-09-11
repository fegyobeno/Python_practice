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

