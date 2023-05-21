import random
from prac_09.car import Car


class UnreliableCar(Car):
    """the unreliable version of the car"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """sometimes drive the car and based on reliability"""
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0