import unittest

from day2.calculate import divide, square


class TestSquare(unittest.TestCase):

    def test_square_success(self):
        self.assertEqual(0, square(0))
        self.assertEqual(1, square(1))
        self.assertEqual(4, square(2))

    def test_square_if_none(self):
        with self.assertRaises(TypeError):
            square(None)

    def test_square_if_str(self):
        with self.assertRaises(TypeError):
            square('a')


class TestDivide(unittest.TestCase):

    def test_calculate_success(self):
        self.assertEqual(3, divide(6, 2))

    def test_calculate_if_x_none(self):
        with self.assertRaises(TypeError):
            divide(None, 2)

    def test_calculate_if_x_str(self):
        with self.assertRaises(TypeError):
            divide('a', 2)

    def test_calculate_if_y_none(self):
        with self.assertRaises(TypeError):
            divide(6, None)

    def test_calculate_if_y_str(self):
        with self.assertRaises(TypeError):
            divide(6, 'a')

    def test_calculate_if_y_zero(self):
        with self.assertRaises(TypeError):
            divide(6, 0)
