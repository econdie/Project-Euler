import math

def getConsecutivePrimes(a,b):
    n = 0
    while True:
        if checkPrime(a,b,n):
            n = n + 1
        else:
            return n

def checkPrime(a,b,n):
    if n**2 + a*n + b > 1:
        if all((n**2 + a*n + b)%j != 0 for j in range(2, int(math.sqrt(n**2 + a*n + b)))):
            return True
        else:
            return False
    else:
        return False

currentMax = [0,0,0]

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        consecutivePrimes = getConsecutivePrimes(a, b)
        if consecutivePrimes > currentMax[2]:
            currentMax = [a,b,consecutivePrimes]
        else:
            continue

print(currentMax[0]*currentMax[1])
