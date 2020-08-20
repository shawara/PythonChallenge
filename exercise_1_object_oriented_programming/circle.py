import math


class Circle:
    def __init__(self, radius: float):
        if radius <= 0.0:
            raise ValueError("Radius must be positive value")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
