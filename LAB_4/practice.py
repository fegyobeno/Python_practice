#EXCEPTIONS
# 63 beépített kivétel; fa hierarchia

# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError as e:
#         return f"Error: Division by zero is not allowed. {e}"
#     except TypeError as e:
#         return f"Error: Invalid input type. Please provide numbers. {e}"
#     except ValueError as e:
#         return f"Error: Value error occurred. {e}"
#     except KeyboardInterrupt:
#         return "Process interrupted by user."
#     finally:
#         print("Execution completed.")

# #ASSERTIONS
# def dummy_assert_example(x):
#     try:
#         if x >0:
#             return True
#         else:
#             raise AssertionError("x should be greater than 0")
#     except AssertionError as e:
#         return f"Error: Assertion failed. {e}"

# print(dummy_assert_example(-1))

# def assert_example(x):
#     try:
#         assert x > 0, "x should be greater than 0"
#     except AssertionError as e:
#         return f"Error: Assertion failed. {e}"

# print(assert_example(-5))

#GENERATOR + YIELD
# Mi értelme van a generátoroknak?
# Memóriahatékonyak: Nem tárolják az összes elemet egyszerre, hanem igény szerint generálják őket
# Végtelen sorozatok kezelése: Olyan sorozatokat is kezel
# amelyek végtelen hosszúak lehetnek

def simple_generator():
    yield 1
    yield 2
    yield 3

print(simple_generator())  # Output: <generator object simple_generator at ...>
print(next(simple_generator()))  # Output: 1
print(next(simple_generator()))  # Output: 1
#print(next(next(simple_generator())))  # Output: Int object is not an iterator
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

def fibonacci_generator(n = float('inf')):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

gen_fib = fibonacci_generator()
for _ in range(10):
    print(next(gen_fib))  # Output: 0 1 1 2 3 5 8 13 21 34

# whenever I need the next number
print(next(gen_fib))


#LAMBDAS
# printing_lambda = lambda x: print(x)

# printing_lambda("Hello, World!")  # Output: Hello, World!

# #Több bemeneti paraméter
# multiple_arguments_lambda = lambda x,y :print(f"{x} {y}")

# multiple_arguments_lambda("Hello", "World!")  # Output: Hello World!

# # Egy soros if-else
# #(if true) if (condition) else (if false)
# check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(check_even(4))  # Output: Even

# # Map
# # map() egy beépített függvény, amely egy másik függvényt alkalmaz egy adott iterálható objektum minden elemére
# # map(function, iterable)
# map_example = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # map objektummal tér vissza

# print(map_example)  # Output: [1, 4, 9, 16, 25]

# # Filter
# # filter() egy beépített függvény, amely egy másik függvényt alkalmaz egy adott iterálható objektum minden elemére, és csak azokat tartalmazza, amelyekre az igaz
# # filter(function, iterable)

# filter_example = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])) # filter objektummal tér vissza

# print(filter_example)  # Output: [2, 4]

# a = lambda *args: sum(args)