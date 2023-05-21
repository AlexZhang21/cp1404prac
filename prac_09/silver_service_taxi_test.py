from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the functionality of the SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Hummer", 200, 2, 4)
    taxi.drive(18)
    fare = taxi.get_fare()
    expected_fare = 148.50
    assert fare == expected_fare, f"Expected fare of {expected_fare:.2f} but got {fare:.2f}"
    print(taxi)


main()
