# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
import math 

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

##get list of first x primes
result = GetPrimalityArray(800000)
primes = GetPrimes(result)

answer = 0
firstPrime = 0
n = 2

while answer < 4:
	factors = []
	for prime in primes:
		#bounded by n/30 as 2 * 3 * 5 = 30 
		if prime > n/30:
			break
		if n%prime==0:
			factors.append(prime)
	if len(factors) == 4:
		answer = answer + 1
	else:
		answer = 0

	n = n + 1

print(n-4)