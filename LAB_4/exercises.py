# Exceptions

# 1. Irj egy függvényt ami felhasználói bemenetet kér, majd számmá alakítja és és elosztja vele az 1-et. (1 / input)
# Kezeld le az összes lehetséges hibát, és írj megfelelő hibaüzenetet.

# 2. Irj egy végtelen ciklust, ami addig iterál amíg a felhasználó ctrl+c-vel meg nem szakítja. 
# Ebben az esetben kezeld le a KeyboardInterrupt kivételt és írj egy üzenetet, hogy a program leállt.

# Assertions
# 3. Irj egy egyszerű unit tesztelőt a következő függvényekhez, divide_by_two és abrakadabra.

def divide_by_two(x):
    return x / 2

def abrakadabra(n):
    if n < 0 and n % 2 == 0 and n < 10:
        return "Abrakadabra"
    else:
        return True

i = int(input("Enter a number: "))

def unit_test():
    try:
        number_of_tests = 1
        counter = 0
        # TODO: add more tests
        assert 1 == 1, "1 should be equal to 1"
        counter += 1

    except AssertionError as e:
        print(f"Test failed: {e}")
    finally:
        print(f"Number of tests passed: {counter}/{number_of_tests}")

unit_test()

# ----------------------------------------------------  Generators + Yield + Lambdas ----------------------------------------------------
# 1. Feladat: Lambda két szám szorzására
multiply = None #TODO
#print(multiply(2, 3))  # Kimenet: 6

# 2. Feladat: Lambda két szám maximumának megtalálására
maximum = None #TODO
#print(maximum(2, 3))  # Kimenet: 3

# 3. Feladat: Lambda egy szám páros voltának ellenőrzésére
is_even = None #TODO
#print(is_even(4))  # Kimenet: True

# 4. Feladat: Lambda egy string megfordítására
reverse_string = None #TODO
#print(reverse_string("hello"))  # Kimenet: "olleh"

# 5. Feladat: Lambda egy szám négyzetének kiszámítására
square = None #TODO
#print(square(4))  # Kimenet: 16

# 6. Feladat: Lambda páros számok szűrésére egy listából
filter_even = None #TODO
#print(filter_even([1, 2, 3, 4, 5, 6]))  # Kimenet: [2, 4, 6]

# 7. Feladat: Lambda stringek listájának nagybetűssé alakítására
to_uppercase = None #TODO
#print(to_uppercase(["hello", "world"]))  # Kimenet: ["HELLO", "WORLD"]

# 8. Feladat: Lambda tuple-ök listájának rendezésére a második elem alapján
sort_by_second = None #TODO
#print(sort_by_second([(1, 3), (2, 2), (3, 1)]))  # Kimenet: [(3, 1), (2, 2), (1, 3)]

# 9. Feladat: Lambda stringek hosszának megtalálására egy listában
lengths = None #TODO
#print(lengths(["hello", "world"]))  # Kimenet: [5, 5]

# 10. Feladat: Lambda egy konstans hozzáadására minden elemhez egy listában
add_constant = None #TODO
#print(add_constant([1, 2, 3], 5))  # Kimenet: [6, 7, 8]

# 11. Feladat: Lambda két lista metszetének megtalálására
intersection = None #TODO
#print(intersection([1, 2, 3], [2, 3, 4]))  # Kimenet: [2, 3]

# 12. Feladat: Lambda annak ellenőrzésére, hogy egy string csak számjegyeket tartalmaz-e
is_digit = None #TODO
#print(is_digit("123"))  # Kimenet: True

# 13. Feladat: Lambda duplikátumok eltávolítására egy listából
remove_duplicates = None #TODO
#print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Kimenet: [1, 2, 3, 4, 5]

# 14. Feladat: Lambda egy szám faktoriálisának kiszámítására
factorial = None #TODO
#print(factorial(5))  # Kimenet: 120

# 15. Feladat: Lambda annak ellenőrzésére, hogy egy string palindróm-e
is_palindrome = None #TODO
#print(is_palindrome("racecar"))  # Kimenet: True
