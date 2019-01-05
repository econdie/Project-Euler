numerators = []
numerators.append(3)
numerators.append(7)
denoms = []
denoms.append(2)
denoms.append(5)
count = 0

#compute numerator and denominator of next number in sequence and compare length
for i in range(2, 1000):
	numerators.append(numerators[i-1]*2+numerators[i-2])
	denoms.append(denoms[i-1]*2+denoms[i-2])
	if len(str(numerators[i]))>len(str(denoms[i])):
		count = count + 1

print(count)

