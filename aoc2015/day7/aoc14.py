from aoc13 import old_wire

with open('aoc13-14.txt') as file_input:
    file = file_input.read().splitlines()

def read_line(string):
    line = string.split('->')
    line[0] = line[0].strip().split()
    line[1] = line[1].strip()
    return line

#print(read_line(file[54]))

def assign(input_list):
    dictionary = {}
    for i in range(len(input_list)):
        if len(input_list[i][0]) == 1 and str(input_list[i][0][0]).isdigit():
            dictionary[input_list[i][1]] = int(input_list[i][0][0])
    return dictionary

#operations: NOT ~, AND &, OR |, RSHIFT >>, LSHIFT <<
def bitwise_operation(input_list):
    if 'NOT' in input_list:
        result = ~int(input_list[1])
    elif 'AND' in input_list:
        result = int(input_list[0]) & int(input_list[2])
    elif 'OR' in input_list:
        result = int(input_list[0]) | int(input_list[2])
    elif 'RSHIFT' in input_list:
        result = int(input_list[0]) >> int(input_list[2])
    elif 'LSHIFT' in input_list:
        result = int(input_list[0]) << int(input_list[2])
    else:
        raise ValueError("Invalid bitwise operation")

    # Mask the result to keep only the least significant 32 bits
    result &= 0xFFFF

    return result

def assign_further(input_list, dictionary):
    for i in range(len(input_list)):
        
        if len(input_list[i][0]) == 2:
            
            if input_list[i][0][1] in dictionary:
                input_list[i][0][1] = dictionary[input_list[i][0][1]]
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])
            
            elif str(input_list[i][0][1]).isdigit():
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])
        
        elif len(input_list[i][0]) == 3:
            
            if input_list[i][0][0] in dictionary and input_list[i][0][2] in dictionary:
                input_list[i][0][0] = dictionary[input_list[i][0][0]]
                input_list[i][0][2] = dictionary[input_list[i][0][2]]
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])
            
            elif input_list[i][0][0] in dictionary and str(input_list[i][0][2]).isdigit():
                input_list[i][0][0] = dictionary[input_list[i][0][0]]
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])

            elif str(input_list[i][0][0]).isdigit() and input_list[i][0][2] in dictionary:
                input_list[i][0][2] = dictionary[input_list[i][0][2]]
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])

            elif str(input_list[i][0][0]).isdigit() and str(input_list[i][0][2]).isdigit():
                dictionary[input_list[i][1]] = bitwise_operation(input_list[i][0])

        elif len(input_list[i][0]) == 1:
            
            if input_list[i][0][0] in dictionary:
                dictionary[input_list[i][1]] = dictionary[input_list[i][0][0]]
                
        
    return(dictionary)
    

def change_instructions(instructions, value):
    for i in range(len(instructions)):
        if len(instructions[i][0]) == 1 and instructions[i][1] == 'b':
            instructions[i][0][0] = value
            #print(value, instructions[i][0][0])
    return instructions

if __name__ == '__main__':
    instructions = []
    for i in range(len(file)):
        instructions.append(read_line(file[i]))
    
    new_instructions = change_instructions(instructions, 16076)
    #print(new_instructions)
    wires = assign(new_instructions)
    while 'a' not in wires:
        new_wires = assign_further(instructions, wires)
        wires = new_wires
    
    print(wires['a'])
