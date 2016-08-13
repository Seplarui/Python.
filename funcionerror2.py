num = 120
def test(num):
    if num < 0:
        raise ValueError('El número es negativo')
    return num
def retest(num):
    if test(num) > 100:
        print('OK')

retest(-1)