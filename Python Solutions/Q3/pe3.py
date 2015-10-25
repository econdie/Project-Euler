import math

answer = 0

for i in range(3, 600851475143):
    if 600851475143%i == 0:
        if all((600851475143/i)%m != 0 for m in range(2, int(math.sqrt(600851475143/i))+1)):
            answer = int(600851475143/i)
            break
    
print(answer)
    
#test