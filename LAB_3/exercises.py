# 15. Feladat
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet(name):
    return f"Hello, {name}!"

@count_calls
def add(a, b):
    return a + b

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob"))    # Output: Hello, Bob!
print(greet("Bob"))
print(greet("Bob"))

print(add(3, 4))       # Output: 7

print(list(enumerate({'a': 1, 'b': 2})))

# 16. Feladat
# Írj egy dekorátort, amely méri, hogy egy függvény futása mennyi időt vett igénybe

# 17. Feladat
# Írj egy dekorátort, amely egy függvény hívását valamilyen vizuális keretbe helyezi

# 18. Feladat
# Írj egy dekorátort, amely visszaadja, hogy egy függvény milyen módon és milyen paraméterekkel lett meghívva

# ----------Próbáld ki a 18. feladatban implementált dekorátort--------------------

# Fordíts meg rekurzívan egy stringet
def reverse_string(s):
    pass
    # TODO: implement this function

# Számold ki rekurzívan két tömb metszetét
def intersection(lst1, lst2):
    pass
    # TODO: implement this function

# Irj egy függvényt ami megtalálja az alábbi fa szerű listában a maximum elemet
l_1 = [1, [2, 3, [4, 5]], [6, 7], 8, [9, 10, [11, 12]]]
l_2 = [16 , [2, 3, [14, 5]], [6, 17], 8, [9, 10, [11, 12]]]

def find_max(lst):
    current_max = float('-inf')
    # TODO: implement this function

print(find_max(l_1))
print(find_max(l_2))
