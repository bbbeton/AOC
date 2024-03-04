numerki =[]
liczby = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('aoc1-2.txt') as file_object:
    for line in file_object:
        linijka=[]
        for i in range(len(line)):
            if ord(line[i])>47 and ord(line[i])<58:
                linijka.append(int(line[i]))
            else:
                for b in range(len(liczby)):
                    licznik = 0
                    if(len(line) - i  >= len(liczby[b])):
                        for a in range(len(liczby[b])):   
                            if liczby[b][a] == line[i+a]:
                                licznik = licznik + 1
                        if licznik == len(liczby[b]):
                            linijka.append(b)
        liczba = int(linijka[0])*10 + int(linijka[-1])
        numerki.append(liczba)

suma = sum(numerki)

print(suma)