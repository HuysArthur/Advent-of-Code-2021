import copy
array = []
with open("input day15", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        row = []
        for c in line:
            row.append(int(c))
        array.append(row)

distanceSourceArray = copy.deepcopy(array)
for i in range(len(array)):
    for j in range(len(array[0])):
        if i == 0:
            if j!=0:
                distanceSourceArray[i][j] += distanceSourceArray[i][j-1]
        elif j==0:
            distanceSourceArray[i][j] += distanceSourceArray[i-1][j]
        else:
            if distanceSourceArray[i-1][j]<distanceSourceArray[i][j-1]:
                distanceSourceArray[i][j] += distanceSourceArray[i-1][j]
            else:
                distanceSourceArray[i][j] += distanceSourceArray[i][j-1]

def getAdjacent(array, pos):
    adjacent = []
    i = pos[0]
    j = pos[1]
    if i!=0:
        adjacent.append([i-1, j])
    if i!=len(array)-1:
        adjacent.append([i+1, j])
    if j!=0:
        adjacent.append([i, j-1])
    if j!=len(array[0])-1:
        adjacent.append([i, j+1])
    return adjacent

def getValue(array, pos):
    return array[pos[0]][pos[1]]

def calculateRisk(array, path):
    risk = 0
    for pos in path:
        risk += getValue(array, pos)
    return risk

pos = [len(array)-1, len(array[0])-1]
path = [pos]
while pos != [0,0]:
    adjacent = getAdjacent(distanceSourceArray, pos)
    p = adjacent[0]
    for i in range(1, len(adjacent)):
        if getValue(distanceSourceArray, p) > getValue(distanceSourceArray, adjacent[i]):
            p = adjacent[i]
    pos = p
    if pos != [0, 0]:
        path = [pos] + path

print(calculateRisk(array, path))

#Part 2

def higher(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 9:
                array[i][j] = 1
            else:
                array[i][j] += 1
    return array

import numpy as np
def expandArray(array, times):
    array = np.array(array)

    toAppend = array.copy()
    for _ in range(times):
        toAppend = higher(toAppend.copy())
        array = np.append(array, toAppend, axis=1)
    
    toAppend = array.copy()
    for _ in range(times):
        toAppend = higher(toAppend.copy())
        array = np.append(array, toAppend, axis=0)

    return array

array = expandArray(array, 4)
print(np.array(array))
distanceSourceArray = copy.deepcopy(array)
for i in range(len(array)):
    for j in range(len(array[0])):
        if i == 0:
            if j!=0:
                distanceSourceArray[i][j] += distanceSourceArray[i][j-1]
        elif j==0:
            distanceSourceArray[i][j] += distanceSourceArray[i-1][j]
        else:
            if distanceSourceArray[i-1][j]<distanceSourceArray[i][j-1]:
                distanceSourceArray[i][j] += distanceSourceArray[i-1][j]
            else:
                distanceSourceArray[i][j] += distanceSourceArray[i][j-1]

print(len(array), len(array[0]))
pos = [len(array)-1, len(array[0])-1]
path = [pos]
while pos != [0,0]:
    adjacent = getAdjacent(distanceSourceArray, pos)
    p = adjacent[0]
    for i in range(1, len(adjacent)):
        if getValue(distanceSourceArray, p) > getValue(distanceSourceArray, adjacent[i]):
            p = adjacent[i]
    pos = p
    if pos != [0, 0]:
        path = [pos] + path

print(calculateRisk(array, path))