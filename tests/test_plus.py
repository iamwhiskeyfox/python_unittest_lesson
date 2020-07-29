from unittest import TestCase
from functions.plus import plus


class PlusFunctionTestCase(TestCase):
    def test_1_plus_1_returns_2(self):
        self.assertEqual(2, plus(1, 1))

    def test_5_plus_5_returns_10(self):
        self.assertEqual(10, plus(5, 5))

    def test_100_plus_200_returns_300(self):
        self.assertEqual(300, plus(100, 200))
