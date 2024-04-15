from itertools import permutations

def list_names(puzzle_input):
    names = set()
    for line in puzzle_input:
        split_line = line.split()
        names.add(split_line[0])
    return list(names)

def get_happiness(puzzle_input):
    happiness_chart = {}
    for line in puzzle_input:
        split_line = line.split()
        person_a = split_line[0]
        person_b = split_line[-1].replace('.', '')
        happiness = int(split_line[3])
        if split_line[2] == "lose":
            happiness *= -1
        happiness_chart[(person_a, person_b)] = happiness
    return happiness_chart

def calculate_total_happiness(seating, happiness_chart):
    total_happiness = 0
    n = len(seating)
    for i in range(n):
        person_a = seating[i]
        person_b = seating[(i + 1) % n]
        total_happiness += happiness_chart.get((person_a, person_b), 0)
        total_happiness += happiness_chart.get((person_b, person_a), 0)
    return total_happiness

if __name__ == "__main__":
    with open('aoc25-26.txt') as file_input:
        file = file_input.read().splitlines()

    possible_seatings = permutations(list_names(file))
    happiness_chart = get_happiness(file)
    
    max_happiness = 0
    for seating in possible_seatings:
        total_happiness = calculate_total_happiness(seating, happiness_chart)
        max_happiness = max(max_happiness, total_happiness)
    
    print(max_happiness)
