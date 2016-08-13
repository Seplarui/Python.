def test(num):
    if num < 0:
        raise ValueError('El número es negativo')
    return num

test(-3)