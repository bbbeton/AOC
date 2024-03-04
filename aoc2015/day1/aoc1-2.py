floor = 0
with open("aoc1-2.txt") as file_object:
    for line in file_object:
        for i in range(len(line)):
            if line[i] == '(':
                floor += 1
            elif line[i] == ')':
                floor -= 1
            if floor == -1:
                print(i+1)
            
        
