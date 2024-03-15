with open('aoc13-14.txt') as file_input:
    file = file_input.read().splitlines()

def read_line(string):
    line = string.split('->')
    line[0] = line[0].strip().split()
    line[1] = line[1].strip()
    return line

print(read_line(file[54]))

def assign(list):
    dict = {}
    for i in range(len(list)):
        if len(list[i][0]) == 1 and list[i][0][0].isdigit():
            dict[list[i][1]] = list[i][0][0]
    return dict

if __name__ == '__main__':
    instructions = []
    for i in range(len(file)):
        instructions.append(read_line(file[i]))
    wires = assign(instructions)
    print(wires)
    
