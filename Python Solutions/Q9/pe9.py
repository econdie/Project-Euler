##x^2 + y^2 = z^2
##x + y + z = 1000
##implies x^2 + y^2 = (1000-x-y)^2
##can just find a y for some 1 < x < 1000 where y^2 = (1000-x-y)^2 - (x^2)

for x in range(1, 1001):
    for y in range(x, 1000):
        if y**2 == (1000-x-y)**2-(x**2):
            print(x*y*(1000-x-y))

    
