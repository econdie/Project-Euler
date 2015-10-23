import math

def calcTwoDig(factorials, answers):
    for i in range(1, 5):
        for j in range(0, 5):
            if factorials[i] + factorials[j] == int(str(i) + str(j)):
                answers.append(factorials[i] + factorials[j])
            else:
                pass

def calcThreeDig(factorials, answers):
    for i in range(1, 7):
        for j in range(0, 7):
            for k in range(0, 7):
                if factorials[i] + factorials[j] + factorials[k] == int(str(i) + str(j) + str(k)):
                    answers.append(factorials[i] + factorials[j] + factorials[k])
                else:
                    pass

def calcFourDig(factorials, answers):
    for i in range(1, 8):
        for j in range(0, 8):
            for k in range(0, 8):
                for l in range(0,8):
                    if factorials[i] + factorials[j] + factorials[k] + factorials[l] == int(str(i) + str(j) + str(k) + str(l)):
                        answers.append(factorials[i] + factorials[j] + factorials[k] + factorials[l])
                    else:
                        pass
    
def calcFiveDig(factorials, answers):
    for i in range(1, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                for l in range(0, 9):
                    for m in range(0, 9):
                        if factorials[i] + factorials[j] + factorials[k] + factorials[l] + factorials[m] == int(str(i) + str(j) + str(k) + str(l) + str(m)):
                            answers.append(factorials[i] + factorials[j] + factorials[k] + factorials[l] + factorials[m])
                        else:
                            pass
            
        
    

factorials = [math.factorial(0), math.factorial(1), math.factorial(2), math.factorial(3), math.factorial(4), math.factorial(5), math.factorial(6), math.factorial(7), math.factorial(8), math.factorial(9)]
answers = []

calcTwoDig(factorials, answers)
calcThreeDig(factorials, answers)
calcFourDig(factorials, answers)
calcFiveDig(factorials, answers)

print(sum(answers))
