def checkPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False
    

palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if(checkPalindrome(i*j)):
            palindromes.append(i*j)


palindromes.sort()

print (palindromes[-1])


        
