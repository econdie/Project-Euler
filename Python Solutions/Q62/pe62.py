# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import Counter

cubes = []
cubeSets = []
counters = {}

#adjust this range until we can find a solution
for i in range(1, 9000):
	cubes.append(i**3)


for cube in cubes:
	cubeList = sorted([int(chars) for chars in str(cube)])
	cubeStrList = [str(x) for x in cubeList]
	cubeStr = "".join(cubeStrList)
	#we found this is the permutation we are looking for from below code. if a cube results in this perm, print the cube (there should be 5)
	if cubeStr == '012334556789':
		print('This cube matches the target permutation:')
		print(cube)
	if cubeStr in counters:
		counters[cubeStr] = counters[cubeStr] + 1
	else:
		counters[cubeStr] = 1

#print the permutation that appears 5 times
print('We searched for this permutation that is the first one to appear 5 times:')
for perms in counters:
	if counters[perms] == 5:
		print(perms)
