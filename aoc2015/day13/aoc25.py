from itertools import permutations

with open('aoc25-26.txt') as file_input:
    file = file_input.read().splitlines()

def list_names(puzzle_input):
    names = []
    for i in range(len(puzzle_input)):
        split_line = puzzle_input[i].split()
        if split_line[0] not in names:
            names.append(split_line[0])
    return names

def get_happiness(puzzle_input):
    happiness_chart = {}
    for i in range(len(puzzle_input)):
        split_line = puzzle_input[i].split()
        relationship = ()
        relationship.append(split_line[0])
        relationship.append(split_line[-1].replace('.',''))
        for element in split_line:
            if 'gain' in split_line:
                if element.isdigit():
                    happiness_chart[relationship] = int(element)
            else:
                if element.isdigit():
                    happiness_chart[relationship] = -int(element)
    return happiness_chart

if __name__ == "__main__":
    possible_seatings = permutations(list_names(file))
    happiness = 0
    changes_in_happiness = []
    happiness_chart = get_happiness(file)
    for seating in list(possible_seatings):
        
    #print(max(changes_in_happiness))
    print(list_names(file))