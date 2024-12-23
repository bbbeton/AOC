with open("aoc9-10.txt") as file_input:
    file = file_input.read().splitlines()

def getInstructions(textFile):
    i = 0
    instructions = []
    while textFile[i]:
        instructions.append(textFile[i].split('|'))
        i += 1
    return instructions

def getUpdates(textFile):
    i = 0
    while textFile[i]:
        i += 1
    updates = []

if __name__ == "__main__":
    print(getInstructions(file))