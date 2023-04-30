"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
from prac_06.car import Car

def main():
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)
    # Create a new Car object called "limo" that is initialised with 100 units of fuel
    limo = Car(100)

    # Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Fuel amount in the car: {limo.fuel} litres")

    # Attempt to drive the car 115 km using the drive method
    distance_driven = limo.drive(115)

    # Print the distance actually driven
    print(f"Distance driven: {distance_driven} km")

    # Print the car object to check if __str__ method is working as expected
    print(limo)


main()
