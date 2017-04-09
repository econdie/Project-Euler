numerators = []
denominators = []

for i in range(10, 100):
	for j in range(i+1, 100):
		
		iDig = list(str(i))
		jDig = list(str(j))
		if '0' in iDig or '0' in jDig:
			continue
		if iDig[0]==jDig[0]:
			if int(iDig[1])/int(jDig[1])==i/j:
				numerators.append(i)
				denominators.append(j)
		if iDig[0]==jDig[1]:
			if int(iDig[1])/int(jDig[0])==i/j:
				numerators.append(i)
				denominators.append(j)
		if iDig[1]==jDig[0]:
			if int(iDig[0])/int(jDig[1])==i/j:
				numerators.append(i)
				denominators.append(j)
		if iDig[1]==jDig[1]:
			if int(iDig[0])/int(jDig[0])==i/j:
				numerators.append(i)
				denominators.append(j)

prodNum = numerators[0]*numerators[1]*numerators[2]*numerators[3]
prodDenom = denominators[0]*denominators[1]*denominators[2]*denominators[3]

print('decimal form of answer - compute denominator from this')
print(prodNum/prodDenom)