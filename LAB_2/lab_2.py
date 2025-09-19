'''
# python bemenet
# input( paraméter )

i = input("Adj meg egy számot:")
print(f"A szám amit megadtál: {i}") # --> nem számít, hogy számot adunk-e meg

# Első opció
i = int(input("Adj meg egy számot[int]:"))
print(f"A szám amit megadtál: {i}") # --> nem számít, hogy számot adunk-e meg
# Nem kezeli a hibákat

# --> if 
i = input("Adj meg egy számot[int]:")
if i.isdigit():
    i = int(i)
    print(f"A szám amit megadtál: {i}")
else:
    print("Nem integert adtál meg!")

# Második opció
try:
    i = int(input("Adj meg egy számot[int]:"))
    print(f"A szám amit megadtál: {i}")
except ValueError:
    print("Nem integert adtál meg!")

# Harmadik opció
i = input("Adj meg egy számot[int]:")
while not i.isdigit():
    print("Nem integert adtál meg!")
    i = input("Adj meg egy számot[int]:")

print(f"A szám amit megadtál: {i}")

# for ciklusváltozó in range

for i in range(5):
    print(i,i+1, sep="almafa", end=" ")
print()

l = [10, True, 30, "40", 50]
for i in l:
    print(f"Value: {i}| position: {l.index(i)+1}| Type: {type(i)}", end="\n")

for i in range(10):
    if i == 10:
        print("10")
        break
else:
    print("A range-ben nem szerepel a 10-es szám")

for i, e in enumerate(l):
    print(f"Value: {e}| position: {i+1}| Type: {type(e)}", end="\n")

# while
# Negyedik opció
while True:
    i = input("Adj meg egy számot[int]:")
    if i.isdigit():
        i = int(i)
        print(f"A szám amit megadtál: {i}")
        break
    else:
        print("Nem integert adtál meg!")

'''
# importok pythonban
from functions import *
from test.functions import add_py

print(add_py(3, 5))

print(add_py(3, 5))

#fontos a sorrend, amelyiket később importáljuk, az felülírja az előzőt

import functions as fn
import test.functions as tf

print(fn.add_py(3, 5))
print(tf.add_py(3, 5))
