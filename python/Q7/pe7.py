##use sieves

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

##true or false primality list of first x numbers
result = GetPrimalityArray(110000)
##list of prime numbers from 2 to x
primes = GetPrimes(result)

if(primes[10000]):
    print(primes[10000])
else:
    print('need to compute more numbers in primality array')
