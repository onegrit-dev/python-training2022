def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError('xは数値で指定してください。x={}'.format(x))
    return x ** 2
