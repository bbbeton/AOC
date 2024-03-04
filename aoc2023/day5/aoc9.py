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

def organise(seed, destination, source, length):
    new_seeds = []
    destination = int(destination)
    source = int(source)
    length = int(length)
    seeds = [int(seed) for seed in seed] 
    for j in range(len(seeds)):
        new_seed = seeds[j]
        if seeds[j]  >= source and seeds[j] < source + length:
            if source > destination:
                new_seed -= (source - destination)
            else:
                new_seed += (destination - source)
        new_seeds.append(new_seed)
    return new_seeds 



my_seeds = get_my_seeds(file[0])

print(my_seeds)

for i in range(1,len(file)):
    try:
        if not file[i][0].isdigit() and file[i][0]:
            check_change=[0] * len(my_seeds)
            mapped = map_seeds(file, i)
            for j in range(len(mapped)):
                new_seeds = organise(my_seeds, mapped[j][0], mapped[j][1], mapped[j][2])
                for k in range(len(new_seeds)):
                    print(f"{new_seeds[k]} - new seeds {my_seeds[k]} - my seeds {check_change[k]} - check change")
                    if new_seeds[k] != int(my_seeds[k]) and check_change[k] == 0:
                        my_seeds[k] = new_seeds[k]
                        check_change[k] = 1
                print(f"After mapping {mapped[j]}: {my_seeds}\n")
            print(f"Mapped:{mapped}\n")
            print(f"{my_seeds}\n\n")
    except Exception:
        pass

print(min(my_seeds))


