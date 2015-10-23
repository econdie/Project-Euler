def checkPrime(n):
    if all(n%m != 0 for m in range(2, int(math.sqrt(n))+1)):
        return True
    else:
        return False

import math
answers = []

for i in range(2, 1000000):
    if checkPrime(i):
        if len(str(i)) == 1:
            answers.append(i)
        elif len(str(i)) == 2:
            tempList = list(str(i))
            tempNum = int(tempList[1] + tempList[0])
            if checkPrime(tempNum):
                answers.append(i)
            else:
               pass
        elif len(str(i)) == 3:
            tempList = list(str(i))
            tempNum1 = int(tempList[2] + tempList[0] + tempList[1])
            tempNum2 = int(tempList[1] + tempList[2] + tempList[0])
            if checkPrime(tempNum1) & checkPrime(tempNum2):
                answers.append(i)
            else:
                pass
        elif len(str(i)) == 4:
            tempList = list(str(i))
            tempNum1 = int(tempList[3] + tempList[0] + tempList[1] + tempList[2])
            tempNum2 = int(tempList[2] + tempList[3] + tempList[0] + tempList[1])
            tempNum3 = int(tempList[1] + tempList[2] + tempList[3] + tempList[0])
            if checkPrime(tempNum1) & checkPrime(tempNum2) & checkPrime(tempNum3):
                answers.append(i)
            else:
                pass
        elif len(str(i)) == 5:
            tempList = list(str(i))
            tempNum1 = int(tempList[4] + tempList[0] + tempList[1] + tempList[2] + tempList[3])
            tempNum2 = int(tempList[3] + tempList[4] + tempList[0] + tempList[1] + tempList[2])
            tempNum3 = int(tempList[2] + tempList[3] + tempList[4] + tempList[0] + tempList[1])
            tempNum4 = int(tempList[1] + tempList[2] + tempList[3] + tempList[4] + tempList[0])
            if checkPrime(tempNum1) & checkPrime(tempNum2) & checkPrime(tempNum3) & checkPrime(tempNum4):
                answers.append(i)
            else:
                pass
        elif len(str(i)) == 6:
            tempList = list(str(i))
            tempNum1 = int(tempList[5] + tempList[0] + tempList[1] + tempList[2] + tempList[3] + tempList[4])
            tempNum2 = int(tempList[4] + tempList[5] + tempList[0] + tempList[1] + tempList[2] + tempList[3])
            tempNum3 = int(tempList[3] + tempList[4] + tempList[5] + tempList[0] + tempList[1] + tempList[2])
            tempNum4 = int(tempList[2] + tempList[3] + tempList[4] + tempList[5] + tempList[0] + tempList[1])
            tempNum5 = int(tempList[1] + tempList[2] + tempList[3] + tempList[4] + tempList[5] + tempList[0])
            if checkPrime(tempNum1) & checkPrime(tempNum2) & checkPrime(tempNum3) & checkPrime(tempNum4) & checkPrime(tempNum5):
                answers.append(i)
            else:
                pass
    else:
        pass

    
    
print(len(answers))


        
