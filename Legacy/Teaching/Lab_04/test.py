class A:
    def __inin__(self):
        pass
    def say_hello(self):
        print("Hello from A")

class B(A):
    def __init__(self):
        self.__super().__init__()
    def say_hello(self):
        print("Hello from B")

class C(B, A):
    pass

a = A()
b = B()
c = C()
a.say_hello()
b.say_hello()
c.say_hello()

print(C.mro())
print(C.__bases__)
