"""
CP1404/CP5632 Practical
Guitar class
Estimate:6 minutes
Actual:  9minutes
"""

CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar instance."""
        return f"Guitar {self.name} ({self.year}), worth ${self.cost:,.2f}."

    def get_age(self):
        """Calculate the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Implement less than comparison based on year."""
        return self.year < other.year
