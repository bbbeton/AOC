with open('aoc3-4.txt') as file_input:
    paper = 0
    for line in file_input:
        num1 = []
        box = []
        for i in range(len(line)):
            liczba = 0
            if ord(line[i])>47 and ord(line[i])<58:
                num1.append(line[i])
            else:
                for a in range(len(num1)):
                    liczba = 10**a*int(num1[-1-a]) + liczba
                num1 = []
            if liczba !=0: 
                box.append(liczba)
            print(box)
            print(line)
        if len(box) == 3:
            b1 = box[0]
            b2 = box[1]
            b3 = box[2]
            if b1 == max(box):
                min1 = b3
                min2 = b2 
            elif b2 == max(box):
                min1 = b3
                min2 = b1    
            elif b3 == max(box):
                min1 = b1
                min2 = b2 
            paper += box[0]*box[1]*box[2] + 2*min1 + 2*min2
        print(len(box))
        print(len(box))
        print(paper)
      
for a in range(len(num1)):
    liczba = 10**a*int(num1[-1-a]) + liczba
print(liczba)
box.append(liczba)
print(box)
b1 = box[0]
b2 = box[1]
b3 = box[2]
if b1 == max(box):
    min1 = b3
    min2 = b2 
elif b2 == max(box):
    min1 = b3
    min2 = b1    
elif b3 == max(box):
    min1 = b1
    min2 = b2 
paper += box[0]*box[1]*box[2] + 2*min1 + 2*min2

print(paper)
                
