with open("aoc7-8.txt") as file_input:
    file = file_input.read().splitlines()

def countLine(line):
    return line.count('XMAS') + line.count('SAMX')

if __name__ == "__main__":
    print(countLine(file[4]))