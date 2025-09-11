# Terminal
python --version python3 --version

# python3 lesson1.py

print('test')

# Python 3.9.6 (default, Aug 11 2023, 19:44:49) [Clang 15.0.0 (clang-1500.0.40.1)] on darwin Type "help", "copyright", "credits" or "license" for more information.

3+2 5 exit()

variable = value

# a = 10 b = 20 if a > b: print("a nagyobb mint")

# a = 20 b = 10

# if a > b: print("a nagyobb mint")

# comment
# """ Comment in more line """

# x = 'alma' y = "alma" print(y, x)


# a = 'alma' A = 1

#variable names
#3alma = 10 a-lma = 20 al ma = 20

#a,b,c = 1,2,3 
#print(a, b, c)

#a=b=c=10 print(a, b, c)


+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y


#Négyzet
a = 4

print(a ** 2)

elements = [1, 2, 3] 
a, b, c = elements 
x, y, z = [10, 20, 30] 
print(a, b, c) 
print(x, y, z)

s = "abc" 
t = "123" 
r = "456" 
print(s+t+r) 
print(s, t, r)

"alma"[2] 

a='alma' 
b=2

#error
print(a+2)

#Traceback (most recent call last): File "/Users/rolandkiraly/Desktop/Python/ELTE Python anyagok/source/lesson1.py", line 50, in <module> print(a+2) TypeError: can only concatenate str (not "int") to str

a='alma' 
b=2

a = 'almafa'*b

#ok
print(a, 2)

print(a,c)

a,b,c = 34,"almafa",True
print(a,b,c)

# type castig
print("Type of b is",type(b)) b = str(b) print("Type of b is",type(b))

int(b) print("Type of b is",type(b)) float(b) print("Type of b is",type(b))


print(a + str(c))

print(f"a {c}")


# Data types
# numeric:
# int, float, complex

#example
a = 2 
b = 1.0 
c = 1j

#complex number = real/imaginary
#pl.: a + bj a = real part, b imaginary part
#j imaginary egység
#j^2 = -1
a = 2j 
print(type(a)) 
z=1j 
print("a=", a) 
print("a + z =", a + z) 
print(a*z)


m = memoryview(bytes(8)) 
print(m)

aa = 10 
print(f"Az aa erteke = {aa}")

s = "alma" 
s2 = """ alma alma """

#-->

#a= 2j 
#a + z = 3j (-2+0j)

# sequens:
# list, tuple, range

l = [1, 2, 3] 
t = (1, 2, 3) does not support item assignment
r = range(6)

s.add(20) 
print(s)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#list[start:stop:step]

l[1:5]
l[::-1]
l[::2]

d = {"first":1, "last":2} 
person = {'name':"Yoda", 'age':300}

print(person.keys()) 
print(person.values()) 
print(person['name'])

s = {'alma', 'korte'}

#immutable set
#fs = frozenset({"alma", "korte"})


# mapping:
# dict

d = {"first":1, "last":2} 
person = {'name':"Yoda", 'age':300}

# set
# set, frozen

s = {'alma', 'korte'}

#immutable
fs = frozenset({"alma", "korte"})

# boolean
# bool

b = True 
b = False

# none type
# NoneType

nt = None

a = 1 
print(type(a))

# set functioons
# str int float complex list tuple range dict set frozenset bool bytes bytearray memoryview

#write an undefined function
def func():
    pass

#Gyakorlaton bemutatott programok a test2.py fájlban
def nagyobb(a, b): 
    if a > b: return a 
    else: return b

print(nagyobb(10, 20))

x = 10 
def fun(): 
    x = 20 
    print("value of the x is", x)

print("value of the x is", x) 
fun()

x = 3 
print(x)
def func(): 
    global x 
    x = 10

func() 
print(x)