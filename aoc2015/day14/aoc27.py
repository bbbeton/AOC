with open('aoc27-28.txt') as file_input:
    file = file_input.read().splitlines()

def get_names(puzzle_input):
    names = []
    for line in puzzle_input:
        split_line = line.split()
        names.append(split_line[0])
    return names

def assign_speeds(puzzle_input):
    speeds = {}
    for line in puzzle_input:
        split_line = line.split()
        speeds[split_line[0]] = [int(split_line[3]), int(split_line[6]), int(split_line[-2])]
    return speeds

def get_max_distance(names, max_time, speeds):
    time = 0
    distance = 0
    max_distance = 0
    for name in names:
        while time < max_time:
            for i in range(speeds[name][1]):
                distance += speeds[name][0]
                time += 1
            time += speeds[name][2]
        max_distance = max(distance, max_distance)
    return max_distance

if __name__ == "__main__":
    names = get_names(file)
    speeds = assign_speeds(file)
    max_time = 2503
    print(get_max_distance(names, max_time, speeds))
    