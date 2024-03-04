def wypisz_liczby(line):
    symbols_to_remove = '!@#$%^&*()_-+=[]><?/~\n`'
    new_line = str(line)
    for symbol in symbols_to_remove:
        if symbol in line:
            new_line = new_line.replace(symbol,'')
    x = new_line.split(".")
    liczby = list(filter(None, x))
    return liczby

def check_prev(curr_line, prev_line, numbers):
    result = []
    licznik = 0
    for i in range(len(curr_line)-1):
        if ord(curr_line[i]) > 47 and ord(curr_line[i]) < 58:
            if i != 0 and i < len(curr_line):
                n = i + len(numbers[licznik]) + 1
                if (ord(curr_line[i+1]) < 47 or ord(curr_line[i+1]) > 58) and (prev_line[n] != '.' or curr_line[n] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                elif (ord(curr_line[i-1]) < 47 or ord(curr_line[i-1]) > 58) and (prev_line[i-1] != '.' or curr_line[i-1] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    if licznik < len(numbers):                   
                        for a in range(len(numbers[licznik])):
                            if prev_line[i+a] != '.' and not prev_line[i+a].isdigit:
                                result.append(numbers[licznik])
                                licznik += 1
                                break                
            elif i == 0:
                n = i + len(numbers[licznik]) + 1
                if (ord(curr_line[i+1]) < 47 or ord(curr_line[i+1]) > 58) and (prev_line[n] != '.' or curr_line[n] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    for a in range(len(numbers[licznik])):
                        if prev_line[i+a] != '.' and not prev_line[i+a].isdigit:
                            result.append(numbers[licznik])
                            licznik += 1
                            break
            else:
                if (ord(curr_line[i-1]) < 47 or ord(curr_line[i-1]) > 58) and (prev_line[i-1] != '.' or curr_line[i-1] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    for a in range(len(numbers[licznik])):
                        if (prev_line[i+a] != '.' or curr_line[i+a] != '.') and not prev_line[i+a].isdigit:
                            result.append(numbers[licznik])
                            licznik += 1
                            break
        return result

def check_next(curr_line, next_line, numbers):
    result = []
    licznik = 0
    for i in range(len(curr_line)-1):
        if licznik >= len(numbers):
            break
        if ord(curr_line[i]) > 47 and ord(curr_line[i]) < 58 and len(numbers) != 0 and licznik < len(numbers):
            if i != 0 and i < len(curr_line) - len(numbers[licznik]) - 1:
                n = i + len(numbers[licznik])
                if (ord(curr_line[i+1]) < 47 or ord(curr_line[i+1]) > 58) and (next_line[n] != '.' or curr_line[n] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                elif (ord(curr_line[i-1]) < 47 or ord(curr_line[i-1]) > 58) and (next_line[i-1] != '.' or curr_line[i-1] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    if licznik < len(numbers):                   
                        for a in range(len(numbers[licznik])):
                            if (next_line[i+a] != '.'):
                                result.append(numbers[licznik])
                                licznik += 1
                                break                
            elif i == 0:
                n = i + len(numbers[licznik]) + 1
                if (ord(curr_line[i+1]) < 47 or ord(curr_line[i+1]) > 58) and (next_line[n] != '.' or curr_line[n] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    for a in range(len(numbers[licznik])):
                        if (next_line[i+a] != '.'):
                            result.append(numbers[licznik])
                            licznik += 1
                            break
            else:
                if (ord(curr_line[i-1]) < 47 or ord(curr_line[i-1]) > 58) and (next_line[i-1] != '.' or curr_line[i-1] != '.'):
                    result.append(numbers[licznik])
                    licznik += 1
                else:
                    if i>len(line)-len(numbers[licznik]):
                        break
                    for a in range(len(numbers[licznik])):
                        if (next_line[i+a] != '.') and not (next_line[i+a].isdigit):
                            result.append(numbers[licznik])
                            licznik += 1
                            break
        
    return result




with open('aoc5-6.txt') as file_input:
    curr_line = []
    next_line = []
    num = []
    result = []
    result_prev = []
    for line in file_input:
        if curr_line != []:
            numbers_line = wypisz_liczby(line)
            numbers_prev = wypisz_liczby(curr_line)
            print(str(numbers_prev)+' previous')
            
            print(str(result_prev)+' previous result')
            result = check_prev(line, curr_line, numbers_line)
            print(str(result) + " wynik")
            for wynik in result:
                num.append(int(wynik))
            result_next = check_next(curr_line, line, numbers_prev)
            print(str(result_next) +" nastepny wynik")
            for wynik in result_next:
                if wynik not in result_prev:
                    num.append(int(wynik))
        print(str(num)+' wynik suma\n\n') 
        result_prev = result
        curr_line = line
    suma = sum(num)
    print(suma) 
    


            

