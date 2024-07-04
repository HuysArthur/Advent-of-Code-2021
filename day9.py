heightmap = []
with open("input day9", 'r') as file:
    for row in file:
        row = row.removesuffix("\n")
        data = []
        for number in row:
            data.append(int(number))
        heightmap.append(data)

#heightmap = [[2,1,9,9,9,4,3,2,1,0],[3,9,8,7,8,9,4,9,2,1],[9,8,5,6,7,8,9,8,9,2],[8,7,6,7,8,9,6,7,8,9],[9,8,9,9,9,6,5,6,7,8]]

lowPointsPositions = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        valuesAround = []
        if i!=0:
            valuesAround.append(heightmap[i-1][j])
        if i!=len(heightmap)-1:
            valuesAround.append(heightmap[i+1][j])
        if j!=0:
            valuesAround.append(heightmap[i][j-1])
        if j!=len(heightmap[0])-1:
            valuesAround.append(heightmap[i][j+1])
        if heightmap[i][j]<min(valuesAround):
            lowPointsPositions.append([i, j])

lowPoints = []
for position in lowPointsPositions:
    lowPoints.append(heightmap[position[0]][position[1]])
print(sum(lowPoints)+len(lowPoints))

def positionsAroundPosition(heightmap, pos):
    positionsAround = []
    i = pos[0]
    j = pos[1]
    if i!=0:
        positionsAround.append([i-1, j])
    if i!=len(heightmap)-1:
        positionsAround.append([i+1, j])
    if j!=0:
        positionsAround.append([i, j-1])
    if j!=len(heightmap[0])-1:
        positionsAround.append([i, j+1])
    return positionsAround   
    
def convertPosArrayToNumber(heightmap, positions):
    array = []
    for pos in positions:
        array.append(heightmap[pos[0]][pos[1]])
    return array

def calculateBasinSize(heightmap, lowPos):
    size = 0
    positionsFound = []
    positionsToDo = [lowPos]
    while len(positionsToDo)!=0:
        positionsAround = positionsAroundPosition(heightmap, positionsToDo[0])
        for pos in positionsAround:
            if heightmap[pos[0]][pos[1]]!=9 and not (pos in positionsFound or pos in positionsToDo):
                positionsToDo.append(pos)
        size+=1
        positionsFound.append(positionsToDo[0])
        positionsToDo.remove(positionsToDo[0])
    return size, lowPos

basinSizes = []
basinPos = []
for lowPointPosition in lowPointsPositions:
    size, pos = calculateBasinSize(heightmap, lowPointPosition)
    basinSizes.append(size)
    basinPos.append(pos)

result = 1
for size in sorted(basinSizes)[-3:]:
    result *= size

print(result)