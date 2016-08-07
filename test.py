def test():
	brk, num = False, 0
	for a in range(1, 20, 2):
		for b in range(1, 20, 3):
			if a == b:
				print(a)
				num += 1
				if num >= 2: brk = True
				break
			#if brk:
			#	break
test()