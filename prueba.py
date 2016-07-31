
n = 13
while n < 10:
    x = 2
    while x < n:
        if n % x == 0:
            print ('%i vale %i * %i' % (n, x, n / x))
            break
            x += 1
        else:
            print('%i es un numero primo' % n)
            n *= 1
