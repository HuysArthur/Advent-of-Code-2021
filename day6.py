import timeit
fishes = []
with open("input day6", 'r') as file:
    for row in file:
        fishes = row.split(',')
        for i in range(len(fishes)):
            fishes[i] = int(fishes[i])

def nextDay(fishes):
    newFishes = []
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            newFishes.append(8)
        else:
            fishes[i] -= 1
    return fishes + newFishes

start = timeit.default_timer()
for i in range(80):
    fishes = nextDay(fishes)
stop = timeit.default_timer()
print("Part1:", len(fishes))
print(f'Time: ', stop - start)

#Part 2
fishes = []
with open("input day6", 'r') as file:
    for row in file:
        fishes = row.split(',')
        for i in range(len(fishes)):
            fishes[i] = int(fishes[i])

data = []
for i in range(9):
    data.append(0)

for fish in fishes:
    data[fish] += 1
print(data)

def nextDay(fishes):
    temp = fishes[0]
    for i in range(1, len(fishes)):
        fishes[i-1] = fishes[i]
    fishes[6] += temp
    fishes[8] = temp
    return fishes

start = timeit.default_timer()
for i in range(256):
    data = nextDay(data)
stop = timeit.default_timer()
print("Part2:", sum(data))
print(f'Time: ', stop - start)
