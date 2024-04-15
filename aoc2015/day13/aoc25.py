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

def calculate_happiness(seating, happiness_chart):
    happiness = 0
    for i in range(len(seating)):
        person_a = seating[i]
        person_b = seating[i-1]
        happiness += happiness_chart.get((person_a, person_b), 0)
        happiness += happiness_chart.get((person_b, person_a), 0)
    return happiness

def get_happiness(puzzle_input):
    happiness_chart = {}
    for i in range(len(puzzle_input)):
        split_line = puzzle_input[i].split()
        for element in split_line:
            if 'gain' in split_line:
                if element.isdigit():
                    happiness_chart[(split_line[0] ,split_line[-1].replace('.',''))] = int(element)
            else:
                if element.isdigit():
                    happiness_chart[(split_line[0] ,split_line[-1].replace('.',''))] = -int(element)
    return happiness_chart

if __name__ == "__main__":
    possible_seatings = permutations(list_names(file))
    changes_in_happiness = []
    happiness_chart = get_happiness(file)
    for seating in list(possible_seatings):
        changes_in_happiness.append(calculate_happiness(seating, happiness_chart))
    print(max(changes_in_happiness))
    #print(list_names(file))