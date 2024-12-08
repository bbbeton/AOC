import re
from aoc5 import getNumbers

with open("aoc5-6.txt") as file_input:
    file = file_input.read()

def findMulInstructions(textFile):
    pattern = "(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don[']t\(\))"
    instructions = re.findall(pattern, textFile)
    return list(filter(None, instructions))

def sumMul(instructions):
    do = True
    sumElements = 0
    for i in range(len(instructions)):
        if instructions[i] == "do()": 
            do = True
        elif instructions[i] == "don't()":
            do = False
        elif do:
            numbers = getNumbers(instructions[i])
            sumElements += numbers[0] * numbers[1]
    return sumElements

if __name__ == "__main__":
    instructions = findMulInstructions(file)
    print(instructions)
    result = sumMul(instructions)
    print(result)