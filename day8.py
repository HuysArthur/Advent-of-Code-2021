outputValues = []
signalPatterns= []
with open("input day8", 'r') as file:
    for row in file:
        row = row.removesuffix("\n")
        signal, output = row.split(" | ")
        outputValues.append(output.split(' '))
        signalPatterns.append(signal.split(' '))

result = 0
for i in range(len(outputValues)):
    outputs = outputValues[i]
    signalPattern = signalPatterns[i]
    
    for signal in signalPattern:
        if len(signal) == 2:
            one = "".join(sorted(signal))
        elif len(signal) == 3:
            seven = "".join(sorted(signal))
        elif len(signal) == 4:
            four = "".join(sorted(signal))
        elif len(signal) == 7:
            eight = "".join(sorted(signal))
    
    for signal in signalPattern:
        if len(signal) == 5:
            foundThree = True
            for c in one:
                if c not in signal:
                    foundThree = False
            if foundThree:
                three = "".join(sorted(signal))
    
    for signal in signalPattern:
        if len(signal) == 5:
            for c in four:
                if c not in three:
                    if c in signal:
                        five = "".join(sorted(signal))
                    elif "".join(sorted(signal))!=three:
                        two = "".join(sorted(signal))
    
    for signal in signalPattern:
        if len(signal) == 6:
            for c in five:
                if c not in signal:
                    zero = "".join(sorted(signal))
    
    for signal in signalPattern:
        if len(signal) == 6:
            foundNine = True
            for c in three:
                if c not in signal:
                    foundNine = False
            if foundNine:
                nine = "".join(sorted(signal))

    for signal in signalPattern:
        if "".join(sorted(signal)) not in [zero, one, two, three, four, five, seven, eight, nine]:
            six = "".join(sorted(signal))

    code = ''
    for output in outputs:
        sortedOutput = "".join(sorted(output))

        if sortedOutput==zero:
            code += '0'
        elif sortedOutput==one:
            code += '1'
        elif sortedOutput==two:
            code += '2'
        elif sortedOutput==three:
            code += '3'
        elif sortedOutput==four:
            code += '4'
        elif sortedOutput==five:
            code += '5'
        elif sortedOutput==six:
            code += '6'
        elif sortedOutput==seven:
            code += '7'
        elif sortedOutput==eight:
            code += '8'
        elif sortedOutput==nine:
            code += '9'
    print(i, code)
    result += int(code)

print(result)