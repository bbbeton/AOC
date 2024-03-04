with open("aoc19-20.txt") as file_input:
    file = file_input.read().splitlines()


def find_start(char):
    for i in range(len(char)):
        for j in range(len(char[i])):
            if char[i][j] == 'S':
                index = [i , j]
                break
        try:
            if index:
                break
        except Exception:
            pass
    return index

def go_right(i, j):
    if file[i,j+1] == '-' and j != len(file[i]) - 1:
        j += 1
    elif file[i,j+1] == 'J' and j != len(file[i]) - 1 and i != len(file) - 1:
        i += 1 
        j += 1
    elif file[i,j+1] == '7' and j != len(file[i]) - 1 and i != 0:
        i -= 1
        j += 1
    return [i,j]

def go_left(i, j):
    if file[i,j-1] == '-' and j != 0:
        j -= 1
    elif file[i,j-1] == 'L' and j != 0:
        i += 1
        j -= 1 
    elif file[i,j-1] == 'F' and j != 0:
        i -= 1
        j -= 1
    return [i, j]

def go_down(i, j):
    if file[i+1, j] == '|' and i != len(file) - 1:
        i += 1
    elif file[i + 1, j] == 'J' and j != 0 and i != len(file) - 1:
        i += 1 
         

    

if __name__ == "__main__":
    line = find_start(file)[0]
    column = find_start(file)[1]

