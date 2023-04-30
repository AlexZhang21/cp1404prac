"""
CP1404/CP5632 Practical
Basic manual tests for Guitar class
Estimate:12 minutes
Actual: 16 minutes
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def run_tests():
    """Tests for Guitar class."""
    name = "Fender Stratocaster"
    year = 1954
    cost = 1299.99

    guitar = Guitar(name, year, cost)
    other = Guitar("Gibson Les Paul", 2010, 1899.95)

    print(f"{guitar.name} get_age() - Expected {69}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {13}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

"""output"""
if __name__ == '__main__':
    run_tests()

