# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

charValues = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
triangles = []
triangleWords = []

#get first n triangle numbers
for n in range(1, 1000):
	triangles.append(int(0.5*n*(n+1)))

#read the provided txt file and clean it appropriately
cleanWords = []
with open('words.txt') as f:
	content = f.readlines()
fileString = content[0]
listString = fileString.split(',')
for word in listString:
	cleanWord = word.split('"')
	cleanWords.append(cleanWord[1])

#iterate the clean word list, compute the character value sums, and check if it exists in the triangle list
for word in cleanWords:
	charValue = 0
	for char in word:
		charValue = charValue + charValues[char]
	if charValue in triangles:
		triangleWords.append(word)

print(len(triangleWords))