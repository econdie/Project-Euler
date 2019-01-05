def getDigitSum(i):
    digitAsString = str(i)
    digitSum = 0
    for j in range(0, len(digitAsString)):
        digitSum = digitSum + int(digitAsString[j])**5
    return digitSum

def checkEquality(i, currentDigitSum):
    return i == currentDigitSum
        
answers = []

#max possible number is (9^5)*6
for i in range(2, (9**5)*6):
    digitSum = getDigitSum(i)
    if checkEquality(i, digitSum) == True:
        answers.append(i)
    
    print(i)
    

print(answers)
