# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
##use sieves

import math
import string

def GetPrimalityArray(n):

    primalityArray = [True] * n

    for i in range(2, int(math.sqrt(n))):
        if primalityArray[i] == True:
            for j in range(i**2, n, i):
                primalityArray[j] = False

    return(primalityArray)

def GetPrimes(primality):
    primes = []
    for i in range(2, len(primality)):
        if primality[i] == True:
            primes.append(i)
    return primes

def CheckCondition(n, primes):
	m = 1
	while 2*(m**2) < n:
		for prime in primes:
			if prime + 2*(m**2) > n:
				break
			elif prime + 2*(m**2) == n:
				return True
			else:
				continue

		m = m + 1
	return False

##get list of first x primes
result = GetPrimalityArray(800000)
primes = GetPrimes(result)

answer = 0
i = 3

#iterate through odd numbers, check for composite and sum condition requirements
while answer == 0:
	if i not in primes:
		if CheckCondition(i, primes) == False:
			answer = i
	i = i + 2

print(answer)