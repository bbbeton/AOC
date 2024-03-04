def game_number(line):
    num = []
    liczba = 0
    for element in line:
        if ord(element)>47 and ord(element)<58:
            num.append(int(element))
        elif element == ':':
            for i in range(len(num)):
                liczba += (10**i)*num[-1 - i]
            break
    return liczba

def powers(line):
    green = 0
    blue = 0
    red = 0
    greens = []
    blues = []
    reds = []
    num = []
    for i in range(len(line)):
        # if green > 13 or red > 12 or blue > 14:
        #     break
        if line[i] == ':' or line[i] == ';':
            green = 0
            blue = 0
            red = 0
            num = []
            liczba = 0
        if line == ',':            
            num = []
            liczba = 0
        if ord(line[i])>47 and ord(line[i])<58:
            num.append(int(line[i]))
        if line[i] == 'g':
            for a in range(len(num)):
                liczba += (10**a)*num[-1 - a]
            green = liczba
            greens.append(green)
            num = []
            liczba = 0
        elif line[i] == 'b':
            for a in range(len(num)):
                liczba += (10**a)*num[-1 - a]
            blue = liczba
            blues.append(blue)
            num = []
            liczba = 0
        elif line[i] == 'r':
            for a in range(len(num)):
                liczba += (10**a)*num[-1 - a]
            red = liczba
            reds.append(red)
            num = []
            liczba = 0
    moc = max(reds)*max(blues)*max(greens)
    return moc
    # if green > 13 or red > 12 or blue > 14:
    #     return False
    # else: 
    #     return True
         


with open('aoc3-4.txt') as file_input:
    pos = 0
    impos = 0
    suma = 0
    for line in file_input:
        line = line.rstrip()
        game_number(line)
        powers(line)
        suma += powers(line)
    print(suma)
