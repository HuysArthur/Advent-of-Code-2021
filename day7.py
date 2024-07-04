with open("input day7", 'r') as file:
    for row in file:
        crabPositions = row.split(',')
        for i in range(len(crabPositions)):
            crabPositions[i] = int(crabPositions[i])

def fuelRequiredToMove(position, moveTo):
    fuelUsed = 0
    fuelcost = 1
    for i in range(0, abs(position-moveTo)):
        fuelUsed += fuelcost
        fuelcost += 1
    return fuelUsed


totalFuel = [0] * max(crabPositions)
for i in range(max(crabPositions)):
    print(i, max(crabPositions)-1)
    fuel = 0
    for pos in crabPositions:
        fuel += fuelRequiredToMove(pos, i)
    totalFuel[i] = fuel

print(min(totalFuel))