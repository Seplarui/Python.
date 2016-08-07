def g(num):
	for i in (range(num)):
		print('Generador %d' % i)
		yield 1

gen = g(200000)
for i in gen:
	print('Uso %d' % i)
