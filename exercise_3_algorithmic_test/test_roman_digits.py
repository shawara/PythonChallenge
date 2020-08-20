import math
import unittest

from .roman_digits import int_to_roman, values, roman


class RomanNumbersTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = {
            32: "XXXII",
            45: "XLV",
            512: "DXII",
            128: "CXXVIII",
            944: "CMXLIV",
            999: "CMXCIX",
        }

    def test_main_values(self):
        for i in range(len(values)):
            self.assertEqual(roman[i], int_to_roman(values[i]))

    def test_data_valuse(self):
        for k, v in self.test_data.items():
            self.assertEqual(v, int_to_roman(k))
