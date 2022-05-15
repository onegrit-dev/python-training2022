import unittest

from day2.calculate import divide, square


class TestSquare(unittest.TestCase):
    """square関数のテストクラス"""

    def test_square_success(self):
        """square関数のテスト（正常系）"""
        self.assertEqual(0, square(0))
        self.assertEqual(1, square(1))
        self.assertEqual(4, square(2))

    def test_square_if_none(self):
        """square関数のテスト（引数がNoneの場合）"""
        with self.assertRaises(TypeError):
            square(None)

    def test_square_if_str(self):
        """square関数のテスト（引数が文字列の場合）"""
        with self.assertRaises(TypeError):
            square('a')


class TestDivide(unittest.TestCase):
    """divide関数のテストクラス"""

    def test_calculate_success(self):
        """divide関数のテスト（正常系）"""
        self.assertEqual(3, divide(6, 2))

    def test_calculate_if_x_none(self):
        """divide関数のテスト（引数xがNoneの場合）"""
        with self.assertRaises(TypeError):
            divide(None, 2)

    def test_calculate_if_x_str(self):
        """divide関数のテスト（引数xが文字列の場合）"""
        with self.assertRaises(TypeError):
            divide('a', 2)

    def test_calculate_if_y_none(self):
        """divide関数のテスト（引数yがNoneの場合）"""
        with self.assertRaises(TypeError):
            divide(6, None)

    def test_calculate_if_y_str(self):
        """divide関数のテスト（引数yが文字列の場合）"""
        with self.assertRaises(TypeError):
            divide(6, 'a')

    def test_calculate_if_y_zero(self):
        """divide関数のテスト（引数yが0の場合）"""
        with self.assertRaises(TypeError):
            divide(6, 0)
