array = []
with open("input day2", 'r') as file:
    for row in file:
        array.append(row)

horizontal = 0
depth = 0
aim = 0
for line in array:

    instruction = line[:line.index(' ')]
    value = int(line[line.index(' '):])

    if instruction == "forward":
        horizontal+=value
        depth+=aim*value
    elif instruction == "up":
        aim-=value
    elif instruction == "down":
        aim+=value

print(horizontal, depth)
print(horizontal*depth)
