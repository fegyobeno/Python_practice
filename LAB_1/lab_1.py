# Konzolra írás
print("Szia világ")

# Változó deklaráció
a = 20
b = 10

# f string
print(f"a értéke: {a}, b értéke: {b}, a + b = {a + b}")
# alternatívan de kevésbé haszálva
print("a értéke: {}, b értéke: {}, a + b = {}".format(a, b, a + b))
#vagy
print("a értéke: " + str(a) + ", b értéke: " + str(b) + ", a + b = " + str(a + b))


# Python dinamikusan típusozott --> a változók futásidőben kapnak típust
a = 10
print(f"{a} is of type {type(a)}")
a = 5.5
print(f"{a} is of type {type(a)}")
a = "almafa"
print(f"{a} is of type {type(a)}")

# logikai műveletek
'''
== -> egyenlő
!= -> nem egyenlő
>  -> nagyobb
<  -> kisebb
>= -> nagyobb vagy egyenlő
<= -> kisebb vagy egyenlő

and -> és
or  -> vagy
not -> nem
'''

# Első rendű logikai műveletek
print(10 == 20)
print(10 != 20)
print(True and not False or True and False)

# Python specifikus(?) műveletek 
a, b, c = 1, 2,3
print(a, b, c)

a=b=c=10
print(a, b, c)

elements = [1, 2, 3]
a, b, c = elements
x, y, z = [10, 20, 30]
print(a, b, c)
print(x, y, z)

# Stringek -> karakter sorozatok

s = "abc"
t = "123"
r = "456"
print(s+t+r)
print(s, t, r) # space between

a='alma'
b=2
#print(a+2) -> error, however
print(a*b) #almaalma

# listák

l = [1,2,3,4,5]
print(l)
l2 = ["alma", 2, 3.5, True]
print(l2)

print(l2[0]) #alma
print(l2[-1]) #True
# slicing -> l[mettől:meddig:lépésköz]
print(l2[1:-1:2]) #2, 3.5


#variables in functions

x = 10
def fun():
    x = 20
    print("value of the x is", x)

fun()

def fun2(x : int) -> None:
    print(f"value of the x is {x}")

fun2(30)

def fun3(x : int) -> int:
    return x

print(fun3(40))

def fun4(x : int) -> str:
    return f"value of the x is {x}"

print(fun4(50))

#global keyword
# akkor használjuk, ha scope-on kívül akarunk változót módosítani
x = 3
def func():
    global x
    x = 10

func()
print(x)


a = 3 + 2j
print(type(a))
z=1j
print("a=", a)
print("a + z =", a + z)
print(a*z)

a = 2+3j
b = 1+2j
print(a*b)

print("real", a.real)
print("imag", a.imag)

r = range(6)
print(r)


d = {"first":1, "last":2}
person = {'name':"Yoda", 'age':300}

print(person.keys())
print(person.values())
print(person['name'])



s = {'alma', 'korte'}
#immutable
fs = frozenset({"alma", "korte"})

s.add(20)
print(s)

bya = bytearray(5)
print(bya)

m = memoryview(bytes(8))
print(m)

x = bool(6)
print(x)

nt = None
print(nt)

s = "alma"
s2 = """
alma
alma
"""
print(s2)

s3 = "alma a fa alatt"
print(s3[:5])
print(s3[3:9])
print(s3[2:])
print(s3[-5:-2])

# string functions