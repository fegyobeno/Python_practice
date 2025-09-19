#Írj egy függvényt ami egy számot vár paraméterül és visszaadja a szám négyzetét!
def square_number(a):
    #TODO: implement this function
    pass

#Írj egy függvényt ami két számot vár paraméterül és kiírja a nagyobbat!
def compare_numbers(a, b):
    #TODO: implement this functionq
    pass
    
#Írj egy függvényt ami egy számot vár paraméterül és visszaadja a szám abszolút értékét!(abs() kulcszó)
def absolute_value(a):
    #TODO: implement this function
    pass

#Írj egy függvényt ami egy stringet vár paraméterül és megadja a string hosszát! (len() kulcszó)
def string_length(s):
    #TODO: implement this function
    pass

#Írj egy függvényt ami egy stringet vár paraméterül és kiírja a string első karakterét!:
def first_char(s):
    #Todo: implement this function
    pass

#Írj egy függvényt ami egy stringet vár paraméterül majd kiírja az utolsó karakterét!:
def last_char(s):
    #TODO: implement this function
    pass

#Írj egy függvényt ami egy stringet vár paraméterül majd kiírja a középső karakterét!:
#import math
#math.floor
def middle_char(s):
    #TODO: implement this function
    pass

#Írj egy függvényt ami egy három elemű tömböt vár paraméterül és kiírja a tömb első és utolsó elemét!
def unpack_list_first_last(elements):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy háromszög két oldalát várja és visszaadja a területét! (Hsz képlet: sqrt(s * (s - a) * (s - b) * (s - c))
# ahol s = a + b + c / 2)
def triangle_area(a, b, c):
    #TODO: implement this function
    pass

#Írj egy függvényt, ami egy számot vár paraméterül és visszaadja a szám hárommal vett maradékát! (%)
def modulo_3(a):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy számot vár paraméterül, és visszaadja, hogy a szám páros vagy páratlan! 
def is_even(a):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy listát vár paraméterül, és visszaadja a lista legnagyobb elemét! (Használd a max() kulcsszót)
def max_in_list(lst):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami két stringet vár paraméterül és visszaadja, hogy az első string tartalmazza-e a másodikat! (Használd az "in" operátort)
def contains_string(s1, s2):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy listát vár paraméterül és visszaadja a lista elemeinek összegét! (Használd a sum() kulcsszót)
def sum_of_list(lst):
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy számot vár paraméterül és visszaadja, hogy a szám pozitív, negatív vagy nulla!
def check_number(a):
    #TODO: implement this function
    pass
    
# Írj egy függvényt, ami egy stringet vár paraméterül és visszaadja a stringet nagybetűkkel! (Használd az upper() függvényt)
def string_upper(s) -> str:
    #TODO: implement this function
    pass

# Írj egy függvényt, ami egy stringet vár paraméterül és visszaadja a stringet kisbetűkkel! (Használd a lower() függvényt)
def string_lower(s) -> str:
    pass

# Írj egy függvényt, ami egy stringet vár paraméterül és visszaadja a stringet olyan módon, hogy az első betűje nagy a többi kicsi! (Használd a title() függvényt)
def string_title(s) -> str:
    pass

#---------------------------Hard exercises---------------------------

# Írj egy függvényt ami egy listát vár paraméterül és rekurzívan visszaadja a lista páros maximumát 
# [1,2,3] -> 2, [1,3,5] -> None, [7,5,3,2,4] -> 4

# Implementáld a tic-tac-toe játékot két játékos részére, command line printekkel
# PL:
# x O X
# O X O
# O X X

# A második játékost cseréld le egy "AI"-ra, aki véletlenszerűen választ egy üres helyet
# Hasznéld a random könyvtárat
# import random

# A második játékos ha tud nyerni akkor nyerjen, máskülönben maradjon a véletlenszerű választásnál

# Implementálj egy függvényt foo(n), ami rekurzívan kiszámolja mind az n faktoriálisát, mind az n!-ik fibonacci számot.  