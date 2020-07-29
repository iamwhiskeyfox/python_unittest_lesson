from unittest import TestCase
from functions.gcd import gcd

class GcdFunctionTestCase(TestCase):
    def test_10_gcd_5_is_5(self):
        self.assertEqual(5, gcd(10, 5))

    def test_33_gcd_27_is_3(self):
        self.assertEqual(3, gcd(33, 27))

    def test_99_gcd_45_is_9(self):
        self.assertEqual(9, gcd(99, 45))

    def test_97_gcd_23_is_1(self):
        self.assertEqual(1, gcd(97, 23))

    def test_10_gcd_100_is_10(self):
        self.assertEqual(10, gcd(10, 100))