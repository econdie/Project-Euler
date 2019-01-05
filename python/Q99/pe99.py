import math

with open('base_exp.txt') as f:
	content = f.readlines()


currentMax = 0
currentMaxLine = 1
lineNum = 0
for contents in content:
	lineNum = lineNum + 1
	nums = contents.rstrip('\n').split(",")
	num1 = int(nums[0])
	num2 = int(nums[1])

	if num2 * math.log(num1) > currentMax:
		currentMax = num2 * math.log(num1)
		currentMaxLine = lineNum
	
	

print(currentMaxLine)