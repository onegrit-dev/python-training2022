import unittest

from day3.calculate import square


class TestCalculate(unittest.TestCase):
    def test_calculate_success(self):
        self.assertEqual(square(0), 0)
        self.assertEqual(square(1), 1)
        self.assertEqual(square(2), 4)

    def test_calculate_if_none(self):
        self.assertRaises(TypeError, square, None)

    def test_calculate_if_str(self):
        self.assertRaises(TypeError, square, 'a')
