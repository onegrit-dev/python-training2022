def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError('xは数値で指定してください。x={}'.format(x))
    return x ** 2


def divide(x, y):
    if not isinstance(x, (int, float)):
        raise TypeError('xは数値で指定してください。x={}'.format(x))
    elif not isinstance(y, (int, float)):
        raise TypeError('yは数値で指定してください。y={}'.format(y))
    elif y == 0:
        raise TypeError('yには0を指定できません。')
    return x / y
