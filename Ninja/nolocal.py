def f():
    a = 0
    def g():
        a=1
        return a
    return g() + a
a = 10
