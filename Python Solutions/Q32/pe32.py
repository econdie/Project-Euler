products = []

for i in range(1, 2000):
	for j in range(1, 2000):
		product = i * j
		digits = sorted(list(str(product))+list(str(i))+list(str(j)))
		uniqueDigits = sorted(list(set(digits)))
		if digits==uniqueDigits and len(digits)==9:
			if '1' in digits and '2' in digits and '3' in digits and '4' in digits and '5' in digits and '6' in digits and '7' in digits and '8' in digits and '9' in digits:
				if product not in products:
					print(product,i,j)
					products.append(product)

print(sum(products))

