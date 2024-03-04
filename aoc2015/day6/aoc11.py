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