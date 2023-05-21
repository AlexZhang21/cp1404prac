from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a type of taxi that includes additional services and charges."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        """Calculate and return the fare of the taxi ride. Includes the flagfall charge."""
        fare = super().get_fare() + self.flagfall
        return fare

    def __str__(self):
        """Return a formatted string representing the SilverServiceTaxi."""
        return f"{super().__str__()} plus flag-fall of ${self.flagfall:.2f}"
