with open('aoc11-12.txt') as file_input:
    file = file_input.read().splitlines()

def read_command(string):
    i = 0
    command = ''
    while not string[i].isdigit():
        command += string[i]
        i += 1
    return(command.strip())

#print(read_commend(file[0]))

def create_table():
    lights = []
    for i in range(0,1000):
        lights.append([])
        for j in range(0,1000):
            lights[i].append(0)
    return lights

def get_nums(string):
    nums = []
    words = string.split()
    for element in words:
        if element[0].isdigit():
            nums.append(element.split(','))
    return nums

def toggle(light):
    return 1 - light

def turn_on(light):
    return 1

def turn_off(light):
    return 0

if __name__ == "__main__":
    lights = create_table()
    for k in range(len(file)):
        command = read_command(file[k])
        curr_lights = get_nums(file[k])
        if command == 'toggle':
            for i in range(int(curr_lights[0][0]), int(curr_lights[1][0]) + 1):
                for j in range(int(curr_lights[0][1]), int(curr_lights[1][1]) + 1):
                    lights[i][j] = toggle(lights[i][j])
        elif command == 'turn on':
            for i in range(int(curr_lights[0][0]), int(curr_lights[1][0]) + 1):
                for j in range(int(curr_lights[0][1]), int(curr_lights[1][1]) + 1):
                    lights[i][j] = turn_on(lights[i][j])
        elif command == 'turn off':
            for i in range(int(curr_lights[0][0]), int(curr_lights[1][0]) + 1):
                for j in range(int(curr_lights[0][1]), int(curr_lights[1][1]) + 1):
                    lights[i][j] = turn_off(lights[i][j])

    total_lights_on = sum(sum(row) for row in lights)
    print(total_lights_on)