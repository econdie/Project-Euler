codes = []
firstPos = {}
secondPos = {}
thirdPos = {}

for i in range(0,10):
	firstPos[str(i)] = 0
	secondPos[str(i)] = 0
	thirdPos[str(i)] = 0

with open('keylog.txt') as f:
	for line in f.readlines():
		codes.append(line.rstrip('\n'))


for code in codes:
	for i in range(0,10):
		if int(code[0]) == i:
			firstPos[code[0]] = firstPos[code[0]] + 1
		if int(code[1]) == i:
			secondPos[code[1]] = secondPos[code[1]] + 1
		if int(code[2]) == i:
			thirdPos[code[2]] = thirdPos[code[2]] + 1

print(firstPos)
print(secondPos)
print(thirdPos)
print(codes)

#use this output to analyze solution by hand, which fairly easily can be worked out to 73162890