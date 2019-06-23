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


calculator = TwoNumbersCalculator(1, 2)
print(calculator)
print('x={}, y={}'.format(calculator.x, calculator.y))
calculator.print_add()

TwoNumbersCalculator.print_author()
# クラスメソッドにはオブジェクトからもアクセス可能
calculator.print_author()

"""
【実行結果】

TwoNumbersCalculator(1, 2)
x=1, y=2
計算結果は3です。
作者はakiyokoです。
作者はakiyokoです。
"""
