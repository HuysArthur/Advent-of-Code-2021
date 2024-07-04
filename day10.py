codeLines = []
with open("input day10", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        codeLines.append(line)

#codeLines = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","{([(<{}[<>[]}>{[]{[(<()>","(((({<>}<{<{<>}{[]{[]{}","[[<[([]))<([[{}[[()]]]","[{[{({}]{}}([{[{{{}}([]","{<[[]]>}<{[{[{[]{()[[[]","[<(<(<(<{}))><([]([]()","<{([([[(<>()){}]>(<<{{","<{([{{}}[<[[[<>{}]]]>[]]"]

def checkSyntax(line):
    openCharacters = ['(', '[', '{', '<']
    closeCharacters = [')', ']', '}', '>']

    openChars = ''
    for i in range(len(line)):
        if line[i] in closeCharacters:
            if openChars == '':
                return line[i]
            if line[i] != closeCharacters[openCharacters.index(openChars[-1])]:
                return line[i]
            else:
                openChars = openChars[:-1]
        elif line[i] in openCharacters:
            openChars += line[i]
    return ''

values = {
    '':0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

result = 0
for codeLine in codeLines:
    #print(values[checkSyntax(codeLine)])
    result += values[checkSyntax(codeLine)]
print(result)

def stringToCompleteCodeLine(line):
    openCharacters = ['(', '[', '{', '<']
    closeCharacters = [')', ']', '}', '>']

    openChars = ''
    for i in range(len(line)):
        if line[i] in closeCharacters:
            openChars = openChars[:-1]
        elif line[i] in openCharacters:
            openChars += line[i]
    openChars = ''.join(reversed(openChars))

    stringToComplete = ""
    for c in openChars:
        stringToComplete += closeCharacters[openCharacters.index(c)]
    return stringToComplete

values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for codeLine in codeLines:
    score = 0
    if checkSyntax(codeLine) == '':
        toComplete = stringToCompleteCodeLine(codeLine)
    
        for c in toComplete:
            score = score*5 + values[c]
        scores.append(score)

import math
print(sorted(scores)[math.ceil((len(scores)-1)/2)])