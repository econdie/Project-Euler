##THIS IS NOT A GOOD SOLUTION. Brute force requires 60s build time. Should have just checked the cyclic primes? https://projecteuler.net/thread=26;page=9

from decimal import *
getcontext().prec = 7000
decimals = []
investigate = []

for i in range(2, 1000):
	#adjust this j max value until investigate list only has single item
	for j in range(1, 980):
		x  = 1/Decimal(i)
		if len(str(x)) > 50:
			if str(x)[50:50+j]==str(x)[50+j:50+(2*j)]==str(x)[50+(2*j):50+(3*j)]:
				decimals.append(i)
		else:
			decimals.append(i)

for i in range(2, 1000):
	if i not in set(decimals):
		investigate.append(i)

print(len(investigate))
print(investigate)