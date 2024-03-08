with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def read_commend(string):
    i = 0
    commend = ''
    while not string[i].isdigit():
        commend += string[i]
        i += 1
    return(commend.rstrip())

#print(read_commend(file[0]))

def create_table():
    lights = []
    for i in range(0,999):
        lights.append([])
        for j in range(0,999):
            lights[i].append(0)
    return lights

def get_nums(string):
    nums = []
    words = string.split()
    for element in words:
        if element[0].isdigit():
            nums.append(element.split(','))
    return nums
    

print(get_nums(file[0]))