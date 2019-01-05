# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

# n	Relatively Prime	φ(n)	n/φ(n)
# 2	1	1	2
# 3	1,2	2	1.5
# 4	1,3	2	2
# 5	1,2,3,4	4	1.25
# 6	1,5	2	3
# 7	1,2,3,4,5,6	6	1.1666...
# 8	1,3,5,7	4	2
# 9	1,2,4,5,7,8	6	1.5
# 10	1,3,7,9	4	2.5
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


###this is very unoptimized

currentMax = 1
currentN = 1

for i in range(1000001, 9, -1):
	factors = set([x for x in range(1,int(i/2)+1) if i%x==0])
	zzTest = set([])
	
	for factor in factors:
		if factor > 1 and factor < i/2:
			maxIters = int(i/factor)
			for j in range(2, maxIters):
				if j * factor not in factors:
					zzTest.add(j*factor)

	factors = factors.union(zzTest)

	numFactors = len(factors) - 1
	totient = i - numFactors - 1
	checkDiv = i/totient

	if checkDiv > currentMax:
		currentMax = checkDiv
		currentN = i
	print(i)
	print(currentN)
