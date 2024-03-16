with open("aoc15-16.txt") as file_input:
    file = file_input.read().splitlines()

def count_code(table):
    code_length = 0
    for line in table:
        line.replace(' ','')
        code_length += len(line)
    return code_length

print(count_code(file))