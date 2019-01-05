answer = 0
x = 1

while answer == 0:
	times2 = 2 * x
	times3 = 3 * x
	times4 = 4 * x
	times5 = 5 * x
	times6 = 6 * x

	xSet = set(list(str(x)))
	x2Set = set(list(str(times2)))
	x3Set = set(list(str(times3)))
	x4Set = set(list(str(times4)))
	x5Set = set(list(str(times5)))
	x6Set = set(list(str(times6)))

	if xSet == x2Set and xSet == x3Set and xSet == x4Set and xSet == x5Set and xSet == x6Set:
		answer = x

	x = x + 1


print(answer)

