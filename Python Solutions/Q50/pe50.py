# Consecutive prime sum
# Problem 50 
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
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
result = GetPrimalityArray(1000000)
primes = GetPrimes(result)
answers = {}
maxLength = 0
bestPrime = 0

##iterate through first and last primes and check if sum is a prime, keep track of max length
for i in range(0, 50):
	for j in range(i+398, i+600):
		if sum(primes[i:j]) in primes:
			answers[str(sum(primes[i:j]))]=j-i
			if j-i > maxLength:
				bestPrime = sum(primes[i:j])
				maxLength = j-i

print(bestPrime)
print(answers[str(bestPrime)])