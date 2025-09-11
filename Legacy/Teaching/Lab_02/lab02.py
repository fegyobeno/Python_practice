#valtozok
a = 2
print(a)
a,b,c = 2,3,4
print(a,b,c)

a = 'almafa'

print(a,c)

a,b,c = 34,"almafa",True
print(a,b,c)

print(a + str(c))

print(f"a {c}")

#print(a+c) #type error

def func():
    x = 10
    print(x)

#scope
#print(x) #undefined exception

def func2(x):
    print(x)

def func3(x):
    return x

def func4(x, y = 3):
    if type(x) == int:
        return x+y
    else:
        return 0