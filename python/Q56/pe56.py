from decimal import *


getcontext().prec = 201
maxSum = 0
for i in range (1, 100):
	for j in range (1, 100):
		currentSum = 0
		exponent = Decimal(i)**Decimal(j)
		listDigits = list(str(exponent))
		for digit in listDigits:
			currentSum = currentSum + int(digit)
		if currentSum > maxSum:
			maxSum = currentSum

print(maxSum)
