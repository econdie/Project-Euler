answer = 0
maxSolutions = 0

for p in range(121, 1001):
	pSolutions = 0
	for a in range(1, p):
		for b in range(1,p-a):
			c = p - a - b
			if a**2 + b**2 == c**2:
				pSolutions = pSolutions + 1

	if pSolutions > maxSolutions:
		maxSolutions = pSolutions
		answer = p

	print(p)

print(answer)



