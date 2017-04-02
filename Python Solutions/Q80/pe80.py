import math
import decimal

rootSum = 0

for i in range(2, 100):
	if math.sqrt(i)!=int(math.sqrt(i)):
		##use decimal package to define level of precision
		num = decimal.Decimal(i)
		dot100 = decimal.Context(prec=102)
		root = num.sqrt(dot100)
		listRoot = list(str(root))
		for j in range(0, 101):
			if listRoot[j] != '.':
				rootSum = rootSum + int(listRoot[j])

print(rootSum)