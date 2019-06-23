class TwoNumbersCalculator:
    author = 'akiyoko'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'TwoNumbersCalculator({}, {})'.format(self.x, self.y)

    def add(self):
        return self.x + self.y

    def print_add(self):
        print('計算結果は{}です。'.format(self.add()))

    @classmethod
    def print_author(cls):
        print('作者は{}です。'.format(cls.author))


class ThreeNumbersCalculator(TwoNumbersCalculator):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return 'ThreeNumbersCalculator({}, {}, {})'.format(self.x, self.y, self.z)

    def add(self):
        return super().add() + self.z


calculator = ThreeNumbersCalculator(1, 2, 3)
print(calculator)
print('x={}, y={}, z={}'.format(calculator.x, calculator.y, calculator.z))
calculator.print_add()

"""
【実行結果】

ThreeNumbersCalculator(1, 2, 3)
x=1, y=2, z=3
計算結果は6です。
"""
