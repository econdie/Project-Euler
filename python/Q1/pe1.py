multiples = []

for i in range(3, 1000):
    if i%3 == 0 or i%5 == 0:
        multiples.append(i)


print (sum(multiples))
