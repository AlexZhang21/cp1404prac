from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    bill = 0
    taxis = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 2, 4.50),
             SilverServiceTaxi("Hummer", 200, 4, 4.50)]
    current_taxi = None
    print("Let's drive!")

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").upper()

        if user_choice == "Q":

            if current_taxi is not None:
                bill += current_taxi.get_fare()
            print("Total trip cost: ${:.2f}".format(bill))
            print("Taxis are now:")

            for taxi in taxis:
                print("{}".format(taxi))
            break

        elif user_choice == "C":
            print("Taxis available: ")

            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))

            if taxi_choice < 0 or taxi_choice >= len(taxis):
                print("Invalid taxi choice")
                print("Bill to date: ${:.2f}".format(bill))
                continue
            current_taxi = taxis[taxi_choice]

            if current_taxi.name == "Limo":
                current_taxi.start_fare()
            print("Bill to date: ${:.2f}".format(bill))

        elif user_choice == "D":

            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: ${:.2f}".format(bill))
                continue
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            bill += current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            print("Bill to date: ${:.2f}".format(bill))

        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(bill))


main()