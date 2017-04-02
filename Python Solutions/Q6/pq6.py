def SumOfSquares(n):
    value = 0
    for i in range(1, n+1):
        value = value + i**2
    return value

sqOfSum = sum(range(1,101))**2
sumOfSq = SumOfSquares(100)

print(sqOfSum - sumOfSq)
