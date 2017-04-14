# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

pandigitals = []

#check for n=2 which requires a 4 digit integer >5000 in order to have a 5 digit int*2 value resulting in 9 digits total
for i in range(5000, 10000, 1):
	n = i*2
	digits = list(str(i)) + list(str(n))
	if '1' in digits and '2' in digits and '3' in digits and '4' in digits and '5' in digits and '6' in digits and '7' in digits and '8' in digits and '9' in digits: 
		pandigitals.append(''.join(digits))

print (max(pandigitals))

