import numpy as np

C1 = []
C2 = []
with open("input day5", 'r') as file:
    for row in file:
        row.removesuffix("\n")
        x1, x2 = row.split(" -> ")
        C1.append([int(x1[:x1.find(',')]), int(x1[x1.find(',')+1:])])
        C2.append([int(x2[:x2.find(',')]), int(x2[x2.find(',')+1:])])

def drawLine(field, c1, c2):
    if c1[0] == c2[0]:
        MIN = min(c1[1], c2[1])
        ABS = abs(c1[1] - c2[1])
        if c1[1] == c2[1]:
            field[c1[1]][c1[0]] += 1
        else:
            for i in range(MIN, MIN+ABS+1):
                field[i][c1[0]] += 1
    elif c1[1] == c2[1]:
        MIN = min(c1[0], c2[0])
        ABS = abs(c1[0] - c2[0])
        if c1[0] == c2[0]:
            field[c1[1]][c1[0]] += 1
        else:
            for i in range(MIN, MIN+ABS+1):
                field[c1[1]][i] += 1
    #Diagonal
    else:
        if c1[0] < c2[0]:
            if c1[1] < c2[1]:
                x = list(range(c1[0], c2[0]+1))
                y = list(range(c1[1], c2[1]+1))
                for tuple in list(zip(x, y)):
                    field[tuple[1]][tuple[0]] += 1
            else:
                x = list(range(c1[0], c2[0]+1))
                y = list(range(c2[1], c1[1]+1))
                y.reverse()
                for tuple in list(zip(x, y)):
                    field[tuple[1]][tuple[0]] += 1
        else:
            if c1[1] < c2[1]:
                x = list(range(c2[0], c1[0]+1))
                x.reverse()
                y = list(range(c1[1], c2[1]+1))
                for tuple in list(zip(x, y)):
                    field[tuple[1]][tuple[0]] += 1
            else:
                x = list(range(c2[0], c1[0]+1))
                x.reverse()
                y = list(range(c2[1], c1[1]+1))
                y.reverse()
                for tuple in list(zip(x, y)):
                    field[tuple[1]][tuple[0]] += 1
    return field

def maxSize(C):
    maxX = 0
    maxY = 0
    for c in C:
        if c[0] > maxX:
            maxX = c[0]
        if c[1] > maxY:
            maxY = c[1]
    print(maxY, maxX)
    return (maxY+1, maxX+1)


def startDrawing(C1, C2):
    field = np.zeros(maxSize(C1 + C2))
    print(field.shape)
    for i in range(len(C1)):
        drawLine(field, C1[i], C2[i])
    return field

def countOverlap(field):
    count=0
    for row in field:
        for x in row:
            if x >= 2:
                count+=1
    print(count)

field = startDrawing(C1, C2)
countOverlap(field)

import matplotlib.pyplot as plt
plt.imshow(field, cmap='hot', interpolation='nearest')
plt.show()