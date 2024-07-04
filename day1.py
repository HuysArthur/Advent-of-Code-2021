array = []
with open("input day1", 'r') as file:
    for row in file:
        array.append(int(row))
        
result = 0
previous = []
current = []
for value in array:
    current.append(value)
    if len(previous) == 3:
        if sum(current) > sum(previous):
            result += 1

    previous = current.copy()
    if len(current) == 3:
        current.remove(current[0])
        
print(result)