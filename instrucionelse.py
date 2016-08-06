def evaluacion(num):
	if num < 0:
		r = 'negativo'
	elif num > 0:
		r = 'positivo'
	else:
		r = 'nulo'
	return r
print(evaluacion(-3))
