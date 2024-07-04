links = []
with open("input day12", 'r') as file:
    for line in file:
        line = line.removesuffix("\n")
        x, y = line.split('-')
        links.append([x, y])

def getLinkedCaves(links, cave):
    caves = []
    for link in links:
        if cave in link:
            i = abs(link.index(cave) - 1)
            caves.append(link[i])
    return caves

def pathsReachedGoal(paths, goal):
    for path in paths:
        if path[-1]!=goal:
            return False
    return True

def removeDuplicates(path):
    newPath = []
    for x in path:
        if x not in newPath:
            newPath.append(x)
    return newPath

def getAantalDuplicateLowerCases(path):
    result = 0
    for x in removeDuplicates(path):
        if x.islower():
            result += path.count(x) - 1
    return result

def getPaths(links, fromCave = "start", toCave = "end"):
    paths = [[fromCave]]
    while not pathsReachedGoal(paths, toCave):
        for p in paths[:]:
            if not pathsReachedGoal([p], toCave):
                newLinks = getLinkedCaves(links, p[-1])
                for link in newLinks:
                    if link.isupper() or (getAantalDuplicateLowerCases(p)<2 and link!=fromCave):
                        if p.count(link)<2:
                            found = True
                        paths.append(p + [link])
                paths.remove(p)
        print(len(paths))
    return paths

print(len(getPaths(links)))