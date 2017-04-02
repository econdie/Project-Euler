target = 200
coinValues = [1, 2, 5, 10, 20, 50, 100, 200]

##1a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200
##equivalent to saying how many ways to arrange 2, 5, 10, 20, 50, 100, and 200 value coins to be
##less than 200 total since we can always fill the remainder with 1 value coin
solutions = []

for h in range(0,2):
    for g in range(0,3):
        for f in range(0, 5):
            for e in range(0, 11):
                for d in range(0, 21):
                    for c in range(0, 41):
                        for b in range(0, 101):
                            if 2*b + 5*(c + 2*d + 4*e + 10*f + 20*g + 40*h) <= 200:
                                solutions.append(True)
                            

print(len(solutions))
