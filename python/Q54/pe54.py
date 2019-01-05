# Poker hands
# Problem 54 
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
#  	2C 3S 8S 8D TD
# Pair of Eights
#  	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
#  	2C 5C 7D 8S QH
# Highest card Queen
#  	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
#  	3D 6D 7D TD QD
# Flush with Diamonds
#  	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#  	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#  	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
#  	3C 3D 3S 9S 9D
# Full House
# with Three Threes
#  	Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

def GetHandValue(hand):
	flush = CheckFlush(hand)
	straight = CheckStraight(hand)
	if flush == 'Royal Flush':
		return 1
	elif flush == 'Flush' and straight == True:
		print('test')
		return 2
	elif CheckFour(hand):
		print('test')
		return 3
	elif CheckHouse(hand):
		return 4
	elif flush == 'Flush':
		return 5
	elif straight == True:
		return 6
	elif CheckThree(hand):
		return 7
	elif CheckPairs(hand):
		return 8
	elif CheckPair(hand):
		return 9
	else:
		return 10




def CheckFlush(hand):
	royal = True
	flush = False
	if hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]:
		flush = True
		for i in range(1,10):
			if hand[0][0] == str(i) or hand[1][0] == str(i) or hand[2][0] == str(i) or hand[3][0] == str(i) or hand[4][0] == str(i):
				royal = False

	else:
		royal = False

	if royal == True and flush == True:
		return 'Royal Flush'
	elif royal == False and flush == True:
		return 'Flush'
	else:
		return 'Nope'

def CheckStraight(hand):
	numberValues = []
	straight = True

	for i in range(0, 5):
		if hand[i][0] == 'T':
			numberValues.append(10)
		elif hand[i][0] == 'J':
			numberValues.append(11)
		elif hand[i][0] == 'Q':
			numberValues.append(12)
		elif hand[i][0] == 'K':
			numberValues.append(13)
		elif hand[i][0] == 'A':
			numberValues.append(14)
		else:
			numberValues.append(int(hand[i][0]))

	numberValues.sort()
	for i in range (0, 4):
		if numberValues[i] != numberValues[i+1] - 1:
			straight = False

	#since Aces are being stored as value 14, we need to explicitly check for ace to 5 straight
	if 14 in numberValues:
		if numberValues[0] == 2 and numberValues[1] == 3 and numberValues[2] == 4 and numberValues[3] == 5:
			straight = True
	return straight

def CheckFour(hand):
	count1 = 0
	count2 = 0
	for i in range(1,5):
		if hand[0][0] == hand[i][0]:
			count1 = count1 + 1
	for j in range(0,4):
		if hand[4][0] == hand[j][0]:
			count2 = count2 + 1

	if count1 == 3 or count2 == 3:
		return True
	else:
		return False

def CheckHouse(hand):
	numberValues = []

	for i in range(0, 5):
		if hand[i][0] == 'T':
			numberValues.append(10)
		elif hand[i][0] == 'J':
			numberValues.append(11)
		elif hand[i][0] == 'Q':
			numberValues.append(12)
		elif hand[i][0] == 'K':
			numberValues.append(13)
		elif hand[i][0] == 'A':
			numberValues.append(14)
		else:
			numberValues.append(int(hand[i][0]))

	numberValues.sort()
	if len(set(numberValues)) == 2:
		return True
	else:
		return False

def CheckThree(hand):
	numberValues = []

	for i in range(0, 5):
		if hand[i][0] == 'T':
			numberValues.append(10)
		elif hand[i][0] == 'J':
			numberValues.append(11)
		elif hand[i][0] == 'Q':
			numberValues.append(12)
		elif hand[i][0] == 'K':
			numberValues.append(13)
		elif hand[i][0] == 'A':
			numberValues.append(14)
		else:
			numberValues.append(int(hand[i][0]))

	numberValues.sort()
	if numberValues[0] == numberValues[1] and numberValues[1] == numberValues[2]:
		return True
	elif numberValues[1] == numberValues[2] and numberValues[2] == numberValues[3]:
		return True
	elif numberValues[2] == numberValues[3] and numberValues[3] == numberValues[4]:
		return True
	else:
		return False

def CheckPairs(hand):
	numberValues = []

	for i in range(0, 5):
		if hand[i][0] == 'T':
			numberValues.append(10)
		elif hand[i][0] == 'J':
			numberValues.append(11)
		elif hand[i][0] == 'Q':
			numberValues.append(12)
		elif hand[i][0] == 'K':
			numberValues.append(13)
		elif hand[i][0] == 'A':
			numberValues.append(14)
		else:
			numberValues.append(int(hand[i][0]))

	numberValues.sort()
	if len(set(numberValues)) == 3:
		return True
	else:
		return False

def CheckPair(hand):
	numberValues = []

	for i in range(0, 5):
		if hand[i][0] == 'T':
			numberValues.append(10)
		elif hand[i][0] == 'J':
			numberValues.append(11)
		elif hand[i][0] == 'Q':
			numberValues.append(12)
		elif hand[i][0] == 'K':
			numberValues.append(13)
		elif hand[i][0] == 'A':
			numberValues.append(14)
		else:
			numberValues.append(int(hand[i][0]))

	numberValues.sort()
	if len(set(numberValues)) == 4:
		return True
	else:
		return False

