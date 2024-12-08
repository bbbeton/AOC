with open ("aoc1-2.txt") as file_input:
    file = file_input.read().splitlines()

def makeArrays(textFile):
    leftColumn = []
    rightColumn = []
    for line in textFile:
        lineNumbers = line.split()
        leftColumn.append(int(lineNumbers[0]))
        rightColumn.append(int(lineNumbers[1]))
    leftColumn.sort()
    rightColumn.sort()
    return leftColumn, rightColumn

def addDistances(leftList, rightList):
    distanceSum = 0
    for i in range(len(leftList)):
        distanceSum += abs(leftList[i] - rightList[i])
    return distanceSum

if __name__ == "__main__":
    print(addDistances(makeArrays(file)[0], makeArrays(file)[1]))
    