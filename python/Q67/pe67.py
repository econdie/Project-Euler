def compareSum(lines, rowNumber, rowPosition):
    sumA = int(lines[rowNumber][rowPosition]) + int(lines[rowNumber-1][rowPosition])
    sumB = int(lines[rowNumber][rowPosition+1]) + int(lines[rowNumber-1][rowPosition])

    if sumA >= sumB:
        lines[rowNumber-1][rowPosition] = sumA
    else:
        lines[rowNumber-1][rowPosition] = sumB

file = open('S:\Python34\Code\pe67.txt', 'r')
lines = []
for i in range(0, 100):
    lines.append(str.split(file.readline()))

#j'th row
for j in reversed(range(0,len(lines))):
    #k'th column
    for k in range(0, len(lines[j])-1):
        compareSum(lines, j, k)

print(lines[0][0])