def CheckTie(hand1, hand2, reference):
	numberValues1 = []
	numberValues2 = []

	for i in range(0, 5):
		if hand1[i][0] == 'T':
			numberValues1.append(10)
		elif hand1[i][0] == 'J':
			numberValues1.append(11)
		elif hand1[i][0] == 'Q':
			numberValues1.append(12)
		elif hand1[i][0] == 'K':
			numberValues1.append(13)
		elif hand1[i][0] == 'A':
			numberValues1.append(14)
		else:
			numberValues1.append(int(hand1[i][0]))

	for i in range(0, 5):
		if hand2[i][0] == 'T':
			numberValues2.append(10)
		elif hand2[i][0] == 'J':
			numberValues2.append(11)
		elif hand2[i][0] == 'Q':
			numberValues2.append(12)
		elif hand2[i][0] == 'K':
			numberValues2.append(13)
		elif hand2[i][0] == 'A':
			numberValues2.append(14)
		else:
			numberValues2.append(int(hand2[i][0]))

	numberValues1.sort()
	numberValues2.sort()


	if reference == 2:
		if numberValues1[4] > numberValues2[4]:
			return 'p1'
		else:
			return 'p2'
	elif reference == 3:
		p1high = 0
		if numberValues1[0] == numberValues1[1]:
			p1high = numberValues1[0]
		else:
			p1high = numberValues1[1]

		p2high = 0
		if numberValues2[0] == numberValues2[1]:
			p2high = numberValues2[0]
		else:
			p2high = numberValues2[1]

		if p1high > p2high:
			return 'p1'
		else:
			return 'p2'
	elif reference == 4:
		p1high = 0
		if numberValues1[0] == numberValues1[2]:
			p1high = numberValues1[0]
		else:
			p1high = numberValues1[2]

		p2high = 0
		if numberValues2[0] == numberValues2[2]:
			p2high = numberValues2[0]
		else:
			p2high = numberValues2[2]

		if p1high > p2high:
			return 'p1'
		else:
			return 'p2'
	elif reference == 5 or reference == 6:
		print('test')
		if numberValues1[4] > numberValues2[4]:
			return 'p1'
		else:
			return 'p2'
	elif reference == 7:
		if numberValues1[2] > numberValues2[2]:
			return 'p1'
		else:
			return 'p2'
	elif reference == 8:
		print('test')
		p1High = numberValues1[3]
		p2High = numberValues2[3]
		p1Low = numberValues1[1]
		p2Low = numberValues2[1]
		# p1Card = 0
		# p2Card = 0
		# may need additional logic here
		if p1High > p2High:
			print('test')
			return 'p1'
		elif p1High == p2High:
			if p1Low > p2Low:
				print('test')
				return 'p1'
		else:
			return 'p2'
	elif reference == 9:
		p1Pair = 0
		p2Pair = 0
		if numberValues1[0] == numberValues1[1]:
			p1Pair = numberValues1[1]
		elif numberValues1[1] == numberValues1[2]:
			p1Pair = numberValues1[1]
		else:
			p1Pair = numberValues1[3]
		if numberValues2[0] == numberValues2[1]:
			p2Pair = numberValues2[1]
		elif numberValues2[1] == numberValues2[2]:
			p2Pair = numberValues2[1]
		else:
			p2Pair = numberValues2[3]

		if p1Pair > p2Pair:
			return 'p1'
		elif p1Pair < p2Pair:
			return 'p2'
		else:
			if numberValues1[4] > numberValues2[4]:
				return 'p1'
			elif numberValues1[4] < numberValues2[4]:
				return 'p2'
			elif numberValues1[3] > numberValues2[3]:
				return 'p1'
			elif numberValues1[3] < numberValues2[3]:
				return 'p2'
			elif numberValues1[2] > numberValues2[2]:
				return 'p1'
			elif numberValues1[2] < numberValues2[2]:
				return 'p2'
			elif numberValues1[1] > numberValues2[1]:
				return 'p1'
			elif numberValues1[1] < numberValues2[1]:
				return 'p2'
			elif numberValues1[0] > numberValues2[0]:
				return 'p1'
			else:
				return 'p2'
	else:
		if numberValues1[4] > numberValues2[4]:
			return 'p1'
		elif numberValues1[4] < numberValues2[4]:
			return 'p2'
		elif numberValues1[3] > numberValues2[3]:
			return 'p1'
		elif numberValues1[3] < numberValues2[3]:
			return 'p2'
		elif numberValues1[2] > numberValues2[2]:
			return 'p1'
		elif numberValues1[2] < numberValues2[2]:
			return 'p2'
		elif numberValues1[1] > numberValues2[1]:
			return 'p1'
		elif numberValues1[1] < numberValues2[1]:
			return 'p2'
		elif numberValues1[0] > numberValues2[0]:
			return 'p1'
		else:
			return 'p2'

with open('poker.txt') as f:
	content = f.readlines()

p1wins = 0
ties = 0

for hand in content:
	cards = hand.split()
	p1hand = cards[0:5]
	p2hand = cards[5:10]
	p1Value = GetHandValue(p1hand)
	p2Value = GetHandValue(p2hand)
	if p1Value < p2Value:
		p1wins = p1wins + 1
	elif p1Value == p2Value:
		tie = CheckTie(p1hand, p2hand, p1Value)
		if tie == 'p1':
			p1wins = p1wins + 1
	else:
		# print(p1hand, p2hand)
		pass
	# print(p1hand)
	# print(p2hand)
	
print(p1wins, ties)