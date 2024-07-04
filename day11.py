squidArray = []
with open("input day11", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        squidRow = []
        for squid in line:
            squidRow.append(int(squid))
        squidArray.append(squidRow)

def getAdjacent(squidArray, pos):
    adjacent = []
    i = pos[0]
    j = pos[1]
    if i!=0:
        if j!=0:
            adjacent.append([i-1, j-1])
        if j!=len(squidArray[0])-1:
            adjacent.append([i-1, j+1])
        adjacent.append([i-1, j])
    if i!=len(squidArray)-1:
        if j!=0:
            adjacent.append([i+1, j-1])
        if j!=len(squidArray[0])-1:
            adjacent.append([i+1, j+1])
        adjacent.append([i+1, j])
    if j!=0:
        adjacent.append([i, j-1])
    if j!=len(squidArray[0])-1:
        adjacent.append([i, j+1])
    return adjacent   

def flash(squidArray, position):
    adjacent = getAdjacent(squidArray, position)
    for pos in adjacent:
        squidArray[pos[0]][pos[1]] += 1
    return squidArray

def getFlashPosition(squidArray):
    for i in range(len(squidArray)):
        for j in range(len(squidArray[0])):
            if squidArray[i][j] > 9:
                return [i, j]
    return None

flashes = 0
step = 0
done = []
while len(done)!=(len(squidArray)*len(squidArray[0])):
    for i in range(len(squidArray)):
        for j in range(len(squidArray[0])):
            squidArray[i][j]+=1
    
    done = [] 
    while getFlashPosition(squidArray) != None:
        flashes+=1
        position = getFlashPosition(squidArray)
        squidArray = flash(squidArray, position)
        done.append(position)
        for pos in done:
            squidArray[pos[0]][pos[1]] = 0
    step+=1

print(step)