class BMICalculator:
    def __init__(self, height, weight):
        self.height = height  # cm
        self.weight = weight  # kg

    def calculate(self):
        return self.weight / (self.height / 100) ** 2

    def judge(self):
        bmi = self.calculate()
        if bmi < 18.5:
            return '低体重'
        elif 18.5 <= bmi and bmi < 25:
            return '普通'
        else:
            return '肥満'

    def print_bmi(self):
        print('身長{}cm・体重{}kgの場合のBMIは、{}です。'.format(
            self.height,
            self.weight,
            self.calculate(),
        ))
        print('体型は{}です。'.format(self.judge()))


calculator = BMICalculator(177, 77)
calculator.print_bmi()

"""
【実行結果】

身長177cm・体重77kgの場合のBMIは、24.577867151840145です。
体型は普通です。
"""
