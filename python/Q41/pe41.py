##use sieves

import math

def GetPrimalityArray(n):

    primalityArray = [True] * n

    for i in range(2, int(math.sqrt(n))):
        if primalityArray[i] == True:
            for j in range(i**2, n, i):
                primalityArray[j] = False

    return(primalityArray)

def GetPandigitalPrimes(primality):
    primes = []
    for i in range(999999, len(primality)):
        if primality[i] == True:
        	flag = True
        	length = len(str(i))
        	digits = list(str(i))
        	for j in range(1, length+1):
        		if str(j) not in digits:
        			flag = False
        	if flag == True:
        		primes.append(i)
    return primes

##true or false primality list of first x numbers - only need to check 7 digit nummbers up to 7654321, 8 or 9 digit pandigital numbers sum to multiple of 3 -> divisible by 3 -> not prime
result = GetPrimalityArray(7654321)
##list of prime numbers from 2 to x
primes = GetPandigitalPrimes(result)

print(max(primes))