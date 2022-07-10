import unittest


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.x = Calculate()

    def test_add_two_small_numbers(self):
        result = self.x.add(5, 4)
        self.assertEqual(9, result)

    def test_substract_two_small_numbers(self):
        result = self.x.substract(2, 2)
        self.assertEqual(0, result)


class Calculate:
    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return y - x

