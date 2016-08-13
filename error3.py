def f(num):
    try:
        return test(num)
    except:
        return 0
        print('Return 0')
    finally:
        print('Siempre se ejecuta2')

f(-1)