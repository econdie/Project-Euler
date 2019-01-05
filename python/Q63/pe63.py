# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

counter = 0
for i in range(1,99):
    for j in range(1, 99):
        temp = i ** j
        if len(str(temp)) == j:
            counter = counter + 1


print(counter)