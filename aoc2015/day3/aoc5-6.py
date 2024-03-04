with open('aoc5-6.txt') as file_input:
    file = file_input.read().splitlines()

current_house = [0,0]
visited_houses_santa = []
visited_houses_robo = []
visited_houses_santa.append(current_house.copy())
visited_houses_robo.append(current_house.copy())
current_house_santa = current_house.copy()
current_house_robo = current_house.copy()
def move(char, house):
    if char == '^':
        house[0] += 1
    elif char == 'v':
        house[0] -= 1
    elif char == '>':
        house[1] += 1
    elif char == '<':
        house[1] -= 1

    return house

for i in range(len(file)):
    for j in range(len(file[i])):
        print(f"Santa: {current_house_santa}, Robo: {current_house_robo}")
        if j % 2 == 0:
            houses = visited_houses_santa
            current_house_santa = move(file[i][j], current_house_santa)
            if current_house_santa not in houses:
                houses.append(current_house_santa.copy())
        elif j % 2 == 1:
            houses = visited_houses_robo
            current_house_robo = move(file[i][j], current_house_robo)
            if current_house_robo not in houses:
                houses.append(current_house_robo.copy())

visited_houses = visited_houses_santa.copy()

for house in visited_houses_robo:
    if house not in visited_houses:
        visited_houses.append(house.copy())

print(len(visited_houses))