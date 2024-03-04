with open('aoc5-6.txt') as f:
    file = f.read().splitlines()


def get_number(i, j):
    left = ''
    right = ''
    x = j - 1
    try:
        while file[i][x].isdigit() and x != -1:
            left += file[i][x]
            x-=1
    except Exception:
        pass

    x = j + 1

    try:
        while file[i][x].isdigit() and x != len(file[i]):
            right += file[i][x]
            x += 1
    except Exception:
        pass

    result = left[::-1] + file[i][j] + right
    return result
   

def get_gear_ratio(i, j):
    top_no = False
    bottom_no = False

    gears = []
    #top
    try:
        if i != 0:
            if file[i-1][j].isdigit():
                gears.append([i-1, j])
                top_no = True
    except Exception:
        pass
    
    #bottom
    try:
        if file[i+1][j].isdigit():
            gears.append([i+1, j])
            bottom_no = True
    except Exception:
        pass
    
    #left
    try:
        if j != 0:
            if file[i][j-1].isdigit():
                gears.append([i, j-1])
    except Exception:
        pass

    #right
    try:
        if file[i][j+1].isdigit():
            gears.append([i, j+1])
    except Exception:
        pass

    #top-right
    try:
        if i != 0 and top_no is False:
            if file[i-1][j+1].isdigit():
                gears.append([i-1, j+1])
    except Exception:
        pass

    #top-left
    try:
        if (i != 0 or j != 0) and top_no is False:
            if file[i-1][j-1].isdigit():
                gears.append([i-1, j-1])
    except Exception:
        pass

    #bottom-right
    try:
        if file[i+1][j+1].isdigit() and bottom_no is False:
            gears.append([i+1, j+1])
    except Exception:
        pass

    #bottom-left
    try:
        if j != 0 and bottom_no is False:
            if file[i+1][j-1].isdigit():
                gears.append([i+1, j-1])
    except Exception:
        pass

    if len(gears) == 2:
        n1 = get_number(gears[0][0], gears[0][1])
        n2 = get_number(gears[1][0], gears[1][1])
        print(n1, n2)

        return int(n1) * int(n2) 
        
    return 0


sum = 0
for i in range(len(file)):
    for j in range(len(file[i])):
        char = file[i][j]
        if file[i][j] == "*":
            gear_ratio = get_gear_ratio(i,j)
            sum += gear_ratio

print(f"Sum: {sum}")