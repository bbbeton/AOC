with open("aoc15-16.txt") as file_input:
    file = file_input.read().splitlines()

def count_code(table):
    code_length = 0
    for line in table:
        line.replace(' ','')
        code_length += len(line)
    return code_length


def strip_line(string):
    actual_length = len(string) - 2
    i = 0
    while i < len(string):
        if string[i] == '\\':
            if string[i+1] == 'x':
                actual_length -= 3
                i += 3
            elif string[i+1] == '\\':
                actual_length -= 1
                i += 1
            elif string[i+1] == '"':
                actual_length -= 1
                i += 1
        i += 1
    return actual_length


def count_characters(table):
    characters_length = 0
    for line in table:
        characters_length += strip_line(line)
    return characters_length

print(count_code(file) - count_characters(file))
print(count_code(file))
print(count_characters(file))