def digitSquare(num):
	numStr = str(num)
	digSum = 0

	for nums in numStr:
		digSum = digSum + int(nums)**2

	return digSum


counter = 0
for i in range(1,10000001):
	flag = 0
	value = digitSquare(i)
	while flag == 0:
		if value != 89 and value != 1:
			value = digitSquare(value)
		else:
			flag = 1
	if value == 89:
		counter = counter + 1

	

print(counter)
