with open('aoc13-14.txt') as file_input:
    file = file_input.read().splitlines()

def read_line(string):
    line = string.split('->')
    line[0] = line[0].strip().split()
    line[1] = line[1].strip()
    return line

print(read_line(file[54]))

def assign(input_list):
    dict = {}
    for i in range(len(input_list)):
        if len(input_list[i][0]) == 1 and input_list[i][0][0].isdigit():
            dict[input_list[i][1]] = int(input_list[i][0][0])
    return dict

#operations: NOT ~, AND &, OR |, RSHIFT >>, LSHIFT <<
def bitwise_operation(input_list):
    if 'NOT' in input_list:
        return ~ int(input_list[1])
    elif 'AND' in input_list:
        return int(input_list[0]) & int(input_list[2])
    elif 'OR' in input_list:
        return int(input_list[0]) | int(input_list[2])
    elif 'RSHIFT' in input_list:
        return int(input_list[0]) >> int(input_list[2])
    elif 'LSHIFT' in input_list:
        return int(input_list[0]) << int(input_list[2])
    else:
        raise ValueError("Invalid bitwise operation")

def assign_further(input_list, dict):
    for i in range(len(input_list)):
        

if __name__ == '__main__':
    instructions = []
    for i in range(len(file)):
        instructions.append(read_line(file[i]))
    wires = assign(instructions)
    print(wires)
    
