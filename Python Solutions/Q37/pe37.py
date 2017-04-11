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

def CheckTruncatable(num, primes):
    listNum = list(str(num))
    for i in range(1, len(listNum)):
        check = listNum[0:i]
        if int(''.join(check)) not in primes:
            return False
    for j in range(1, len(listNum)):
        check = listNum[j:len(listNum)]
        if int(''.join(check)) not in primes:
            return False
    return True
    
    

##true or false primality list of first x numbers
result = GetPrimalityArray(800000)
##list of prime numbers from 2 to x
primes = GetPrimes(result)
truncatables = []

for prime in primes:
    if prime > 7 and CheckTruncatable(prime, primes):
        truncatables.append(prime)
            
print(truncatables)
print(sum(truncatables))
