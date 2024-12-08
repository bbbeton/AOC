from aoc1 import makeArrays

with open ("aoc1-2.txt") as file_input:
    file = file_input.read().splitlines()

def countNoInstances(leftArray, rightArray):
    similarityScore = 0
    for i in range(len(leftArray)):
        instances = rightArray.count(leftArray[i])
        similarityScore += leftArray[i] * instances
    return similarityScore
    

if __name__ == "__main__":
    print(countNoInstances(makeArrays(file)[0], makeArrays(file)[1]))