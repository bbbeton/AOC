with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def read_commend(char):
    i = 0
    commend = ''
    while not char[i].isdigit():
        commend += char[i]
        i += 1
    return(commend.rstrip())

print(read_commend(file[0]))

def create_table():
    lights = []
    for i in range(0,999):
        lights.append([])
        for j in range(0,999):
            lights[i].append(0)
    return lights

print(create_table())