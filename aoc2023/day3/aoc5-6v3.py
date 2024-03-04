with open('aoc5-6.txt') as file_input:

    file = file_input.read().splitlines()

def wypisz_liczby(line):
    symbols_to_remove = '!@#$%^&*()_-+=[]><?/~\n`'
    new_line = str(line)
    for symbol in symbols_to_remove:
        if symbol in line:
            new_line = new_line.replace(symbol,'')
    x = new_line.split(".")
    liczby = list(filter(None, x))
    return liczby

def is_wanted(char):
    #sprawdza czy . albo liczba czy znak
    if char.isdigit() or ord(char) == 46:
        return False
    return True

def is_star(char):
    #sprawdza czy to gwiazdka
    if ord(char) == 42:
        return True
    return False

def is_digit(char):
    #sprawdza czy to numerek
    if char.isdigit():
        return True
    return False


def count_numbers(i, j):
    #top
    top = 0
    bottom = 0
    number = 0
    try:
        if i != 0:
            result = is_digit(file[i-1][j])
            if result:
                print('top')
                number += 1
                top +=1            
    except Exception:
        pass

    #bottom
    try:
        result = is_digit(file[i+1][j])
        if result:
            print('bottom')
            number += 1
            bottom += 1
    except Exception:
        pass

    #left
    try:
        if j != 0:
            result = is_digit(file[i][j-1])
            if result:
                print('left')
                number += 1
    except Exception:
        pass

    #right
    try:
        result = is_digit(file[i][j+1])
        if result:
            print('right')
            number += 1
    except Exception:
        pass

    #top-right
    try:
        if i != 0:
            result = is_digit(file[i-1][j+1])
            if result and top == 0:
                print('tright')
                number += 1
    except Exception:
        pass

    #top-left
    try:
        if i != 0 or j != 0:
            result = is_digit(file[i-1][j-1])
            if result and top == 0:
                print('tleft')
                number += 1
    except Exception:
        pass

    #bottom-right
    try:
        result = is_digit(file[i+1][j+1])
        if result and bottom == 0:
                print('bright')
                number += 1
    except Exception:
        pass

    #bottom-left
    try:
        if j != 0:
            result = is_digit(file[i+1][j-1])
            if result and bottom == 0:
                print('bleft')
                number += 1
    except Exception:
        pass

    return number


def check_neighbours(i, j):
    #top
    try:
        if i != 0:
            result = is_wanted(file[i-1][j])
            if result:
                return True
    except Exception:
        pass

    #bottom
    try:
        result = is_wanted(file[i+1][j])
        if result:
            return True
    except Exception:
        pass

    #left
    try:
        if j != 0:
            result = is_wanted(file[i][j-1])
            if result:
                return True
    except Exception:
        pass

    #right
    try:
        result = is_wanted(file[i][j+1])
        if result:
            return True
    except Exception:
        pass

    #top-right
    try:
        if i != 0:
            result = is_wanted(file[i-1][j+1])
            if result:
                return True
    except Exception:
        pass

    #top-left
    try:
        if i != 0 or j != 0:
            result = is_wanted(file[i-1][j-1])
            if result:
                return True
    except Exception:
        pass

    #bottom-right
    try:
        result = is_wanted(file[i+1][j+1])
        if result:
            return True
    except Exception:
        pass

    #bottom-left
    try:
        if j != 0:
            result = is_wanted(file[i+1][j-1])
            if result:
                return True
    except Exception:
        pass

    return False


def find_number(i, j):
    number = ''
    a = 0
    for g in range(0,5):
        if (file[i][j - g].isdigit() and not file [i][j - 1 - g].isdigit() and j - g - 1>= 0) or file[i][j - g].isdigit() and j-g == 0:
            while file[i][j-g+a].isdigit():
                number += file[i][j - g + a]
                a += 1
                if j-g+a == len(file[i]):
                    break
        if number != '':
            break
    if number == '':
        return 0
    return int(number)

# def find_number2(i, j, numbers):
#     number = ''
#     for g in range(0,3):
#         if file[i][j - g].isdigit() and not file [i][j - 1 - g].isdigit() and j - g > -1:
#             while file[i][j-g+a].isdigit():
#                 a = 0
#                 number += file[i][j - g + a]
#                 a += 1
#         if number != 0:
#             breakle[i][j].isdigit():
#             return number [0]
#     return number

suma = 0

for i in range(len(file)):
    number = ''
    is_number = False
    is_adjacent = False
    
    for j in range(len(file[i])):
        if is_star(file[i][j]) and count_numbers(i, j) == 2:
            num1 = 0
            num2 = 0
            if i != 0:
                num = find_number(i-1, j+1)
                print(f"{num} number")
                if num != 0:
                    if num1 == 0:
                        num1 = num
                        print(f"{num} number {num1} num1")
                        num = find_number(i-1, j-1)
                        if num != 0 and num != num1:
                            num2 = num
                            print(f"{num} number {num2} num2")
                    elif num1 != 0:
                        num2 = num
                        print(f"{num} number {num2} num2")

            if i < len(file) - 1:
                num = find_number(i+1, j+1)
                print(f"{num} number")
                if num != 0:
                    if num1 == 0:
                        num1 = num
                        print(f"{num} number {num1} num1")
                        num = find_number(i+1, j-1)
                        if num != 0 and num != num1:
                            num2 = num
                            print(f"{num} number {num2} num2")
                    elif num1 != 0:
                        num2 = num
                        print(f"{num} number {num2} num2")
            if j != 0 and file[i][j-1].isdigit():
                num = find_number(i, j-1)
                print(f"{num} number")
                if num != 0:
                    if num1 == 0:
                        num1 = num
                        print(f"{num} number {num1} num1")
                    elif num1 != 0:
                        num2 = num
                        print(f"{num} number {num2} num2")
            if j < len(file[i]) - 1 and file[i][j+1].isdigit():
                num = find_number(i, j+1)
                print(f"{num} number")
                if num != 0:
                    if num1 == 0:
                        num1 = num
                        print(f"{num} number {num1} num1")
                    elif num1 != 0:
                        num2 = num
                        print(f"{num} number {num2} num2")
            print(num1)
            print(str(num2)+'\n')
            print(suma)
            print(num1*num2)
            suma += int(num1)*int(num2)
            
            

                
print(f"Sum: {suma}")




