with open("input day16", 'r') as file:
    for line in file:
        input = line.removesuffix("\n")

binaryInput =bin(int(input, 16))[2:]
binaryInput = '0'*(len(input)*4 - len(binaryInput)) + binaryInput

def getVersion(binair):
    return int(binair[:3], 2)

def getTypeID(binair):
    return int(binair[3:6], 2)

def getLengthTypeID(binair):
    return int(binair[6], 2)

def getLength(binair):
    return int(binair[7:7+15], 2)

def getNumberOfSubPackets(binair):
    return int(binair[7:7+11], 2)

def getSubPacket(binair, number):
    return binair[18 + (number*11):29 + (number*11)]

def getOutput(binair):
    values = ""
    i = 6
    print("Version:", getVersion(binair))
    print("TypeID:", getTypeID(binair))
    if getTypeID(binair) == 4:
        while binair[i] != '0':
            values += binair[i+1:i+5]
            i += 5
        values += binair[i+1:i+5]
    else:
        if getLengthTypeID(binair) == 0:
            print("length:", getLength(binair))
            print("10:", )
            print("20:", )
        else:
            number = getNumberOfSubPackets(binair)
            print("sub-packets:", number)
            subPackets = []
            for i in range(number):
                subPackets.append(getSubPacket(binair, i))
            for packet in subPackets:
                print(packet)
                getOutput(packet)
            


    return values

print(binaryInput)
print(getOutput(binaryInput))
