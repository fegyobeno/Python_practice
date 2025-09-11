from vehicle import Vehicle
from vehicle import Auto

# Import the Vehicle class from vehicle.py

# Create an instance of the Vehicle class
my_vehicle = Vehicle(make="Toyota", model="Corolla", year=2020)

# Display the vehicle information
print(my_vehicle.return_speed())

# Create an instance of the Auto class
my_auto = Auto(make="Ford", model="Focus", year=2019, doors=4)
print(my_auto.return_speed())
