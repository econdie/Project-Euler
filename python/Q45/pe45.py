answer = -3

triangles = [0]
pentagons = [0]
hexagons = [0]

for n in range(1, 100000):
	triangles.append(n*(n+1)/2)
	pentagons.append(n*((3*n)-1)/2)
	hexagons.append(n*((2*n)-1))

for triangle in triangles:
	if triangle > 40755:
		if triangle in pentagons and triangle in hexagons:
			answer = triangle
			break

print(answer)