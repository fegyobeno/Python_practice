class SomeClass:
    def __init__(self):
        self.__private_var = 42  # Private variable
        self._private_var = 10  # Protected variable

    def get_private_var(self):
        return self.__private_var
    # property tag - zárójel nélküli hívás, yey
    @property
    def private_var(self):
        if self.__private_var < 0:
            return 0
        else:
            return self.__private_var
    
obj = SomeClass()
print(obj.get_private_var())  # Accessing private variable via public method
print(obj._private_var)  # Accessing protected variable (not recommended)
print(obj._SomeClass__private_var)  # Accessing private variable via name mangling

# van számítás de nincs (), a háttérben meghívódik a getter
print(obj.private_var)  # Accessing private variable via property