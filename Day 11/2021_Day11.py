data = []
with open("input11.txt") as f:
    line = f.readline()
    while line:
        data.append([int(x) for x in line.strip('\n')])
        line = f.readline()


def addOne(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] += 1


def getElement(data, x, y):
    if x < 0 or x >= len(data):
        return -1
    if y < 0 or y >= len(data[x]):
        return -1
    return data[x][y]


def processFlashes(data):
    flashes = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] > 9:
                flashes += 1
                data[x][y] = -100000000
                eight = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
                for one in eight:
                    if getElement(data, *one) != -1:
                        data[one[0]][one[1]] += 1
    return flashes

def removeAllNegativity(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] < 0:
                data[x][y] = 0

def areYouAllZeroes(data):
    total=0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] ==0:
                total += 1
    
    return total == len(data) * len(data[0])

totalFlashes = 0
generation = 0

"""
for generation in range(100):
    addOne(data)
    flashes = processFlashes(data)
    while flashes > 0:
        totalFlashes += flashes
        flashes = processFlashes(data)
    removeAllNegativity(data)

"""
print("Part 1 : " + str(totalFlashes))

# print the matrix
def printMatrix(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            print(data[x][y], end="")
        print("")

while True:
    generation +=1
    addOne(data)
    printMatrix(data)
    print("??????????")
    flashes = processFlashes(data)
    while flashes > 0:
        totalFlashes += flashes
        flashes = processFlashes(data)
    removeAllNegativity(data)
    if areYouAllZeroes(data):
        print("Part 2 : " + str(generation))
        break
