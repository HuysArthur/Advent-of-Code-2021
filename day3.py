array = []
with open("input day3", 'r') as file:
    for row in file:
        array.append(row.removesuffix("\n"))

binaryNumberGamma = ""
binaryNumberEpsilon = ""
for i in range(len(array[0])):
    count = 0
    for line in array:
        if line[i] == "1":
            count+=1
    if count > len(array)/2:
        binaryNumberGamma += "1"
        binaryNumberEpsilon += "0"
    else:
        binaryNumberGamma += "0"
        binaryNumberEpsilon += "1"

print(binaryNumberGamma, binaryNumberEpsilon)
print(int(binaryNumberGamma, 2) * int(binaryNumberEpsilon, 2))

oxygenArray = []
for line in array:
    oxygenArray.append(line)

for i in range(len(array[0])):
    countOne = 0
    countZero = 0
    for line in oxygenArray:
        if line[i] == "1":
            countOne += 1
        else:
            countZero += 1
    
    temp = []
    for line in oxygenArray:
        if countOne>=countZero:
            if line[i] == "1":
                temp.append(line)
        else:
            if line[i] == "0":
                temp.append(line)
    oxygenArray = []
    for line in temp:
        oxygenArray.append(line)

co2Array = []
for line in array:
    co2Array.append(line)

for i in range(len(array[0])):
    countOne = 0
    countZero = 0
    for line in co2Array:
        if line[i] == "1":
            countOne += 1
        else:
            countZero += 1
    
    temp = []
    if len(co2Array) != 1:
        for line in co2Array:
            if countOne<countZero:
                if line[i] == "1":
                    temp.append(line)
            else:
                if line[i] == "0":
                    temp.append(line)
        co2Array = []
        for line in temp:
            co2Array.append(line)

print(int(oxygenArray[0], 2)* int(co2Array[0], 2))
