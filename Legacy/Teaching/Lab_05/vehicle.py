class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def return_speed(self):
        pass

    def __del__(self):
        print("Destructor called") #--> hasznos ha file-t akarunk meghívni

class Auto(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def return_speed(self):
        return 100