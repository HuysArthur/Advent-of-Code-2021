import numpy as np
from numpy.core.fromnumeric import reshape

array = []
header = []
board = []
with open("input day4", 'r') as file:
    for row in file:
        line = row.removesuffix("\n").strip()
        if len(header) == 0:
            while line.find(',') != -1:
                header.append(int(line[:line.index(',')]))
                line = line[line.index(',')+1:]
        elif line != "":
            r = []
            while line.find(' ') != -1:
                r.append(int(line[:line.index(' ')]))
                line = line[line.index(' ')+1:].strip()
            r.append(int(line))
            board.append(r)
        else:
            if len(board)!=0:
                array.append([board, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]])
                board = []
    array.append([board, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]])

found = False
for number in header:
    if found:
        print(result)
        break

    for board in array:
        for i in range(len(board[0])):
            for j in range(len(board[0][0])):
                if board[0][i][j] == number:
                    board[1][i][j] = 1

    for board in array:
        # Check row for bingo
        for i in range(len(board[1])):
            bingo = True
            for j in range(len(board[1][0])):
                if board[1][i][j] != 1:
                    bingo = False
            if bingo == True:
                numbers = []
                for i in range(len(board[1])):
                    for j in range(len(board[1][0])):
                        if board[1][i][j] == 0:
                            numbers.append(board[0][i][j])

                result = sum(numbers) * number
                found = True

        # Check column for bingo
        for j in range(len(board[1][0])):
            bingo = True
            for i in range(len(board[1])):
                if board[1][i][j] != 1:
                    bingo = False
            if bingo == True:
                numbers = []
                for i in range(len(board[1])):
                    for j in range(len(board[1][0])):
                        if board[1][i][j] == 0:
                            numbers.append(board[0][i][j])
                        
                result = sum(numbers) * number
                found = True


#Part 2
for board in array:
    board[1] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

boardBingo = [0] * len(array)
for number in header:
    for board in array:
        for i in range(len(board[0])):
            for j in range(len(board[0][0])):
                if board[0][i][j] == number:
                    board[1][i][j] = 1

    x = 0
    for board in array:
        if boardBingo[x] == 0:
            bingo = False
            for i in range(5):
                bingo = True
                for j in range(5):
                    if board[1][i][j] != 1:
                        bingo = False
                        break
                if bingo == True:
                    numbers = []
                    for i in range(len(board[1])):
                        for j in range(len(board[1][0])):
                            if board[1][i][j] == 0:
                                numbers.append(board[0][i][j])

                    result = sum(numbers) * number
                    boardBingo[x] = 1

            # Check column for bingo
            for j in range(len(board[1][0])):
                bingo = True
                for i in range(len(board[1])):
                    if board[1][i][j] != 1:
                        bingo = False
                if bingo == True:
                    numbers = []
                    for i in range(len(board[1])):
                        for j in range(len(board[1][0])):
                            if board[1][i][j] == 0:
                                numbers.append(board[0][i][j])
                            
                    result = sum(numbers) * number
                    boardBingo[x] = 1
        x+=1
        print(board)
    
    if 0 not in boardBingo:
        print(result)
        break