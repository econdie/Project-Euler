evenFibs = [2]

currentFibs = [1,2]

while currentFibs[1] < 4000000:
    nextFib = sum(currentFibs)
    if nextFib%2 == 0:
        evenFibs.append(nextFib)

    currentFibs[0] = currentFibs[1]
    currentFibs[1] = nextFib

print(sum(evenFibs))
