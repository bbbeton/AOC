with open('aoc25-26.txt') as file_input:
    file = file_input.read().splitlines()

def list_names(puzzle_input):
    names = []
    for i in range(len(puzzle_input)):
        split_line = puzzle_input[i].split()
        if split_line[0] not in names:
            names.append(split_line[0])
    return names

if __name__ == "__main__":