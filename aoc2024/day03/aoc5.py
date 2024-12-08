import re

with open("aoc5-6.txt") as file_input:
    file = file_input.read()

def findMulInstructions(textFile):
    pattern = "mul\(\d+,\d+\)"
    instructions = re.findall(pattern, textFile)
    return instructions

def getNumbers(mul):
    numbers = mul.split(',')
    for i in range(len(numbers)):
        numbers[i] = int(re.sub("\D", "", numbers[i]))
    return numbers

def multiplyScore(instructions):
    scoreSum = 0
    for i in range(len(instructions)):
        numbers = getNumbers(instructions[i])
        scoreSum += numbers[0] * numbers[1]
    return scoreSum

if __name__ == "__main__":
    print(multiplyScore(findMulInstructions(file)))