import numpy as np
from numpy.testing._private.utils import jiffies
X = []
Y = []
with open("input day13", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        if ',' in line:
            x, y = line.split(',')
            X.append(int(x))
            Y.append(int(y))

array = np.zeros((max(Y)+1, max(X)+1), dtype=bool)
#array = np.zeros((894+1, 1330+1), dtype=bool)
for i in range(len(X)):
    array[Y[i]][X[i]] = True

def mirrorVertical(array):
    mirrored = np.zeros(array.shape, dtype=bool)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            mirrored[i][array.shape[1]-1-j] = array[i][j]
    return mirrored

def foldVertical(array, x):
    left = array[:, :x]
    right = array[:, x+1:]
    mirroredRight = mirrorVertical(right)
    for i in range(left.shape[0]):
        for j in range(left.shape[1]):
            if mirroredRight[i][j]:
                left[i][j] = True
    return left

def mirrorHorizontal(array):
    mirrored = np.zeros(array.shape, dtype=bool)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            mirrored[array.shape[0]-1-i][j] = array[i][j]
    return mirrored

def foldHorizontal(array, x):
    top = array[:x, :]
    bottom = array[x+1:, :]
    mirroredBottom = mirrorHorizontal(bottom)
    for i in range(top.shape[0]):
        for j in range(top.shape[1]):
            if mirroredBottom[i][j]:
                top[i][j] = True
    return top

def countDots(array):
    count = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i][j]:
                count += 1
    return count

afterFold = foldVertical(array, 655)
afterFold = foldHorizontal(afterFold, 447)
afterFold = foldVertical(afterFold, 327)
afterFold = foldHorizontal(afterFold, 223)
afterFold = foldVertical(afterFold, 163)
afterFold = foldHorizontal(afterFold, 111)
afterFold = foldVertical(afterFold, 81)
afterFold = foldHorizontal(afterFold, 55)
afterFold = foldVertical(afterFold, 40)
afterFold = foldHorizontal(afterFold, 27)
afterFold = foldHorizontal(afterFold, 13)
afterFold = foldHorizontal(afterFold, 6)
print(afterFold)
print(format(countDots(afterFold), "b"))

import matplotlib.pyplot as plt
plt.imshow(afterFold)
plt.show()