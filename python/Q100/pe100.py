# (n/m) * (n-1/m-1) = 0.5

# n * (n-1)
# _________   =  0.5
# m * (m-1) 

# -> 2n^2 - 2n - m^2 + m = 0
#diophantine equation
#n_n+1 = 3 * n + 2 * m - 2
#m_m+1 = 4 * n + 3 * m - 3
import math

n = 15
m = 21
maximum = 10 ** 12

while(m < maximum):
	nIter = 3 * n + 2 * m - 2
	mIter = 4 * n + 3 * m - 3

	n = nIter
	m = mIter

	
print(n)
