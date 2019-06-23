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


class CatBMICalculator(BMICalculator):
    def judge(self):
        bmi = self.calculate()
        if bmi < 50:
            return '低体重'
        elif 50 <= bmi and bmi < 70:
            return '普通'
        else:
            return '肥満'


cat_calculator = CatBMICalculator(30, 4)
cat_calculator.print_bmi()

cat_calculator = CatBMICalculator(35, 8)
cat_calculator.print_bmi()

cat_calculator = CatBMICalculator(40, 12)
cat_calculator.print_bmi()

"""
【実行結果】

身長30cm・体重4kgの場合のBMIは、44.44444444444444です。
体型は低体重です。
身長35cm・体重8kgの場合のBMIは、65.30612244897961です。
体型は普通です。
身長40cm・体重12kgの場合のBMIは、74.99999999999999です。
体型は肥満です。
"""
