def test():
    yield 1
    yield 2
    yield 3
    return

print test()
