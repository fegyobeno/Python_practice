# Exercise 1
# Print all numbers from 1 to 10
def print_numbers():
    for i in range(1, 11):
        print(i)

# Exercise 2
# Print all even numbers from 1 to 20
def print_even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

# Exercise 3
# Print the multiplication table of 5
def multiplication_table_5():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

# Exercise 4
# Calculate the sum of all numbers from 1 to 100
def sum_of_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    return total

# Exercise 5
# Print the first 10 Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        print(a)
        a, b = b, a + b

# Exercise 6
# Print all prime numbers between 1 and 50
def print_primes():
    for num in range(2, 51):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

# Exercise 7
# Print the factorial of a number n
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Exercise 8
# Print the first n odd numbers
def print_odd_numbers(n):
    count = 0
    num = 1
    while count < n:
        if num % 2 != 0:
            print(num)
            count += 1
        num += 1

# Exercise 9
# Reverse a given number
def reverse_number(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

print(reverse_number(1234))  # 4321)

# Exercise 10
# Print the sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total

# Exercise 11
# Print the first n terms of the sequence 1, 4, 9, 16, ...
def print_square_sequence(n):
    for i in range(1, n + 1):
        print(i * i)

# Exercise 12
# Print the first n terms of the sequence 1, 2, 4, 8, 16, ...
def print_power_of_two_sequence(n):
    for i in range(n):
        print(2 ** i)

# Exercise 13
# Print the first n terms of the sequence 1, 3, 6, 10, 15, ...
def print_triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(total)

# Exercise 14
# Print the elements of an array
def print_array_elements(arr):
    for element in arr:
        print(element)

# Exercise 15
# Find the maximum element in an array
def find_max_element(arr):
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

# Exercise 16
# Reverse an array without using the arr[::-1] syntax
def reverse_array(arr):
    return arr[::-1]

# Exercise 17
# Calculate the sum of elements in an array without using the sum() function
def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total

# Exercise 18
# Find the average of elements in an array without using the avg() function
def average_of_array(arr):
    total = sum_of_array(arr)
    return total / len(arr)

# Exercise 19
# Flatten a 2D array
def flatten_2d_array(arr):
    return [element for sublist in arr for element in sublist]

# Exercise 20
# Create a list of squares of elements in an array
def squares_of_elements(arr):
    return [x * x for x in arr]

# Exercise 21
# Filter out even numbers from an array
def filter_even_numbers(arr):
    return [x for x in arr if x % 2 != 0]

# Exercise 22
# Create a list of tuples (number, square) for each element in an array
def number_square_tuples(arr):
    return [(x, x * x) for x in arr]

# Exercise 23
# Create a list of elements greater than a given value
def elements_greater_than(arr, value):
    return [x for x in arr if x > value]

# Exercise 24
# Create a list of strings with their lengths
def strings_with_lengths(arr):
    return [(s, len(s)) for s in arr]

# Exercise 25
# Create a list of elements that are present in both arrays
def common_elements(arr1, arr2):
    return [x for x in arr1 if x in arr2]

# Exercise 26
# Create a list of elements that are unique to the first array
def unique_to_first_array(arr1, arr2):
    return [x for x in arr1 if x not in arr2]

# Exercise 27
# Create a list of elements that are unique to both arrays
def unique_to_both_arrays(arr1, arr2):
    return [x for x in arr1 + arr2 if (x in arr1 and x not in arr2) or (x in arr2 and x not in arr1)]

# Exercise 28
# Create a list of elements that are divisible by a given number
def elements_divisible_by(arr, divisor):
    return [x for x in arr if x % divisor == 0]

