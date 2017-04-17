# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

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
result = GetPrimalityArray(100000)
primes = GetPrimes(result)
answerNum = ''
answer = False

##deeply nested loop that takes a 4 digit prime and check if there exists two other 4 digit primes that are permutations, with equal distance between p1 p2 and p3
for prime1 in primes:
    if len(str(prime1))==4:
        for prime2 in primes:
            if len(str(prime2))==4:
                prime1set = set(list(str(prime1)))
                prime2set = set(list(str(prime2)))
                if prime1set == prime2set and prime1 != prime2:
                    for prime3 in primes:
                        if len(str(prime3))==4:
                            prime3set = set(list(str(prime3)))
                            if prime1set == prime3set and prime1 != prime3:
                                if (prime2-prime1)==(prime3-prime2) and prime1 != 1487:
                                    answerNum = (str(prime1)+str(prime2)+str(prime3))
                                    answer = True

    if answer == True:
        break

print(answerNum)