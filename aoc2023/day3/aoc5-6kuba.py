with open('aoc5-6.txt') as file_input:

    file = file_input.read().splitlines()
    

def is_wanted_char(char):
    #check if char is number or is . (dot)
    if char.isdigit() or ord(char) == 46:
        return False
    return True


def check_adjacents(i, j):
    #top
    try:
        if i != 0:
            result = is_wanted_char(file[i-1][j])
            if result:
                return True
    except Exception:
        pass
    
    #bottom
    try:
        result = is_wanted_char(file[i+1][j])
        if result:
            return True
    except Exception:
        pass
    
    #left
    try:
        if j != 0:
            result = is_wanted_char(file[i][j-1])
            if result:
                return True
    except Exception:
        pass

    #right
    try:
        result = is_wanted_char(file[i][j+1])
        if result:
            return True
    except Exception:
        pass

    #top-right
    try:
        if i != 0:
            result = is_wanted_char(file[i-1][j+1])
            if result:
                return True
    except Exception:
        pass

    #top-left
    try:
        if i != 0 or j != 0:
            result = is_wanted_char(file[i-1][j-1])
            if result:
                return True
    except Exception:
        pass

    #bottom-right
    try:
        result = is_wanted_char(file[i+1][j+1])
        if result:
            return True
    except Exception:
        pass

    #bottom-left
    try:
        if j != 0:
            result = is_wanted_char(file[i+1][j-1])
            if result:
                return True
    except Exception:
        pass

    return False

sum = 0
for i in range(len(file)):
    number = ''
    is_number = False
    is_adjacent = False

    for j in range(len(file[i])):
        if file[i][j].isdigit():
            number += file[i][j]
            is_number = True
            if check_adjacents(i,j):
                is_adjacent = True
        else:
            is_number = False

        if is_number == False or j == len(file[i])-1:   
            if is_adjacent:
                print(number)
                sum += int(number)
                is_adjacent = False
            number = ''
        
print(f"Sum: {sum}")