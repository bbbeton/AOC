with open("aoc15-16.txt") as file_input:
    file = file_input.read().splitlines()

def count_code(table):
    code_length = 0
    for line in table:
        line.replace(' ','')
        code_length += len(line)
    return code_length

def recode_line(table):
    line_length = len(table) + 2
    specials = ['"', '\\']
    for i in range(len(table)):
        if table[i] in specials:
            line_length += 1
    return line_length

def count_characters(table):
    characters_length = 0
    for line in table:
        characters_length += recode_line(line)
    return characters_length

print(- count_code(file) + count_characters(file))
print(count_code(file))
print(count_characters(file))