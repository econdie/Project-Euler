d2options = []
d3options = []
d4options = []
d5options = []
d6options = []
d7options = []
d8options = []

for n in range(12, 1000, 2):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d2options.append(strN)

for n in range(12, 1000, 3):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d3options.append(strN)

for n in range(15, 1000, 5):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d4options.append(strN)

for n in range(14, 1000, 7):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d5options.append(strN)

for n in range(11, 1000, 11):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d6options.append(strN)

for n in range(13, 1000, 13):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d7options.append(strN)

for n in range(17, 1000, 17):
	if n < 100:
		strN = '0' + str(n)
	else:
		strN = str(n)
	digits = sorted(list(strN))
	digitsUnique = sorted(list(set(digits)))
	if digits == digitsUnique:
		d8options.append(strN)

answers = []
for d8option in d8options:
	chain8 = d8option[0:2]
	for d7option in d7options: 
		if d7option[1:3] == chain8:
			chain7 = d7option[0:2]
			for d6option in d6options:
				if d6option[1:3] == chain7:
					chain6 = d6option[0:2]
					for d5option in d5options:
						if d5option[1:3] == chain6:
							chain5 = d5option[0:2]
							for d4option in d4options:
								if d4option[1:3] == chain5:
									chain4 = d4option[0:2]
									for d3option in d3options:
										if d3option[1:3] == chain4:
											chain3 = d3option[0:2]
											for d2option in d2options:
												if d2option[1:3] == chain3:
													checkNum = d2option + d3option[2] + d4option[2] + d5option[2] + d6option[2] + d7option[2] + d8option[2]
													digits = sorted(list(checkNum))
													digitsUnique = sorted(list(set(digits)))
													if digits == digitsUnique:
														for i in range(0, 10, 1):
															if str(i) not in digits:
																checkNum = str(i) + checkNum
																answers.append(int(checkNum))
	
print(sum(answers))


