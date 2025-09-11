# General lambda function
general_lambda = lambda *args, **kwargs: (args, kwargs)
print(general_lambda(1, 2, 3, a=4, b=5))  # Output: ((1, 2, 3), {'a': 4, 'b': 5})

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Exercise 1: Lambda to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# Exercise 2: Lambda to find the maximum of two numbers
maximum = lambda x, y: x if x > y else y
print(maximum(2, 3))  # Output: 3

# Exercise 3: Lambda to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True

# Exercise 4: Lambda to reverse a string
reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))  # Output: "olleh"

# Exercise 5: Lambda to calculate the square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Exercise 6: Lambda to filter even numbers from a list
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print(filter_even([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]

# Exercise 7: Lambda to convert a list of strings to uppercase
to_uppercase = lambda lst: list(map(lambda s: s.upper(), lst))
print(to_uppercase(["hello", "world"]))  # Output: ["HELLO", "WORLD"]

# Exercise 8: Lambda to sort a list of tuples by the second element
# sorted(iterable, key = kulcsfüggvény ami megadja hogy melyik elemet hasonlítsa össze)
sort_by_second = lambda lst: sorted(lst, key=lambda x: x[1])
print(sort_by_second([(1, 3), (2, 2), (3, 1)]))  # Output: [(3, 1), (2, 2), (1, 3)]

# Exercise 9: Lambda to find the length of each string in a list
lengths = lambda lst: list(map(lambda s: len(s), lst))
print(lengths(["hello", "world"]))  # Output: [5, 5]

# Exercise 10: Lambda to add a constant to each element in a list
add_constant = lambda lst, c: list(map(lambda x: x + c, lst))
print(add_constant([1, 2, 3], 5))  # Output: [6, 7, 8]

# Exercise 11: Lambda to find the intersection of two lists
intersection = lambda lst1, lst2: list(filter(lambda x: x in lst2, lst1))
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

# Exercise 12: Lambda to check if a string only contains digits
is_digit = lambda s: s.isdigit() #or all(map(lambda x: x.isdigit(), s))
print(is_digit("123"))  # Output: True

# Exercise 13: Lambda to remove duplicates from a list
# dict.fromkeys() egy dictionary-t hoz létre a megadott kulcsokból ({key: None, ...})
# a key nem lehet duplicate
remove_duplicates = lambda lst: list(dict.fromkeys(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# Exercise 14: Lambda to find the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Exercise 15: Lambda to check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("racecar"))  # Output: True