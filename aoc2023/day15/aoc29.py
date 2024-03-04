with open('aoc29-30.txt') as file_input:
    file = file_input.read().splitlines()

elements = file[0].split(',')

def hash_algorithm(char, value):
    curr_value = int(ord(char)) + value
    curr_value *= 17
    curr_value = curr_value%256

    return curr_value

    
sum = 0
for element in elements:
    #print(element)
    value = 0
    for character in element:
        value = hash_algorithm(character, value)
    #print(value)
    sum += value
print(sum)
        
