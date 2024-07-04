pairs = []
inserts = []
with open("input day14", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        if " -> " in line:
            pair, insert = line.split(" -> ")
            pairs.append(pair)
            inserts.append(insert)
        elif line != '':
            input = line

def insertPairs(input, pairs, inserts):
    new_input = input
    for i in range(len(input)-1):
        index = pairs.index(input[i:i+2])
        toInsert = inserts[index]
        new_input = new_input[:(i*2)+1] + toInsert + new_input[(i*2)+1:]
    return new_input

for time in range(10):
    input = insertPairs(input, pairs, inserts)

data = []
count = []
for c in input:
    if c not in data:
        data.append(c)
        count.append(0)
    index = data.index(c)
    count[index]+=1

print(max(count) - min(count))

#Part 2
pairs = []
inserts = []
with open("input day14", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        if " -> " in line:
            pair, insert = line.split(" -> ")
            pairs.append(pair)
            inserts.append(insert)
        elif line != '':
            input = line
            
inputPairs = []
amount = []
for i in range(len(input)-1):
    pair = input[i:i+2]
    if pair not in inputPairs:
        inputPairs.append(pair)
        amount.append(1)
    else:
        index = inputPairs.index(pair)
        amount[index] += 1

def insertPairs(inputPairs, amount, pairs, inserts):
    newInputPairs = inputPairs.copy()
    newAmount = [0] * len(amount)
    for i in range(len(inputPairs)):
        index = pairs.index(inputPairs[i])
        toInsert = inserts[index]
        newPairs = [inputPairs[i][0] + toInsert, toInsert + inputPairs[i][1]]
        for pair in newPairs:
            if pair not in newInputPairs:
                newInputPairs.append(pair)
                newAmount.append(amount[inputPairs.index(inputPairs[i])])
            else:
                index = newInputPairs.index(pair)
                newAmount[index] += amount[inputPairs.index(inputPairs[i])]
    return newInputPairs, newAmount

for time in range(40):
    print(time)
    inputPairs, amount = insertPairs(inputPairs, amount, pairs, inserts)
    
data = []
count = []
for pair in inputPairs:
    for c in pair:
        if c not in data:
            data.append(c)
            count.append(0)
        index = data.index(c)
        count[index]+=amount[inputPairs.index(pair)]

for i in range(len(count)):
    if data[i] == input[0] or data[i] == input[-1]:
        count[i] += 1
    count[i] = int(count[i] / 2)

print(data, count)
print(max(count) - min(count))