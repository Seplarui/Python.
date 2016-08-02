def gen(num):
    for i in range(num):
        print ('Generador %d' % i)
        yield i
        return


for i in gen:
    print('Uso %d' % i)
