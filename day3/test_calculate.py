import unittest

from day3.calculate import square, divide


class TestSquare(unittest.TestCase):
    def test_calculate_success(self):
        self.assertEqual(square(0), 0)
        self.assertEqual(square(1), 1)
        self.assertEqual(square(2), 4)

    def test_calculate_if_none(self):
        self.assertRaises(TypeError, square, None)

    def test_calculate_if_str(self):
        self.assertRaises(TypeError, square, 'a')


class TestDivide(unittest.TestCase):
    def test_calculate_success(self):
        self.assertEqual(divide(6, 2), 3)

    def test_calculate_if_x_none(self):
        self.assertRaises(TypeError, divide, None, 2)

    def test_calculate_if_x_str(self):
        self.assertRaises(TypeError, divide, 'a', 2)

    def test_calculate_if_y_none(self):
        self.assertRaises(TypeError, divide, 6, None)

    def test_calculate_if_y_str(self):
        self.assertRaises(TypeError, divide, 6, 'a')

    def test_calculate_if_y_zero(self):
        self.assertRaises(TypeError, divide, 6, 0)
