from prac_09.taxi import Taxi


def main():
    # Create a new taxi object with different variable names
    taxi_1 = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40 km
    taxi_1.drive(40)

    # Print the taxi's details
    print(taxi_1)
    # Print the current fare
    print("Current fare: $" + str(taxi_1.get_fare()))

    # Restart the meter and drive the car 100 km
    taxi_1.start_fare()
    taxi_1.drive(100)

    # Print the details of the taxi
    print(taxi_1)
    # Print the current fare
    print("Current fare: $" + str(taxi_1.get_fare()))


main()
