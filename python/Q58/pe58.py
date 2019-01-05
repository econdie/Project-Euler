import math
import numpy

def GetPrimalityArray(n):

    primalityArray = np.array([True] * n)

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

##get list of first x primes DOESNT WORK DUE TO MEMORY ALLOCATION FOR PYTHON LISTS
# primes = set(GetPrimes(GetPrimalityArray(350000000)))

##use numpy  for effecient memory storage, so we can store a large prime list
#algorithm taken from here http://code.activestate.com/recipes/577331-fastest-way-to-list-all-primes-below-n-in-python/
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


primes = set(primesfrom2to(870000000))

primeCount = 8
diagonalCount = 13

ratio = 8/13

d1 = 31
d1inc = 18
d2 = 37
d2inc = 20
d3 = 43
d3inc = 22

sideLength = 7

while ratio > 0.1:
    diagonalCount = diagonalCount + 4

    d1 = d1 + d1inc + 8
    d2 = d2 + d2inc + 8
    d3 = d3 + d3inc + 8

    d1inc = d1inc + 8
    d2inc = d2inc + 8
    d3inc = d3inc + 8

    if d1 in primes:
        primeCount = primeCount + 1

    if d2 in primes:
        primeCount = primeCount + 1

    if d3 in primes:
        primeCount = primeCount + 1

    sideLength = sideLength + 2
    ratio = primeCount / diagonalCount

print(sideLength)
