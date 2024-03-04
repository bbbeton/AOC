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
    for i in range(a, len(block)):
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
    destination = int(destination)
    source = int(source)
    length = int(length)
    new_seed = int(seed)
    if new_seed >= source and new_seed < source + length:
        if source > destination:
            new_seed -= (source - destination)
        else:
            new_seed += (destination - source)
    return new_seed 

my_seeds = get_my_seeds(file[0])
print(my_seeds)

minimum = int(my_seeds[0])

for m in range(1, len(my_seeds), 2):
    curr_seed_org = int(my_seeds[m-1])
    range_seed = int(my_seeds[m])

    # print(f"{curr_seed_org} - curr seed")
    # print(f"{range_seed} - range seed")

    for n in range(range_seed):
        curr_seed = curr_seed_org + n
        for i in range(1, len(file)):
            try:
                if file[i] and not file[i][0].isdigit():
                    # print(f"Processing line: {file[i]}")
                    mapped = map_seeds(file, i)
                    for j in range(len(mapped)):
                        new_seed = organise(curr_seed, mapped[j][0], mapped[j][1], mapped[j][2])
                        #print(f"{new_seed} - new seeds {curr_seed} - my seeds ")
                        if new_seed != curr_seed:
                            curr_seed = new_seed
                            break
                        # print(f"After mapping {mapped[j]}: {my_seeds}\n")
                    #print(f"Mapped:{mapped}\n")
                    #print(f"{curr_seed}\n\n")
            except Exception as e:
                print(f"Error: {e}")

        if minimum > curr_seed:
            minimum = curr_seed

print(minimum)
