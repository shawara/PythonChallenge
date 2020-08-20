import math
import unittest

from .circle import Circle


class CircleTest(unittest.TestCase):

    def setUp(self):
        self.radius = 10
        self.circle = Circle(self.radius)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_not_number_radius(self):
        with self.assertRaises(TypeError):
            Circle("lol")

    def test_area(self):
        self.assertEqual(math.pi * self.radius * self.radius, self.circle.area())

    def test_perimeter(self):
        self.assertEqual(2 * math.pi * self.radius, self.circle.perimeter())
