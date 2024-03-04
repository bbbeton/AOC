with open('aoc9-10.txt') as file_input:
    file = file_input.read().splitlines()

def get_my_seeds(line):
    numbers = ''
    for i in range(len(line)):
        numbers += line[i]
        if line[i] == ':':
            numbers = ''
    seeds = numbers.split()
    return seeds

def map_seeds(block, a):
    numbers = ''
    mapped = []
    for i in range(a,len(block)):
        if block[i]:
            for j in range(len(block[i])):
                numbers += block[i][j]
                if block[i][j] == ':':
                    numbers = ''
            
            mapped.append(numbers.split())
            numbers = ''
        else:
            break
    mapped = list(filter(None, mapped))
    return mapped

def organise(a, b):
    organised = []
    a = int(a)
    b = int(b)
    for i in range(b):
        organised.append(a)
        a += 1
    return organised        


my_seeds = get_my_seeds(file[0])

print(my_seeds)

for i in range(1,len(file)):
    try:
        if not file[i][0].isdigit() and file[i][0]:
            mapped = map_seeds(file, i)
            print(f"{mapped} - mapped")
            sources = []
            destinations = []
            map_table_block = []
            print(len(mapped))
            sources_organise = organise(mapped[1][0],mapped[1][2])
            for k in range(len(mapped)):
                sources_organise = organise(mapped[k][0],mapped[k][2])
                print(f"{sources_organise} - sources organise")
                destinations_organise = organise(mapped[k][1],mapped[k][2])
                print(f"{destinations_organise} - destinations organise")
                sources.extend(sources_organise)
                destinations.extend(destinations_organise)
            print(f"{sources} - sources")
            print(f"{destinations} - destinations")
            print(my_seeds)
            for seed in range(len(my_seeds)):
                for l in range(len(sources)):
                    if my_seeds[seed] == str(destinations[l]):
                        print(f"{my_seeds[seed]} found!")
                        my_seeds[seed] = str(sources[l])
                        break
            print(f"{my_seeds}\n")
    except Exception:
        pass

print(min(my_seeds))
